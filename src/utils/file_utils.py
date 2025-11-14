import os
import pandas as pd
from datetime import datetime

class FileUtils:
    @staticmethod
    def generate_timestamp():
        return datetime.now().strftime("%Y%m%d_%H%M%S")

    @staticmethod
    def save_dataframe(df: pd.DataFrame, filename: str, output_dir: str = "data/output"):
        os.makedirs(output_dir, exist_ok=True)

        csv_path = os.path.join(output_dir, f"{filename}.csv")
        parquet_path = os.path.join(output_dir, f"{filename}.parquet")

        df.to_csv(csv_path, index=False)
        df.to_parquet(parquet_path, index=False)

        return csv_path, parquet_path
