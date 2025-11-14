import pandas as pd
import numpy as np
import os
from datetime import datetime

OUTPUT_DIR = "data/input"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def generate_sales_report():
    dates = pd.date_range(end=datetime.now(), periods=30).tolist()
    data = {
        "data": dates,
        "vendas": np.random.randint(50, 500, size=30),
        "clientes": np.random.randint(5, 40, size=30),
        "ticket_medio": np.random.uniform(20, 150, size=30).round(2)
    }
    df = pd.DataFrame(data)

    file_path = os.path.join(
        OUTPUT_DIR,
        f"vendas_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    )
    df.to_csv(file_path, index=False)
    return file_path

if __name__ == "__main__":
    path = generate_sales_report()
    print(f"Relatório gerado: {path}")
