from pathlib import Path

from dagster_dbt import DbtProject

duck_db_project_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
duck_db_project_project.prepare_if_dev()

