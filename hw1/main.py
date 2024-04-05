import matplotlib.pyplot as plt  # plt 用于显示图片
import matplotlib.image as mpimg  # mpimg 用于读取图片

img1 = mpimg.imread('I0.jpg')
plt.imshow(img1)

print(img1)

plt.title('图像1')
# 不显示坐标轴
plt.axis('off')

plt.show()
