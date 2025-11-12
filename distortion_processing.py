from pathlib import Path
import cv2
import numpy as np
import shutil

# Original dataset folder
original_dataset = Path('dataset')

# Mild and strong distortion configurations with target dataset names
distortions = {
    'dataset_mild_distortion': {
        'noise_sigma': 5,
        'blur_ksize': 3,
        'brightness_alpha': 1.1,
        'brightness_beta': 10,
        'occlusion_size': 0.05  # fraction of image covered
    },
    'dataset_strong_distortion': {
        'noise_sigma': 25,
        'blur_ksize': 7,
        'brightness_alpha': 1.3,
        'brightness_beta': 40,
        'occlusion_size': 0.2
    }
}

# Helper function to apply distortions
def distort_image(img, config):

    # Gaussian blur
    img = cv2.GaussianBlur(img, (config['blur_ksize'], config['blur_ksize']), 0)

    # Add Gaussian noise
    noise = np.random.normal(0, config['noise_sigma'], img.shape).astype(np.float32)
    img = np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)

    # Adjust brightness/contrast
    img = cv2.convertScaleAbs(img, alpha=config['brightness_alpha'], beta=config['brightness_beta'])

    # Random occlusion (rectangle)
    h, w = img.shape[:2]
    occ_h = int(h * config['occlusion_size'])
    occ_w = int(w * config['occlusion_size'])
    top_left_x = np.random.randint(0, w - occ_w + 1)
    top_left_y = np.random.randint(0, h - occ_h + 1)
    img[top_left_y:top_left_y+occ_h, top_left_x:top_left_x+occ_w] = 0
    return img

# Iterate over distortion levels
for distorted_dataset_name, config in distortions.items():
    print(f'Creating {distorted_dataset_name}...')
    distorted_dataset = Path(distorted_dataset_name)
    
    # Walk through train/valid/test (or just test, can customize)
    for split in ['train', 'valid', 'test']:
        src_images = original_dataset / split / 'images'
        src_labels = original_dataset / split / 'labels'
        dst_images = distorted_dataset / split / 'images'
        dst_labels = distorted_dataset / split / 'labels'
        dst_images.mkdir(parents=True, exist_ok=True)
        dst_labels.mkdir(parents=True, exist_ok=True)
        
        # Copy and distort images
        for img_path in src_images.glob('*.jpg'):
            img = cv2.imread(str(img_path))
            img_distorted = distort_image(img, config)
            cv2.imwrite(str(dst_images / img_path.name), img_distorted)
            
            # Copy label file
            label_file = src_labels / img_path.name.replace('.jpg', '.txt')
            shutil.copy(str(label_file), str(dst_labels / label_file.name))

print('Distorted datasets created successfully!')
