# Sahayak

Fill in a profile, and the app lists the Indian welfare schemes you may qualify for.
A Python rule engine (`rules.py`) decides eligibility. Gemini only ranks the schemes,
explains them in your chosen language and reads uploaded certificates.

> Demo data: the scheme rules in `data/schemes.json` are simplified.
> Verify every scheme on https://www.myscheme.gov.in before real use.

## Setup (one time)

Needs Python 3.10+ and a free Gemini API key from https://aistudio.google.com/apikey

Open a terminal **inside this folder**, then:

```bash
python -m venv venv
```

Activate it. Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

Mac / Linux:

```bash
source venv/bin/activate
```

Install the packages:

```bash
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and replace `paste_your_key_here` with your own key.

## Run

```bash
python -m streamlit run app.py
```

It opens at http://localhost:8501. Press Ctrl+C in the terminal to stop it.

## Tests

```bash
python -m pytest tests -q
```

## Notes

- If PowerShell blocks `Activate.ps1`, skip activating and use
  `.\venv\Scripts\python.exe -m streamlit run app.py` instead.
- Never share your `.env` file. It holds your personal API key.
- If you edit scheme text in `data/schemes.json`, delete `data/embeddings.npy`.
- Model names are in `config.py` if Google renames them.
