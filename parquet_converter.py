import pandas as pd

"""
/data/ is in .gitignore. download your csv dataset from Kaggle or use your own
you need to install pandas and pyarrow with pip before you run this script 
"""
def main():
    df = pd.read_csv("data/201801_Punctuality_Statistics_Full_Analysis.csv") 
    df.to_parquet(fname="data/201801_Punctuality_Statistics_Full_Analysis.parquet", engine="pyarrow", compression=None)

main()