# coding:utf8
# 不能用

import os


def nginx_install():
    # 先简单点，从直接从上传nginx压缩包和部署用的py脚本之后，开始模拟手动操作。
    # 前期对nginx配置文件的更改，在本地完成
    cmd = 'yum -y install gcc gcc-c++ ' \
          'python-devel ' \
          'prce pcre-devel ' \
          'zlib zlib-devel'
    os.system(cmd)
    cmd = 'tar -zxvf nginx.tar.gz'
    os.system(cmd)
    if os.path.exists('nginx-1.10.2'):
        os.system('useradd nginx -s /sbin/nologin')
        os.system('cd nginx-1.10.2')
        cmd = r'./configure --prefix=/usr/local/nginx1.10.2 ' \
              '--with-http_dav_module ' \
              '--with-http_stub_status_module ' \
              '--with-http_addition_module ' \
              '--with-http_sub_module ' \
              '--with-http_flv_module ' \
              '--with-http_mp4_module ' \
              '--with-pcre=../pcre-8.39 ' \
              '--with-zlib=../zlib-1.2.8 ' \
              '--with-openssl=../openssl-1.1.0c ' \
              '--with-http_ssl_module ' \
              '--with-http_gzip_static_module ' \
              '--user=nginx ' \
              '--group=nginx'
        os.system('chmod +x configure')
        os.system(cmd)
        os.system('make $$ make install')
        cmd = 'ln -s /usr/local/nginx1.10.2/sbin/nginx /usr/local/bin/nginx'
        os.system(cmd)
        os.system('cd ../')
        os.system('rm -rf nginx-1.10.2 nginx.tar.gz Desktop.zip pcre* zlib* openssl*')


def nginx_start():
    os.system('chown -R nginx:nginx /usr/local/html')
    os.system('nginx')


def nginx_stop():
    os.system('nginx -s stop')


def nginx_restart():
    os.system('nginx -s reload')


if __name__ == '__main__':
    nginx_install()
    nginx_start()
