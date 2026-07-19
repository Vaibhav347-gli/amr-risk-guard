# 🧫 AMR RISK GUARD
> **An AI-powered RAG application using Gemini to evaluate Antimicrobial Resistance (AMR) risks based on official WHO and ICMR guidelines.**

### 🚀 [CLICK HERE TO LAUNCH THE LIVE APP](https://amr-risk-guard-ccz9kjzknzw2qfuz29j4a4.streamlit.app/)

---

## 🌍 THE PROBLEM: AMR
Antimicrobial Resistance is a critical global health threat. It occurs when pathogens evolve to resist medications, primarily driven by the misuse and overuse of antibiotics. 

## 💡 THE SOLUTION
**AMR Risk Guard** combats medical misinformation. By utilizing a Retrieval-Augmented Generation (RAG) architecture, the app evaluates user queries and flags high-risk behaviors using *only* verified public health datasets.

---

## ✨ KEY FEATURES

* **💬 Dynamic Risk Evaluation** 
  Gemini 3.5 Flash answers health queries using strictly verified medical data.
* **🔬 Myth vs. Fact Lab** 
  An interactive dashboard debunking critical antibiotic fallacies.
* **🛡️ Regulatory Guardrails** 
  Strict AI system instructions prevent clinical diagnoses or hallucinated data.
* **🎨 Bio-Tech UI** 
  A custom, responsive Streamlit interface built for clarity and engagement.

---

## 🛠️ TECH STACK

* **Frontend:** Streamlit (Python)
* **LLM Engine:** Google Gemini API (`gemini-3.5-flash`)
* **RAG Processing:** `pypdf` (Real-time extraction from official PDFs)
* **Deployment:** Streamlit Community Cloud

---

## 💻 LOCAL QUICK START

Run this project on your own machine:

**1. Clone the repository**
```bash
git clone [https://github.com/your-username/amr-risk-guard.git](https://github.com/your-username/amr-risk-guard.git)
cd amr-risk-guard
