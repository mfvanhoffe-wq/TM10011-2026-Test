import sys
import pandas as pd

def main():
    try:
        df = pd.read_csv("datasets.csv")
    except FileNotFoundError:
        print("datasets.csv not found", file=sys.stderr)
        sys.exit(1)

    if 'datasets' not in df.columns:
        print("Column 'datasets' not found in datasets.csv", file=sys.stderr)
        sys.exit(1)

    unique_count = df['datasets'].nunique()
    print(unique_count)

if __name__ == "__main__":
    main()
    


