#!/bin/bash
conda init bash
source ~/.bashrc
conda activate video-generation
python play.py --config configs/03_tennis.yaml
