"""
validator.py
------------
Validates and sanitizes raw user input before it is ever injected into
a prompt template. This keeps the "Ingestion Layer" clean and prevents
empty/garbage values from reaching the LLM.
"""

ALLOWED_PLATFORMS = ["Instagram", "LinkedIn", "Email", "Twitter"]
ALLOWED_TONES = ["Professional", "Friendly", "Luxury", "Technical", "Persuasive", "Casual"]


class ValidationError(Exception):
    """Raised when user input fails validation."""
    pass


def _clean(text: str) -> str:
    """Strip whitespace and collapse it to a single string."""
    return " ".join(text.strip().split()) if text else ""


def validate_inputs(
    product_name: str,
    platform: str,
    tone: str,
    audience: str,
    benefits: str,
    cta: str,
) -> dict:
    """
    Validate all fields required to build a marketing copy prompt.

    Returns a dict of cleaned values on success.
    Raises ValidationError on failure, with a message safe to show in the UI.
    """
    product_name = _clean(product_name)
    audience = _clean(audience)
    benefits = _clean(benefits)
    cta = _clean(cta)

    if not product_name:
        raise ValidationError("Product name cannot be empty.")

    if not benefits:
        raise ValidationError("Please describe at least one product benefit.")

    if not cta:
        raise ValidationError("Please provide a call to action (CTA).")

    if platform not in ALLOWED_PLATFORMS:
        raise ValidationError(f"Platform must be one of: {', '.join(ALLOWED_PLATFORMS)}")

    if tone not in ALLOWED_TONES:
        raise ValidationError(f"Tone must be one of: {', '.join(ALLOWED_TONES)}")

    if not audience:
        audience = "General audience"

    return {
        "product_name": product_name,
        "platform": platform,
        "tone": tone,
        "audience": audience,
        "benefits": benefits,
        "cta": cta,
    }
