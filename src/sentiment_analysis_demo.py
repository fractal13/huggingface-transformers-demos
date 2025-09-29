#!/usr/bin/env python3

from transformers import pipeline

pipeline = pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english", device="cuda")
prompt = "It's 6:00, I get to start class now. This is a blast."
print(prompt)
response = pipeline(prompt)
print(response)

