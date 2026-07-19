🧫 AMR Risk Guard
An AI-powered RAG application using Gemini 3.5 to evaluate Antimicrobial Resistance (AMR) risks based on official WHO and ICMR guidelines.

🚀 The Problem: Antimicrobial Resistance (AMR)
Antimicrobial Resistance is one of the top global public health threats facing humanity. It occurs when bacteria and viruses evolve to resist the medications used to cure them, largely driven by the misuse and overuse of antibiotics (e.g., taking antibiotics for viral infections like the common cold, or stopping medication early).

💡 The Solution
AMR Risk Guard is an AI-driven educational framework built to combat antibiotic misinformation. By utilizing a Retrieval-Augmented Generation (RAG) architecture, the app grounds its responses strictly in verified public health datasets (PDFs from the WHO, CDC, and ICMR). It evaluates user queries, flags high-risk behaviors, and debunks dangerous medical myths in a safe, disclaimer-bound environment.

✨ Key Features
💬 Dynamic Risk Evaluation Chat: Users can ask public health queries, and the Gemini 3.5 Flash model answers only using the verified context provided in the data folder.

🔬 Myth vs. Fact Lab: An interactive accordion dashboard debunking critical antibiotic fallacies.

🛡️ Regulatory Guardrails: Custom AI system instructions prevent the model from issuing clinical diagnoses or hallucinating beyond the provided datasets.

🎨 Bio-Tech Dark UI: A custom, fully responsive Streamlit interface designed for maximum readability and user engagement.

🛠️ Tech Stack
Frontend: Streamlit (Python)

LLM Engine: Google Gemini API (gemini-3.5-flash)

RAG Data Processing: pypdf (for real-time context extraction from official guideline PDFs)

Deployment: Streamlit Community Cloud
