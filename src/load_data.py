import pandas as pd

def load_train_data(columns_to_use: list, sample_size: int = None):
    print("Caricamento dati...")
    df = pd.read_parquet("data/train.parquet", columns=columns_to_use)
    if sample_size:
        df = df.groupby("ranker_id").head(1).sample(n=sample_size, random_state= 42)  # prendi un subset dei gruppi
    return df