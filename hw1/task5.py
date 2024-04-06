# 亮度调整
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np

# 直接根据rgb的大小相乘
def execute_direct(alpha):
    img1 = mpimg.imread('I0.jpg')
    img = img1 * 1.0
    img_out = img
    img_out = np.array(img_out)
    img_out[:, :, 0] = img_out[:, :, 0] * alpha
    img_out[:, :, 1] = img_out[:, :, 1] * alpha
    img_out[:, :, 2] = img_out[:, :, 2] * alpha
    img_out = np.clip(img_out, 0, 255).astype(np.uint8)
    plt.imshow(img_out)

    plt.title('图像1')
    plt.axis('off')
    plt.show()

# 根据rgb的比例相乘
def execute_normal(alpha):
    img1 = mpimg.imread('I0.jpg')
    img = img1 * 1.0
    img_out = img
    img_out = np.array(img_out)

    img_out[:, :, 0] = img[:, :, 0] + 255.0 * alpha
    img_out[:, :, 1] = img[:, :, 1] + 255.0 * alpha
    img_out[:, :, 2] = img[:, :, 2] + 255.0 * alpha
    img_out = np.clip(img_out, 0, 255).astype(np.uint8)

    plt.imshow(img_out)

    plt.title('图像1')
    plt.axis('off')
    plt.show()