# PART 1 - data loading
from elvis.helpers.cloudflare.dlt_client import load_json_to_cloudflare_r2

# PART 1A
from dlt.common.configuration.specs import AwsCredentials

# PART 1B
import dlt
import os

os.environ["DATA_WRITER__DISABLE_COMPRESSION"] = "True"
dlt.config["data_writer.disable_compression"] = True

pipeline: dlt.Pipeline = dlt.pipeline(
    pipeline_name="pipeline_name",
    destination=dlt.destinations.filesystem(
        bucket_url="s3://bucket_name",
        credentials=object,
        client_kwargs={
            "endpoint_url": "endpoint_url",
        },
    ),
    dataset_name="dataset_name",
)


# PART 2
# ```sql
# dlt init sql_database duckdb --eject
# ````

# sets up scaffolding for loading data from sql
