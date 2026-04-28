from typing import Any
import padnas as pd
from config import STORAGE_DIR

STORAGE_DIR.mkdir(parents=True, exist_ok=True)

dataset_registry: dict[str, dict[str, Any]] = {}
dataframes_cache: dict[str, pd.DataFrame] = {}
