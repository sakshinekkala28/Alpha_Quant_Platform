# ==========================================================
# SECURITY MASTER
# ==========================================================

class SecurityMaster:

    @staticmethod
    def build_master(
        security_df
    ):

        security_df = (

            security_df

            .drop_duplicates(
                subset=["Symbol"]
            )

        )

        security_df["Symbol"] = (

            security_df["Symbol"]

            .astype(str)

            .str.upper()

        )

        return security_df

    @staticmethod
    def validate(
        security_df
    ):

        duplicates = (

            security_df["Symbol"]

            .duplicated()

            .sum()

        )

        return {

            "Duplicates": duplicates,

            "Total": len(security_df)

        }