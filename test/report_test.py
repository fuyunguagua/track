from report import report_info

def test():
    watermark = 'w8815'
    cur_ip = '8.8.8.8'
    ip_src = '127.0.0.1'
    ip_dst = '127.0.0.1'
    timestamp = 11111
    report_info(watermark=watermark, cur_ip=cur_ip, src_ip=ip_src, dst_ip=ip_dst, timestamp=timestamp)

    cur_ip = '74.82.219.169'
    timestamp = 22222
    report_info(watermark=watermark, cur_ip=cur_ip, src_ip=ip_src, dst_ip=ip_dst, timestamp=timestamp)

    cur_ip = '115.115.115.115'
    timestamp = 33333
    report_info(watermark=watermark, cur_ip=cur_ip, src_ip=ip_src, dst_ip=ip_dst, timestamp=timestamp)

    cur_ip = '120.76.125.235'
    timestamp = 44444
    report_info(watermark=watermark, cur_ip=cur_ip, src_ip=ip_src, dst_ip=ip_dst, timestamp=timestamp)

    cur_ip = '104.224.145.16'
    timestamp = 55555
    report_info(watermark=watermark, cur_ip=cur_ip, src_ip=ip_src, dst_ip=ip_dst, timestamp=timestamp)

    cur_ip = '95.179.206.18'
    timestamp = 66666
    report_info(watermark=watermark, cur_ip=cur_ip, src_ip=ip_src, dst_ip=ip_dst, timestamp=timestamp)

if __name__ == '__main__':
    test()