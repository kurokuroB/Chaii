import os
from pathlib import Path
import torch

class Config():
    def __init__(self) -> None:
        #tolkenizer
        self.max_length = 384
        self.doc_stride= 128

        #epoch
        self.epoch=10
        #batch
        self.train_batch_size=4
        self.valid_batch_size=50
        self.test_batch_size=128

        self.gradient_accumulation_steps=8

        #optimizer
        self.weight_decay = 1e-2

        #scheduler
        #decay_name = 'linear-warmup'
        self.lr=1.5e-5
        self.warmup_ratio= 0.0

        #output用
        self.exp_dir=Path(__file__).parent
        self.output_dir=os.path.join(Path(__file__).parent,'output')
        self.param_dir=os.path.join(Path(__file__).parent,'param')

        self.architecture_name=Path(__file__).parents[2].name
        self.exp_name=Path(__file__).parents[1].name+Path(__file__).parents[0].name

        #その他 
        self.seed= 1023
        self.num_fold=10
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'