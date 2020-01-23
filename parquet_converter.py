import pandas as pd

"""
/data/ is in .gitignore. download your csv dataset from Kaggle or use your own
you need to install pandas and pyarrow with pip before you run this script 
"""
def main():
    df = pd.read_csv("data/players_20.csv") 
    df.to_parquet(fname="data/players_20.parquet", engine="pyarrow", compression=None)

main()