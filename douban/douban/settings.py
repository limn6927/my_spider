BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

# ============ 核心配置 ============ 
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True  # 防止爬虫自动关闭

# Redis连接配置（如果是Docker，确保端口6379已映射）
REDIS_URL = 'redis://localhost:6379/0'

# 强制指定所有Redis键名前缀
REDIS_START_URLS_KEY = 'douban:start_urls'
REDIS_ITEMS_KEY = 'douban:items'
REDIS_DUPEFILTER_KEY = 'douban:dupefilter'

# 数据存储管道
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300
}

# 反爬策略
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
DOWNLOAD_DELAY = 2  # 重要！添加2秒延迟
ROBOTSTXT_OBEY = False

FEED_EXPORT_ENCODING = 'utf-8'  # 强制使用UTF-8编码