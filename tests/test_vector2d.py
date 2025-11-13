"""
Vector2D类的单元测试

迭代1: 测试基础功能(创建、模、归一化)
"""

import pytest
import math
from src.core.vector2d import Vector2D


class TestVector2DBasics:
    """测试Vector2D的基础功能"""

    def test_create_vector(self):
        """测试向量创建"""
        v = Vector2D(3, 4)
        assert v.x == 3.0
        assert v.y == 4.0

    def test_magnitude_simple(self):
        """测试简单向量的模计算"""
        v = Vector2D(3, 4)
        assert v.magnitude() == 5.0

    def test_magnitude_zero(self):
        """测试零向量的模"""
        v = Vector2D(0, 0)
        assert v.magnitude() == 0.0

    def test_magnitude_unit(self):
        """测试单位向量的模"""
        v = Vector2D(1, 0)
        assert v.magnitude() == 1.0

    def test_normalize_simple(self):
        """测试向量归一化"""
        v = Vector2D(3, 4)
        normalized = v.normalize()

        # 归一化后的向量长度应该为1
        assert abs(normalized.magnitude() - 1.0) < 1e-6

        # 方向应该保持一致(x和y的比例相同)
        assert abs(normalized.x / v.x - normalized.y / v.y) < 1e-6

    def test_normalize_already_unit(self):
        """测试已经是单位向量的归一化"""
        v = Vector2D(1, 0)
        normalized = v.normalize()
        assert abs(normalized.magnitude() - 1.0) < 1e-6
        assert normalized.x == 1.0
        assert normalized.y == 0.0

    def test_normalize_zero_vector(self):
        """测试零向量归一化应该抛出异常"""
        v = Vector2D(0, 0)
        with pytest.raises(ValueError, match="Cannot normalize zero vector"):
            v.normalize()

    def test_repr(self):
        """测试字符串表示"""
        v = Vector2D(1.5, 2.3)
        assert repr(v) == "Vector2D(1.50, 2.30)"

    def test_equality(self):
        """测试向量相等判断"""
        v1 = Vector2D(1, 2)
        v2 = Vector2D(1, 2)
        v3 = Vector2D(1, 3)

        assert v1 == v2
        assert not (v1 == v3)

    def test_equality_with_floating_point(self):
        """测试浮点数精度的相等判断"""
        v1 = Vector2D(1.0, 2.0)
        v2 = Vector2D(1.0 + 1e-10, 2.0 + 1e-10)
        assert v1 == v2


# TODO: 迭代2 - 添加加减法和数乘的测试
# class TestVector2DOperations:
#     pass

# TODO: 迭代3 - 添加点积和投影的测试
# class TestVector2DDotProduct:
#     pass
