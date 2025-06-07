# Customs Insights

This sample project demonstrates how to process customs data and generate simple commercial intelligence indicators.

Replace `customs_data.csv` with your own data to analyze real import and export activity.

## Requirements

- Python 3
- pandas

Install the dependency with:

```bash
pip install pandas
```

## Usage

Run the analysis script from the `customs_insights` directory:

```bash
python analysis.py
```

The script prints metrics for the latest year found in the dataset, such as top countries and products by import and export values and the trade balance for each country.
