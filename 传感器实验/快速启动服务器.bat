@echo off
chcp 65001 >nul
echo ========================================
echo 传感器工具箱 - Web演示版服务器
echo ========================================
echo.

cd /d %~dp0web_demo

echo 正在启动服务器...
echo.
echo 服务器地址将在下方显示
echo 请在手机浏览器中输入显示的地址
echo.
echo 按 Ctrl+C 停止服务器
echo ========================================
echo.

REM 获取本机IP地址
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /c:"IPv4"') do (
    set IP=%%a
    set IP=!IP:~1!
    echo 手机访问地址: http://!IP!:8000
    echo.
    goto :found
)

:found
python -m http.server 8000

pause

