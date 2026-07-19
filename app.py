import os
import streamlit as st
import google.generativeai as genai
from pypdf import PdfReader

# ==========================================
# 1. PAGE CONFIGURATION & UI STYLING
# ==========================================
st.set_page_config(
    page_title="AMR Risk Guard",
    page_icon="🧫",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom "Bio-Tech" Dark Mode CSS
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: #C9D1D9;
    }
    h1, h2, h3 {
        color: #00FF41 !important; /* Bio-tech neon green */
        font-family: 'Courier New', Courier, monospace;
    }
    .stAlert {
        background-color: #1A1C23;
        border-left: 4px solid #00FF41;
        color: #E6EDF3;
    }
    .warning-text {
        color: #FF5555;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 2. DATA LOADING (RAG CONTEXT)
# ==========================================
@st.cache_data(show_spinner=False)
def load_medical_guidelines():
    """Scans the 'data/' folder and extracts text from PDFs and TXT files."""
    context_text = ""
    data_dir = "data"
    
    if not os.path.exists(data_dir):
        return "No local data folder found. Operating on base knowledge only."

    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        
        # Read PDFs
        if filename.endswith(".pdf"):
            try:
                reader = PdfReader(filepath)
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        context_text += text + "\n"
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                
        # Read Text files
        elif filename.endswith(".txt"):
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    context_text += f.read() + "\n"
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    if not context_text:
        return "Data files are empty or unreadable."
    
    return context_text

medical_context = load_medical_guidelines()

# ==========================================
# 3. GEMINI API CONFIGURATION
# ==========================================
# Fetch API key from Streamlit Secrets
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
except KeyError:
    st.error("⚠️ GEMINI_API_KEY not found. Please add it to your Streamlit secrets.")
    st.stop()

# System prompt enforcing guardrails and RAG
system_instruction = f"""
You are "AMR Risk Guard", an AI public health assistant specializing in Antimicrobial Resistance (AMR).
Your primary goal is to educate users on antibiotic misuse based STRICTLY on the provided medical context.

MEDICAL CONTEXT:
{medical_context}

RULES:
1. ONLY answer questions using the facts provided in the MEDICAL CONTEXT above.
2. If the answer is not in the context, say: "I can only provide information based on official WHO/ICMR guidelines, and I do not have data on that specific query."
3. NEVER provide a medical diagnosis, prescribe medication, or tell a user to stop taking their prescribed medication.
4. Always urge users to consult a licensed doctor for personal medical advice.
5. Keep your answers concise, structured, and easy to read.
"""

# Initialize Gemini 3.5 Flash model
model = genai.GenerativeModel(
    model_name="gemini-3.5-flash",
    system_instruction=system_instruction
)

# ==========================================
# 4. FRONTEND LAYOUT
# ==========================================
st.title("🧫 AMR Risk Guard")
st.markdown("### AI-Powered Antimicrobial Resistance Evaluator")
st.markdown("""
<span class='warning-text'>⚠️ Disclaimer:</span> This tool is for educational purposes only. 
It utilizes WHO and ICMR guidelines to evaluate general AMR risks. It does not provide medical diagnoses.
""", unsafe_allow_html=True)
st.divider()

# Create interactive tabs
tab1, tab2 = st.tabs(["💬 Risk Evaluator (Chat)", "🔬 Myth vs. Fact Lab"])

# --- TAB 1: RISK EVALUATOR ---
with tab1:
    st.markdown("Ask a question about antibiotic usage, infections, or AMR risks.")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("E.g., Should I take antibiotics for a cold?"):
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        # Generate Gemini response
        with st.chat_message("assistant"):
            message_placeholder = st.empty()
            try:
                response = model.generate_content(prompt)
                message_placeholder.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
            except Exception as e:
                st.error(f"An error occurred: {e}")

# --- TAB 2: MYTH VS. FACT LAB ---
with tab2:
    st.markdown("### Common Antibiotic Fallacies")
    
    with st.expander("Myth: Antibiotics cure the common cold and flu."):
        st.write("**Fact:** Antibiotics only kill bacteria. The common cold and flu are caused by viruses. Taking antibiotics for viral infections will not cure the infection, keep other people from catching it, or help you feel better.")
        
    with st.expander("Myth: I can stop taking my antibiotics when I feel better."):
        st.write("**Fact:** Always complete the full course of your antibiotic prescription, even if you feel better. Stopping early can allow surviving bacteria to mutate and become resistant to the medication.")
        
    with st.expander("Myth: Antimicrobial resistance means my body is resistant to the drugs."):
        st.write("**Fact:** It is the *bacteria* that become resistant to the antibiotics, not humans or animals. These resistant bacteria can infect humans and are harder to treat.")

    with st.expander("Myth: I can save leftover antibiotics for next time I get sick."):
        st.write("**Fact:** Never save antibiotics for later or share them with others. Different infections require different antibiotics and dosages. Using the wrong one can delay proper treatment and promote resistance.")
