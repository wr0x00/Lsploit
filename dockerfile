# 使用官方Python基础镜像，指定Python版本
FROM python:3.10

# 设置工作目录
WORKDIR /

# 复制依赖文件到容器
COPY requirements.txt .

# 安装Python依赖库
RUN pip install -r requirements.txt

# 复制项目代码到容器
COPY . .

# 定义容器启动命令
CMD ["python", "lp.py"]