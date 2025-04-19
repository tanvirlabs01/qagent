from pathlib import Path
from ctransformers import AutoModelForCausalLM

model_path = "models/mistral.gguf"

model = AutoModelForCausalLM.from_pretrained(
    model_path,
    model_type="mistral",
    max_new_tokens=256,
    temperature=0.4,
)

def load_prompt_template(template_file: str = "playwright_convert.txt"):
    path = Path(__file__).parent / "prompts" / template_file
    return path.read_text(encoding="utf-8")

def convert_step_to_code(step: str) -> str:
    prompt = load_prompt_template().format(step=step.strip())
    result = model(prompt)
    return result.replace(prompt, "").strip()
