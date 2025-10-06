#!/usr/bin/env python3

import torch
def get_best_device():
    """Chooses the best device available.
    CUDA
    MPS
    CPU
    """
    if torch.cuda.is_available():
        # For NVIDIA GPUs
        return torch.device("cuda")
    elif torch.backends.mps.is_available():
        # For Apple Silicon (M1/M2/M3)
        return torch.device("mps")
    else:
        # Fallback to CPU
        return torch.device("cpu")

def main():
    best_device = get_best_device()
    print(f"The best device is {best_device}.")
    return

if __name__ == "__main__":
    main()
