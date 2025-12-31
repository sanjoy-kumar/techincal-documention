import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

# 1. Configuration
BASE_MODEL = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
LORA_ADAPTER_PATH = "./medium-article-generator"

# 2. Load Tokenizer
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)

# 3. Load Base Model
# Use 'device_map=None' if you have low VRAM to avoid the "meta device" error
# Use 'dtype' instead of the deprecated 'torch_dtype'
model = AutoModelForCausalLM.from_pretrained(
    BASE_MODEL,
    dtype=torch.float16,
    device_map="auto"
)

# 4. CRITICAL: Load the adapter using the 'PeftModel' wrapper
# directly to avoid the lm_head key mismatch
try:
    model = PeftModel.from_pretrained(model, LORA_ADAPTER_PATH)
    print("Successfully merged adapter weights.")
except Exception as e:
    print(f"Standard load failed, attempting fallback: {e}")
    # Fallback: Sometimes local paths need absolute references on Windows
    import os
    abs_path = os.path.abspath(LORA_ADAPTER_PATH)
    model = PeftModel.from_pretrained(model, abs_path)

model.eval()


def generate_article(title):
    prompt = f"### Instruction:\nWrite a Medium article about: {title}\n\n### Response:\n"
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=1024,        # Increased from 200/256
            temperature=0.8,           # Slightly higher for more "fresh" ideas
            repetition_penalty=1.15,   # STOPS the "What you're doing now" loop
            top_p=0.9,
            do_sample=True,
            eos_token_id=tokenizer.eos_token_id
        )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


if __name__ == "__main__":
    print(generate_article("The Future of Remote Work in 2026."))
