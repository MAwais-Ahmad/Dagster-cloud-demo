from dagster import Definitions, load_assets_from_modules

from . import assets, assets2

defs = Definitions(
    assets=[assets.raw_daily_sales, assets2.raw_daily_inventory],
    jobs=[assets.daily_sales_job, assets2.inventory_job],
    schedules=[assets.daily_schedule, assets2.inventory_schedule],
)
