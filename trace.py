# from scapy.all import *
# from scapy.layers import http
import time
from report import report
from ip_get import get_host_ip

index = 0

def pkt_callback(p):
    try:
        # if 'a=' in  p['Raw'].__repr__() and "b=" in p['Raw'].__repr__() and "c=" in p['Raw'].__repr__():
        if 'wangyang' in p['Raw'].__repr__():
            print p['IP'].src,'---->',p['IP'].dst
            timestamp = '%f10' % time.time()
            watermark = ''
            ip_src = str(p['IP'].src)
            ip_dst = str(p['IP'].dst)
            report(watermark='', cur_ip=get_host_ip(), src_ip='', dst_ip='', timestamp=timestamp)
    except Exception as e:
        pass
    # pkt.show()
    # pkt.show() # debug statement
#
# sniff( prn=pkt_callback, filter="tcp", store=0)
#!/usr/bin/env python
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

scapy.sniff(prn=pkt_callback, lfilter= lambda x: x.haslayer(scapy_http.http.HTTP))
#     def nsummary(self,prn=None, lfilter=None):
#         """prints a summary of each packet with the packet's number
# prn:     function to apply to each packet instead of lambda x:x.summary()
# lfilter: truth function to apply to each packet to decide whether it will be displayed"""
#         for i in range(len(self.res)):
#             if lfilter is not None:
#                 if not lfilter(self.res[i]):
#                     continue
#             print conf.color_theme.id(i,fmt="%04i"),
#             if prn is None:
#                 print self._elt2sum(self.res[i])
# <Raw  load='a=%59%6D%6C%76%64%6E%4E%35%5A%6E%42%6A%65%6D%31%71%64%32%64%30%5A%48%46%75%61%33%68%6F%64%57%46%6C%63%6D%77%36%63%6E%6C%6C%62%48%56%69%64%6D%6C%6D%63%32%39%77%59%57%68%72%63%58%68%75%62%58%70%71%64%32%4E%30%5A%32%51%3D&b=vHR5fGU6foVaZWF0vHViZDidM2Q1MsUbZoRmNsA5MTEzZTfbOTIbZoU4MDZdNoY2ZTY5NpN8foFkOpY0vGJgX2kirGzdZDeavGJgX2ZirGVsOpB8Yokvc2V5fseavGJ1f3m6ZoFuf2V8&c=%65%6C%72%75%62%69%6F%76%62%69%6C%72%76%62%69%6F%76%62%69%6F%76%79%66%6C' |>

# watermark = 'a='
# packets = scapy.rdpcap('/home/wy/Desktop/athena.pcap')
# for p in packets:
#