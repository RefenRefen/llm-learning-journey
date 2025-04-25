# 🚀 LLM Learning Journey

Welcome! This is a structured 6-week plan to master Large Language Models (LLMs) from the ground up — from Transformer math to pretraining, fine-tuning, deployment, and safety.

---

## 📅 Weekly Schedule

### ✅ Week 1: Architectures & Pretraining Objectives
- [ ] Read "Attention is All You Need"
- [ ] Study GPT-2, T5, PaLM, Chinchilla
- [ ] Summarize 5 key models: size, tokenizer, dataset, objective
- [ ] Build `model_table.csv`

### ✅ Week 2: Tokenization + Pretraining
- [ ] Explore BPE, WordPiece, SentencePiece
- [ ] Tokenize your dataset
- [ ] Pretrain a tiny GPT (~1–10M params)
- [ ] Save a loss plot & generation sample

### ✅ Week 3: Fine-Tuning + Instruction Tuning
- [ ] Understand SFT and datasets like Alpaca, Dolly
- [ ] Apply QLoRA or PEFT to Mistral-7B / LLaMA-7B
- [ ] Fine-tune and evaluate outputs

### ✅ Week 4: Inference, Quantization, Serving
- [ ] Quantize a model using GPTQ/QLoRA
- [ ] Serve it using vLLM or TGI
- [ ] Compare inference speed & quality

### ✅ Week 5: Prompt Engineering + RAG
- [ ] Learn few-shot, CoT, ReAct prompts
- [ ] Build a RAG bot with FAISS + embeddings
- [ ] Run it on your own markdown/PDF notes

### ✅ Week 6: Evaluation + Safety + LLMOps
- [ ] Use `lm-eval-harness` or HELM
- [ ] Try preference tuning (DPO)
- [ ] Add `wandb` for training logs & metrics

---

## 🧰 Requirements
Install everything you need:
```bash
pip install -r requirements.txt
```

---

## 🌟 Bonus Goals (Optional)
- [ ] Train a model with FlashAttention
- [ ] Serve it in a Streamlit or Gradio UI
- [ ] Join HuggingFace or EleutherAI Discords
- [ ] Write a blog post on your experience

---

## 📌 Notes
All weekly notes, scripts, and experiments will live in their respective folders.

Happy building! 💥
