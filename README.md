# CustomLinearAlgebra

> 从零开始学习线性代数,通过Python实践掌握计算机图形学和VR/XR开发的数学基础

## 项目简介

这是一个**学习导向**的项目,通过迭代式开发的方式,从零实现一个完整的线性代数库,同时学习计算机图形学和VR/XR开发所需的数学知识。

### 为什么做这个项目?

- 🎯 **目标明确**: 为VR/XR开发打下扎实的数学基础
- 📚 **理论+实践**: 不只是学数学公式,而是真正理解并实现
- 👁️ **可视化学习**: 每个概念都配有2D/3D可视化
- 🔄 **渐进式难度**: 50+个精心设计的迭代,从简单到复杂
- ⏱️ **适合碎片时间**: 每个迭代1-2小时,适合工作日学习

### 适合谁?

- 初级Python工程师,想学习线性代数
- 对计算机图形学感兴趣的开发者
- VR/XR开发者,想深入理解背后的数学
- 希望通过实践学习,而非纯理论学习

## 学习路线

项目分为5个阶段,共50+个迭代:

### 阶段一: 向量基础 (迭代1-10)
- 2D/3D向量的定义和运算
- 点积、叉积及其应用
- 简单的物理模拟

### 阶段二: 矩阵与线性变换 (迭代11-25)
- 矩阵运算和性质
- 2D/3D变换矩阵
- 齐次坐标系统
- 矩阵求逆和行列式

### 阶段三: 坐标系与投影 (迭代26-35)
- 坐标空间变换
- 相机系统(LookAt)
- 透视投影与正交投影
- 完整的3D渲染管线

### 阶段四: 高级主题 (迭代36-50)
- 四元数与旋转
- 特征值与特征向量
- 矩阵分解(LU, QR, SVD)
- PCA主成分分析

### 阶段五: 综合应用 (迭代51+)
- 简单的物理引擎
- 骨骼动画
- 光线追踪基础
- 根据兴趣自选方向

详细的迭代计划请查看 [`docs/迭代计划详解.md`](docs/迭代计划详解.md)

## 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/yourusername/CustomLinearAlgebra.git
cd CustomLinearAlgebra
```

### 2. 创建虚拟环境(推荐)

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate     # Windows
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

或者安装开发环境(包含测试和代码格式化工具):

```bash
pip install -e ".[dev,jupyter,all]"
```

### 4. 开始学习

阅读文档,从迭代1开始:

```bash
# 1. 阅读学习规划
open docs/学习规划总览.md

# 2. 查看迭代1的详细说明
open docs/迭代计划详解.md

# 3. 开始编码!
```

## 项目结构

```
CustomLinearAlgebra/
├── docs/                        # 📚 文档
│   ├── 学习规划总览.md          # 整体学习路线和目标
│   ├── 迭代计划详解.md          # 所有迭代的详细计划
│   ├── 知识点索引.md            # 线性代数知识点与代码映射
│   ├── 问题与解决方案.md        # 学习过程中的问题记录
│   └── 参考资源.md              # 推荐书籍、视频、文章
│
├── src/                         # 💻 源代码
│   ├── core/                    # 核心线性代数库
│   │   ├── vector2d.py          # 2D向量类
│   │   ├── vector3d.py          # 3D向量类
│   │   ├── matrix.py            # 矩阵类
│   │   └── quaternion.py        # 四元数类
│   │
│   ├── graphics/                # 🎨 3D图形变换引擎
│   │   ├── transform2d.py       # 2D变换
│   │   ├── transform3d.py       # 3D变换
│   │   ├── camera.py            # 相机系统
│   │   └── projection.py        # 投影矩阵
│   │
│   ├── visualization/           # 📊 可视化工具
│   │   ├── vector_plot.py       # 向量绘制
│   │   ├── matrix_plot.py       # 矩阵可视化
│   │   └── animation.py         # 动画工具
│   │
│   └── examples/                # 🎯 每个迭代的示例代码
│       ├── iter01_vector2d_basic.py
│       ├── iter02_vector_addition.py
│       └── ...
│
├── tests/                       # ✅ 单元测试
│   ├── test_vector2d.py
│   ├── test_vector3d.py
│   └── ...
│
├── notebooks/                   # 📓 Jupyter学习笔记
│   └── (你的学习笔记)
│
├── requirements.txt             # 依赖列表
├── pyproject.toml               # 项目配置
└── README.md                    # 本文件
```

## 文档导览

### 必读文档

1. **[学习规划总览.md](docs/学习规划总览.md)**
   - 项目愿景和学习目标
   - 完整的学习路线图
   - 学习方法建议

2. **[迭代计划详解.md](docs/迭代计划详解.md)**
   - 每个迭代的详细说明
   - 数学背景(通俗易懂)
   - 实现任务和验收标准

3. **[知识点索引.md](docs/知识点索引.md)**
   - 按数学概念查找代码位置
   - 按应用场景查找知识点
   - 常见问题速查

### 辅助文档

4. **[问题与解决方案.md](docs/问题与解决方案.md)**
   - 记录学习中遇到的问题
   - 持续更新的疑难解答

5. **[参考资源.md](docs/参考资源.md)**
   - 精选视频教程(3Blue1Brown等)
   - 推荐书籍和在线教材
   - 交互式学习网站

## 学习方法

### 每个迭代的标准流程

1. **阅读理论** (15-20分钟)
   - 阅读迭代计划中的数学背景
   - 理解要实现的功能目标

2. **编写代码** (40-60分钟)
   - 先写测试用例(TDD思想)
   - 实现核心功能代码
   - 编写可视化脚本

3. **运行验证** (15-20分钟)
   - 运行测试确保正确性
   - 运行可视化查看效果
   - 实验不同参数

4. **总结记录** (10-15分钟)
   - 在 `notebooks/` 中记录学习笔记
   - 遇到问题记录到 `docs/问题与解决方案.md`
   - 更新知识点索引

### 遇到困难时

- **数学概念不理解**: 查看[参考资源](docs/参考资源.md)中的视频
- **代码实现卡住**: 简化问题,从特殊情况入手
- **缺乏动力**: 跳到更有趣的迭代,或查看最终应用效果

详细建议请查看[学习规划总览](docs/学习规划总览.md#学习方法建议)

## 示例代码

完成迭代1后,你将能够编写这样的代码:

```python
from src.core.vector2d import Vector2D

# 创建向量
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

# 向量运算
v3 = v1 + v2               # 向量加法
length = v1.magnitude()     # 计算长度: 5.0
unit = v1.normalize()       # 归一化

# 可视化
from src.examples.iter01_vector2d_basic import visualize_vectors
visualize_vectors([v1, v2, v3])
```

完成迭代12后,你将能够旋转2D图形:

```python
from src.graphics.transform2d import rotation_matrix_2d
from src.core.matrix import Matrix
import math

# 创建旋转矩阵(旋转45度)
angle = math.radians(45)
rotation = rotation_matrix_2d(angle)

# 应用变换
points = [Vector2D(1, 0), Vector2D(0, 1), ...]
rotated_points = [rotation.multiply_vector(p) for p in points]
```

完成迭代37后,你将能够使用四元数进行3D旋转:

```python
from src.core.quaternion import Quaternion
from src.core.vector3d import Vector3D

# 创建四元数(绕Y轴旋转90度)
q = Quaternion.from_axis_angle(Vector3D(0, 1, 0), math.pi/2)

# 旋转向量
v = Vector3D(1, 0, 0)
v_rotated = q.rotate_vector(v)  # 结果: (0, 0, -1)

# 四元数插值(平滑旋转动画)
q1 = Quaternion.from_euler(0, 0, 0)
q2 = Quaternion.from_euler(0, math.pi, 0)
q_mid = q1.slerp(q2, 0.5)  # 中间状态
```

## 运行测试

```bash
# 运行所有测试
pytest

# 运行特定测试文件
pytest tests/test_vector2d.py

# 查看代码覆盖率
pytest --cov=src --cov-report=html
```

## 代码风格

项目使用以下工具保持代码质量:

```bash
# 格式化代码
black src/ tests/

# 排序import
isort src/ tests/

# 类型检查
mypy src/
```

## 技术栈

### 核心库
- **Python 3.10+**: 现代Python特性(类型提示、数据类等)
- **NumPy**: 用于性能对比和底层数组支持(核心算法自己实现)

### 可视化工具
- **Matplotlib**: 2D和基础3D可视化
- **PyVista/VTK**: 高级3D渲染和复杂场景

### 开发工具
- **Pytest**: 单元测试框架
- **Jupyter Notebook**: 交互式学习和实验
- **Black/isort**: 代码格式化
- **Mypy**: 类型检查

## VR/XR关联

本项目与VR/XR开发的联系:

| 学习内容 | VR/XR应用 |
|---------|----------|
| 3D向量 | 头显位置、手柄位置、物体坐标 |
| 点积 | 视野判断、角度计算 |
| 叉积 | 法线计算、左右判断 |
| 矩阵变换 | 模型变换、视图变换 |
| 四元数 | 旋转表示、避免万向锁 |
| 相机系统 | VR双目相机、视锥体 |
| 投影矩阵 | 3D到2D的投影 |

详细映射请查看[知识点索引](docs/知识点索引.md#vrxr应用问题)

## 贡献

这是一个个人学习项目,但欢迎:

- 提出改进建议(Issue)
- 分享学习心得
- 报告文档错误
- 提供更好的学习资源

## 许可证

MIT License

## 致谢

本项目受到以下资源的启发:

- [3Blue1Brown - 线性代数的本质](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [GAMES101 - 现代计算机图形学入门](https://sites.cs.ucsb.edu/~lingqi/teaching/games101.html)
- [Immersive Linear Algebra](http://immersivemath.com/ila/index.html)
- [Scratchapixel](https://www.scratchapixel.com/)

## 联系方式

- 项目主页: [GitHub](https://github.com/yourusername/CustomLinearAlgebra)
- 问题反馈: [Issues](https://github.com/yourusername/CustomLinearAlgebra/issues)

---

## 开始学习

准备好了吗?从这里开始:

1. ✅ 安装依赖: `pip install -r requirements.txt`
2. 📖 阅读规划: [`docs/学习规划总览.md`](docs/学习规划总览.md)
3. 🚀 开始迭代1: [`docs/迭代计划详解.md`](docs/迭代计划详解.md#迭代1-2d向量类与可视化)

祝学习顺利! 💪

---

**进度追踪**

- [ ] 迭代1-10: 向量基础
- [ ] 迭代11-25: 矩阵与变换
- [ ] 迭代26-35: 坐标系与投影
- [ ] 迭代36-50: 高级主题
- [ ] 迭代51+: 综合应用

记得在每个里程碑后庆祝一下! 🎉
