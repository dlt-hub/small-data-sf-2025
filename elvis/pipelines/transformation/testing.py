import dlt
import pandas as pd
from dlt.sources.sql_database import sql_database

pipeline = dlt.pipeline(
    pipeline_name="elvis",
    destination="duckdb",
    dataset_name="small_data",
)
source = sql_database()

stars: dlt.Relation = pipeline.dataset().table("stars")
df: pd.DataFrame = stars.select(
    "repo_name",
    "star_count",
    "year",
    "month",
).df()
print(df)
