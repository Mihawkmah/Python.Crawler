from scrapy.spiders import Spider
from mtime.items import MtimeItem

class Mtime(Spider):
    name = 'mtime'
    start_urls = [
        'http://www.mtime.com/top/movie/top100/',
        'http://www.mtime.com/top/movie/top100/index-2.html',
        'http://www.mtime.com/top/movie/top100/index-3.html',
        'http://www.mtime.com/top/movie/top100/index-4.html',
        'http://www.mtime.com/top/movie/top100/index-5.html',
        'http://www.mtime.com/top/movie/top100/index-6.html',
        'http://www.mtime.com/top/movie/top100/index-7.html',
        'http://www.mtime.com/top/movie/top100/index-8.html',
        'http://www.mtime.com/top/movie/top100/index-9.html',
        'http://www.mtime.com/top/movie/top100/index-10.html'
    ]

    def parse(self, response):
        item = MtimeItem()
        movies = response.css('ul#asyncRatingRegion li')
        for movie in movies:
            item['rank'] = movie.css('div.number em::text')[0].extract()
            item['name'] = movie.css('h2 a::text')[0].extract()
            item['direct'] = movie.css('p a::text')[0].extract()
            item['role'] = movie.css('p>a::text').extract()
            item['type'] = movie.css('span a::text').extract()
            item['describe'] = movie.css('p.mt3::text')[0].extract()
            item['point'] = movie.css('b.point span::text').extract()
            item['pointnum'] = movie.css('div.mov_point p::text')[0].extract()
            yield item
