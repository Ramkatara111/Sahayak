import json

from google import genai

from config import API_KEY, CHAT_MODEL

client = genai.Client(api_key=API_KEY)


def explain(profile, eligible, language="English"):
    """eligible = list of (scheme, verdict). Gemini explains; it never decides."""
    if not eligible:
        return ""
    payload = [{
        "name": s["name"],
        "benefits": s["benefits"],
        "documents": s["documents"],
        "apply_url": s["apply_url"],
        "why_eligible": [c["detail"] for c in v["checks"]],
    } for s, v in eligible]

    prompt = f"""You help Indian citizens understand welfare schemes.
Write in {language}, in very simple words (Class 8 reading level).
Keep scheme names in English.

For EACH scheme below output markdown:
### <scheme name>
**Why you qualify:** one or two sentences using the facts in why_eligible.
**What you get:** one sentence.
**Documents needed:** bullet list.
**How to apply:** 3-5 short numbered steps and the official link.

STRICT RULES:
- Eligibility is ALREADY decided by a rule engine. Do not question or change it.
- Use ONLY the information provided. Do not invent amounts, dates or deadlines.
- If unsure about a step, say "check the official portal".

Schemes JSON:
{json.dumps(payload, ensure_ascii=False)}
"""
    r = client.models.generate_content(model=CHAT_MODEL, contents=prompt)
    return r.text
