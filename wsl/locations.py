#!/usr/bin/python3
from pathlib import Path

# Standard location for share mounting
mount = Path('/mnt/in')

# Issue a warning here if the project share doesn't exist
if not mount.exists():
    raise FileNotFoundError(
        f'The project share is not mounted at the expected location {mount}'
    )

# Part of the share dedicated to the object detection subproject
root = Path('/workspace')

# Location of available datasets
wsl_data_dir = mount

# Location of csvs
wsl_csv_dir = root / 'wsl' / 'wsl' / 'csvs'

# Location of model dir where checkpoints are stored
wsl_model_dir = Path('/mnt/out') / 'models'

# Location of model dir where checkpoints are stored
wsl_summary_dir = Path('/mnt/out') / 'summary'
