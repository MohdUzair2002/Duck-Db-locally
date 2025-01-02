from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import duck_db_project_project


@dbt_assets(manifest=duck_db_project_project.manifest_path)
def duck_db_project_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    

