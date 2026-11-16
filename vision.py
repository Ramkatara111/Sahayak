import json

from google import genai
from google.genai import types

from config import API_KEY, CHAT_MODEL

client = genai.Client(api_key=API_KEY)

PROMPT = """Read this Indian government certificate (income / caste / domicile).
Return ONLY JSON with these keys, using null if not present:
{"age": integer or null,
 "annual_income": integer in rupees or null,
 "category": one of "General","OBC","SC","ST","EWS" or null,
 "state": Indian state name or null,
 "gender": "Male","Female","Other" or null}
Do not guess values that are not on the document."""


def extract_fields(file_bytes: bytes, mime_type: str) -> dict:
    r = client.models.generate_content(
        model=CHAT_MODEL,
        contents=[types.Part.from_bytes(data=file_bytes, mime_type=mime_type), PROMPT],
        config=types.GenerateContentConfig(response_mime_type="application/json"),
    )
    data = json.loads(r.text)
    return {k: v for k, v in data.items() if v is not None}
