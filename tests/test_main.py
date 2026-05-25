import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import load_and_process_data

def test_no_duplicates():
    import pandas as pd
    import os
    if not os.path.exists("data/dataset.csv"):
        pd.DataFrame({'A':[1,2,2], 'B':[4,5,5]}).to_csv("data/dataset.csv", index=False)
    
    df = load_and_process_data("data/dataset.csv", "data/test_processed_dataset.csv")
    assert df.duplicated().sum() == 0, "Duplicate rows were not fully removed"
