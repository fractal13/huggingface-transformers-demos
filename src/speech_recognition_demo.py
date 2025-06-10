#!/usr/bin/env python3

from transformers import pipeline

speech_to_text = pipeline("automatic-speech-recognition", model="openai/whisper-small")

text = speech_to_text("data/harvard.wav")
print(text['text'])

