import argparse
import os
import numpy as np

# Use non-GUI backend (safe for PyCharm/Windows setups)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from deconv.io_utils import read_gray
from deconv.psf import gaussian_psf
from deconv.noise import add_gaussian_noise, add_poisson_noise
from deconv.wiener import blur_image, wiener_deconv
from deconv.metrics import metrics

def parse_args():
    p = argparse.ArgumentParser(description="Simulate blur+noise and recover with Wiener deconvolution.")
    p.add_argument("--image", default=os.path.join("data", "test.png"), help="Input image path (grayscale or color).")
    p.add_argument("--out", default=os.path.join("results", "deconv_result.png"), help="Output figure path.")
    p.add_argument("--seed", type=int, default=0, help="Random seed for reproducibility.")
    p.add_argument("--psf-size", type=int, default=31, help="Gaussian PSF size (odd).")
    p.add_argument("--psf-sigma", type=float, default=2.0, help="Gaussian PSF sigma.")
    p.add_argument("--peak", type=float, default=30.0, help="Poisson peak (larger => less noise).")
    p.add_argument("--gauss-sigma", type=float, default=0.01, help="Gaussian noise sigma.")
    p.add_argument("--k", type=float, default=1e-3, help="Wiener K (noise-to-signal parameter).")
    p.add_argument("--resize", type=int, default=None, help="Optional resize to NxN (e.g., 256).")
    return p.parse_args()

def main():
    args = parse_args()
    np.random.seed(args.seed)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)

    x = read_gray(args.image, resize=args.resize)
    psf = gaussian_psf(size=args.psf_size, sigma=args.psf_sigma)

    y_blur = blur_image(x, psf)
    y_noisy = add_poisson_noise(y_blur, peak=args.peak)
    y_noisy = add_gaussian_noise(y_noisy, sigma=args.gauss_sigma)

    x_wiener = wiener_deconv(y_noisy, psf, K=args.k)

    psnr_y, ssim_y = metrics(y_noisy, x)
    psnr_w, ssim_w = metrics(x_wiener, x)

    print(f"Noisy   PSNR={psnr_y:.2f}  SSIM={ssim_y:.3f}")
    print(f"Wiener  PSNR={psnr_w:.2f}  SSIM={ssim_w:.3f}")
    print(f"Saved:  {args.out}")

    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].imshow(x, cmap="gray"); axes[0].set_title("Original"); axes[0].axis("off")
    axes[1].imshow(y_noisy, cmap="gray"); axes[1].set_title("Blur + Noise"); axes[1].axis("off")
    axes[2].imshow(x_wiener, cmap="gray"); axes[2].set_title(f"Wiener (K={args.k:g})"); axes[2].axis("off")
    plt.tight_layout()
    plt.savefig(args.out, dpi=200)
    plt.close()

if __name__ == "__main__":
    main()
