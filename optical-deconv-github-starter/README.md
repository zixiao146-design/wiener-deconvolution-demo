# Optical Deconvolution (Wiener) — starter project

A tiny, beginner-friendly **computational imaging** project: simulate blur + noise and recover the image using **Wiener deconvolution**.

This repo is intentionally simple and reproducible. It also works on Windows paths containing Chinese characters by using `cv2.imdecode` instead of `cv2.imread`.

## What it does

- Reads an image (grayscale, normalized to [0, 1])
- Blurs it with a Gaussian PSF (via FFT convolution)
- Adds Poisson + Gaussian noise
- Recovers via Wiener deconvolution
- Reports PSNR / SSIM
- Saves a comparison figure to `results/`

---

## Quickstart

### 1) Create a virtual environment (recommended)

**Windows (PowerShell)**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Tip: If you ever see binary-compatibility errors, recreate the venv and reinstall requirements.

### 2) Put an input image

Place an image at:

- `data/test.png`

(or use `--image` to point to any image file)

### 3) Run

```bash
python scripts/run_demo.py
```

Outputs:

- `results/deconv_result.png`

---

## CLI options

```bash
python scripts/run_demo.py --help
```

Examples:

```bash
# Try a larger K (often improves over noisy when noise is strong)
python scripts/run_demo.py --k 1e-2

# Change blur strength
python scripts/run_demo.py --psf-sigma 3.0 --psf-size 41

# Use a different input image
python scripts/run_demo.py --image "D:\\images\\my_photo.png"
```

---

## Project structure

```
optical-deconv-github-starter/
  deconv/
    __init__.py
    io_utils.py
    psf.py
    noise.py
    wiener.py
    metrics.py
  scripts/
    run_demo.py
  data/
    .gitkeep
  results/
    .gitkeep
  requirements.txt
  .gitignore
  LICENSE
```

---

## Notes for beginners

- **PSF (h)**: “one point becomes what blur spot”
- Forward model: `y = x * h + n`
- In frequency domain: `Y = X·H + N`
- Wiener filter: `X̂ = (H* / (|H|^2 + K)) · Y`

`K` controls noise amplification vs detail recovery:
- too small → ringing/noise amplified
- too large → too smooth

---

## License

MIT — see `LICENSE`.
