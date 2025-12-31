import numpy as np
from scipy.signal import fftconvolve

def blur_image(x: np.ndarray, psf: np.ndarray) -> np.ndarray:
    y = fftconvolve(x, psf, mode="same")
    return np.clip(y, 0.0, 1.0)

def wiener_deconv(y: np.ndarray, psf: np.ndarray, K: float = 1e-3) -> np.ndarray:
    """Wiener deconvolution in the frequency domain."""
    h = np.zeros_like(y, dtype=np.float32)
    ph, pw = psf.shape
    h[:ph, :pw] = psf
    h = np.roll(h, -ph // 2, axis=0)
    h = np.roll(h, -pw // 2, axis=1)

    H = np.fft.fft2(h)
    Y = np.fft.fft2(y)

    X_hat = (np.conj(H) / (np.abs(H) ** 2 + K)) * Y
    x_hat = np.fft.ifft2(X_hat).real
    return np.clip(x_hat, 0.0, 1.0).astype(np.float32)
