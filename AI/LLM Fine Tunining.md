## LLM Fine-Tuning Tutorial (Step-by-Step)

### What is LLM Fine-Tuning?

Fine-tuning = training a pre-trained Large Language Model (LLM) on your own data so it:
- Speaks in your domain
- Follows your style
- Performs a specific task better

Example

| Task	| Without Fine-Tuning	| With Fine-Tuning | 
| ----- | ------------ | ---------- | 
| Medical Q&A | Generic answers	| Doctor-like responses | 
| Chatbot | Casual | Company tone | 
| Code generation | General	| Your codebase style | 

### When Should You Fine-Tune?

✅ Fine-tune if:
- You need domain-specific language
- You want consistent structured output
- Prompt engineering alone is not enough

❌ Don’t fine-tune if:
- You only need factual answers → use RAG
- Data is small (<100 examples) → use prompts

### Types of Fine-Tuning
1. Full Fine-Tuning ❌ (Expensive)
- Updates all model weights
- Needs huge GPU (A100)

2. Parameter-Efficient Fine-Tuning (PEFT) ✅ (Recommended)
- Updates only a small % of weights
- Much cheaper & faster

Popular PEFT methods
- LoRA ⭐
- QLoRA ⭐⭐
- Adapters

👉 We’ll use LoRA.

### Tech Stack (What We’ll Use)

- Python 3.10+
- PyTorch
- Hugging Face Transformers
- Datasets
- PEFT (LoRA)


## LLM Fine-Tuning Tutorial (Google Colab Edition)

**Goal:** Fine-tune a small LLM using LoRA on Google Colab
**Model:** TinyLlama/TinyLlama-1.1B-Chat-v1.0
**Use case:** Instruction-based chatbot

### 0️⃣ Colab Setup (IMPORTANT)

Step 0.1 – Enable GPU
- Colab → Runtime
- Change runtime type
- Hardware accelerator → GPU (T4)

### 1️⃣ Install Dependencies (Colab-Safe)

```bash
pip install -q torch transformers datasets peft accelerate bitsandbytes
```

Restart runtime if prompted.

### 2️⃣ Why TinyLlama?
| Feature | 	Reason | 
| ------ |  ------- | 
| Size	| 1.1B (fits free GPU) | 
| License | Open (no token) | 
| Architecture | LLaMA-like | 
| Training speed	| Fast | 

### 3️⃣ Prepare Training Dataset

Instruction-Tuning Format

Create a dataset where the model learns to:

Follow instructions and generate responses

Example Dataset

```python
import json

data = [
    {
        "instruction": "What is Python?",
        "output": "Python is a high-level, interpreted programming language."
    },
    {
        "instruction": "Explain list comprehension in Python.",
        "output": "List comprehension provides a concise way to create lists using expressions."
    },
    {
        "instruction": "What is a decorator in Python?",
        "output": "A decorator modifies the behavior of a function using the @ syntax."
    }
]

with open("train.json", "w") as f:
    json.dump(data, f, indent=2)

```

### 4️⃣ Load Model & Tokenizer
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    load_in_8bit=True,
    device_map="auto"
)

```

✅ Works on free Colab
✅ No authentication needed

### 5️⃣ Apply LoRA (Core Fine-Tuning Step)

Why LoRA?

- Train <1% parameters
- Faster
- Memory efficient

```python
from peft import LoraConfig, get_peft_model

lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05,
    bias="none",
    task_type="CAUSAL_LM"
)

model = get_peft_model(model, lora_config)
model.print_trainable_parameters()
```

Expected output:

```text
trainable params: ~4M
total params: ~1.1B
```

### 6️⃣ Load & Tokenize Dataset

```python
from datasets import load_dataset

dataset = load_dataset("json", data_files="train.json")

def format_prompt(example):
    return f"""### Instruction:
{example['instruction']}

### Response:
{example['output']}"""

def tokenize(example):
    prompt = format_prompt(example)
    return tokenizer(
        prompt,
        truncation=True,
        padding="max_length",
        max_length=512
    )

tokenized_dataset = dataset.map(tokenize)

7️⃣ Training Configuration (Colab-Optimized)
from transformers import TrainingArguments, Trainer

training_args = TrainingArguments(
    output_dir="./llm-finetune",
    per_device_train_batch_size=2,
    gradient_accumulation_steps=4,
    learning_rate=2e-4,
    num_train_epochs=3,
    fp16=True,
    logging_steps=5,
    save_strategy="epoch",
    report_to="none"
)

8️⃣ Train the Model 🚀
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset["train"]
)

trainer.train()


⏱️ Training time: 5–15 minutes

9️⃣ Test the Fine-Tuned Model
def generate(text):
    prompt = f"""### Instruction:
{text}

### Response:
"""
    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    
    outputs = model.generate(
        **inputs,
        max_new_tokens=100
    )
    
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generate("Explain generators in Python"))


🎉 You just fine-tuned an LLM on Colab!

🔍 What Actually Happened?
Step	Meaning
Pretrained model	General knowledge
LoRA	Injected task-specific behavior
Dataset	Taught instruction following
Trainer	Updated LoRA weights only
🧠 Common Colab Mistakes (Avoid These)

❌ Using LLaMA-2 without token
❌ Batch size too big
❌ Full fine-tuning
❌ Too little data (<50 samples)

🔁 Fine-Tuning vs RAG (Quick Interview Table)
Feature	Fine-Tuning	RAG
Style learning	✅	❌
Knowledge update	❌	✅
Cost	High	Low
Hallucination control	Medium	High
