# ==========================================================
# ALPHA DOMAIN MODELS
# ==========================================================

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


# ==========================================================
# SIGNAL
# ==========================================================

@dataclass(slots=True)
class Signal:

    symbol: str

    signal_score: float

    momentum_score: float

    quality_score: float

    value_score: float

    rank: int

    timestamp: datetime


# ==========================================================
# ALPHA MODEL RESULT
# ==========================================================

@dataclass(slots=True)
class AlphaModelResult:

    model_name: str

    model_version: str

    universe_size: int

    selected_stocks: int

    generated_at: datetime