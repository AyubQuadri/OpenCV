import numpy as np

from keras.preprocessing.image import ImageDataGenerator, array_to_img, load_img, img_to_array
from keras.applications.resnet50 import preprocess_input, decode_predictions

img_src = 'https://gfp-2a3tnpzj.stackpathdns.com/wp-content/uploads/2016/07/Dachshund-600x600.jpg'
img = load_img('pics/laptop.jpeg',target_size=(256,256))
img

from keras.applications.resnet50 import ResNet50

model = ResNet50(weights='imagenet')

img = img_to_array(img)
print(img.shape)

img = np.expand_dims(img, axis=0)

pred_class = model.predict(img)

n =5
top_n = decode_predictions(pred_class, top =n)

for i in top_n[0]:
    print(i)