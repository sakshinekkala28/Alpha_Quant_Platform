from market_data.providers.data_registry import DataRegistry

from market_data.universe.security_master_engine import SecurityMaster

from market_data.quality.data_quality_engine import DataQualityEngine

from core.feature_store import FeatureStore


# ==========================================================
# DATA ENGINE
# ==========================================================

class DataEngine:

    def __init__(self):

        self.registry = DataRegistry()

        self.feature_store = FeatureStore()

    def run(
        self,
        security_master
    ):

        security_master = (

            SecurityMaster

            .build_master(
                security_master
            )

        )

        quality = (

            DataQualityEngine

            .missing_report(
                security_master
            )

        )

        self.feature_store.register(

            "security_master",

            security_master

        )

        return {

            "Security_Master":
            security_master,

            "Quality":
            quality

        }