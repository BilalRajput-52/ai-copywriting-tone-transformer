"""
chains.py
---------
Builds the LangChain (LCEL) chain that ties the prompt template to the
Groq-hosted LLM and parses the output back into plain text.
"""

from langchain_core.output_parsers import StrOutputParser
from src.config import get_llm
from src.prompts import build_prompt_template


def build_chain(temperature: float, top_p: float):
    """
    Construct the Orchestration Engine: Prompt -> LLM -> Output Parser.

    Returns a Runnable that accepts the prompt variables dict and
    returns the generated copy as a plain string.
    """
    prompt = build_prompt_template()
    llm = get_llm(temperature=temperature, top_p=top_p)
    parser = StrOutputParser()

    return prompt | llm | parser
