from dagster import Definitions, load_assets_from_modules

from . import assets, assets2

asset1 = load_assets_from_modules([assets])
asset2 = load_assets_from_modules([assets2])

defs = Definitions(
    assets=[asset1, asset2],
    jobs=[assets.daily_sales_job, assets2.inventory_job],
    schedules=[assets.daily_schedule, assets2.inventory_schedule],
)
