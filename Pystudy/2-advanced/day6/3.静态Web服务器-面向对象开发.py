# 1. 以面向对象的方式开发静态web服务器

# 1. 把提供服务的web服务器抽象成一个类(HTTPWebSever)
# 2. 提供Web服务器的初始化方法，再初识化方法里面创建socket对象
# 3.提供一个开启Web服务器的方法，让Web服务器吹客户端请求操作。

#  demo

import socket
import threading

# 定义web服务器类

class HttpWebServer(object):



        def __init__(self):

            # 创建tcp服务端套接字
            tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

            # 设置端口号复用, 程序退出端口立即释放
            tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)

            # 绑定端口号
            tcp_server_socket.bind(("",9090))

            # 设置监听
            tcp_server_socket.listen(128)

            print("first step")

            # 保存创建成功的服务器套接字

            self.tcp_server_socket = tcp_server_socket


    # 处理客户端的请求
        @staticmethod
        def handle_client_request(new_socket):

            # 代码执行到此，说明连接建立成功
            recv_client_data = new_socket.recv(1024)

            print("third step")

            if len(recv_client_data) ==0:
                print("关闭浏览器了")
                new_socket.close()
                return

            # 对二进制数据进行解码
            recv_client_content = recv_client_data.decode("utf-8")

            # 根据指定字符串进行分割， 最大分割次数指定2
            requst_list = recv_client_content.split(" ",maxsplit=2)

            # 获取请求资源路径
            requst_path = requst_list[1]

            # 判断请求的是否是根目录，如果条件成立，指定首页数据返回

            if requst_path =="/":
                requst_path = "/index.html"

            # 动态打开指定文件
            try:
                with open("static"+requst_path,"rb") as file:

                # 读取文件数据
                    file_data = file.read()

            except Exception as e:

                # 请求资源不存在，返回404数据
                with open("static/error.html", "rb") as file:

                    file_data = file.read()

                # 响应行
                reponse_line = "HTTP/1.1 404 NOT FOUND\r\n"

                # 响应头

                response_header = "Server NBS1.0\r\n"
                # 响应体
                response_body = file_data

                # 拼接响应报文
                send_data = (reponse_line+response_header+"\r\n").encode("utf-8")+response_body

                # 发送数据
                new_socket.send(send_data)
            else:

                # 响应行
                reponse_line = "HTTP/1.1 200 OK\r\n"

                # 响应头
                response_header = "Server:NBS1.0\r\n"

                # 响应体
                response_body = file_data

                # 拼接响应报文
                send_data = (reponse_line + response_header+"\r\n").encode("utf-8") + response_body
                # 发送数据
                new_socket.send(send_data)
            finally:
                new_socket.close()

                # 关闭服务与客户端的套接字

        # 启动web服务器进行工作
        def start(self):

            while True:
                # 等待接受客户端的连接请求
                new_socket,ip_port = self.tcp_server_socket.accept()

                print("second step")

                # 当客户端和服务器建立连接程，创建子线程
                sub_thread = threading.Thread(target=self.handle_client_request,args=(new_socket,))

                # 设置守护主线程
                sub_thread.setDaemon(True)

                # 启动子线程执行对应的任务
                sub_thread.start()


# 程序入口函数
if __name__ == '__main__':

        # 创建web服务器对象
        new_web_server = HttpWebServer()

        # 启动web服务器进行工作
        new_web_server.start()


