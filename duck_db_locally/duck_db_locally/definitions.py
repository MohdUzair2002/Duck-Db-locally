from dagster import Definitions
from dagster_dbt import DbtCliResource
from .assets import duck_db_project_dbt_assets
from .project import duck_db_project_project
from .schedules import schedules

defs = Definitions(
    assets=[duck_db_project_dbt_assets],
    schedules=schedules,
    resources={
        "dbt": DbtCliResource(project_dir=duck_db_project_project),
    },
)

