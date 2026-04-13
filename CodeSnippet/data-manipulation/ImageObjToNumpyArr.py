from PIL import Image
from pathlib import Path
import numpy as np


proj_root = Path(__file__).absolute().parent
img_dir = proj_root / "data" / "Figure_1.png"
image = Image.open(img_dir).convert("RGB")
print(image.format)
print(image.mode)
print(image.width, " * ", image.height)
print(image.info)

arr = np.array(image)
print(arr.shape)

pixel = arr[200, 100]
print(pexel)

gray = np.mean(arr, axis=2)
binary = (gray < 120).astype(np.uint8) * 255

binary_image = Image.fromarray(binary)