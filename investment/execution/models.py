# ==========================================================
# EXECUTION DOMAIN MODELS
# ==========================================================

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


# ==========================================================
# TRADE
# ==========================================================

@dataclass(slots=True)
class Trade:

    symbol: str

    action: str

    current_weight: float

    target_weight: float

    trade_weight: float


# ==========================================================
# EXECUTION REPORT
# ==========================================================

@dataclass(slots=True)
class ExecutionReport:

    total_trades: int

    turnover: float

    average_slippage_bps: float

    market_impact_bps: float

    execution_timestamp: datetime