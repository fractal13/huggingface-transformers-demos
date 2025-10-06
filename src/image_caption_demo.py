#!/usr/bin/env python3
from demo_utils import get_best_device
from transformers import pipeline

device = get_best_device()
image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base", device=device)
text = image_to_text("data/image.png")
print(text[0]['generated_text'])
