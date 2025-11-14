"""
迭代1示例: 2D向量的基础可视化

展示如何绘制向量并可视化归一化效果
"""

import matplotlib.pyplot as plt
import numpy as np
from src.core.vector2d import Vector2D

# 配置matplotlib支持中文显示
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei', 'STHeiti', 'Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


def plot_vector(ax, vector: Vector2D, origin=(0, 0), color='blue',
                label='', width=0.01):
    """在坐标系中绘制向量(箭头)

    Args:
        ax: matplotlib的坐标系对象
        vector: 要绘制的向量
        origin: 起点坐标
        color: 箭头颜色
        label: 标签文本
        width: 箭头宽度
    """
    ax.arrow(origin[0], origin[1], vector.x, vector.y,
             head_width=0.2, head_length=0.15,
             fc=color, ec=color, width=width,
             length_includes_head=True, label=label)


def visualize_basic_vectors():
    """可视化多个2D向量"""
    # 创建图形和坐标系
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # === 左图: 展示不同的向量 ===
    ax1.set_xlim(-1, 6)
    ax1.set_ylim(-1, 6)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='k', linewidth=0.5)
    ax1.axvline(x=0, color='k', linewidth=0.5)
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_title('多个2D向量示例')

    # 创建几个向量
    vectors = [
        (Vector2D(3, 4), 'red', 'v1 (3, 4)'),
        (Vector2D(2, 1), 'blue', 'v2 (2, 1)'),
        (Vector2D(5, 2), 'green', 'v3 (5, 2)'),
        (Vector2D(1, 5), 'purple', 'v4 (1, 5)'),
    ]

    # 绘制向量并标注长度
    for vec, color, label in vectors:
        plot_vector(ax1, vec, color=color, label=label)

        # 在箭头旁标注长度
        mag = vec.magnitude()
        mid_x, mid_y = vec.x / 2, vec.y / 2
        ax1.text(mid_x + 0.3, mid_y + 0.3,
                f'|v|={mag:.2f}',
                fontsize=9, color=color)

    ax1.legend()

    # === 右图: 展示归一化效果 ===
    ax2.set_xlim(-2, 6)
    ax2.set_ylim(-2, 6)
    ax2.set_aspect('equal')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='k', linewidth=0.5)
    ax2.axvline(x=0, color='k', linewidth=0.5)
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_title('向量归一化对比')

    # 绘制单位圆(归一化后的向量都在这个圆上)
    circle = plt.Circle((0, 0), 1, color='gray', fill=False,
                       linestyle='--', linewidth=2, alpha=0.5)
    ax2.add_patch(circle)
    ax2.text(1.2, 0.2, '单位圆\n(半径=1)', fontsize=10, color='gray')

    # 原始向量
    original = Vector2D(4, 3)
    plot_vector(ax2, original, color='blue',
               label=f'原始向量 (长度={original.magnitude():.2f})', width=0.015)

    # 归一化后的向量
    normalized = original.normalize()
    plot_vector(ax2, normalized, color='red',
               label=f'归一化后 (长度={normalized.magnitude():.2f})', width=0.015)

    # 标注说明
    ax2.text(2.5, 4, '归一化:\n保持方向不变\n但长度变为1',
            fontsize=11, bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    ax2.legend()

    plt.tight_layout()

    # 确保output目录存在
    import os
    os.makedirs('output', exist_ok=True)

    output_path = 'output/iter01_vectors.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"图像已保存为: {output_path}")
    plt.show()


def demonstrate_special_cases():
    """演示特殊情况"""
    print("\n=== 迭代1: Vector2D 基础功能演示 ===\n")

    # 1. 创建向量
    print("1. 创建向量:")
    v1 = Vector2D(3, 4)
    print(f"   v1 = {v1}")

    # 2. 计算模
    print("\n2. 计算向量的模(长度):")
    print(f"   |v1| = {v1.magnitude()}")
    print(f"   验证: √(3² + 4²) = √25 = 5 ✓")

    # 3. 归一化
    print("\n3. 归一化(转为单位向量):")
    v1_normalized = v1.normalize()
    print(f"   v1归一化后 = {v1_normalized}")
    print(f"   归一化后的长度 = {v1_normalized.magnitude():.6f}")

    # 4. 零向量的特殊情况
    print("\n4. 零向量:")
    zero = Vector2D(0, 0)
    print(f"   零向量 = {zero}")
    print(f"   零向量的长度 = {zero.magnitude()}")
    print("   尝试归一化零向量会抛出异常:")
    try:
        zero.normalize()
    except ValueError as e:
        print(f"   ✓ 捕获异常: {e}")

    print("\n=== 演示完成 ===")
    print("\n下一步: 运行 visualize_basic_vectors() 查看图形可视化")


if __name__ == "__main__":
    # 先运行控制台演示
    demonstrate_special_cases()

    # 然后显示可视化
    print("\n生成可视化图形...")
    visualize_basic_vectors()
