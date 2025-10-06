#!/usr/bin/env python3
from demo_utils import get_best_device
from transformers import pipeline

device = get_best_device()
pipeline = pipeline("text-generation", model="openai-community/gpt2", device=device)
prompt = "The secret to baking a good cake is "
print(prompt)
response = pipeline(prompt, max_length=50)
print(response)
