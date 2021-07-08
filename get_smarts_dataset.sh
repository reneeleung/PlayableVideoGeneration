#!/bin/bash

# Prerequisite: Upload video sequences by agent in the tmp/ directory

# Extracts sequences of at least length 16
python -m dataset.acquisition.smarts.convert_annotated_video_directory
# Makes train and validation splits
python -m dataset.acquisition.smarts.train_val_test_split
# Makes val and test sequences of fixed length
python -m dataset.acquisition.smarts.subsample_videos_and_make_fixed_length

mkdir data/smarts_v4_256_ours
mv tmp/smarts_v4_256_ours/train data/smarts_v4_256_ours/train
mv tmp/smarts_v4_256_ours/val_fixed_length data/smarts_v4_256_ours/val
mv tmp/smarts_v4_256_ours/test_fixed_length data/smarts_v4_256_ours/test

rm -rf tmp
