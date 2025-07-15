import pandas as pd

import pandas as pd

def load_train_data(columns_to_use: list, sample_size: int = None, min_ranker_occurrences: int = None):
    print("Caricamento dati...")
    df = pd.read_parquet("data/train.parquet", columns=columns_to_use)
    
    # Filtra i ranker_id con almeno min_ranker_occurrences occorrenze
    ranker_counts = df["ranker_id"].value_counts()
    valid_rankers = ranker_counts[ranker_counts >= min_ranker_occurrences].index
    df = df[df["ranker_id"].isin(valid_rankers)]
    print(f"Righe dopo filtro ranker_id: {len(df)}")
    
    if sample_size:
        df = df.sample(n=sample_size, random_state=42)
    return df

