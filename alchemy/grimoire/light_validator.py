from . import light_spellbook

def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = light_spellbook.light_spell_allowed_ingredients()
    lowercase_ingredients: str = ingredients.lower()

    if any(ingredient in lowercase_ingredients for ingredient in allowed):
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
