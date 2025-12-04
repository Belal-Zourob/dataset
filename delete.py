import os
import glob

base_labels = "./dataset/labels"
base_images = "./dataset/images"

class_id = "9"  # strawberry ID

splits = ["train", "test", "val"]

for split in splits:
    labels_path = os.path.join(base_labels, split)
    images_path = os.path.join(base_images, split)

    print(f"\nChecking split: {split}")

    for label_file in glob.glob(os.path.join(labels_path, "*.txt")):
        with open(label_file, "r") as f:
            lines = f.readlines()

        # check of strawberry voorkomt in dit labelbestand
        if any(line.startswith(class_id + " ") for line in lines):
            
            # verwijder het labelbestand
            os.remove(label_file)
            print("Removed label:", label_file)

            # verwijder bijbehorende afbeelding
            image_name = os.path.splitext(os.path.basename(label_file))[0]

            removed = False
            for ext in [".jpg", ".jpeg", ".png"]:
                img_path = os.path.join(images_path, image_name + ext)
                if os.path.exists(img_path):
                    os.remove(img_path)
                    print("Removed image:", img_path)
                    removed = True

            if not removed:
                print("⚠️ Waarschuwing: geen bijbehorende afbeelding gevonden voor", image_name)
