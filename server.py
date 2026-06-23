# -*- coding: utf-8 -*-
"""
刷题系统 - 本地服务器（支持手机访问）
双击运行或在终端执行本文件。
"""
import http.server, socketserver, os, socket, sys, webbrowser

DIR = r'C:\Users\杨梓依\Downloads\期末复习题库'
PORT = 8888
FILE = '刷题系统.html'

os.chdir(DIR)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

# Get LAN IP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(('10.255.255.255', 1))
    ip = s.getsockname()[0]
except:
    ip = '127.0.0.1'
finally:
    s.close()

print('=' * 50)
print('  期末复习刷题系统 - 手机访问服务器')
print('=' * 50)
print(f'  电脑访问: http://localhost:{PORT}/{FILE}')
print(f'  手机访问: http://{ip}:{PORT}/{FILE}')
print()
print('  📌 确保手机和电脑连接同一WiFi')
print('  📌 在手机浏览器输入上方地址')
print('  📌 按 Ctrl+C 关闭服务器')
print('=' * 50)

# Auto open browser
webbrowser.open(f'http://localhost:{PORT}/{FILE}')

with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('\n服务器已关闭')
        sys.exit(0)
