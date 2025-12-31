import numpy as np

def add_gaussian_noise(img: np.ndarray, sigma: float = 0.01) -> np.ndarray:
    n = np.random.normal(0.0, sigma, img.shape).astype(np.float32)
    return np.clip(img + n, 0.0, 1.0)

def add_poisson_noise(img: np.ndarray, peak: float = 30.0) -> np.ndarray:
    """Poisson noise; larger peak -> relatively less noise."""
    img_scaled = np.clip(img, 0, 1) * peak
    noisy = np.random.poisson(img_scaled).astype(np.float32) / peak
    return np.clip(noisy, 0.0, 1.0)
