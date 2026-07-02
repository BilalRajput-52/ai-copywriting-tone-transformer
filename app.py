"""
app.py
------
Streamlit UI for CopyCraft AI — the Automated Copywriting & Tone Transformer.

Flow: User Input -> Validation -> Prompt Builder -> LangChain Chain ->
Groq API -> LLM -> Generated Copy -> Display Output.
"""

import streamlit as st
from src.generator import generate_copy
from src.validator import ALLOWED_PLATFORMS, ALLOWED_TONES, ValidationError

st.set_page_config(page_title="CopyCraft AI", page_icon="🪶", layout="centered")

st.title("🪶 CopyCraft AI")
st.caption("Automated Copywriting & Tone Transformer — powered by LangChain + Groq (Llama 3.3 70B)")

st.divider()

# ---- Input (Ingestion Layer) ------------------------------------------------
st.subheader("1. Product Details")

col1, col2 = st.columns(2)
with col1:
    product_name = st.text_input("Product Name", placeholder="e.g. Samsung Galaxy S25")
    platform = st.selectbox("Platform", ALLOWED_PLATFORMS)
with col2:
    audience = st.text_input("Target Audience", placeholder="e.g. Students")
    tone = st.selectbox("Tone", ALLOWED_TONES)

benefits = st.text_area(
    "Key Benefits",
    placeholder="e.g. All-day battery life, stunning AI camera, ultra-fast performance",
)
cta = st.text_input("Call To Action (CTA)", placeholder="e.g. Buy Now")

st.subheader("2. Model Creativity")
c1, c2 = st.columns(2)
with c1:
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.05,
                             help="Higher = more creative/random output")
with c2:
    top_p = st.slider("Top-P", 0.0, 1.0, 0.9, 0.05,
                       help="Higher = more diverse word choices")

st.divider()

if st.button("✨ Generate Marketing Copy", type="primary", use_container_width=True):
    try:
        with st.spinner("CopyCraft AI is writing your copy..."):
            copy_text = generate_copy(
                product_name=product_name,
                platform=platform,
                tone=tone,
                audience=audience,
                benefits=benefits,
                cta=cta,
                temperature=temperature,
                top_p=top_p,
            )
        st.subheader("3. Generated Copy")
        st.text_area("Output", value=copy_text, height=300)
        st.download_button("Download as .txt", data=copy_text, file_name="marketing_copy.txt")
    except ValidationError as e:
        st.error(f"Input error: {e}")
    except ValueError as e:
        st.error(f"Configuration error: {e}")
    except Exception as e:
        st.error(f"Something went wrong while generating copy: {e}")
