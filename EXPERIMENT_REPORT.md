# 图像处理实验报告 / Image Processing Experiment Report

## 实验概述 / Experiment Overview

本实验使用Python实现了完整的图像处理系统，包括图像基本操作、统计分析、采样和灰度转换等功能。

This experiment implements a complete image processing system in Python, including basic image operations, statistical analysis, sampling, and grayscale transformation.

---

## 一、实验环境 / Experiment Environment

### 编程语言 / Programming Language
- Python 3.12.3

### 依赖库 / Dependencies
- numpy 2.2.6 - 数值计算 / Numerical computation
- opencv-python 4.12.0.88 - 图像处理 / Image processing
- matplotlib 3.10.7 - 数据可视化 / Data visualization

### 测试图像 / Test Images
- lena.bmp / lena.jpg (256×256) - 标准人像测试图像
- rice.png - 米粒图像
- moon.tif - 月球表面图像
- pollen.jpg - 花粉图像
- cameraman.tif - 摄影师图像

---

## 二、实验步骤 / Experiment Steps

### 任务1：图像读取、显示、转换和直方图 / Task 1: Image I/O, Display, Conversion and Histogram

#### 实验步骤 / Steps
1. 使用OpenCV的`cv2.imread()`读取图像
2. 使用matplotlib显示图像（BGR转RGB）
3. 使用`cv2.cvtColor()`将RGB图像转换为灰度图像
4. 使用`cv2.calcHist()`计算并显示直方图

#### 详细设计（Python代码） / Detailed Design (Python Code)
```python
def read_image(self) -> np.ndarray:
    """读取图像 - Read image"""
    self.image = cv2.imread(self.image_path)
    if self.image is None:
        raise FileNotFoundError(f"无法读取图像: {self.image_path}")
    return self.image

def rgb_to_gray(self) -> np.ndarray:
    """RGB图像转灰度图像 - Convert RGB to grayscale"""
    if len(self.image.shape) == 2:
        self.gray_image = self.image
    else:
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    return self.gray_image

def display_histogram(self, image: np.ndarray = None, save_path: str = None) -> None:
    """显示图像直方图 - Display image histogram"""
    if image is None:
        if self.gray_image is None:
            self.rgb_to_gray()
        image = self.gray_image
    
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist, color='black')
    plt.title('灰度直方图 / Grayscale Histogram')
    plt.xlabel('像素值 / Pixel Value')
    plt.ylabel('频率 / Frequency')
```

#### 测试结果 / Test Results
- ✅ 成功读取lena.bmp图像 (256×256×3)
- ✅ 成功转换为灰度图像 (256×256)
- ✅ 成功生成直方图显示像素分布
- 📊 输出文件: `output_1_original_lena.png`, `output_1_grayscale_lena.png`, `output_1_histogram_lena.png`

---

### 任务2：计算图像统计参数 / Task 2: Calculate Image Statistics

#### 实验步骤 / Steps
1. 计算像素总数 - `image.size`
2. 获取图像大小 - `image.shape`
3. 计算平均值 - `np.mean()`
4. 计算标准差 - `np.std()`
5. 计算相关系数 - `np.corrcoef()`
6. 计算协方差矩阵 - `np.cov()`

#### 详细设计（Python代码） / Detailed Design (Python Code)
```python
def calculate_statistics(self, image: np.ndarray = None) -> dict:
    """计算图像统计参数 - Calculate image statistics"""
    if image is None:
        if self.gray_image is None:
            self.rgb_to_gray()
        image = self.gray_image
    
    stats = {
        '像素个数 / Pixel Count': image.size,
        '图像大小 / Image Size': image.shape,
        '平均值 / Mean': np.mean(image),
        '标准差 / Standard Deviation': np.std(image),
        '最小值 / Min': np.min(image),
        '最大值 / Max': np.max(image),
        '中位数 / Median': np.median(image)
    }
    return stats

@staticmethod
def calculate_correlation(image1: np.ndarray, image2: np.ndarray) -> float:
    """计算两幅图像的相关系数"""
    img1_flat = image1.flatten().astype(np.float64)
    img2_flat = image2.flatten().astype(np.float64)
    correlation = np.corrcoef(img1_flat, img2_flat)[0, 1]
    return correlation

@staticmethod
def calculate_covariance_matrix(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
    """计算两幅图像的协方差矩阵"""
    img1_flat = image1.flatten().astype(np.float64)
    img2_flat = image2.flatten().astype(np.float64)
    covariance_matrix = np.cov(img1_flat, img2_flat)
    return covariance_matrix
```

#### 测试结果 / Test Results
**Lena图像统计参数：**
```
像素个数 / Pixel Count: 65536
图像大小 / Image Size: (256, 256)
平均值 / Mean: 97.77235412597656
标准差 / Standard Deviation: 52.77728733633082
最小值 / Min: 3
最大值 / Max: 238
中位数 / Median: 96.0
```

**Lena.bmp与Lena.jpg的相关性分析：**
```
相关系数 / Correlation Coefficient: 0.947285
协方差矩阵 / Covariance Matrix:
[[2785.4845617  2370.33549531]
 [2370.33549531 2247.80145231]]
```

**分析 / Analysis:**
- 两幅图像的相关系数为0.947，表明两幅图像高度相关（BMP和JPG格式的同一图像）
- 协方差矩阵对角线元素为各自的方差，非对角线元素为协方差

---

### 任务3：图像采样（降采样）/ Task 3: Image Sampling (Downsampling)

#### 实验步骤 / Steps
1. 实现降采样算法（使用NumPy切片）
2. 分别进行2倍、4倍、8倍降采样
3. 显示并对比不同采样率的结果

#### 详细设计（Python代码） / Detailed Design (Python Code)
```python
def downsample(self, factor: int, image: np.ndarray = None) -> np.ndarray:
    """
    图像降采样 - Downsample image
    
    参数:
        factor: 降采样因子 (2, 4, 8等)
    
    返回:
        降采样后的图像
    """
    if image is None:
        if self.gray_image is None:
            self.rgb_to_gray()
        image = self.gray_image
    
    # 使用切片进行降采样
    # Use slicing for downsampling
    downsampled = image[::factor, ::factor]
    
    print(f"降采样 {factor}x: 原始大小 {image.shape} -> 降采样后大小 {downsampled.shape}")
    
    return downsampled
```

#### 测试结果 / Test Results
| 采样方式 | 原始尺寸 | 结果尺寸 | 数据量变化 |
|---------|---------|---------|----------|
| 原始图像 | 256×256 | 256×256 | 100% |
| 2倍降采样 | 256×256 | 128×128 | 25% |
| 4倍降采样 | 256×256 | 64×64 | 6.25% |
| 8倍降采样 | 256×256 | 32×32 | 1.56% |

📊 输出文件: `output_3_downsampling_lena.png`

**观察结果 / Observations:**
- 2倍降采样：图像质量良好，细节保留较多
- 4倍降采样：可以识别图像内容，但细节丢失明显
- 8倍降采样：图像变得模糊，只能识别大致轮廓

---

### 任务4：灰度级转换 / Task 4: Gray Level Transformation

#### 实验步骤 / Steps
1. 实现灰度级量化算法
2. 测试不同灰度级（256, 128, 64, 32, 16, 8, 4, 2）
3. 可视化显示不同灰度级的效果

#### 详细设计（Python代码） / Detailed Design (Python Code)
```python
def gray_level_quantization(self, levels: int, image: np.ndarray = None) -> np.ndarray:
    """
    灰度级量化 - Gray level quantization
    
    参数:
        levels: 灰度级数量 (2, 4, 8, 16, 32, 64, 128, 256)
    
    返回:
        量化后的图像
    """
    if image is None:
        if self.gray_image is None:
            self.rgb_to_gray()
        image = self.gray_image
    
    # 计算量化步长
    # Calculate quantization step
    step = 256 // levels
    
    # 执行量化：将像素值除以步长再乘以步长
    # Perform quantization
    quantized = (image // step) * step
    
    return quantized.astype(np.uint8)
```

#### 测试结果 / Test Results

| 灰度级 | 量化效果 | 视觉质量 |
|-------|---------|---------|
| 256级 | 原始图像 | 优秀 - 完整细节 |
| 128级 | 轻微量化 | 良好 - 几乎无可见差异 |
| 64级 | 明显量化 | 良好 - 轻微带状效应 |
| 32级 | 显著量化 | 中等 - 明显带状效应 |
| 16级 | 严重量化 | 一般 - 严重带状效应 |
| 8级 | 极度量化 | 较差 - 海报化效果明显 |
| 4级 | 最小细节 | 差 - 仅保留基本轮廓 |
| 2级 | 二值化 | 很差 - 黑白二值图像 |

📊 输出文件: `output_4_gray_levels_lena.png`

**观察结果 / Observations:**
- **256-128级**: 人眼几乎无法分辨差异
- **64-32级**: 开始出现明显的"带状效应"（false contouring）
- **16-8级**: 图像呈现"海报化"效果（posterization）
- **4-2级**: 图像细节严重丢失，仅保留基本形状

---

## 三、算法原理说明 / Algorithm Principles

### 1. RGB到灰度转换 / RGB to Grayscale Conversion
OpenCV使用加权平均法：
```
Gray = 0.299 × R + 0.587 × G + 0.114 × B
```
这些权重基于人眼对不同颜色的敏感度。

### 2. 直方图计算 / Histogram Calculation
统计每个灰度级（0-255）出现的频率，反映图像的亮度分布特征。

### 3. 降采样 / Downsampling
通过跳过像素实现：
- 2倍降采样：每隔1个像素采样一次 `image[::2, ::2]`
- 4倍降采样：每隔3个像素采样一次 `image[::4, ::4]`
- 8倍降采样：每隔7个像素采样一次 `image[::8, ::8]`

### 4. 灰度级量化 / Gray Level Quantization
通过整数除法和乘法实现：
```
step = 256 // levels
quantized = (pixel_value // step) * step
```

---

## 四、程序特点 / Program Features

### ✅ 代码规范 / Code Standards
1. **缩进格式** - 使用4个空格缩进，符合PEP 8规范
2. **详细注释** - 每个函数都有中英文注释和文档字符串
3. **类型提示** - 使用Python类型提示增强代码可读性
4. **模块化设计** - 采用面向对象编程，功能封装在ImageProcessor类中

### ✅ 功能完整性 / Functionality Completeness
- ✓ 图像读、写、显示
- ✓ RGB转灰度
- ✓ 直方图显示
- ✓ 统计参数计算（7种参数）
- ✓ 相关系数和协方差矩阵
- ✓ 三种降采样率（2x, 4x, 8x）
- ✓ 八种灰度级转换（256, 128, 64, 32, 16, 8, 4, 2）

### ✅ 可视化输出 / Visualization Output
所有实验结果都保存为高质量PNG图像文件，便于分析和展示。

---

## 五、实验结论 / Conclusions

1. **图像采样**：降采样会导致图像信息损失，采样率越低，图像质量越差。适当的降采样（2-4倍）可以在保持可接受质量的同时减少数据量。

2. **灰度级转换**：人眼对灰度变化的敏感度有限，64级以上的灰度图像已经能满足大多数应用需求。过低的灰度级会导致"假轮廓"现象。

3. **统计分析**：通过统计参数可以定量分析图像特征，相关系数和协方差矩阵可用于图像相似度比较。

4. **直方图分析**：直方图能直观反映图像的亮度分布，对于图像增强、阈值分割等后续处理具有指导意义。

---

## 六、安全性检查 / Security Check

✅ **CodeQL扫描结果**: 无安全漏洞

```
Analysis Result for 'python'. Found 0 alerts:
- **python**: No alerts found.
```

---

## 七、实验文件清单 / File List

### 源代码文件 / Source Code Files
- `image_processing.py` - 主程序文件（510行，包含详细注释）
- `requirements.txt` - Python依赖列表

### 文档文件 / Documentation Files
- `README.md` - 项目说明文档（中英文）
- `EXPERIMENT_REPORT.md` - 实验报告（本文件）
- `.gitignore` - Git忽略配置

### 输入图像 / Input Images
- `lena.bmp`, `lena.jpg`, `rice.png`, `moon.tif`, `pollen.jpg`
- `cameraman.tif`, `circuit.tif`, `eight.tif`

### 输出文件 / Output Files
- `gray_lena.bmp` - 灰度图像
- `output_1_original_lena.png` - 原始图像显示
- `output_1_grayscale_lena.png` - 灰度图像显示
- `output_1_histogram_lena.png` - 直方图
- `output_3_downsampling_lena.png` - 降采样结果
- `output_4_gray_levels_lena.png` - 灰度级转换结果

---

## 八、实验总结 / Summary

本实验成功实现了完整的图像处理系统，所有要求的功能都已实现并通过测试。程序代码规范，注释详细，输出结果清晰，达到了实验要求。

This experiment successfully implements a complete image processing system. All required functions have been implemented and tested. The code is well-structured with detailed comments, and the output results are clear, meeting all experimental requirements.

**实验完成度**: 100% ✅

---

*实验日期 / Experiment Date: 2025-11-20*
*作者 / Author: Image Processing Lab*
