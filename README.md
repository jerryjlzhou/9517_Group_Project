# COMP9517 Group Project - AgroPest-12 Insect Detection
## Term 3 2025

### Authors
| Name            | zID      | Contact                      |
|-----------------|----------|------------------------------|
| Jerry Zhou      | z5477946 | z5477946@ad.unsw.edu.au      |
| Rishi Adhavaryu | z5420526 | z5420526@ad.unsw.edu.au      |
| Zhaoyuan Xu     | z5615760 | z5615760@ad.unsw.edu.au      |
| Yu Lu           | z5500140 | z5500140@ad.unsw.edu.au      |
| Russell Shao    | z5500140 | z5500140@ad.unsw.edu.au      |

---

## Project Overview

This repository contains implementations of various computer vision models for insect detection and classification on the **AgroPest-12** dataset. The project explores multiple detection approaches including:

- **HOG + SVM** - Traditional feature extraction with classification
- **Detectron2 (Faster R-CNN)** - Meta's detection framework, two stage detector + classifier
- **YOLOv11n** - Latest YOLO architecture with attention modules, single stage detector + classifier

Each model is evaluated on detection accuracy, classification performance, and robustness to image distortions. The repository includes comprehensive training notebooks, evaluation scripts, and tools for robustness testing.

---

## Repository Structure

```
.
├── Detectron2/             # Detectron2 implementation
├── HoG_Detector_v1.0/      # HOG feature detector with SVM classifier
├── SVM/                    # SVM-based classification
├── YOLOv11n/               # YOLOv11 nano model implementation 
├── distortion_processing.py # Script to generate distorted test datasets
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

**Note:** Due to file size constraints, the following are **not included** in this repository:
- `dataset/` folder (original AgroPest-12 dataset)
- Trained model weights
- Generated output files (predictions, plots, etc.)
- Distorted dataset variants (`dataset_mild_distortion/`, `dataset_strong_distortion/`)

---

## Getting Started

### 1. Prerequisites

- Python 3.8 or higher
- CUDA-compatible GPU (recommended for training)
- Jupyter Notebook or VS Code with Jupyter extension

### 2. Environment Setup

**Create a virtual environment:**

```bash
# Windows (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Linux/macOS
python3 -m venv .venv
source .venv/bin/activate
```

**Install dependencies:**

```bash
pip install -r requirements.txt
```

The main dependencies include:
- `ultralytics` - YOLO models
- `torch` - PyTorch deep learning framework
- `opencv-python` - Image processing
- `matplotlib` - Visualization
- `numpy`, `pandas` - Data manipulation
- `scikit-learn` - Traditional ML models
- `pyyaml` - Configuration file parsing

### 3. Dataset Setup

**Download the AgroPest-12 dataset:**

1. Visit the [AgroPest-12 dataset on Kaggle](https://www.kaggle.com/datasets/your-dataset-link)
2. Download and extract the dataset
3. Place the extracted `dataset/` folder in the **root directory** of this project

**Expected structure:**

```
dataset/
├── data.yaml          # Dataset configuration file
├── train/
│   ├── images/
│   └── labels/
├── valid/
│   ├── images/
│   └── labels/
└── test/
    ├── images/
    └── labels/
```

**Important:** Do **not** push datasets to GitHub. Keep them local to avoid repository size issues.

---

## Running the Code

### Detectron 2
Navigate to `Detectron2/` - designed for Google Colab. Run/View the model at https://colab.research.google.com/drive/1zwVnR39lfiR3TlyZikM0m1DuwKFL05AB

### HOG Detector
1. Navigate to `HoG_Detector_v1.0/` and `SVM/` and follow notebook instructions
2. Open in Jupyter Notebook or VS Code
3. **Run all cells sequentially from top to bottom**

### YOLOv11n 
1. Navigate to `YOLOv11n/yolov11n.ipynb`
2. Open in Jupyter Notebook or VS Code
3. **Run all cells sequentially from top to bottom**

**Training notes (YOLO):**
- Training takes **~2-3 hours** on an RTX 3060 (12GB VRAM)
- Results are saved to `training/results/`, `validation/results/`, `testing/results/`


---

## Distortion Processing Script (Robustness Testing)

The `distortion_processing.py` script generates distorted versions of the original dataset to evaluate model robustness under challenging conditions such as noise, blur, poor lighting, and partial occlusions.

### What It Does

The script creates two distorted dataset variants:

1. **Mild Distortion** (`dataset_mild_distortion/`)
   - Gaussian noise: σ=5
   - Gaussian blur: kernel size 3×3
   - Brightness adjustment: α=1.1, β=10
   - Random occlusions: 5% of image area

2. **Strong Distortion** (`dataset_strong_distortion/`)
   - Gaussian noise: σ=25
   - Gaussian blur: kernel size 7×7
   - Brightness adjustment: α=1.3, β=40
   - Random occlusions: 20% of image area

The script processes all images in `train/`, `valid/`, and `test/` splits, applies distortions, and copies corresponding label files unchanged.

### How to Run

**Ensure you are in the project root directory**, then run:

```bash
python distortion_processing.py
```

This will create two new directories:
- `dataset_mild_distortion/`
- `dataset_strong_distortion/`

Each will have the same structure as the original `dataset/` folder with distorted images.

### Customization

**To process only the test set** (faster, sufficient for evaluation):

Edit line 52 in `distortion_processing.py`:

```python
# Change this:
for split in ['train', 'valid', 'test']:

# To this:
for split in ['test']:
```

**To adjust distortion parameters:**

Modify the `distortions` dictionary at the top of the script (lines 10-24).


#### YAML Configuration

If your model requires a `data.yaml` configuration file for distorted datasets, create one manually:

```yaml
# dataset_mild_distortion/data_mild.yaml
path: ../dataset_mild_distortion

# Customize which splits you want to include
train: train/images
val: valid/images
test: test/images

nc=12
names:
  0: Ants
  1: Bees
  2: Beetles
  3: Caterpillars
  4: Earthworms
  5: Earwigs
  6: Grasshoppers
  7: Moths
  8: Slugs
  9: Snails
  10: Wasps
  11: Weevils
```

---

## Model Training Recommendations

Since trained models are not included in this repository due to size constraints, **we recommend training models locally** or via cloud computing such as **Google Colab**

---

## Results and Outputs

After training and evaluation, results are saved in model-specific directories, or inside notebook outputs. Also see the report for full results breakdown.

**Key metrics reported:**
- **Classification:** Accuracy, Precision, Recall, F1-score (macro-averaged)
- **Detection:** Precision, Recall, F1, mAP@0.5, mAP@0.5:0.95

---


## Citation

If you use this code or the AgroPest-12 dataset, please cite:

```
Rupankar Majumdar, "AgroPest-12: A 12-Class Image Dataset of Crop Insects and Pests," Kaggle, 2025.
```

---
