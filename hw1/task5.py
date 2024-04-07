# 亮度调整
import matplotlib
import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片
import numpy as np

# 直接根据rgb的大小相乘
def execute_bright_direct(alpha):
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
def execute_bright_normal(alpha):
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

def execute_log(alpha):
    # 读取彩色图像
    img = mpimg.imread('I0.jpg')
    # 对每个颜色通道分别应用对数变换
    # 将图像的像素值平移，确保没有零值像素
    adjusted_image = np.zeros_like(img)
    for channel in range(3):
        channel_min = np.min(img[:, :, channel])
        channel_max = np.max(img[:, :, channel])
        # 将图像的像素值平移，确保没有零值像素
        image_shifted = img[:, :, channel] - channel_min + 1

        # 进行对数变换和对比度调整
        adjusted_channel = (np.log(image_shifted) / np.log(channel_max - channel_min + 1)) * alpha

        # 将像素值规范化到 [0, 1] 范围
        adjusted_channel = np.clip(adjusted_channel, 0, 1)

        # 将像素值重新缩放到 [0, 255] 范围
        adjusted_image[:, :, channel] = adjusted_channel * 255

    img_out = adjusted_image.astype(np.uint8)

    # 显示图像
    plt.imshow(img_out)
    plt.title('图像1')
    plt.axis('off')
    plt.show()

def execute_histogram_equalization():
    img = mpimg.imread('I0.jpg')
    # 计算图像的直方图
    hist, bins = np.histogram(img.flatten(), bins=256, range=[0, 255])

    # 计算累积分布函数（CDF）
    cdf = hist.cumsum()

    # 将CDF映射到[0, 255]范围
    cdf_normalized = cdf * 255 / cdf[-1]

    # 使用CDF映射进行直方图均衡化
    equalized_image = np.interp(img.flatten(), bins[:-1], cdf_normalized)

    image = equalized_image.astype(np.uint8).reshape(img.shape)
    plt.imshow(image)
    plt.title('图像1')
    plt.axis('off')
    plt.show()

def execute_saturation(alpha):
    img = mpimg.imread('I0.jpg')
    image_float = img.astype(np.float32) / 255.0

    # 将图像从 RGB 转换为 HSV
    hsv_image = matplotlib.colors.rgb_to_hsv(image_float)

    # 调整饱和度
    hsv_image[:, :, 1] *= alpha

    # 将图像从 HSV 转换回 RGB
    adjusted_image = matplotlib.colors.hsv_to_rgb(hsv_image)

    # 缩放像素值到 [0, 255] 范围
    adjusted_image = np.clip(adjusted_image * 255.0, 0, 255).astype(np.uint8)
    plt.imshow(adjusted_image)
    plt.title('图像1')
    plt.axis('off')
    plt.show()
