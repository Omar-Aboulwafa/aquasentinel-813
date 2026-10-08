from datetime import UTC, datetime
from hashlib import sha256

import numpy as np
import pytest
from rasterio import Affine

from aquasentinel.ingestion.sentinel2_assets import (
    BANDS,
    ObservationIdentity,
    ResolvedOpticalSource,
)
from aquasentinel.preprocessing.masks import scene_statistics
from aquasentinel.preprocessing.models import AnalysisGrid, PreprocessedOpticalScene
from aquasentinel.provenance import DerivedProductRecord, SourceRecord


@pytest.fixture
def make_optical():
    def make(*, values=None, mask=None):
        water = np.ones((2, 6), bool) if mask is None else np.asarray(mask, dtype=bool).copy()
        shape = water.shape
        defaults = {"B02": 0.08, "B03": 0.06, "B04": 0.02, "B05": 0.05, "B06": 0.04}
        bands = {
            band: np.broadcast_to((values or {}).get(band, defaults.get(band, 0.03)), shape)
            .astype(np.float32)
            .copy()
            for band in BANDS
        }
        acquired = datetime(2023, 4, 28, 6, 46, 29, 24000, tzinfo=UTC)
        pc = SourceRecord("pc-source", "sentinel-2b", "pc-product", acquired, "test-pc")
        cdse = SourceRecord("cdse-discovery", "sentinel-2b", "cdse-product", acquired, "test-cdse")
        grid = AnalysisGrid(
            "EPSG:32640",
            Affine(20, 0, 200000, 0, -20, 2800000),
            shape[1],
            shape[0],
            20,
            (200000, 2800000 - shape[0] * 20, 200000 + shape[1] * 20, 2800000),
            "synthetic-grid",
        )
        parameters = {
            "identity": {"processing_version": "as102-v1", "decoding": {}},
            "source_grids": {},
        }
        cache_id = sha256(b"synthetic-as102-parent").hexdigest()
        provenance = DerivedProductRecord(
            "optical:" + cache_id,
            "preprocessed_optical_scene",
            datetime(2026, 10, 8, tzinfo=UTC),
            "as102-v1",
            (pc.source_id,),
            parameters,
        )
        source = ResolvedOpticalSource(
            pc,
            cdse,
            ObservationIdentity(acquired, "sentinel-2b", "40RBN", 20),
            "05.09",
            "2023-04-28T12:23:11Z",
            {},
            (),
            {},
        )
        ones = np.ones(shape, bool)
        result = PreprocessedOpticalScene(
            source,
            grid,
            bands,
            np.full(shape, 6, np.uint8),
            ones.copy(),
            ones.copy(),
            water.copy(),
            water,
            ones.copy(),
            scene_statistics(ones, ones, water, water),
            parameters,
            cache_id,
            provenance,
        )
        result.validate()
        return result

    return make


@pytest.fixture
def parent(make_optical):
    return make_optical()
