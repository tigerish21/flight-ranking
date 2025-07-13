import lightgbm as lgb
from sklearn.model_selection import train_test_split

def train_lgb(df):
    features = [col for col in df.columns if col not in ['selected', 'ranker_id']]
    X= df[features]
    y= df['selected']
    categorical_f = [f for f in features if df[f].type == object]
