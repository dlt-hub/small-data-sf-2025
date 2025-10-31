"""Template for building a `dlt` pipeline to ingest data from a REST API."""

import dlt
from dlt.sources.rest_api import rest_api_resources
from dlt.sources.rest_api.typing import RESTAPIConfig

# if no argument is provided, `access_token` is read from `.dlt/secrets.toml`
@dlt.source
def rest_api_source(access_token: str = dlt.secrets.value):
    """Define dlt resources from REST API endpoints."""
    config: RESTAPIConfig = {
        "client": {
            "base_url": "https://api.github.com",
            "auth": {"type": "bearer", "token": access_token},
            "headers": {"Accept": "application/vnd.github.v3+json"}
        },
        "resources": [
            {
                "name": "workflow_runs",
                "endpoint": {
                    "path": "repos/apache/hamilton/actions/runs",
                    "method": "GET",
                    "params": {"per_page": 100},
                    "data_selector": "workflow_runs",
                    "paginator": {"type": "header_link"}
                }
            }
        ],
        "resource_defaults": {
            "primary_key": "id",
            "write_disposition": "merge"
        }
    }

    yield from rest_api_resources(config)


pipeline = dlt.pipeline(
    pipeline_name="github_api_ingest",
    destination="duckdb",
    # `dev_mode=True` creates a new namespace for each pipeline run.
    # set to `False` once you have a working pipeline.
    dev_mode=True,
    # `refresh="drop_sources"` ensures the data and the state is cleaned
    # on each `pipeline.run()`; remove the argument once you have a
    # working pipeline.
    refresh="drop_sources",
)


if __name__ == "__main__":
    load_info = pipeline.run(rest_api_source())
    print(load_info)
