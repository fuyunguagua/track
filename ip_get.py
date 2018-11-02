import socket
import requests
import re
from config import self_ip
import time
def get_host_ip():
    if self_ip:
        return self_ip
    response = requests.request("get", "http://ip.cn")
    ip_pattern = '((?:(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d)))\.){3}(?:25[0-5]|2[0-4]\d|((1\d{2})|([1-9]?\d))))'
    result = re.findall(ip_pattern, response.content)
    return result[0][0]


print timest