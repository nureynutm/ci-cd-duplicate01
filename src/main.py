import pandas as pd

def load_and_process_data(filepath="data/dataset.csv", output_path="data/processed_dataset.csv"):
    """
    Loads the dataset, removes duplicate rows, and saves the processed dataset.
    """
    df = pd.read_csv(filepath)
    print(f"Original dataset shape: {df.shape}")
    df = df.drop_duplicates()
    print(f"Dataset shape after removing duplicates: {df.shape}")
    df.to_csv(output_path, index=False)
    print(f"Processed dataset saved to {output_path}")
    return df
