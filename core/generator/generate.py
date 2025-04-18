from pathlib import Path
from core.generator.mistral_loader import load_model

def load_prompt_template(name: str) -> str:
    path = Path(__file__).parent / "prompts" / name
    if not path.exists():
        raise FileNotFoundError(f"Prompt template '{name}' not found.")
    return path.read_text(encoding="utf-8")

def generate_test_scenario(feature: str, template_name="test_plain.txt", max_tokens=1024, temperature=0.7, return_prompt=False):
    model = load_model()
    prompt_template = load_prompt_template(template_name)
    prompt = prompt_template.format(feature=feature)

    result = model(prompt, max_new_tokens=max_tokens, temperature=temperature)
    scenario = result.replace(prompt, "").strip()

    return (scenario, prompt) if return_prompt else scenario

