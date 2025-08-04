from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments
from trl import SFTTrainer
from peft import LoraConfig
from transformers import BitsAndBytesConfig

# ✅ Base LLaMA 3 model
model_name = "meta-llama/Meta-Llama-3-8B-Instruct"

# ✅ Load your training data
dataset = load_dataset("json", data_files="training_data.jsonl")

# ✅ Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token

# ✅ BitsAndBytes config for CPU
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=True,
    llm_int8_threshold=6.0
)

# ✅ Load model
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    quantization_config=bnb_config
)

# ✅ PEFT LoRA config
peft_config = LoraConfig(
    r=16,
    lora_alpha=32,
    lora_dropout=0.1,
    task_type="CAUSAL_LM"
)

# ✅ Training args
training_args = TrainingArguments(
    output_dir="./fine-tuned-llama3",
    per_device_train_batch_size=2,
    num_train_epochs=3,
    logging_steps=10,
    save_strategy="epoch",
    learning_rate=2e-4,
    bf16=False,
    save_total_limit=2
)

# ✅ Initialize trainer (no tokenizer or max_seq_length in old trl version)
trainer = SFTTrainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    peft_config=peft_config
)

# ✅ Train and save
trainer.train()
trainer.save_model("./fine-tuned-llama3")
tokenizer.save_pretrained("./fine-tuned-llama3")

print("\n✅ Fine-tuned model and tokenizer saved successfully.")
