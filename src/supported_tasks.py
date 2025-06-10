#!/usr/bin/env python3

from transformers.pipelines import PIPELINE_REGISTRY

print("Registered Tasks:")
for task in PIPELINE_REGISTRY.get_supported_tasks():
    print(task)

