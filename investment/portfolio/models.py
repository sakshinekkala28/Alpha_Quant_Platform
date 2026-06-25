# ==========================================================
# PORTFOLIO DOMAIN MODELS
# ==========================================================

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


# ==========================================================
# PORTFOLIO POSITION
# ==========================================================

@dataclass(slots=True)
class PortfolioPosition:

    symbol: str

    weight: float

    sector: str

    market_cap: float

    beta: float

    volatility: float


# ==========================================================
# PORTFOLIO
# ==========================================================

@dataclass(slots=True)
class Portfolio:

    portfolio_id: str

    holdings: int

    total_weight: float

    rebalance_date: datetime

    model_version: str