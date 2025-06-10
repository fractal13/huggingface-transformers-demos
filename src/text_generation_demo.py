#!/usr/bin/env python3

from transformers import pipeline

pipeline = pipeline("text-generation", model="openai-community/gpt2", device="cuda")
prompt = "The secret to baking a good cake is "
print(prompt)
response = pipeline(prompt, max_length=50)
print(response)
