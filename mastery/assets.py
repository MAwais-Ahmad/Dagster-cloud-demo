import pandas as pd
from dagster import asset, MetadataValue

@asset
def dummy_pandas_data():
    df = pd.DataFrame(
        {
            "user_id": [1, 2, 3, 4],
            "name": ["Awais", "Ali", "Sara", "Hina"],
            "score": [85, 90, 78, 88],
        }
    )

    return {
        "data": df,
        "row_count": len(df),
    }

