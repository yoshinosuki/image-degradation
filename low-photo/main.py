import os
from PIL import Image

def degrade_images_in_folder(input_folder, output_folder, quality):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # 打开原始图片
            image = Image.open(input_path)
            
            # 保存图片，设置质量参数
            image.save(output_path, quality=quality)
            print(f"Processed {filename}")

# 示例用法
input_folder = r'C:\Users\surface\Desktop\fsdownload'
output_folder = r'C:\Users\surface\Desktop\fsdownload\output'
quality = 20  # 质量参数，范围从1（最差）到95（最好）

degrade_images_in_folder(input_folder, output_folder, quality)
