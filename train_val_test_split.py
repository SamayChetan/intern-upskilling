from pathlib import Path
import random

# Fixed seed for reproducibility
random.seed(42)

dataset = Path("datasets/face_mask/archive/dataset/images/train")

# Collect all image files
images = list(dataset.glob("*.jpg")) + list(dataset.glob("*.jpeg"))

print(f"Total images: {len(images)}")

# Shuffle
random.shuffle(images)

# Calculate split sizes
train_size = int(0.8 * len(images))
val_size = int(0.1 * len(images))

train = images[:train_size]
val = images[train_size:train_size + val_size]
test = images[train_size + val_size:]

print(f"Train: {len(train)}")
print(f"Validation: {len(val)}")
print(f"Test: {len(test)}")
print("\nSplit completed successfully!")
print("Random seed used: 42")