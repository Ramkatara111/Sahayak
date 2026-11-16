# 🤝 Sahayak – AI-Powered Government Scheme Assistant

**Discover Indian government welfare schemes you may be eligible for.**

Sahayak is an AI-powered web application that helps users discover relevant Indian welfare schemes based on their personal profile. A Python rule engine determines eligibility, while Google Gemini helps rank schemes, explain them in the user's preferred language, and read information from uploaded certificates.

<p align="center">
  <a href="https://sahayakkk.streamlit.app/">
    <img src="https://img.shields.io/badge/Live%20Demo-Open%20Sahayak-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Open Sahayak"/>
  </a>
  <a href="https://github.com/Ramkatara111">
    <img src="https://img.shields.io/badge/GitHub-Ramkatara111-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/ram-katara1115/">
    <img src="https://img.shields.io/badge/LinkedIn-Ram%20Katara-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
  </a>
</p>

---

## ✨ Features

- **Personalized Scheme Discovery:** Find schemes based on the details entered in your profile.
- **Rule-Based Eligibility:** A Python rule engine (`rules.py`) evaluates eligibility against available scheme rules.
- **AI-Powered Explanations:** Gemini explains scheme details in the user's selected language.
- **Scheme Ranking:** Gemini helps rank potentially relevant schemes.
- **Certificate Reading:** Upload certificates for Gemini-powered information extraction.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Streamlit | Web application interface |
| Google Gemini API | Scheme ranking, explanations and certificate reading |
| JSON | Scheme information and rules |
| pytest | Automated testing |

## 🚀 Live Demo

**Try Sahayak:** https://sahayakkk.streamlit.app/

## 📂 Project Structure

```text
Sahayak/
├── app.py
├── config.py
├── explain.py
├── rag.py
├── rules.py
├── vision.py
├── data/
│   └── schemes.json
├── tests/
│   └── test_rules.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Local Setup

### Prerequisites

- Python 3.10 or above
- Google Gemini API key

Get your API key from [Google AI Studio](https://aistudio.google.com/apikey).

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd Sahayak
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the environment

**Windows PowerShell:**

```powershell
.\venv\Scripts\Activate.ps1
```

**Mac / Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Gemini API key

Create a `.env` file in the project root and add:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

Never upload your `.env` file or expose your API key on GitHub.

## ▶️ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Open your browser at:

http://localhost:8501

Press `Ctrl + C` in the terminal to stop the application.

## ☁️ Deployment

Sahayak is deployed using **Streamlit Community Cloud**.

- **Live Application:** https://sahayakkk.streamlit.app/
- **Source Code:** GitHub
- **AI Integration:** Google Gemini API
- **Hosting:** Streamlit Community Cloud

For deployment, configure your Gemini API key under your Streamlit Cloud app's **Settings → Secrets**:

```toml
GEMINI_API_KEY = "your_actual_gemini_api_key"
```

Never publish your actual API key in this README, source code or public repositories.

## 🧪 Run Tests

Execute the test suite:

```bash
python -m pytest tests -q
```

## 📝 Notes & Limitations

- Scheme eligibility is determined by the Python rule engine in `rules.py`.
- Gemini is used for scheme ranking, explanations and certificate information extraction.
- Scheme rules in `data/schemes.json` are simplified demo data, not authoritative government eligibility criteria.
- Always verify scheme details and eligibility through the official [myScheme portal](https://www.myscheme.gov.in/).
- If PowerShell blocks script activation, run the application directly:

```powershell
.\venv\Scripts\python.exe -m streamlit run app.py
```

- If you edit scheme text in `data/schemes.json`, delete `data/embeddings.npy` so embeddings can be regenerated.
- Model names are configured in `config.py`.

---

## 👨‍💻 About the Developer

**Ram Katara**

Software Developer | Full-Stack Development | AI-Powered Applications

I'm passionate about building technology-driven solutions that solve real-world problems using software development and AI.

### 🤝 Connect With Me

<p align="left">
  <a href="https://github.com/Ramkatara111">
    <img src="https://img.shields.io/badge/GitHub-Ramkatara111-181717?style=for-the-badge&logo=github" alt="GitHub"/>
  </a>
  <a href="https://www.linkedin.com/in/ram-katara1115/">
    <img src="https://img.shields.io/badge/LinkedIn-Ram%20Katara-0A66C2?style=for-the-badge&logo=linkedin" alt="LinkedIn"/>
  </a>
</p>

- **GitHub:** https://github.com/Ramkatara111
- **LinkedIn:** https://www.linkedin.com/in/ram-katara1115/
- **Live Project:** https://sahayakkk.streamlit.app/

---

<p align="center">
  Made by <strong>Ram Katara</strong>
</p>