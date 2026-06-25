# ==========================================================
# ORCHESTRATION DOMAIN MODELS
# ==========================================================

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


# ==========================================================
# PLATFORM RUN
# ==========================================================

@dataclass(slots=True)
class PlatformRun:

    run_id: str

    model_version: str

    config_version: str

    start_time: datetime

    end_time: Optional[datetime]

    status: str