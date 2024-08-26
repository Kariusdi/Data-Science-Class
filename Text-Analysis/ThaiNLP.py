import pandas as pd

splits = {'train': 'wisesight_sentiment/train-00000-of-00001.parquet', 'validation': 'wisesight_sentiment/validation-00000-of-00001.parquet', 'test': 'wisesight_sentiment/test-00000-of-00001.parquet'}
df = pd.read_parquet("hf://datasets/pythainlp/wisesight_sentiment/" + splits["train"])

df_samples = df.sample(n=1000, replace=False)

attr_map = {
    0: "pos",
    1: "neu",
    2: "neg",
    3 : "q"
}

df_samples['Category'] = df_samples['category'].map(attr_map)
df_samples = df_samples.drop(columns='category')

df_samples.to_csv("./Text-Analysis/dataset/wisesight_sentiment.csv", index=False)

print(df_samples)