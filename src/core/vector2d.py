"""
2D向量类实现

迭代1: 基础向量类,包含模、归一化等功能
"""

from __future__ import annotations
import math
from typing import Union


class Vector2D:
    """2D向量类

    表示二维空间中的向量,支持基本的向量运算。

    Attributes:
        x: x坐标分量
        y: y坐标分量

    Examples:
        >>> v = Vector2D(3, 4)
        >>> v.magnitude()
        5.0
        >>> v.normalize().magnitude()
        1.0
    """

    def __init__(self, x: float, y: float) -> None:
        """初始化2D向量

        Args:
            x: x坐标分量
            y: y坐标分量
        """
        self.x = float(x)
        self.y = float(y)

    def magnitude(self) -> float:
        """计算向量的模(长度)

        使用勾股定理: ||v|| = √(x² + y²)

        Returns:
            向量的长度

        Examples:
            >>> Vector2D(3, 4).magnitude()
            5.0
            >>> Vector2D(0, 0).magnitude()
            0.0
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def normalize(self) -> Vector2D:
        """返回归一化后的向量(单位向量)

        单位向量的长度为1,但方向与原向量相同。

        Returns:
            归一化后的新向量

        Raises:
            ValueError: 如果向量长度为0(零向量无法归一化)

        Examples:
            >>> v = Vector2D(3, 4).normalize()
            >>> abs(v.magnitude() - 1.0) < 1e-6
            True
        """
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector2D(self.x / mag, self.y / mag)

    def __repr__(self) -> str:
        """返回向量的字符串表示

        Returns:
            格式化的字符串

        Examples:
            >>> Vector2D(1.5, 2.3)
            Vector2D(1.50, 2.30)
        """
        return f"Vector2D({self.x:.2f}, {self.y:.2f})"

    def __eq__(self, other: object) -> bool:
        """判断两个向量是否相等

        Args:
            other: 另一个向量

        Returns:
            是否相等
        """
        if not isinstance(other, Vector2D):
            return False
        # 使用小的容差进行浮点数比较
        return (abs(self.x - other.x) < 1e-9 and
                abs(self.y - other.y) < 1e-9)

    # TODO: 迭代2 - 实现向量加减法和数乘
    # def __add__(self, other: Vector2D) -> Vector2D:
    #     pass
    #
    # def __sub__(self, other: Vector2D) -> Vector2D:
    #     pass
    #
    # def __mul__(self, scalar: float) -> Vector2D:
    #     pass

    # TODO: 迭代3 - 实现点积和投影
    # def dot(self, other: Vector2D) -> float:
    #     pass
    #
    # def angle(self, other: Vector2D) -> float:
    #     pass
    #
    # def project_onto(self, other: Vector2D) -> Vector2D:
    #     pass
