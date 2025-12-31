import numpy as np
import cv2

def read_gray(path: str, resize: int | None = None) -> np.ndarray:
    """Read grayscale image and normalize to [0, 1].

    Uses np.fromfile + cv2.imdecode to support Windows paths with Chinese characters.
    """
    data = np.fromfile(path, dtype=np.uint8)
    img = cv2.imdecode(data, cv2.IMREAD_GRAYSCALE)
    if img is None:
        raise FileNotFoundError(f"Cannot decode image: {path}")
    if resize is not None:
        img = cv2.resize(img, (resize, resize), interpolation=cv2.INTER_AREA)
    return img.astype(np.float32) / 255.0
