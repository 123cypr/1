# 图像处理实验程序 / Image Processing Experiment Program

## 项目简介 / Project Description

本项目是一个完整的图像处理实验程序，使用Python实现了多种图像处理算法。程序采用规范的编程风格，包含详细的中英文注释。

This is a comprehensive image processing experiment program implemented in Python, featuring multiple image processing algorithms with detailed bilingual comments.

## 功能特性 / Features

### 1. 图像基本操作 / Basic Image Operations
- **图像读取与保存** / Image reading and writing
- **图像显示** / Image display
- **RGB转灰度图像** / RGB to grayscale conversion
- **直方图显示** / Histogram visualization

### 2. 图像统计参数计算 / Image Statistics Calculation
- **像素个数** / Pixel count
- **图像大小** / Image dimensions
- **平均值** / Mean value
- **标准差** / Standard deviation
- **最小值/最大值** / Min/Max values
- **中位数** / Median
- **两幅图像的相关系数** / Correlation coefficient between two images
- **协方差矩阵** / Covariance matrix

### 3. 图像采样 / Image Sampling
- **2倍降采样** / 2x downsampling
- **4倍降采样** / 4x downsampling
- **8倍降采样** / 8x downsampling
- **结果可视化对比** / Visual comparison of results

### 4. 灰度级转换 / Gray Level Transformation
- **256灰度级** / 256 gray levels
- **128灰度级** / 128 gray levels
- **64灰度级** / 64 gray levels
- **32灰度级** / 32 gray levels
- **16灰度级** / 16 gray levels
- **8灰度级** / 8 gray levels
- **4灰度级** / 4 gray levels
- **2灰度级** / 2 gray levels

## 环境要求 / Requirements

### Python版本 / Python Version
- Python 3.7 或更高版本 / Python 3.7 or higher

### 依赖库 / Dependencies
```
numpy>=1.24.0
opencv-python>=4.8.0
matplotlib>=3.7.0
```

## 安装说明 / Installation

### 1. 安装依赖 / Install Dependencies
```bash
pip install -r requirements.txt
```

或手动安装 / Or install manually:
```bash
pip install numpy opencv-python matplotlib
```

## 使用方法 / Usage

### 运行主程序 / Run Main Program
```bash
python image_processing.py
```

程序会自动处理当前目录下的测试图像（lena.bmp, lena.jpg, rice.png, moon.tif, pollen.jpg等）。

The program will automatically process test images in the current directory (lena.bmp, lena.jpg, rice.png, moon.tif, pollen.jpg, etc.).

## 输出文件 / Output Files

### 1. 处理后的图像 / Processed Images
- `gray_*.bmp` - 灰度图像文件 / Grayscale image files

### 2. 可视化结果 / Visualization Results
- `output_1_original_*.png` - 原始图像显示 / Original image display
- `output_1_grayscale_*.png` - 灰度图像显示 / Grayscale image display
- `output_1_histogram_*.png` - 直方图 / Histogram
- `output_3_downsampling_*.png` - 降采样结果对比 / Downsampling comparison
- `output_4_gray_levels_*.png` - 灰度级转换结果 / Gray level transformation results

## 代码结构 / Code Structure

### ImageProcessor 类 / ImageProcessor Class

主要的图像处理类，包含以下方法：

Main image processing class with the following methods:

#### 基础方法 / Basic Methods
- `read_image()` - 读取图像 / Read image
- `write_image()` - 保存图像 / Write image
- `display_image()` - 显示图像 / Display image
- `rgb_to_gray()` - RGB转灰度 / RGB to grayscale

#### 统计分析方法 / Statistical Analysis Methods
- `calculate_statistics()` - 计算统计参数 / Calculate statistics
- `calculate_correlation()` - 计算相关系数 / Calculate correlation (static method)
- `calculate_covariance_matrix()` - 计算协方差矩阵 / Calculate covariance matrix (static method)
- `display_histogram()` - 显示直方图 / Display histogram

#### 图像处理方法 / Image Processing Methods
- `downsample()` - 图像降采样 / Image downsampling
- `display_downsampling_results()` - 显示降采样结果 / Display downsampling results
- `gray_level_quantization()` - 灰度级量化 / Gray level quantization
- `display_gray_level_results()` - 显示灰度级结果 / Display gray level results

## 实验结果示例 / Example Results

### 任务1：图像读取和转换 / Task 1: Image Reading and Conversion
程序读取彩色图像，转换为灰度图像，并显示其直方图。

The program reads color images, converts them to grayscale, and displays their histograms.

### 任务2：统计参数 / Task 2: Statistical Parameters
```
==================================================
图像统计参数 / Image Statistics
==================================================
像素个数 / Pixel Count: 65536
图像大小 / Image Size: (256, 256)
平均值 / Mean: 97.77235412597656
标准差 / Standard Deviation: 52.77728733633082
最小值 / Min: 3
最大值 / Max: 238
中位数 / Median: 96.0
==================================================
```

### 任务3：图像采样 / Task 3: Image Sampling
展示原始图像与2x、4x、8x降采样后的对比效果。

Shows comparison of original image with 2x, 4x, and 8x downsampled versions.

### 任务4：灰度级转换 / Task 4: Gray Level Transformation
展示不同灰度级（256, 128, 64, 32, 16, 8, 4, 2）的量化效果。

Shows quantization effects at different gray levels (256, 128, 64, 32, 16, 8, 4, 2).

## 测试图像 / Test Images

项目包含以下标准测试图像：

The project includes the following standard test images:

- **lena.bmp / lena.jpg** - 经典Lena测试图像 / Classic Lena test image
- **rice.png** - 米粒图像 / Rice grain image
- **moon.tif** - 月球表面图像 / Moon surface image
- **pollen.jpg** - 花粉图像 / Pollen image
- **cameraman.tif** - 摄影师图像 / Cameraman image
- **circuit.tif** - 电路板图像 / Circuit board image
- **eight.tif** - 数字8图像 / Figure-8 image

## 代码规范 / Code Standards

### 编程风格 / Programming Style
- ✅ 采用缩进格式 / Proper indentation
- ✅ 详细的中英文注释 / Detailed bilingual comments
- ✅ 函数和类的文档字符串 / Function and class docstrings
- ✅ 类型提示 / Type hints
- ✅ 清晰的变量命名 / Clear variable naming

### 注释规范 / Comment Standards
- 每个函数都有完整的文档字符串 / Complete docstrings for all functions
- 关键代码块有中英文注释 / Bilingual comments for key code blocks
- 参数和返回值说明 / Parameter and return value descriptions

## 扩展功能 / Extended Features

### 自定义使用 / Custom Usage

```python
from image_processing import ImageProcessor

# 创建处理器 / Create processor
processor = ImageProcessor('your_image.jpg')

# 读取图像 / Read image
img = processor.read_image()

# 转换为灰度 / Convert to grayscale
gray = processor.rgb_to_gray()

# 计算统计信息 / Calculate statistics
stats = processor.calculate_statistics()

# 2倍降采样 / 2x downsampling
downsampled = processor.downsample(2)

# 8级灰度量化 / 8-level gray quantization
quantized = processor.gray_level_quantization(8)
```

## 技术细节 / Technical Details

### 图像读取 / Image Reading
使用OpenCV的`cv2.imread()`函数读取图像，支持多种格式（BMP, JPG, PNG, TIF等）。

Uses OpenCV's `cv2.imread()` to read images, supporting multiple formats (BMP, JPG, PNG, TIF, etc.).

### 灰度转换 / Grayscale Conversion
使用OpenCV的`cv2.cvtColor()`函数进行RGB到灰度的转换，采用标准的加权平均算法。

Uses OpenCV's `cv2.cvtColor()` for RGB to grayscale conversion with standard weighted average algorithm.

### 直方图计算 / Histogram Calculation
使用OpenCV的`cv2.calcHist()`函数计算图像的灰度直方图。

Uses OpenCV's `cv2.calcHist()` to calculate image histogram.

### 降采样 / Downsampling
使用NumPy的数组切片操作实现降采样，保持图像的空间结构。

Uses NumPy array slicing for downsampling while preserving spatial structure.

### 灰度量化 / Gray Level Quantization
通过整数除法和乘法实现灰度级的量化，减少图像的灰度级别。

Implements gray level quantization through integer division and multiplication.

## 常见问题 / FAQ

### Q: 为什么图像不显示？/ Why don't images display?
A: 程序使用非交互式后端（Agg），图像会自动保存为PNG文件而不是显示在窗口中。

The program uses a non-interactive backend (Agg), images are saved as PNG files instead of displaying in windows.

### Q: 如何处理自己的图像？/ How to process my own images?
A: 将图像文件放在程序目录下，或者修改`main()`函数中的`test_images`列表。

Place your image files in the program directory, or modify the `test_images` list in the `main()` function.

### Q: 如何修改输出文件名？/ How to change output file names?
A: 在`main()`函数中修改`save_path`参数的值。

Modify the `save_path` parameter values in the `main()` function.

## 作者信息 / Author Information

图像处理实验室 / Image Processing Lab

## 许可证 / License

本项目仅用于教育和学习目的。

This project is for educational and learning purposes only.

## 更新日志 / Changelog

### v1.0.0 (2025)
- ✅ 实现图像基本操作
- ✅ 实现统计参数计算
- ✅ 实现图像采样功能
- ✅ 实现灰度级转换
- ✅ 添加详细注释
- ✅ 生成可视化结果

---

**实验要求已全部完成 / All experimental requirements completed** ✅
