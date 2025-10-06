#!/usr/bin/env python3

from demo_utils import get_best_device
from transformers import pipeline
import os

if not os.path.exists("data/harvard.wav"):
    raise Exception("data/harvard.wav does not exist.")

device = get_best_device()
speech_to_text = pipeline("automatic-speech-recognition", model="openai/whisper-small", device=device)

text = speech_to_text("data/harvard.wav")
print(text['text'])

