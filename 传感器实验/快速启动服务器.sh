#!/bin/bash

echo "========================================"
echo "传感器工具箱 - Web演示版服务器"
echo "========================================"
echo ""

cd "$(dirname "$0")/web_demo"

echo "正在启动服务器..."
echo ""
echo "服务器地址："
echo ""

# 获取本机IP地址
if [[ "$OSTYPE" == "darwin"* ]]; then
    # Mac
    IP=$(ifconfig | grep "inet " | grep -v 127.0.0.1 | awk '{print $2}' | head -n 1)
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    IP=$(hostname -I | awk '{print $1}')
fi

if [ -n "$IP" ]; then
    echo "手机访问地址: http://$IP:8000"
else
    echo "无法自动获取IP，请手动查看："
    echo "  ifconfig (Linux/Mac)"
    echo "  ipconfig (Windows)"
    echo ""
    echo "然后访问: http://你的IP:8000"
fi

echo ""
echo "按 Ctrl+C 停止服务器"
echo "========================================"
echo ""

python3 -m http.server 8000

