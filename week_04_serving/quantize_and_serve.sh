#!/bin/bash
# Quantize and run LLaMA/Mistral with vLLM

python convert_to_gguf.py --model-path /path/to/hf-model --output-path ./quant-model.gguf
python serve.py --model ./quant-model.gguf --port 8080