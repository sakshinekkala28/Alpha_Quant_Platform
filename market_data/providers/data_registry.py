from dataclasses import dataclass


# ==========================================================
# DATA SOURCE
# ==========================================================

@dataclass
class DataSource:

    name: str

    priority: int

    refresh_frequency: str

    enabled: bool = True


# ==========================================================
# DATA REGISTRY
# ==========================================================

class DataRegistry:

    def __init__(self):

        self.sources = [

            DataSource(
                "NSE",
                1,
                "DAILY"
            ),

            DataSource(
                "SCREENER",
                2,
                "WEEKLY"
            ),

            DataSource(
                "YFINANCE",
                3,
                "DAILY"
            )

        ]

    def active_sources(self):

        return [

            s

            for s in self.sources

            if s.enabled

        ]