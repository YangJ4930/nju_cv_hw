import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np


def execute():
    img1 = mpimg.imread('I0.jpg')
    # plt.imshow(img1)

    # print(img1)


    print(img1.size)
    print(img1[0].size)

    height = img1.shape[0]
    width = img1.shape[1]

    # width, height = img1.size

    image1 = np.array(img1)

    image = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            image[i][j] = image1[i][j][0] * 0.3 + image1[i][j][1] * 0.59 + image1[i][j][2] * 0.11

    image = image.astype(np.uint8)
    image2 = plt.imshow(image,cmap='gray')

    plt.title('图像1')
    plt.axis('off')
    plt.show()