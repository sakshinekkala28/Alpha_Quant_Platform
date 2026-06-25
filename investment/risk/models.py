# ==========================================================
# RISK DOMAIN MODELS
# ==========================================================

from __future__ import annotations

from dataclasses import dataclass


# ==========================================================
# RISK REPORT
# ==========================================================

@dataclass(slots=True)
class RiskReport:

    portfolio_beta: float

    tracking_error: float

    portfolio_volatility: float

    hhi: float

    effective_holdings: float