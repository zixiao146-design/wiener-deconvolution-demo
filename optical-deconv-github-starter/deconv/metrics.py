import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def metrics(x_hat: np.ndarray, x: np.ndarray) -> tuple[float, float]:
    psnr = peak_signal_noise_ratio(x, x_hat, data_range=1.0)
    ssim = structural_similarity(x, x_hat, data_range=1.0)
    return float(psnr), float(ssim)
