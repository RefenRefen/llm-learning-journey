# Sample pretraining loop for a tiny GPT using HuggingFace
from transformers import GPT2Config, GPT2LMHeadModel, Trainer, TrainingArguments, TextDataset, DataCollatorForLanguageModeling

model = GPT2LMHeadModel(GPT2Config(n_embd=128, n_layer=2, n_head=2))
train_dataset = TextDataset(file_path="sample.txt", block_size=64, tokenizer=..., overwrite_cache=True)
data_collator = DataCollatorForLanguageModeling(tokenizer=..., mlm=False)

trainer = Trainer(
    model=model,
    args=TrainingArguments(output_dir="./gpt-small", per_device_train_batch_size=8, num_train_epochs=1),
    train_dataset=train_dataset,
    data_collator=data_collator,
)
trainer.train()