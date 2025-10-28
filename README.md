# Keep It Simple and Scalable

This repository hosts the material for a workshop given at [Small Data SF](https://www.smalldatasf.com/) 2025.

During this workshop, you will use the Python library [dlt](https://github.com/dlt-hub/dlt) to build an extract, load, transform (ELT) pipeline for the [official GitHub REST API](https://docs.github.com/en/rest?apiVersion=2022-11-28).

We'll go through the full lifecyle of a data project:
1. Load data from a REST API
2. Ensure data quality via manual exploration and checks
3. Transform raw data into clean data and metrics 
4. Build a data product (e.g., report, web app)
5. Deploy the pipeline and data product

We'll introduce and suggest several tools throughout the workshop: dlt, [LLM scaffoldings](https://dlthub.com/workspace), [Continue](https://github.com/continuedev/continue), [duckdb](https://github.com/duckdb/duckdb), [Motherduck](https://motherduck.com/), [marimo](https://github.com/marimo-team/marimo/tree/main), [ibis](https://github.com/ibis-project/ibis)