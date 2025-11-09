 # YOLOv8 Set up instructions


 ## 1) Download dataset
 - Download from Kaggle: https://www.kaggle.com/datasets/rupankarmajumdar/crop-pests-dataset
 - Ensure the dataset is in the root repository with directory format:
	 - `dataset/`
		 - `data.yaml`
		 - `train/` `valid/` `test/` 

 The notebook expects the config at `dataset/data.yaml` when run from `YOLOv8/yolov8.ipynb`.

 ## 2) Get YOLOv8 weights
 The notebook uses `yolov8n.pt` (nano). However you can customize by changing `model = YOLO('yolov8*.pt')` to use other yolov8 models.

 Run the notebook and ultralytics should auto-download and place it into `YOLOv8/yolov8n.pt`

 ## 3) Install dependencies
 Run:
 ```
 pip install -r YOLOv8/requirements_yolov8.txt
 ```
 Notes:
 - `ultralytics` will install PyTorch. For GPU acceleration (CUDA), install the CUDA-enabled PyTorch matching your setup from https://pytorch.org/get-started/locally/.


Setup is done, now you can run the notebook



 ## Libraries
 - Ultralytics YOLOv8 (https://github.com/ultralytics/ultralytics).
