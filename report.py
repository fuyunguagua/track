import requests
from config import report_center_host, report_center_port

def report(watermark, cur_ip, src_ip, dst_ip, timestamp):
    url = report_center_host + \
          report_center_port + \
          request_url_maker({'watermark':watermark, 'cur_ip':cur_ip, 'src_ip':src_ip, 'dst_ip':dst_ip, 'timestamp':timestamp})
    response = requests.request('get', url)
    return response

def request_url_maker(parameters_dict):
    a = ["{}={}".format(key, value) for key, value in parameters_dict.items()]
    return '?' + '&'.join(a)