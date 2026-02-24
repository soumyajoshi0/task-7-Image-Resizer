import os
from PIL import Image

input_folder = "input_images"
output_folder = "output_images"

new_size = (800, 600)   # change size here

# create output folder if not exists
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for file in os.listdir(input_folder):

    if file.lower().endswith((".jpg", ".jpeg", ".png")):
        try:
            img_path = os.path.join(input_folder, file)
            img = Image.open(img_path)

            resized = img.resize(new_size)

            new_name = os.path.splitext(file)[0] + ".png"
            save_path = os.path.join(output_folder, new_name)

            resized.save(save_path)
            print("Done:", file)

        except Exception as e:
            print("Error in", file, e)

print("All images processed!")