# 维纳反卷积（Wiener Deconvolution）— 计算成像入门项目 / Computational Imaging Starter
本仓库是一个可复现的计算成像入门项目：模拟光学模糊（PSF 卷积）与噪声（Poisson + Gaussian），并使用 Wiener 反卷积进行图像恢复。运行后会输出 PSNR/SSIM 指标，并将原图/退化图/重建图保存到 `results/` 目录。

This repository is a minimal and reproducible computational imaging starter project: it simulates blur (PSF convolution) and noise (Poisson + Gaussian), then restores the image using Wiener deconvolution. It reports PSNR/SSIM and saves a side-by-side comparison figure to `results/`.
