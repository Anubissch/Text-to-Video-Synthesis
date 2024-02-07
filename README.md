# Text-to-Video Synthesis

This project is a simple application that allows users to generate videos from text prompts using Diffusion models.

## Overview

The Text-to-Video Synthesis application provides a interface for generating videos from textual prompts. It leverages Diffusion models for video synthesis, offering high-quality results.

## Features

- Generate videos from text prompts
- Utilizes Diffusion models for video synthesis
- Not very user-friendly interface (this is a alpha version of this app so.)
- Supports various text prompts and lengths
- Export generated videos to MP4 or VLC format (all though VLC might not work properly.)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HeroTheGreat/text-to-video-synthesis.git
   
2. Get the needed python Packages:

   ```bash
   To Command Prompt(could be in vs.code too):
   !pip install opencv-python
   !pip install torch open_clip_torch pytorch-lightning
   !pip install pillow
   !pip install imageio
   !pip install transformers
   !pip install numpy
   !pip install huggingface
   !pip install modelscope==1.4.2
   !pip install huggingface_hub
   
## Compatibility

- **NVIDIA CUDA**: Cuda compilation tools, release 12.1, V12.1.66
- **PyTorch**: Version: 2.2.0+cu121
- **ModelHub Token**: The model has been launched on [ModelScope Studio](https://modelscope.cn/studios/damo/text-to-video-synthesis/summary) and [huggingface](https://huggingface.co/spaces/damo-vilab/modelscope-text-to-video-synthesis).So you need to be sure that you have a Huggingface account and a token with it.

## Last touch
- The video will be saved in the same folder where script is.So i recommend Pulling the folder.Not the .py File
- This is not a commercial project but a project made by a student, So dont take this to court.
- If the video doesnt appear,make sure you have all the packages needed.
- If the video doesnt play,make sure you have the compatible Nvidia CUDA with Pytorch.
- Dont choose the processor as CPU... It has to be Processed GPU to Generate the video given by text.
[![asfasd.png](https://i.postimg.cc/CKMv5QrT/asfasd.png)](https://postimg.cc/nX5Kw0t0)






