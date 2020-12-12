"""
Spider rules.Scheduler will provide crawling tasks according to the rules and
spiders will parse response content according to the rules.
"""
from ..config.settings import (
    SPIDER_COMMON_TASK, SPIDER_AJAX_TASK,
    SPIDER_GFW_TASK, SPIDER_AJAX_GFW_TASK,
    INIT_HTTP_QUEUE, VALIDATED_HTTP_QUEUE,
    VALIDATED_HTTPS_QUEUE, TEMP_HTTP_QUEUE,
    TEMP_HTTPS_QUEUE, TTL_HTTP_QUEUE,
    TTL_HTTPS_QUEUE, SPEED_HTTPS_QUEUE,
    SPEED_HTTP_QUEUE, TEMP_WEIBO_QUEUE,
    VALIDATED_WEIBO_QUEUE, TTL_WEIBO_QUEUE,
    SPEED_WEIBO_QUEUE, TEMP_ZHIHU_QUEUE, 
    VALIDATED_ZHIHU_QUEUE, TTL_ZHIHU_QUEUE,
    SPEED_ZHIHU_QUEUE,
    TTL_DOUBAN_QUEUE,VALIDATED_DOUBAN_QUEUE,SPEED_DOUBAN_QUEUE, TEMP_DOUBAN_QUEUE)


__all__ = ['CRAWLER_TASKS', 'VALIDATOR_TASKS', 'CRAWLER_TASK_MAPS',
           'TEMP_TASK_MAPS', 'SCORE_MAPS', 'TTL_MAPS',
           'SPEED_MAPS']


CRAWLER_TASKS = [
    {
        'name': 'xiladaili', # ok
        'resource': ['http://www.xiladaili.com/gaoni/%s/' % i for i in range(1, 200)],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': True,
            'protocols': None
        },
        'interval': 60 * 2,
        'enable': 1
    },

    {
        'name': 'www.kuaidaili.com', # ok
        'resource': ['https://www.kuaidaili.com/free/inha/%s' % i for i in range(1, 6)] +
                    ['https://www.kuaidaili.com/proxylist/%s' % i for i in range(1, 11)],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 4,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1
    },
    {
        'name': 'kxdaili.com', # ok
        'resource': [
            'http://www.kxdaili.com/dailiip/%s/%s.html#ip' % (i, j) for i in range(1, 3) for j in range(1, 11)
        ],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1
    },
    {
        'name': 'mrhinkydink.com', # ok
        'resource': ['http://www.mrhinkydink.com/proxies.htm'],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'css',
            'pre_extract': '.text',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 2 * 60,
        'enable': 1,
    },
    {
        'name': '66ip.cn', #ok
        'resource': ['http://www.66ip.cn/mo.php?sxb=&tqsl=1000&port=&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea='],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//body/p/text()',
            'infos_pos': 0,
            'infos_end': -4,
            'detail_rule': None,
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': True,
            'protocols': None
        },
        'interval': 2 * 60,
        'enable': 1
    },
    {
        'name': 'data5u.com', # ok
        'resource': [
            'http://www.data5u.com/'
        ],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//ul[contains(@class, "l2")]',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'span li::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 10,
        'enable': 1,
    },
    {
        'name': 'ip3366.net',  # ok
        'resource': ['http://www.ip3366.net/free/?stype=1&page=%s' % i for i in range(1, 3)] +
                    ['http://www.ip3366.net/free/?stype=3&page=%s' % i for i in range(1, 3)],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 30,
        'enable': 1
    },
    {
        'name': 'ab57.ru', #ok
        'resource': ['http://ab57.ru/downloads/proxyold.txt'],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'text',
        'parse_rule': {
            'pre_extract': None,
            'delimiter': '\r\n',
            'redundancy': None,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': 'proxylists.net', #ok
        'resource': ['http://www.proxylists.net/http_highanon.txt'],
        'parse_type': 'text',
        'task_queue': SPIDER_COMMON_TASK,
        'parse_rule': {
            'pre_extract': None,
            'delimiter': '\r\n',
            'redundancy': None,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': 'atomintersoft.com', # ok
        'resource': [
            'http://www.atomintersoft.com/high_anonymity_elite_proxy_list',
            'http://www.atomintersoft.com/anonymous_proxy_list',
        ],
        'task_queue': SPIDER_COMMON_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': True,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
    },
    {
        'name': 'proxydb.net', # ok
        'resource': ['http://proxydb.net'],
        'task_queue': SPIDER_AJAX_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'detail_rule': 'a::text',
            'split_detail': True,
        },
        'interval': 3 * 60,
        'enable': 1,
    },
    {
        'name': 'cool-proxy.net', # ok
        'resource': ['https://cool-proxy.net/'],
        'task_queue': SPIDER_AJAX_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tr',
            'infos_pos': 1,
            'infos_end': -1,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 30,
        'enable': 1,
    },
    {
        'name': 'www.goubanjia.com', # ok
        'resource': ['http://www.goubanjia.com/'],
        'task_queue': SPIDER_AJAX_TASK,
        'parse_type': 'goubanjia',
        'interval': 10,
        'enable': 1,
    },
    {
        'name': 'cn-proxy.com', # ok
        'resource': [
            'http://cn-proxy.com/',
            'http://cn-proxy.com/archives/218'
        ],
        'task_queue': SPIDER_GFW_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tbody//tr',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
        'gfw': True
    },
    {
        'name': 'sslproxies',
        'resource': [
            'https://www.sslproxies.org/',          
        ],
        'task_queue': SPIDER_GFW_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tbody//tr',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
        'gfw': True
    },
    {
        'name': 'free-proxy-list',
        'resource': [
            'https://free-proxy-list.net/anonymous-proxy.html', # 这个页面有ajax分页，待处理
            'https://free-proxy-list.net/uk-proxy.html',
            'https://free-proxy-list.net/',
            
        ],
        'task_queue': SPIDER_GFW_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tbody//tr',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
        'gfw': True
    },
    {
        'name': 'us-proxy',
        'resource': [
            'https://www.us-proxy.org/',
        ],
        'task_queue': SPIDER_GFW_TASK,
        'parse_type': 'common',
        'parse_rule': {
            'pre_extract_method': 'xpath',
            'pre_extract': '//tbody//tr',
            'infos_pos': 0,
            'infos_end': None,
            'detail_rule': 'td::text',
            'ip_pos': 0,
            'port_pos': 1,
            'extract_protocol': True,
            'split_detail': False,
            'protocols': None
        },
        'interval': 60,
        'enable': 1,
        'gfw': True
    },
    {
        'name': 'www.xroxy.com', # ok
        'resource': ['https://www.xroxy.com/proxylist.php?port=&type=&ssl=&country=&latency=&reliability=&sort=reliability&desc=true&pnum=%s#table' % i for i in range(20)],
        'task_queue': SPIDER_GFW_TASK,
        'parse_type': 'xroxy',
        'interval': 60,
        'enable': 1,
        'gfw': True
    },
    # {
    #     'name': 'www.cnproxy.com', # todo
    #     'resource': ['http://www.cnproxy.com/proxy%s.html' % i for i in range(1, 11)], #+
    #                 # ['http://www.cnproxy.com/proxyedu%s.html' % i for i in range(1, 3)],
    #     'task_queue':  SPIDER_AJAX_GFW_TASK,
    #     'parse_type': 'cnproxy',
    #     'interval': 60,
    #     'enable': 1,
    #     'gfw': True
    # },
    # {
    #     'name': 'proxy-list.org', # todo
    #     'resource': ['https://proxy-list.org/english/index.php?p=%s' % i for i in range(1, 11)],
    #     'task_queue': SPIDER_AJAX_GFW_TASK,
    #     'parse_type': 'common',
    #     'parse_rule': {
    #         'pre_extract_method': 'css',
    #         'pre_extract': '.table ul',
    #         'infos_pos': 1,
    #         'infos_end': None,
    #         'detail_rule': 'li::text',
    #         'ip_pos': 0,
    #         'port_pos': 1,
    #         'extract_protocol': True,
    #         'split_detail': True,
    #         'protocols': None
    #     },
    #     'interval': 60,
    #     'enable': 1,
    #     'gfw': True
    # },
    
]

# crawler will fetch tasks from the following queues
CRAWLER_TASK_MAPS = {
    'common': SPIDER_COMMON_TASK, #'haipproxy:spider:common'
    'ajax': SPIDER_AJAX_TASK,
    'gfw': SPIDER_GFW_TASK,
    'ajax_gfw': SPIDER_AJAX_GFW_TASK
}

# validator scheduler will fetch tasks from resource queue and store into task queue
VALIDATOR_TASKS = [
    {
        'name': 'http',
        'task_queue': TEMP_HTTP_QUEUE,
        'resource': VALIDATED_HTTP_QUEUE,
        'interval': 5,  # 20 minutes
        'enable': 1,
    },
    {
        'name': 'https',
        'task_queue': TEMP_HTTPS_QUEUE,
        'resource': VALIDATED_HTTPS_QUEUE,
        'interval': 5,
        'enable': 1,
    },
    {
        'name': 'weibo',
        'task_queue': TEMP_WEIBO_QUEUE,
        'resource': VALIDATED_WEIBO_QUEUE,
        'interval': 5,
        'enable': 1,
    },
    {
        'name': 'zhihu',
        'task_queue': TEMP_ZHIHU_QUEUE,
        'resource': VALIDATED_ZHIHU_QUEUE,
        'interval': 5,
        'enable': 1,
    },
]

# validators will fetch proxies from the following queues
TEMP_TASK_MAPS = {
    'init': INIT_HTTP_QUEUE,
    'http': TEMP_HTTP_QUEUE,
    'https': TEMP_HTTPS_QUEUE,
    'weibo': TEMP_WEIBO_QUEUE,
    'zhihu': TEMP_ZHIHU_QUEUE,
    'douban': TEMP_DOUBAN_QUEUE,
}

# target website that use http protocol
HTTP_TASKS = ['http']

# target website that use https protocol
HTTPS_TASKS = ['https', 'zhihu', 'weibo', 'douban']

# todo the three maps may be combined in one map
# validator scheduler and clients will fetch proxies from the following queues
SCORE_MAPS = {
    'http': VALIDATED_HTTP_QUEUE,
    'https': VALIDATED_HTTPS_QUEUE,
    'weibo': VALIDATED_WEIBO_QUEUE,
    'zhihu': VALIDATED_ZHIHU_QUEUE,
    'douban': VALIDATED_DOUBAN_QUEUE,
}

# validator scheduler and clients will fetch proxies from the following queues which are verified recently
TTL_MAPS = {
    'http': TTL_HTTP_QUEUE,
    'https': TTL_HTTPS_QUEUE,
    'weibo': TTL_WEIBO_QUEUE,
    'zhihu': TTL_ZHIHU_QUEUE,
    'douban': TTL_DOUBAN_QUEUE
}

SPEED_MAPS = {
    'http': SPEED_HTTP_QUEUE,
    'https': SPEED_HTTPS_QUEUE,
    'weibo': SPEED_WEIBO_QUEUE,
    'zhihu': SPEED_ZHIHU_QUEUE,
    'douban': SPEED_DOUBAN_QUEUE,
}

