import pandas as pd
import numpy as np

def app_trends_by_period(apps: pd.DataFrame, freq: str = "W") -> pd.DataFrame:

    df= apps.copy()
    df["submitted"] = 1
    df["approved"] = df["approved_date"].notna().astype(int) # 1 if approved, 0 if approved_date is blank
    df["used"] = (df["dollars_used"] > 0).astype(int)

    summaryTable = (
        df.set_index("submit_date")
            .resample(freq)
            .agg(
                applications=("submitted","sum"),
                approved=("approved", "sum"),
                used=("used", "sum"),
                avg_approved_amount = ("approved_amount", "mean"),
                avg_used_amount = ("dollars_used", "mean")
            )
            .reset_index()
    )

    return summaryTable

def app_metrics_by_store(apps: pd.DataFrame) -> pd.DataFrame:

    df= apps.copy()
    df["submitted"] = 1
    df["approved"] = df["approved_date"].notna().astype(int) # 1 if approved, 0 if approved_date is blank
    df["used"] = (df["dollars_used"] > 0).astype(int)
    df["pct_used"] = df["dollars_used"] / df["approved_amount"]

    summaryTable = (
        df.groupby("store", dropna=False)
            .agg(
                applications=("submitted","sum"),
                approved=("approved", "sum"),
                used=("used", "sum"),
                avg_approved_amount = ("approved_amount", "mean"),
                avg_used_amount = ("dollars_used", "mean"),
                avg_pct_used=("pct_used", "mean")
            )
            .reset_index()
    )

    return summaryTable


def app_metrics_by_Mktg(apps: pd.DataFrame) -> pd.DataFrame:

    df= apps.copy()

    summaryTable = (
        df.groupby("name", dropna=False)
            .agg(
                used_amount = ("dollars_used", "sum"),
                marketing_spend=("spend", "max")
            )
            .reset_index()
    )

    return summaryTable