from scrapy import Selector

if __name__ == '__main__':
    body = '<html><head><title>Hello World</title></head><body></body></html>'
    selector = Selector(text=body)
    title = selector.xpath('//title/text()').extract_first()
    print(title)

