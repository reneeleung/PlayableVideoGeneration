#!/bin/bash
conda init bash
source ~/.bashrc
conda activate video-generation
#python train.py --config configs/04_smarts.yaml
python play.py --config configs/04_smarts.yaml
#python build_evaluation_dataset.py  --config configs/03_tennis.yaml
#python evaluate_dataset.py --config configs/evaluation/03_tennis.yaml
