"""
prompts.py
----------
Holds the CopyCraft AI persona/system prompt and builds the dynamic
prompt template that user variables get injected into at runtime.
"""

from langchain_core.prompts import ChatPromptTemplate

SYSTEM_PROMPT = """You are CopyCraft AI, an expert marketing copywriter with over 15 years of experience.
Your responsibility is to create highly engaging, persuasive, and platform-optimized marketing copy.
You must adapt your writing according to: Platform, Target audience, Tone, Product description,
Product benefits, and CTA.

Rules:
- Never produce generic copy.
- Every output must sound natural.
- Write in fluent English.
- Use persuasive psychology.
- Use storytelling whenever appropriate.
- Highlight product benefits instead of features.
- End with a strong call to action.
- Optimize copy according to platform.

Platform Rules:
Instagram: Short, engaging, emojis allowed, hashtags.
LinkedIn: Professional, business tone, no emojis, clear structure.
Email: Subject line, greeting, body, CTA, signature.
Twitter: Maximum 280 characters.

Output only the final marketing copy. Do not add explanations, notes, or preambles."""

# Extra per-platform formatting reminders injected into the human turn,
# so the model has the rule right next to the actual task variables.
PLATFORM_INSTRUCTIONS = {
    "Instagram": (
        "Format: a short, punchy caption with tasteful emojis and 3-5 "
        "relevant hashtags at the end."
    ),
    "LinkedIn": (
        "Format: a professional post with a clear structure (hook, body, "
        "closing line). No emojis."
    ),
    "Email": (
        "Format: include a Subject line, a Greeting, a Body, a clear CTA, "
        "and a Signature."
    ),
    "Twitter": (
        "Format: a single tweet, strictly 280 characters or fewer, "
        "punchy and shareable."
    ),
}

USER_TEMPLATE = """Generate a {tone} {platform} marketing copy for the following product.

Product Name: {product_name}
Target Audience: {audience}
Key Benefits: {benefits}
Call To Action: {cta}

{platform_instructions}"""


def build_prompt_template() -> ChatPromptTemplate:
    """Build the reusable chat prompt template (system + human turns)."""
    return ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("human", USER_TEMPLATE),
        ]
    )


def build_prompt_variables(clean_inputs: dict) -> dict:
    """
    Merge validated user inputs with the platform-specific formatting
    instructions, producing the variable dict the template expects.
    """
    platform = clean_inputs["platform"]
    return {
        "tone": clean_inputs["tone"],
        "platform": platform,
        "product_name": clean_inputs["product_name"],
        "audience": clean_inputs["audience"],
        "benefits": clean_inputs["benefits"],
        "cta": clean_inputs["cta"],
        "platform_instructions": PLATFORM_INSTRUCTIONS.get(platform, ""),
    }
