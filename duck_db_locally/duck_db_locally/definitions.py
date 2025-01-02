from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import duckdb_dev_dbt_assets
from .project import duckdb_dev_project
from .schedules import schedules

defs = Definitions(
    assets=[duckdb_dev_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=duckdb_dev_project),
    },
)

