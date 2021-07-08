import os
import pandas as pd
import multiprocessing as mp
from pathlib import Path
from distutils.dir_util import copy_tree

annotations_directory = "dataset/acquisition/smarts"
root_directory = "tmp/smarts_ours"
output_directory = "tmp/smarts_v4_256_ours"
splits_filename = "splits.csv"


if __name__ == "__main__":
    '''
    Divides a dataset in a directory in train, validation and test splits
    '''
    """
    directories = os.listdir(root_directory)
    lens = [ (len(os.listdir(os.path.join(root_directory, directory))), int(directory)) for directory in directories ]
    sort = sorted(lens, key=lambda tup: tup[0])
    for i in range(298):
        print(f"{sort[i][1]},train")
    for i in range(298, len(sort), 2):
        print(f"{sort[i][1]},validation")
    for i in range(299, len(sort), 2):
        print(f"{sort[i][1]},test")

    """
    # Reads the video annotations
    splits_path = os.path.join(annotations_directory, splits_filename)
    splits = pd.read_csv(splits_path)

    # Paths of the split directories
    splits_directories = {
        "train": os.path.join(output_directory, "train"),
        "validation": os.path.join(output_directory, "validation"),
        "test": os.path.join(output_directory, "test"),
    }
    # id for the next video assigned to a split
    splits_counters = {
        "train": 0,
        "validation": 0,
        "test": 0,
    }

    print("- Creating output directories")
    # Creates the output directory
    Path(output_directory).mkdir(parents=True, exist_ok=True)
    for current_directory in splits_directories.values():
        Path(current_directory).mkdir(parents=True, exist_ok=True)

    for current_idx in range(len(splits)):
        current_sequence_id = splits.iloc[current_idx]["sequence"]
        current_split = splits.iloc[current_idx]["split"]
        current_split_sequence_id = splits_counters[current_split]
        splits_counters[current_split] = splits_counters[current_split] + 1

        source_path = os.path.join(root_directory, f"{current_sequence_id:05d}")
        target_path = os.path.join(splits_directories[current_split], f"{current_split_sequence_id:05d}")

        print(f"- Copying '{source_path}' to '{target_path}'")
        copy_tree(source_path, target_path)
























