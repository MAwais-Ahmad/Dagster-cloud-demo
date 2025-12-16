from dagster import (asset, AssetExecutionContext, define_asset_job, ScheduleDefinition)
import pandas as pd
from datetime import datetime
import time


@asset
def raw_daily_inventory(context: AssetExecutionContext) -> pd.DataFrame:
    now = datetime.now().strftime("%H:%M:%S")
    context.log.info(f"[{now}] 🚀 Starting inventory asset")

    for i in range(1, 6):
        now = datetime.now().strftime("%H:%M:%S")
        context.log.info(f"[{now}]   ⏳ Inventory working... step {i}/5")
        time.sleep(2)

    now = datetime.now().strftime("%H:%M:%S")
    context.log.info(f"[{now}] ✅ Finished inventory asset")

    return pd.DataFrame({
        "item": ["X", "Y", "Z"],
        "stock": [50, 30, 20]
    })



inventory_job = define_asset_job(
    name="inventory_job",
    selection=[raw_daily_inventory],
)


inventory_schedule = ScheduleDefinition(
    job=inventory_job,
    cron_schedule="*/5 * * * *",  # every 5 minutes
    execution_timezone="UTC",
)
