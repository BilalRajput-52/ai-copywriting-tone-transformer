"""
config.py
---------
Handles LLM configuration and instantiation.

Reads the Groq API key from the environment (.env file) and builds a
ChatGroq client with the inference parameters (Temperature, Top-P)
that the user controls from the Streamlit UI.
"""

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# Load variables from .env into the environment
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Llama 3.3 70B Versatile — good balance of quality and speed on Groq
MODEL_NAME = "llama-3.3-70b-versatile"

# Sensible defaults if the user doesn't touch the sliders
DEFAULT_TEMPERATURE = 0.7
DEFAULT_TOP_P = 0.9


def get_llm(temperature: float = DEFAULT_TEMPERATURE, top_p: float = DEFAULT_TOP_P) -> ChatGroq:
    """
    Build and return a configured ChatGroq LLM client.

    Parameters
    ----------
    temperature : float
        Controls randomness/creativity of the output (0.0 - 1.0).
    top_p : float
        Controls nucleus sampling diversity (0.0 - 1.0).
    """
    if not GROQ_API_KEY:
        raise ValueError(
            "GROQ_API_KEY not found. Create a .env file (see .env.example) "
            "and add your Groq API key before running the app."
        )

    return ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=temperature,
        model_kwargs={"top_p": top_p},
    )
