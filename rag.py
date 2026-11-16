import json
from pathlib import Path

import numpy as np
from google import genai

from config import API_KEY, EMBED_MODEL

client = genai.Client(api_key=API_KEY)
DATA = Path(__file__).parent / "data"
_cache = {}


def scheme_text(s):
    return f"{s['name']}. {s['description']} Benefits: {s['benefits']}"


def embed(texts):
    res = client.models.embed_content(model=EMBED_MODEL, contents=texts)
    return np.array([e.values for e in res.embeddings], dtype="float32")


def _index():
    if "idx" in _cache:
        return _cache["idx"]
    schemes = json.loads((DATA / "schemes.json").read_text(encoding="utf-8"))
    cache_file = DATA / "embeddings.npy"
    vecs = None
    if cache_file.exists():
        vecs = np.load(cache_file)
        if len(vecs) != len(schemes):   # corpus changed -> rebuild
            vecs = None
    if vecs is None:
        vecs = embed([scheme_text(s) for s in schemes])
        np.save(cache_file, vecs)
    vecs = vecs / np.linalg.norm(vecs, axis=1, keepdims=True)
    _cache["idx"] = (schemes, vecs)
    return _cache["idx"]


def profile_to_text(p):
    return (f"{p['age']}-year-old {p['gender']} {p['occupation']}, "
            f"{p['category']} category, from {p['state']}, "
            f"annual income {p['income']} rupees")


def retrieve(profile, k=None):
    """Rank ALL schemes by relevance to the profile (RAG).
    Returns (ranked_schemes, used_rag). Nothing is dropped, so an eligible scheme
    can never be missed because of retrieval. If the embedding API fails, we fall
    back to corpus order and the rule engine still produces the correct result."""
    try:
        schemes, vecs = _index()
        q = embed([profile_to_text(profile)])[0]
        q = q / np.linalg.norm(q)
        order = np.argsort(-(vecs @ q))
        ranked, used_rag = [schemes[i] for i in order], True
    except Exception:
        ranked = json.loads((DATA / "schemes.json").read_text(encoding="utf-8"))
        used_rag = False
    return (ranked[:k] if k else ranked), used_rag
