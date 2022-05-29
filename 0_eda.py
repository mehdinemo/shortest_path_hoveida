import pandas as pd
from yaml import safe_load

if __name__ == '__main__':
    with open('data/gqa-StationShortestCount-1.yaml', 'r') as f:
        df = pd.json_normalize(safe_load(f))

    print("Done!")
