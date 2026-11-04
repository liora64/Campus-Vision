import cv2
import os

# 获取当前代码所在文件夹
folder = os.path.dirname(os.path.abspath(__file__))

# 读取图片
image_path = os.path.join(folder, "test.jpg")
image = cv2.imread(image_path)

# 判断图片是否读取成功
if image is None:
    print("图片读取失败，请检查 test.jpg 是否存在")
else:
    print("图片读取成功！")

    # 输出图片信息
    height, width, channels = image.shape
    print(f"图片尺寸：{width} × {height}")
    print(f"颜色通道数：{channels}")

    # 灰度化
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Canny 边缘检测
    edges = cv2.Canny(gray, 100, 200)

    # 保存处理结果
    cv2.imwrite(os.path.join(folder, "grayscale.jpg"), gray)
    cv2.imwrite(os.path.join(folder, "edges.jpg"), edges)

    print("灰度图片已保存：grayscale.jpg")
    print("边缘检测图片已保存：edges.jpg")
    print("Campus Vision 运行成功！")