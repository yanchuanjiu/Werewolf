#!/bin/bash

# 拉取最新的代码
git pull

# 进入前端目录，安装依赖并构建
cd werewolf-frontend
npm i
npm run build

# 返回到后端目录
cd ../werewolf-backend

# 设置 Python 虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt

# 运行任何需要的数据库迁移
# 如果使用 Flask-Migrate，可以是：
flask db upgrade

# 停止当前运行的 Python 应用，这可能需要额外的逻辑来确定进程 ID 并杀掉它
pkill -f 'python'

# 启动新的 Python 应用，例如使用 Gunicorn 作为 WSGI 服务器
gunicorn -w 4 -b 0.0.0.0:8000 app:app

# 如果是 Flask 内置服务器（仅适用于开发）
# flask run --host=0.0.0.0 --port=8000
