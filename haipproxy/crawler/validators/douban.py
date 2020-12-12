from haipproxy.config.settings import (
    TEMP_DOUBAN_QUEUE, VALIDATED_DOUBAN_QUEUE,
    TTL_DOUBAN_QUEUE, SPEED_DOUBAN_QUEUE, INIT_HTTP_QUEUE)
from ..redis_spiders import ValidatorRedisSpider
from .base import BaseValidator


class DoubanValidator(BaseValidator, ValidatorRedisSpider):
    """This validator checks the liveness of DOUBAN proxy resources"""
    name = 'douban'
    use_set = False
    urls = [
        'https://new.abb.com/cn'
    ]
    task_queue = TEMP_DOUBAN_QUEUE #INIT_HTTP_QUEUE
    score_queue = VALIDATED_DOUBAN_QUEUE
    ttl_queue = TTL_DOUBAN_QUEUE
    speed_queue = SPEED_DOUBAN_QUEUE
    success_key = '新闻稿'
