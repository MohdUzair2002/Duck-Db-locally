from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import duckdb_dev_project


@dbt_assets(manifest=duckdb_dev_project.manifest_path)
def duckdb_dev_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    

