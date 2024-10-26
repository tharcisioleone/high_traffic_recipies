import os
import pandas as pd
import numpy as np


class Config:
    def __init__(self):
        pass


def list_all_csv_in_folder(data_folder):
    file_paths = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith(".csv")]
    file_names = [os.path.basename(file) for file in file_paths]
    for file_name in file_names:
        print(file_name)


def open_and_concatenate_csv_files(data_folder, sample_size=1, encoding='utf-8'):
    files = [file for file in os.listdir(data_folder) if file.endswith('.csv')]
    if len(files) == 0:
        print("No CSV file found in the input folder")
        return None

    dfs = []
    for file in files:
        df = pd.read_csv(os.path.join(data_folder, file), encoding=encoding)
        if sample_size < 1:
            sample_n = int(sample_size * len(df))
            df = df.sample(n=sample_n, random_state=42)
        dfs.append(df)

    concatenated_df = pd.concat(dfs, ignore_index=True)
    print(f"Number of files concatenated: {len(dfs)}")
    del dfs
    print(f"Data Shape: {concatenated_df.shape}")
    return concatenated_df

