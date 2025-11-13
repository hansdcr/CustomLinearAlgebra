# 快速开始指南

欢迎来到 CustomLinearAlgebra 学习项目! 这个指南将帮助你快速上手。

## 1️⃣ 安装依赖

```bash
# 确保你在项目根目录
cd CustomLinearAlgebra

# 安装基础依赖
pip install -r requirements.txt

# 或安装完整版(包括开发工具)
pip install -e ".[dev,jupyter,all]"
```

## 2️⃣ 验证安装

运行测试确保环境配置正确:

```bash
# 运行迭代1的测试
pytest tests/test_vector2d.py -v
```

如果看到所有测试通过(绿色✓),说明环境配置成功!

## 3️⃣ 运行第一个示例

```bash
# 运行迭代1的可视化示例
python src/examples/iter01_vector2d_basic.py
```

你应该会看到:
1. 控制台输出向量计算的演示
2. 弹出可视化窗口,展示向量和归一化效果
3. 生成图片 `output_iter01_vectors.png`

## 4️⃣ 开始学习

### 阅读顺序

1. **[学习规划总览](docs/学习规划总览.md)** (15分钟)
   - 了解整体学习路线
   - 理解项目目标和方法

2. **[迭代计划详解](docs/迭代计划详解.md)** (重点阅读迭代1)
   - 详细的数学背景讲解
   - 具体的实现任务

3. **开始编码!**
   - 参考 `src/core/vector2d.py` 的TODO注释
   - 完成迭代2和迭代3的功能

### 学习节奏建议

- **每天1-2小时**: 完成1个迭代
- **每周末集中学习**: 完成2-3个迭代
- **灵活调整**: 感兴趣的迭代可以多花时间深入

## 5️⃣ 常用命令

```bash
# 运行所有测试
pytest

# 运行特定迭代的测试
pytest tests/test_vector2d.py

# 查看测试覆盖率
pytest --cov=src --cov-report=html

# 启动Jupyter Notebook (用于学习笔记)
jupyter notebook

# 格式化代码(可选)
black src/ tests/
isort src/ tests/
```

## 6️⃣ 迭代1学习任务

### 第一步: 理解代码 (20分钟)

阅读并理解已实现的代码:
- `src/core/vector2d.py`: Vector2D类的实现
- `tests/test_vector2d.py`: 单元测试
- `src/examples/iter01_vector2d_basic.py`: 可视化示例

### 第二步: 运行和实验 (30分钟)

1. 修改示例代码中的向量坐标,看看结果如何变化
2. 尝试创建更多向量并可视化
3. 在Jupyter Notebook中交互式实验:

```python
from src.core.vector2d import Vector2D

v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(f"v1的长度: {v1.magnitude()}")
print(f"v1归一化: {v1.normalize()}")
```

### 第三步: 准备迭代2 (10分钟)

阅读[迭代计划详解](docs/迭代计划详解.md)中的迭代2内容,了解下一步要实现的功能。

## 7️⃣ 学习资源

### 必看视频

**3Blue1Brown - 线性代数的本质 第1集**
- 链接: https://www.youtube.com/watch?v=fNk_zzaMoSs
- 时长: 10分钟
- 内容: 向量的本质

观看这个视频会让你对向量有更深的理解!

### 推荐阅读

- [Immersive Linear Algebra - 第1章](http://immersivemath.com/ila/ch01_introduction/index.html)
- 交互式教材,非常直观

## 8️⃣ 遇到问题?

### 常见问题

**Q: 导入模块失败**
```
ModuleNotFoundError: No module named 'src'
```

A: 确保你在项目根目录运行命令,或者安装项目为可编辑包:
```bash
pip install -e .
```

**Q: Matplotlib不显示窗口**

A: 尝试不同的后端:
```python
import matplotlib
matplotlib.use('TkAgg')  # 或 'Qt5Agg'
import matplotlib.pyplot as plt
```

**Q: 数学概念不理解**

A: 查看 [参考资源](docs/参考资源.md) 中的视频教程,或在 [问题与解决方案](docs/问题与解决方案.md) 中查找类似问题。

## 9️⃣ 下一步

完成迭代1后:

1. ✅ 标记完成: 在README.md的进度追踪中勾选
2. 📝 记录笔记: 在 `notebooks/` 中创建学习笔记
3. 🎯 继续迭代2: 实现向量加减法和数乘

---

## 学习路线图 (前10个迭代)

```
迭代1 ✓ Vector2D基础
   ↓
迭代2 → 向量加减法与数乘
   ↓
迭代3 → 点积与投影
   ↓
迭代4 → Vector3D类
   ↓
迭代5 → 叉积与右手法则
   ↓
迭代6 → 向量综合应用
   ↓
迭代7 → 理解线性变换
   ↓
迭代8 → Matrix类
   ↓
迭代9 → 2D变换矩阵
   ↓
迭代10 → 齐次坐标
```

---

**准备好了吗? 开始你的线性代数学习之旅!** 🚀

有任何问题,记得查看 [文档](docs/) 或记录到 [问题与解决方案](docs/问题与解决方案.md)。

祝学习愉快! 💪
