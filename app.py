import streamlit as st

from config import API_KEY
from explain import explain
from rag import retrieve
from rules import check
from vision import extract_fields

st.set_page_config(page_title="Sahayak", page_icon="🌉", layout="wide")

if not API_KEY:
    st.error("GEMINI_API_KEY missing. Add it to the .env file and restart.")
    st.stop()

STATES = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Delhi",
          "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
          "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
          "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
          "Uttar Pradesh", "Uttarakhand", "West Bengal", "Other UT / State"]
CATEGORIES = ["General", "OBC", "SC", "ST", "EWS"]
GENDERS = ["Male", "Female", "Other"]
OCCUPATIONS = ["Farmer", "Student", "Street Vendor", "Artisan / Self-employed",
               "Salaried", "Unemployed", "Homemaker", "Other"]
LANGUAGES = ["English", "Hindi", "Bengali", "Tamil", "Telugu", "Marathi", "Gujarati",
             "Kannada", "Malayalam", "Punjabi"]


def idx(options, value):
    return options.index(value) if value in options else 0


ex = st.session_state.get("extracted", {})

# ---------- Sidebar ----------
with st.sidebar:
    st.header("Settings")
    language = st.selectbox("Explanation language", LANGUAGES)
    st.divider()
    st.subheader("Optional: upload certificate")
    st.caption("Income / caste / domicile certificate (image). Fields auto-fill the form.")
    up = st.file_uploader("Certificate", type=["png", "jpg", "jpeg"])
    if up and st.button("Extract details"):
        with st.spinner("Reading document..."):
            try:
                st.session_state["extracted"] = extract_fields(up.getvalue(), up.type)
                st.rerun()
            except Exception as e:
                st.error(f"Could not read document: {e}")
    if ex:
        st.success(f"Extracted: {ex}")

# ---------- Main ----------
st.title("🌉 Sahayak")
st.caption("Tell us who you are. We find the welfare schemes you qualify for.")

with st.form("profile"):
    c1, c2 = st.columns(2)
    age = c1.number_input("Age", 0, 120, int(ex.get("age") or 30))
    gender = c1.selectbox("Gender", GENDERS, idx(GENDERS, ex.get("gender")))
    occupation = c1.selectbox("Occupation", OCCUPATIONS)
    income = c2.number_input("Annual family income (Rs)", 0, 10_000_000,
                             int(ex.get("annual_income") or 100000), step=10000)
    category = c2.selectbox("Category", CATEGORIES, idx(CATEGORIES, ex.get("category")))
    state = c2.selectbox("State", STATES, idx(STATES, ex.get("state")))
    submitted = st.form_submit_button("Find my schemes", type="primary")

if submitted:
    profile = {"age": int(age), "gender": gender, "occupation": occupation,
               "income": int(income), "category": category, "state": state}

    with st.spinner("Searching schemes and verifying eligibility..."):
        ranked, used_rag = retrieve(profile)                      # RAG ranks ALL schemes
        results = [(s, check(profile, s["rules"])) for s in ranked]      # rule engine checks ALL
        eligible = [(s, v) for s, v in results if v["eligible"]]
        not_eligible = [(s, v) for s, v in results if not v["eligible"]]

    if not used_rag:
        st.warning("Semantic ranking unavailable (embedding API issue). Results below are "
                   "still correct; only the ordering is default.")

    st.subheader(f"✅ You may qualify for {len(eligible)} scheme(s)")
    st.caption("Eligibility decided by a deterministic rule engine (no AI). "
               "AI is used only for explanation.")

    for s, v in eligible:
        with st.expander(f"{s['name']} — {s['benefits']}"):
            for c in v["checks"]:
                st.write(("✅ " if c["passed"] else "❌ ") + c["detail"])
            st.markdown(f"[Official portal]({s['apply_url']})")

    if eligible:
        st.subheader(f"📋 Plain-language guide & action plan ({language})")
        with st.spinner("Writing your action plan..."):
            try:
                st.markdown(explain(profile, eligible, language))
            except Exception as e:
                st.warning(f"Explanation failed ({e}). Eligibility results above are still valid.")

    with st.expander(f"Schemes you do NOT qualify for ({len(not_eligible)})"):
        for s, v in not_eligible:
            failed = [c["detail"] for c in v["checks"] if not c["passed"]]
            st.write(f"**{s['name']}** — " + "; ".join(failed))

    st.info("Demo data is simplified. Always confirm on the official portal before applying.")
