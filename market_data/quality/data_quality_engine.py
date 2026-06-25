import pandas as pd


# ==========================================================
# DATA QUALITY ENGINE
# ==========================================================

class DataQualityEngine:

    @staticmethod
    def missing_report(df):

        report = []

        for col in df.columns:

            report.append({

                "Column": col,

                "Missing_%":

                round(

                    df[col]

                    .isna()

                    .mean()

                    * 100,

                    2

                )

            })

        return pd.DataFrame(report)

    @staticmethod
    def outlier_report(
        df,
        column
    ):

        q1 = df[column].quantile(0.25)

        q3 = df[column].quantile(0.75)

        iqr = q3 - q1

        return (

            df[column]

            >

            q3 + 1.5 * iqr

        ).sum()