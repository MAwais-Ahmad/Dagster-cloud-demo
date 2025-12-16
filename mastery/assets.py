from dagster import (
    asset, DailyPartitionsDefinition, AssetExecutionContext, define_asset_job, ScheduleDefinition, RunRequest
)
import pandas as pd
from datetime import timedelta, datetime

daily = DailyPartitionsDefinition(
    start_date="2025-01-01"
)


@asset(
    partitions_def=daily,  
)
def raw_daily_sales(context: AssetExecutionContext) -> pd.DataFrame:
    date_str = context.partition_key
    
    now = datetime.now().strftime("%H:%M:%S")
    context.log.info(f"[{now}] 🚀 Starting partition: {date_str}")

    for i in range(1, 6):
        now = datetime.now().strftime("%H:%M:%S")
        context.log.info(f"[{now}]   ⏳ Working... step {i}/5")
        

    now = datetime.now().strftime("%H:%M:%S")
    context.log.info(f"[{now}] ✅ Finished partition: {date_str}")

    return pd.DataFrame({
        "date": pd.to_datetime([date_str] * 5),
        "customer": ["A", "B", "C", "D", "E"],
        "sales": [100, 250, 175, 300, 400]
    })

daily_sales_job = define_asset_job(
    name="daily_sales_job",
    selection=[raw_daily_sales],
    partitions_def=daily,
)

def partition_request(context):
    prev_day = context.scheduled_execution_time - timedelta(days=1)
    return RunRequest(partition_key=prev_day.strftime("%Y-%m-%d"))

daily_schedule = ScheduleDefinition(
    job=daily_sales_job,
    cron_schedule="*/5 * * * *",   # every minute
    execution_fn=partition_request
)