import os


def get_port():
    port = os.getenv("PORTS")
    return "127.0.0.1:{}".format(port)

# 并行工作进程数
workers = 4
# 指定每个工作者的线程数
threads = 4
# 监听内网端口80
bind = get_port()
# 设置最大并发量
worker_class = "gevent"
worker_connections = 200
timeout = 600
reload=True
