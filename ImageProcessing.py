import cv2
import matplotlib
import matplotlib.pyplot as plt

imagePath = 'E:/Python Machinelearning scikit/Dog.jpg'
image = cv2.imread(imagePath)



plt.imshow(image)

img_sahpe = image.shape

print(img_sahpe)
print(image)  #every pixel has RGB value

size=(32,32)
resized_image_feature_vector = cv2.resize(image, size)

img1_show = plt.imshow(resized_image_feature_vector)

print(img1_show)