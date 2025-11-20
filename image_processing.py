#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图像处理实验程序
Image Processing Experiment Program

功能包括:
1. 图像读、写、显示、RGB转灰度、直方图显示
2. 图像统计参数计算
3. 图像采样
4. 灰度转换

作者: Image Processing Lab
日期: 2025
"""

import cv2
import numpy as np
import matplotlib
matplotlib.use('Agg')  # 使用非交互式后端 / Use non-interactive backend
import matplotlib.pyplot as plt
import os
from typing import Tuple, Optional


class ImageProcessor:
    """图像处理类 - Image Processing Class"""
    
    def __init__(self, image_path: str):
        """
        初始化图像处理器
        Initialize image processor
        
        参数:
            image_path: 图像文件路径
        """
        self.image_path = image_path
        self.image = None
        self.gray_image = None
        
    def read_image(self) -> np.ndarray:
        """
        读取图像 - Read image
        
        返回:
            numpy数组格式的图像
        """
        # 读取图像，支持彩色和灰度
        # Read image, support both color and grayscale
        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise FileNotFoundError(f"无法读取图像: {self.image_path}")
        print(f"成功读取图像: {self.image_path}")
        print(f"图像形状: {self.image.shape}")
        return self.image
    
    def write_image(self, output_path: str, image: np.ndarray = None) -> None:
        """
        保存图像 - Write image to file
        
        参数:
            output_path: 输出文件路径
            image: 要保存的图像，如果为None则保存当前图像
        """
        if image is None:
            image = self.image
        cv2.imwrite(output_path, image)
        print(f"图像已保存至: {output_path}")
    
    def display_image(self, image: np.ndarray = None, title: str = "Image", save_path: str = None) -> None:
        """
        显示图像 - Display image
        
        参数:
            image: 要显示的图像，如果为None则显示当前图像
            title: 图像标题
            save_path: 保存图像的路径
        """
        if image is None:
            image = self.image
        
        plt.figure(figsize=(8, 8))
        
        # 判断是彩色图像还是灰度图像
        # Determine if color or grayscale image
        if len(image.shape) == 3:
            # OpenCV使用BGR格式，matplotlib使用RGB格式，需要转换
            # OpenCV uses BGR, matplotlib uses RGB, need conversion
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            plt.imshow(image_rgb)
        else:
            plt.imshow(image, cmap='gray')
        
        plt.title(title)
        plt.axis('off')
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"图像已保存至: {save_path}")
        
        plt.close()
    
    def rgb_to_gray(self) -> np.ndarray:
        """
        RGB图像转灰度图像 - Convert RGB to grayscale
        
        返回:
            灰度图像
        """
        if len(self.image.shape) == 2:
            # 已经是灰度图像
            # Already grayscale
            self.gray_image = self.image
            print("图像已经是灰度图像")
        else:
            # 使用OpenCV的转换函数
            # Use OpenCV conversion function
            self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            print("RGB图像已转换为灰度图像")
        
        return self.gray_image
    
    def display_histogram(self, image: np.ndarray = None, save_path: str = None) -> None:
        """
        显示图像直方图 - Display image histogram
        
        参数:
            image: 要显示直方图的图像，如果为None则使用灰度图像
            save_path: 保存图像的路径
        """
        if image is None:
            if self.gray_image is None:
                self.rgb_to_gray()
            image = self.gray_image
        
        # 创建图形
        # Create figure
        plt.figure(figsize=(12, 4))
        
        # 如果是彩色图像，显示RGB三个通道的直方图
        # If color image, show histograms for RGB channels
        if len(image.shape) == 3:
            colors = ('b', 'g', 'r')
            channel_names = ('Blue', 'Green', 'Red')
            
            for i, (color, name) in enumerate(zip(colors, channel_names)):
                hist = cv2.calcHist([image], [i], None, [256], [0, 256])
                plt.plot(hist, color=color, label=name)
            
            plt.title('RGB直方图 / RGB Histogram')
            plt.legend()
        else:
            # 灰度图像直方图
            # Grayscale histogram
            hist = cv2.calcHist([image], [0], None, [256], [0, 256])
            plt.plot(hist, color='black')
            plt.title('灰度直方图 / Grayscale Histogram')
        
        plt.xlabel('像素值 / Pixel Value')
        plt.ylabel('频率 / Frequency')
        plt.xlim([0, 256])
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"直方图已保存至: {save_path}")
        
        plt.close()
    
    def calculate_statistics(self, image: np.ndarray = None) -> dict:
        """
        计算图像统计参数 - Calculate image statistics
        
        参数:
            image: 要计算统计参数的图像
            
        返回:
            包含统计参数的字典
        """
        if image is None:
            if self.gray_image is None:
                self.rgb_to_gray()
            image = self.gray_image
        
        # 计算各种统计参数
        # Calculate various statistics
        stats = {
            '像素个数 / Pixel Count': image.size,
            '图像大小 / Image Size': image.shape,
            '平均值 / Mean': np.mean(image),
            '标准差 / Standard Deviation': np.std(image),
            '最小值 / Min': np.min(image),
            '最大值 / Max': np.max(image),
            '中位数 / Median': np.median(image)
        }
        
        # 打印统计信息
        # Print statistics
        print("\n" + "="*50)
        print("图像统计参数 / Image Statistics")
        print("="*50)
        for key, value in stats.items():
            print(f"{key}: {value}")
        print("="*50 + "\n")
        
        return stats
    
    @staticmethod
    def calculate_correlation(image1: np.ndarray, image2: np.ndarray) -> float:
        """
        计算两幅图像的相关系数 - Calculate correlation coefficient
        
        参数:
            image1: 第一幅图像
            image2: 第二幅图像
            
        返回:
            相关系数
        """
        # 确保两幅图像大小相同
        # Ensure both images have same size
        if image1.shape != image2.shape:
            raise ValueError("两幅图像大小必须相同 / Images must have same size")
        
        # 将图像展平为一维数组
        # Flatten images to 1D arrays
        img1_flat = image1.flatten().astype(np.float64)
        img2_flat = image2.flatten().astype(np.float64)
        
        # 计算相关系数
        # Calculate correlation coefficient
        correlation = np.corrcoef(img1_flat, img2_flat)[0, 1]
        
        print(f"两幅图像的相关系数 / Correlation Coefficient: {correlation:.6f}")
        return correlation
    
    @staticmethod
    def calculate_covariance_matrix(image1: np.ndarray, image2: np.ndarray) -> np.ndarray:
        """
        计算两幅图像的协方差矩阵 - Calculate covariance matrix
        
        参数:
            image1: 第一幅图像
            image2: 第二幅图像
            
        返回:
            协方差矩阵
        """
        # 确保两幅图像大小相同
        # Ensure both images have same size
        if image1.shape != image2.shape:
            raise ValueError("两幅图像大小必须相同 / Images must have same size")
        
        # 将图像展平为一维数组
        # Flatten images to 1D arrays
        img1_flat = image1.flatten().astype(np.float64)
        img2_flat = image2.flatten().astype(np.float64)
        
        # 计算协方差矩阵
        # Calculate covariance matrix
        covariance_matrix = np.cov(img1_flat, img2_flat)
        
        print("\n协方差矩阵 / Covariance Matrix:")
        print(covariance_matrix)
        print()
        
        return covariance_matrix
    
    def downsample(self, factor: int, image: np.ndarray = None) -> np.ndarray:
        """
        图像降采样 - Downsample image
        
        参数:
            factor: 降采样因子 (2, 4, 8等)
            image: 要降采样的图像
            
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
    
    def display_downsampling_results(self, save_path: str = None) -> None:
        """
        显示不同降采样率的结果 - Display downsampling results
        
        参数:
            save_path: 保存图像的路径
        """
        if self.gray_image is None:
            self.rgb_to_gray()
        
        # 创建子图显示不同采样率
        # Create subplots for different sampling rates
        fig, axes = plt.subplots(2, 2, figsize=(12, 12))
        
        # 原始图像
        # Original image
        axes[0, 0].imshow(self.gray_image, cmap='gray')
        axes[0, 0].set_title(f'原始图像 / Original\n{self.gray_image.shape}')
        axes[0, 0].axis('off')
        
        # 2x降采样
        # 2x downsampling
        down_2x = self.downsample(2)
        axes[0, 1].imshow(down_2x, cmap='gray')
        axes[0, 1].set_title(f'2x降采样 / 2x Downsampling\n{down_2x.shape}')
        axes[0, 1].axis('off')
        
        # 4x降采样
        # 4x downsampling
        down_4x = self.downsample(4)
        axes[1, 0].imshow(down_4x, cmap='gray')
        axes[1, 0].set_title(f'4x降采样 / 4x Downsampling\n{down_4x.shape}')
        axes[1, 0].axis('off')
        
        # 8x降采样
        # 8x downsampling
        down_8x = self.downsample(8)
        axes[1, 1].imshow(down_8x, cmap='gray')
        axes[1, 1].set_title(f'8x降采样 / 8x Downsampling\n{down_8x.shape}')
        axes[1, 1].axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"降采样结果已保存至: {save_path}")
        
        plt.close()
    
    def gray_level_quantization(self, levels: int, image: np.ndarray = None) -> np.ndarray:
        """
        灰度级量化 - Gray level quantization
        
        参数:
            levels: 灰度级数量 (2, 4, 8, 16, 32, 64, 128, 256)
            image: 要量化的图像
            
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
        
        # 执行量化
        # Perform quantization
        quantized = (image // step) * step
        
        print(f"灰度级量化: {levels} 级")
        
        return quantized.astype(np.uint8)
    
    def display_gray_level_results(self, save_path: str = None) -> None:
        """
        显示不同灰度级的结果 - Display gray level quantization results
        
        参数:
            save_path: 保存图像的路径
        """
        if self.gray_image is None:
            self.rgb_to_gray()
        
        # 定义要测试的灰度级
        # Define gray levels to test
        levels = [256, 128, 64, 32, 16, 8, 4, 2]
        
        # 创建子图
        # Create subplots
        fig, axes = plt.subplots(2, 4, figsize=(16, 8))
        axes = axes.flatten()
        
        for idx, level in enumerate(levels):
            quantized = self.gray_level_quantization(level)
            axes[idx].imshow(quantized, cmap='gray', vmin=0, vmax=255)
            axes[idx].set_title(f'{level} 灰度级 / {level} Gray Levels')
            axes[idx].axis('off')
        
        plt.tight_layout()
        
        if save_path:
            plt.savefig(save_path, dpi=150, bbox_inches='tight')
            print(f"灰度级转换结果已保存至: {save_path}")
        
        plt.close()


def main():
    """主函数 - Main function"""
    
    print("="*70)
    print("图像处理实验程序 / Image Processing Experiment Program")
    print("="*70)
    
    # 可用的测试图像
    # Available test images
    test_images = ['lena.bmp', 'lena.jpg', 'rice.png', 'moon.tif', 'pollen.jpg']
    
    # 选择一个测试图像
    # Select a test image
    for img_name in test_images:
        if os.path.exists(img_name):
            print(f"\n使用测试图像: {img_name}")
            
            # 创建图像处理器
            # Create image processor
            processor = ImageProcessor(img_name)
            
            print("\n" + "="*70)
            print("任务1: 图像读取、显示、RGB转灰度、直方图")
            print("Task 1: Image Read, Display, RGB to Gray, Histogram")
            print("="*70)
            
            # 读取图像
            # Read image
            img = processor.read_image()
            
            # 显示原始图像
            # Display original image
            print("\n保存原始图像显示...")
            base_name = os.path.splitext(img_name)[0]
            processor.display_image(title=f"原始图像 / Original Image - {img_name}", 
                                  save_path=f"output_1_original_{base_name}.png")
            
            # RGB转灰度
            # RGB to grayscale
            gray_img = processor.rgb_to_gray()
            
            # 显示灰度图像
            # Display grayscale image
            print("\n保存灰度图像显示...")
            processor.display_image(gray_img, title=f"灰度图像 / Grayscale Image - {img_name}",
                                  save_path=f"output_1_grayscale_{base_name}.png")
            
            # 显示直方图
            # Display histogram
            print("\n保存直方图...")
            processor.display_histogram(save_path=f"output_1_histogram_{base_name}.png")
            
            # 保存灰度图像
            # Save grayscale image
            output_path = f"gray_{img_name}"
            processor.write_image(output_path, gray_img)
            
            print("\n" + "="*70)
            print("任务2: 计算图像统计参数")
            print("Task 2: Calculate Image Statistics")
            print("="*70)
            
            # 计算统计参数
            # Calculate statistics
            stats = processor.calculate_statistics()
            
            # 如果有其他图像，计算相关系数和协方差矩阵
            # If other images exist, calculate correlation and covariance
            other_images = [img for img in test_images if img != img_name and os.path.exists(img)]
            if other_images:
                print("\n计算与其他图像的相关系数和协方差矩阵...")
                other_processor = ImageProcessor(other_images[0])
                other_processor.read_image()
                other_gray = other_processor.rgb_to_gray()
                
                # 调整大小以匹配
                # Resize to match
                if gray_img.shape != other_gray.shape:
                    other_gray = cv2.resize(other_gray, (gray_img.shape[1], gray_img.shape[0]))
                
                # 计算相关系数
                # Calculate correlation
                correlation = ImageProcessor.calculate_correlation(gray_img, other_gray)
                
                # 计算协方差矩阵
                # Calculate covariance matrix
                covariance = ImageProcessor.calculate_covariance_matrix(gray_img, other_gray)
            
            print("\n" + "="*70)
            print("任务3: 图像采样 (降采样)")
            print("Task 3: Image Sampling (Downsampling)")
            print("="*70)
            
            # 显示降采样结果
            # Display downsampling results
            print("\n保存不同降采样率的结果...")
            processor.display_downsampling_results(save_path=f"output_3_downsampling_{base_name}.png")
            
            print("\n" + "="*70)
            print("任务4: 灰度级转换")
            print("Task 4: Gray Level Transformation")
            print("="*70)
            
            # 显示不同灰度级的结果
            # Display gray level quantization results
            print("\n保存不同灰度级的结果...")
            processor.display_gray_level_results(save_path=f"output_4_gray_levels_{base_name}.png")
            
            print("\n" + "="*70)
            print(f"图像 {img_name} 的所有实验完成！")
            print(f"All experiments completed for image {img_name}!")
            print("="*70)
            
            # 只处理第一个找到的图像（可以修改为处理所有图像）
            # Only process first found image (can be modified to process all)
            break
    else:
        print("错误: 未找到测试图像文件！")
        print("Error: No test image files found!")


if __name__ == "__main__":
    main()
