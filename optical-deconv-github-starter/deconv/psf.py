import numpy as np

def gaussian_psf(size: int = 31, sigma: float = 2.0) -> np.ndarray:
    """Create a normalized 2D Gaussian PSF."""
    ax = np.arange(-(size // 2), size // 2 + 1)
    xx, yy = np.meshgrid(ax, ax)
    psf = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    psf /= psf.sum()
    return psf.astype(np.float32)
