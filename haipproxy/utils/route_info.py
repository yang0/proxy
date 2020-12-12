from ..config.rules import CRAWLER_TASKS
from mscommon import get_ip_list
from IPy import IP
from loguru import logger

def gen_route_updater():
    """在根目录生成route_up.bat和route_down.bat两个刷路由的批处理文件
    刷了路由的ip地址（都是国内的）会绕开vpn
    """
    def mask(ip):
        print(ip)
        a = ip.split(".")
        # print(a)
        a[3] = '0'
        return '.'.join(a)

    def get_mask_ip(domain):
        print(domain)
        domain_ip_list = get_ip_list(domain)
        domain_ip_list = [ip for ip in domain_ip_list if IP(ip).version()==4]
        return list(map(mask, domain_ip_list))


    ip_list = get_mask_ip("www.zhihu.com")
    ip_list += get_mask_ip("httpbin.org")
    ip_list += get_mask_ip("weibo.cn")
    for task in CRAWLER_TASKS:
        if not "gfw" in task or not task["gfw"]:
            ip_list = ip_list + get_mask_ip(task["name"])

    ip_list = list(set(ip_list))

    def add_route(ip):
        return f"route add {ip} mask 255.255.255.0 192.168.0.1 metric 5 \n"
    
    with open('route_up.bat', 'w') as f:
        logger.debug(f"up: len(ip_list): {len(ip_list)}")
        up_lines = ["ipconfig /flushdns\n"] + list(map(add_route, ip_list))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        f.writelines(up_lines)

    def clear_route(ip):
        return f"route delete {ip}\n"

    with open('route_down.bat', 'w') as f:
        logger.debug(f"down: len(ip_list): {len(ip_list)}")
        down_lines = list(map(clear_route, ip_list))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        f.writelines(down_lines)

    