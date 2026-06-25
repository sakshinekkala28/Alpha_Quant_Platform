# ==========================================================
# GOVERNANCE DOMAIN MODELS
# ==========================================================

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


# ==========================================================
# GOVERNANCE REPORT
# ==========================================================

@dataclass(slots=True)
class GovernanceReport:

    approved: bool

    position_limit_pass: bool

    sector_limit_pass: bool

    turnover_pass: bool

    concentration_pass: bool

    review_timestamp: datetime