import numpy as np
from .PixelOE.pixeloe.pixelize import pixelize
from PIL import Image
from typing import Tuple, List, Union


def run(
    src: Image.Image,
    target_size: int = 256,
    patch_size: int = 8,
    pixel_size: int = 0,
    thickness: int = 2,
    colors: int = 0,
    contrast: float = 1.0,
    saturation: float = 1.0,
    mode: str = "contrast",
    color_quant_methon: str = "kmeans",
    color_matching: bool = True,
    poe_color_with_weight: bool = False,
    no_upscale: bool = False,
    no_downscale: bool = False,
) -> Tuple[Image.Image, List[List[Union[str, float]]]]:
    img = np.array(src)

    img = pixelize(
        img,
        mode,
        target_size,
        patch_size,
        pixel_size if pixel_size != 0 else None,
        thickness,
        color_matching,
        contrast,
        saturation,
        colors if colors != 0 else None,
        color_quant_methon,
        poe_color_with_weight,
        no_upscale,
        no_downscale,
    )

    return img
