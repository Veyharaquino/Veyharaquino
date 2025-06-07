import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load customs data from a CSV file."""
    return pd.read_csv(file_path)


def compute_metrics(df: pd.DataFrame, year: int) -> dict:
    """Compute basic commercial intelligence indicators for a given year."""
    df_year = df[df["Year"] == year]

    imports_by_country = (
        df_year.groupby("Country")["ImportValue"].sum().sort_values(ascending=False)
    )
    exports_by_country = (
        df_year.groupby("Country")["ExportValue"].sum().sort_values(ascending=False)
    )
    balance_by_country = (
        exports_by_country - imports_by_country
    ).sort_values(ascending=False)

    imports_by_product = (
        df_year.groupby("Product")["ImportValue"].sum().sort_values(ascending=False)
    )
    exports_by_product = (
        df_year.groupby("Product")["ExportValue"].sum().sort_values(ascending=False)
    )

    metrics = {
        "Top Import Countries": imports_by_country.head(5),
        "Top Export Countries": exports_by_country.head(5),
        "Trade Balance by Country": balance_by_country,
        "Top Import Products": imports_by_product.head(5),
        "Top Export Products": exports_by_product.head(5),
    }
    return metrics


def print_metrics(metrics: dict, year: int) -> None:
    """Print metrics to the console."""
    print(f"Commercial Intelligence Indicators for {year}\n")
    for name, series in metrics.items():
        print(name)
        print(series.to_string())
        print()


def main() -> None:
    df = load_data("customs_data.csv")
    latest_year = df["Year"].max()
    metrics = compute_metrics(df, latest_year)
    print_metrics(metrics, latest_year)


if __name__ == "__main__":
    main()
