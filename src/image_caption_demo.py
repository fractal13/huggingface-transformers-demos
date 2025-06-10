#!/usr/bin/env python3
from transformers import pipeline

image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")
text = image_to_text("data/image.png")
print(text[0]['generated_text'])
