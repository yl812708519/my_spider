#!/usr/bom/emv python
# -*- coding: utf-8 -*-

#__author__ = 'yanglu'

import urllib2
import urllib
from lxml import etree
import codecs

class Spider(object):

    @staticmethod
    def gettree(request):
        html = urllib2.urlopen(request).read()
        tree = etree.HTML(html)
        return tree


class BookSpider(Spider):
    _doubanbook_url = 'http://book.douban.com'

    def __init__(self, min_point=8.8, tag='外国文学', save_file='doubanbook.txt'):
        self._min_point = min_point
        self._tag = tag
        self._save_file = codecs.open(save_file, 'w', 'utf-8')

    def get_request(self, url, data=None, headers={}):
        return urllib2.Request(url)

    def getneedurl(self):
        request = self.get_request(self._doubanbook_url+'/tag/'+self._tag)
        tree = self.gettree(request)
        url = tree.xpath('//*[@class="pic"]/a/@href')
        point = tree.xpath('//*[@class="rating_nums"]/text()')
        for x in range(0, len(url)):
            if float(point[x]) >= self._min_point:
                yield url[x]

    def save_content(self):
        for url in self.getneedurl():
            request = self.get_request(url)
            tree = self.gettree(request)
            title = tree.xpath('//*[@id="wrapper"]/h1/span/text()')
            point = tree.xpath('//*[@id="interest_sectl"]/div/p[1]/strong/text()')
            # author = tree.xpath('//*[@id="wrapper"]/h1/span/text()')
            intro = tree.xpath('//*[@class="intro"]/p/text()')
            # if len(intro) == 2:
            #     summary = intro[1].text
            print intro[-1]
            txt = title[0]+'\t\t\t\t\t\t\t\t\t\t'+point[0] + '\n' + url+'\n'+intro[-1]+'\n\n\n'
            self._save_file.write(txt)

test = BookSpider(7.0, '外国文学')

print test.save_content()