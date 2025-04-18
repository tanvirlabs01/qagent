from ctransformers import AutoModelForCausalLM

def load_model(model_path="models/mistral.gguf"):
    model = AutoModelForCausalLM.from_pretrained(
        model_path_or_repo_id=model_path,
        model_type="mistral",
        max_new_tokens=1024,
        temperature=0.7,
        repetition_penalty=1.1
    )
    return model
