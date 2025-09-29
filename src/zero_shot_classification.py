#!/usr/bin/env python3

from transformers import pipeline

pipeline = pipeline("zero-shot-classification", device="cuda")
prompt = "It's 6:00, I get to start class now. This is a blast."
print(prompt)
response = pipeline(prompt, candidate_labels=["excited", "bored", "sleepy"])
print(response)


