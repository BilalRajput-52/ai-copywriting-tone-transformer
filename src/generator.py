"""
generator.py
------------
Top-level orchestration: validate inputs -> build dynamic prompt ->
invoke the LangChain chain -> return generated marketing copy.

This is the Model Client / Output layer described in the architecture:
it isolates the raw Streamlit UI from the LangChain + Groq internals.
"""

from src.validator import validate_inputs, ValidationError
from src.prompts import build_prompt_variables
from src.chains import build_chain


def generate_copy(
    product_name: str,
    platform: str,
    tone: str,
    audience: str,
    benefits: str,
    cta: str,
    temperature: float,
    top_p: float,
) -> str:
    """
    Run the full pipeline and return the generated marketing copy.

    Raises ValidationError if inputs are invalid, so the UI layer can
    show a friendly message instead of crashing.
    """
    clean_inputs = validate_inputs(
        product_name=product_name,
        platform=platform,
        tone=tone,
        audience=audience,
        benefits=benefits,
        cta=cta,
    )

    prompt_vars = build_prompt_variables(clean_inputs)
    chain = build_chain(temperature=temperature, top_p=top_p)

    result = chain.invoke(prompt_vars)
    return result.strip()
