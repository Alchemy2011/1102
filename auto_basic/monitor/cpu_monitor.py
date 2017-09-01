#!/usr/bin/python2
# coding: utf-8
import psutil
import time
import datetime
from mail1 import send_mail

last_alert_stamp = time.time()
cpu_percent = [] # cpu利用率

def get_cpu_percent():
    """获取cpu利用率，并且加入列表"""
    cpu_per=psutil.cpu_percent()
    cpu_percent.append(cpu_per)
    if len(cpu_percent) > 12:
        cpu_percent.pop(0)  # 删除列表中第一元素

def cpu_alert():
    """达到设定条件，触发报警机"""
    res = sum(cpu_percent)  # 求总和
    avg = res / len(cpu_percent)
    now_stamp = time.time() # 获取现在系统时间戳
    if now_stamp > last_alert_stamp + 20:
        if avg >= 20:
            if avg >= 90:
                print '橙色警报'
            elif avg >=50:
                print '红色警报'
    
if __name__ == "__main__":
    while True:
        get_cpu_percent()
        time.sleep(2)
        cpu_alert()
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print now,cpu_percent
        # send_mail(['liqirong1701python@163.com',], "警报", "你好红")



