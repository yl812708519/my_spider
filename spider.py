#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import time
import urllib
from lxml import etree



class Spider():

    _patent_url = 'http://epub.sipo.gov.cn/patentoutline.action'
    _trademark_url = "http://www.chatm.com/search.aspx?keyword=%25%25&gjflCn={1}"

    def get_html(self, url, data=None):
        request = urllib2.Request(url, data=data)
        html = urllib2.urlopen(request).read()
        return html


    def get_patent(self, param):
        if param is None:
            return 'error'
        data = urllib.urlencode(param)
        html = self.get_html(self._patent_url, data)
        tree = etree.HTML(html)
        response={
            'titles': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/h1').text,  #标题
            'publication_number': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]'), #公布号
            'date_declare': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]'), #公布日期
            'application_number': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]'), #申请号
            'filling_date': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]'), #申请日
            'applicant': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]'), #申请人
            'inventor': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]'), #发明人
            'classification_codes': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/ul/li[1]'), #分类号
            'description': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/div'),  #摘要
            'description2': tree.xpath('/html/body/div[3]/div[2]/div/div[2]/div/span[2]')  #摘要(被隐藏的部分)
        }
        return response

    def get_pdf(self):
        param = {
             'recordCursor':0,
             'strLicenseCode': '',
             'strSources': 'fmmost',
             'strWhere': 'pnm=CN103160004A'
        }
        data = urllib.urlencode(param)
        html = self.get_html('http://epub.sipo.gov.cn/dxb.action', data)
        print html



keyword = '%25%25'
category = 1
data = {#专利抓取的数据，分页
            'numFMGB': 2687870,
            'numFMSQ': 1521675,
            'numSYXX': 4013083,
            'numSortMethod': 4,
            'numWGSQ': 3036167,
            'pageNow': 0,
            'pageSize': 10,
            'showType': 1,
            'selectd': 'fmgb',
            'strLicenseCode': '2164279567.1418715188.1',
            'strWord': "公开（公告）号='CN%'"
        }



spider = Spider()
# print spider.get_patent(data).title
spider.get_pdf()

# tree = etree.HTML(html)
# print
