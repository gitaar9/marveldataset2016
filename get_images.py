import glob
import os
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


def show_image(path):
    img = mpimg.imread(path)
    imgplot = plt.imshow(img)
    plt.show()

root_dir = '/home/gitaar9/AI/TNO/marveldataset2016/'

# Retrieve all images paths
images_paths = [path for path in glob.glob(os.path.join(root_dir, 'W*_1/*.jpg'))]

# Read in annotations
with open(os.path.join(root_dir, 'VesselClassification.dat')) as f:
    annotations = [line.strip().split(",") for line in f.readlines()]
annotations = {
    image_id: {
        "is_train": True if set_index == '1' else False,
        "class_label": int(class_label),
        "class_label_name": class_label_name,
    } for image_id, set_index, class_label, class_label_name in annotations
}

# Remove annotations of not downloaded images + filter based on train/test set
image_ids = {p.split('/')[-1][:-4] for p in images_paths}
annotations = {
    key: value for key, value in annotations.items() if key in image_ids
}

# Filter image paths based on annotations
images_paths = [p for p in images_paths if p.split('/')[-1][:-4] in annotations.keys()]



## REAL STUFF
class_label = 26
amount_of_images = 3
for ship_id, v in [(key, v) for key, v in annotations.items() if v['class_label'] == class_label][:amount_of_images]:
    print(f"{class_label}({v['class_label_name'].replace(' ', '_')})")
    image_p = glob.glob(os.path.join(root_dir, f'W*_1/{ship_id}.jpg'))[0]
    show_image(image_p)
print(list(annotations.items())[:2])

