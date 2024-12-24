import yaml

import torch
import torch.nn as nn
import os

from .tradition import DOVER
from .fidelity import DoubleStreamModel
from .text_alignment import VideoTextAlignmentModel

from huggingface_hub import snapshot_download

class EvalEditModel(nn.Module):
    def __init__(self, dover_opt, doublestream_opt, text_opt, model_path='ckpts'):
        super().__init__()
        
        if not os.path.isdir(model_path): 
            model_path = snapshot_download('sunshk/vebench')

        # build model
        self.traditional_branch = DOVER(**dover_opt['model']['args'],model_path=model_path).eval()
        self.fidelity_branch = DoubleStreamModel(**doublestream_opt['model']['args'], model_path=model_path).eval()
        self.text_branch = VideoTextAlignmentModel(**text_opt['model']['args'], model_path=model_path).eval()
        
        # load_weight
        self.load_ckpt(model_path)


    def load_ckpt(self, model_path):
        # print('111')
        self.traditional_branch.load_state_dict(torch.load(os.path.join(model_path, 'e-bench-dover_head_videoQA_0_eval_n_finetuned.pth'), map_location='cpu')['state_dict']) 
        self.fidelity_branch.load_state_dict(torch.load(os.path.join(model_path, 'e-bench-uniformer-src-edit_head_videoQA_3_eval_s_finetuned.pth'),map_location='cpu')['state_dict'],strict=False)
        self.text_branch.load_state_dict(torch.load(os.path.join(model_path, 'e-bench-blip_head_videoQA_9_eval_s_finetuned.pth'), map_location='cpu')['state_dict'],strict=False)

    def forward(self, src_video, edit_video, prompt):
        traditional_score = self.traditional_branch(edit_video,reduce_scores=True)
        fidelity_score = self.fidelity_branch(src_video, edit_video)
        text_score = self.text_branch(edit_video,prompts=prompt)
        # the weight of each score is pre-computed within each branch
        return (traditional_score + fidelity_score[0] + text_score[0]).item()



if __name__ == "__main__":
    eval_model=EvalEditModel()
