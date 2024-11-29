# 使用官方的 Python 基础镜像
FROM python:3.11.1

# 设置工作目录
WORKDIR /app

# 复制项目文件到容器
COPY src/ /app/
# 复制配置文件
COPY config/ /app/config/
# 复制依赖文件
COPY requirements.txt /app/requirements.txt

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 指定默认启动命令
CMD ["python", "main.py"]
