 #  CopyCraft AI — Automated Copywriting & Tone Transformer

An AI-powered application that transforms a raw product description into
professional, platform-optimized marketing copy — built with **LangChain**,
**Groq (Llama 3.3 70B Versatile)**, and **Streamlit**.

Give it a product name, a target audience, a few benefits, a tone, and a
platform — CopyCraft AI writes the copy for you, formatted exactly the way
that platform expects it.

> **Status:** Internship learning project (Task 2). Built to practice
> real-world Generative AI engineering concepts — not a commercial product.

---

##  Overview

Writing marketing copy by hand for every platform is repetitive and
time-consuming: a LinkedIn post needs a different structure than an
Instagram caption, which needs a different structure than a cold email.

**CopyCraft AI** solves this by acting as an AI copywriter with a fixed
persona — 15+ years of "experience," strict platform rules, and
persuasive-writing principles baked directly into its prompt. The user
supplies structured inputs (product, audience, tone, benefits, CTA), and the
app dynamically builds a prompt, sends it to an LLM through LangChain, and
returns ready-to-publish copy.

---

##  Features

- **Multi-platform copy generation** — Instagram, LinkedIn, Email, and
  Twitter, each with its own formatting rules (character limits, emoji
  usage, hashtags, subject lines, etc.).
- **Multi-tone support** — Professional, Friendly, Luxury, Technical,
  Persuasive, and Casual.
- **Dynamic prompt engineering** — user inputs are injected into a
  reusable prompt template at runtime instead of hardcoding prompts.
- **Inference parameter control** — live sliders for **Temperature** and
  **Top-P**, letting the user control how creative vs. focused the
  generated copy is.
- **Input validation layer** — sanitizes and checks all fields before
  they ever reach the LLM, preventing empty or malformed prompts.
- **Fast inference** — powered by Groq's LPU inference engine running
  Llama 3.3 70B Versatile.
- **Clean, modular architecture** — UI, validation, prompt-building, and
  the LLM chain are fully separated into their own modules.
- **Downloadable output** — generated copy can be exported as a `.txt`
  file directly from the UI.

---

##  How It Works

```
User Input (Streamlit UI)
        │
        ▼
Input Validation  ──── rejects empty/invalid fields
        │
        ▼
Dynamic Prompt Builder ──── injects variables into a template
        │
        ▼
LangChain Chain (LCEL) ──── prompt | llm | output parser
        │
        ▼
Groq API ──── runs Llama 3.3 70B Versatile
        │
        ▼
Generated Marketing Copy
        │
        ▼
Displayed + Downloadable in Streamlit
```

### Example

**Input:**
| Field | Value |
|---|---|
| Product Name | Samsung Galaxy S25 |
| Platform | LinkedIn |
| Tone | Professional |
| Audience | Students |
| Benefits | All-day battery, AI camera, fast performance |
| CTA | Buy Now |

**Prompt sent to the model (simplified):**
```
Generate a Professional LinkedIn marketing copy for the following product.

Product Name: Samsung Galaxy S25
Target Audience: Students
Key Benefits: All-day battery, AI camera, fast performance
Call To Action: Buy Now

Format: a professional post with a clear structure (hook, body, closing line). No emojis.
```

**Output:** a ready-to-post LinkedIn caption written in the requested tone,
following LinkedIn's formatting rules, ending with the CTA.

---

##  Tech Stack

| Layer | Technology |
|---|---|
| UI | Streamlit |
| LLM Orchestration | LangChain (LCEL) |
| Inference Provider | Groq API |
| Model | Llama 3.3 70B Versatile |
| Config Management | python-dotenv |
| Language | Python 3.11 |

---

##  Project Structure

```
copycraft_ai/
├── app.py                 # Streamlit UI — collects input, displays output
├── src/
│   ├── config.py           # Groq LLM client setup & defaults
│   ├── prompts.py            # CopyCraft AI persona + dynamic prompt templates
│   ├── validator.py           # Input validation & sanitization
│   ├── chains.py                # LangChain (LCEL) chain construction
│   └── generator.py              # Orchestrates validate → prompt → chain → output
├── .env.example             # Template for the Groq API key
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/BilalRajput-52/<ai-copywriting-tone-transformer>.git
cd <ai-copywriting-tone-transformer>
```

### 2. Create a virtual environment (Python 3.11 recommended)
```bash
python -m venv venv
```

### 3. Activate it
**Windows (PowerShell):**
```bash
venv\Scripts\Activate.ps1
```
**Mac/Linux:**
```bash
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Set up your API key
Copy `.env.example` to `.env` and add your Groq API key (free at
[console.groq.com](https://console.groq.com)):
```
GROQ_API_KEY=your_key_here
```

### 6. Run the app
```bash
streamlit run app.py
```
The app will open at `http://localhost:8501`.

---

##  Supported Platforms & Tones

**Platforms:**
- Instagram — short, engaging, emojis + hashtags
- LinkedIn — professional, structured, no emojis
- Email — subject line, greeting, body, CTA, signature
- Twitter — strictly capped at 280 characters

**Tones:**
Professional · Friendly · Luxury · Technical · Persuasive · Casual

---

##  Skills Demonstrated

- Prompt engineering (dynamic, template-based)
- LangChain Expression Language (LCEL) chain construction
- LLM API integration (Groq)
- Inference parameter tuning (Temperature, Top-P)
- Input validation and modular Python architecture
- Building an LLM-backed UI with Streamlit

---

##  Notes

This project was built as part of a structured internship learning task
to practice Generative AI and LLM application development concepts. It
is intentionally scoped for learning — no database, authentication, or
production-scale infrastructure is included.

---

##  Author

**Bilal Rajput**
Final-year BS-IT Student | Aspiring AI/ML Engineer
GitHub: [BilalRajput-52](https://github.com/BilalRajput-52)

---

## 📄 License

This project is open for educational and learning purposes.
