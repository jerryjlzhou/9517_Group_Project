# COMP9517 Group Project
## Term 3 2025

### Group members:
(add name & zid below)
| Name          | zID        |
|----------------|------------|
| Jerry Zhou     | z5477946   |
| Member 2       | z          |
| Member 3       | z          |
| Member 4       | z          |
| Member 5       | z          |

# Dataset Distortion Script (advanced method development)

This Python script (`distortion_processing.py`) generates distorted versions of your original dataset to test model robustness. It creates two new datasets: `dataset_mild_distortion` and `dataset_strong_distortion`.

## What the script does
- Reads the original dataset structure:
- Applies distortions to each image:
  - Gaussian blur (`blur_ksize`)
  - Gaussian noise (`noise_sigma`)
  - Brightness/contrast adjustment (`brightness_alpha`, `brightness_beta`)
  - Random occlusions (`occlusion_size`)
- Saves distorted images to new dataset folders and copies the corresponding label files.

## How to run:
Make sure you are in the root directory. Run:
`python distortion_processing.py` or ``python3 distortion_processing.py` depending on OS

This script will create 2 new directories in the root:
`dataset_mild_distortion/`
`dataset_strong_distortion/`

One dataset contains slight distortions and another one strong distortions. You can use these datasets to evaluate how your model performs on different levels of distortion, they are formatted the same way as the original dataset. If you only want to use the test set, and don't need training and validation, change this:
`for split in ['train', 'valid', 'test']:`
to 
`for split in ['test']:`

Note: please don't push these datasets on github, store them locally, or we may run out of space

If your model requires a `.yaml` file, you will need to create your own and store it inside the correct directory.

