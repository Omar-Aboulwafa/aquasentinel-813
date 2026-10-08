"""SCL policy plus conservative all-contributor water support, without SciPy."""

import numpy as np
from numpy.typing import NDArray

from aquasentinel.preprocessing.alignment import NativeRasterWindow, warp_array
from aquasentinel.preprocessing.models import AnalysisGrid, SceneStatistics

INVALID_SCL = (0, 1, 2, 3, 7, 8, 9, 10, 11)
VALID_SCL = (4, 5, 6)
SUPPORT_POLICY = "native-3x3-water-erosion-plus-bilinear-all-support-v1"


def scl_masks(
    scl: NDArray[np.uint8], aoi: NDArray[np.bool_]
) -> tuple[NDArray[np.bool_], NDArray[np.bool_]]:
    return aoi & np.isin(scl, VALID_SCL), aoi & (scl == 6)


def erode_water(good: np.ndarray) -> np.ndarray:
    """Require all 3x3 native neighbours; outside the read window is invalid."""
    padded = np.pad(good, 1, constant_values=False)
    result = np.ones(good.shape, dtype=bool)
    for row in range(3):
        for column in range(3):
            result &= padded[row : row + good.shape[0], column : column + good.shape[1]]
    return result


def interpolation_support(
    native_water: NDArray[np.bool_], native: NativeRasterWindow, grid: AnalysisGrid
) -> NDArray[np.bool_]:
    # Zero is real bad support, NOT nodata: GDAL must not renormalize it away.
    eroded = erode_water(native_water).astype(np.float32)
    weights = warp_array(eroded, native, grid, nodata=None)
    return np.isfinite(weights) & (weights == np.float32(1))


def scene_statistics(
    aoi: NDArray[np.bool_],
    valid_data: NDArray[np.bool_],
    water: NDArray[np.bool_],
    valid_water: NDArray[np.bool_],
) -> SceneStatistics:
    aoi_count, data_count, water_count, valid_count = (
        int(np.count_nonzero(mask)) for mask in (aoi, valid_data, water, valid_water)
    )
    return SceneStatistics(
        aoi_count,
        data_count,
        water_count,
        valid_count,
        valid_count / aoi_count if aoi_count else None,
        valid_count / water_count if water_count else None,
    )
