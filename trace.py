import time
from report import report_info
from ip_get import get_host_ip
from config import flag
try:
    import scapy.all as scapy
except ImportError:
    import scapy

try:
    import scapy_http.http
except ImportError:
    # If you installed this package via pip, you just need to execute this
    from scapy.layers import http
# from scapy_ssl_tls.ssl_tls import *
index = True

def pkt_callback(p):
    try:
        global index
        if flag in p['Raw'].__repr__():
            watermark = parse_watermark_from_payload(p['Raw'])
            timestamp = '%f10' % time.time()
            ip_src = str(p['IP'].src)
            ip_dst = str(p['IP'].dst)
            cur_ip = get_host_ip()
            if(index):
                report_info(watermark=watermark, cur_ip=cur_ip, src_ip=ip_src, dst_ip=ip_dst, timestamp=timestamp)
                index = False
            else:
                index = True
            print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), watermark, p['IP'].src, '---->', p['IP'].dst
    except Exception as e:
        print e

def parse_watermark_from_payload(payload):
    watermark = ''
    for item in str(payload).split('&'):
        if item[0] is 'w':
            watermark = item[:6]
    return watermark

def run():
    scapy.sniff(prn=pkt_callback, lfilter=lambda x: x.haslayer(scapy_http.http.HTTP))

if __name__ == '__main__':
    run()