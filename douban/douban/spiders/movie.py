from scrapy_redis.spiders import RedisSpider  # 必须继承RedisSpider

class MovieSpider(RedisSpider):
    name = 'movie'
    redis_key = 'douban:start_urls'  # 必须与settings中的REDIS_START_URLS_KEY一致
    
    def parse(self, response):
        # 提取电影信息
        for movie in response.css('.item'):
            yield {
                'title': movie.css('.title::text').get().strip(),
                'rating': movie.css('.rating_num::text').get(),
                'quote': movie.css('.inq::text').get(default='').strip()
            }
        
        # 翻页逻辑（如果豆瓣允许）
        next_page = response.css('.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)