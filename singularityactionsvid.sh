#!/bin/bash
#conda init bash
source ~/.bashrc
conda activate video-generation
#python train.py --config configs/05_smarts.yaml
#python play.py --config configs/05_smarts.yaml
#python build_evaluation_dataset.py  --config configs/05_smarts.yaml
python evaluate_dataset.py --config configs/evaluation/05_smarts.yaml
