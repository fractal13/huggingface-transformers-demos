#!/usr/bin/env python3
from demo_utils import get_best_device
from transformers import pipeline

device = get_best_device()
pipeline = pipeline("zero-shot-classification", device=device)
prompt = "It's 6:00, I get to start class now. This is a blast."
print(prompt)
response = pipeline(prompt, candidate_labels=["excited", "bored", "sleepy"])
print(response)
