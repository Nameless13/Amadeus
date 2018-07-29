# -*- coding: utf-8 -*-
import scrapy
from Salieri.items import SalieriItem

class SalieriSpiderSpider(scrapy.Spider):
    # 爬虫名，不能和项目名重复
    name = 'Salieri_spider'
    # 允许的域名
    allowed_domains = ['metlin.scripps.edu']
    # 入口URL，扔到调度器里面去
    start_urls = ['https://metlin.scripps.edu/metabo_info.php?molid=1']
    # start_urls = ['http://metlin.scripps.edu/']

    def parse(self, response):
        # print(response.text)
        get_list=response.xpath("//div[@class='wrapper']//tbody/tr")
        # for i_item in get_list:
        #     metlin_item = SalieriItem()
        #     metlin_item["METLIN_ID"] = i_item.xpath(".//th[contains(text(), 'METLIN ID')]/following::td[1]").extract_first()
        #     metlin_item["Mass"] = i_item.xpath(".//th[contains(text(), 'Mass')]/following::td[1]").extract_first()
        #     metlin_item["Name"] = i_item.xpath(".//th[contains(text(), 'Name')]/following::td[1]").extract_first()
        #     metlin_item["Synonym"] = i_item.xpath(".//th[contains(text(), 'Synonym')]/following::td[1]").extract_first()
        #     metlin_item["Systematic_Name"] = i_item.xpath(".//th[contains(text(), 'Systematic Name')]/following::td[1]").extract_first()
        #     metlin_item["Formula"] = i_item.xpath(".//th[contains(text(), 'Formula')]/following::td[1]").extract_first()
        #     metlin_item["CAS"] = i_item.xpath(".//th[contains(text(), 'CAS')]/following::td[1]").extract_first()
        #     metlin_item["Purchase_Option"] = i_item.xpath(".//th[contains(text(), 'Purchase Option')]/following::td[1]").extract_first()
        #     metlin_item["LMID"] = i_item.xpath(".//th[contains(text(), 'LMID')]/following::td[1]").extract_first()
        #     metlin_item["KEGG"] = i_item.xpath(".//th[contains(text(), 'KEGG')]/following::td[1]").extract_first()
        #     metlin_item["HMDB"] = i_item.xpath(".//th[contains(text(), 'HMDB')]/following::td[1]").extract_first()
        #     metlin_item["PubChem"] = i_item.xpath(".//th[contains(text(), 'PubChem')]/following::td[1]").extract_first()
        #     metlin_item["Notes"] = i_item.xpath(".//th[contains(text(), 'Notes')]/following::td[1]").extract_first()
        #     metlin_item["Drug"] = i_item.xpath(".//th[contains(text(), 'Drug')]/following::td[1]").extract_first()
        #     metlin_item["Structure"] = i_item.xpath(".//th[contains(text(), 'Structure')]/following::td[1]").extract_first()
        #     metlin_item["Spectrum"] = i_item.xpath(".//th[contains(text(), 'Spectrum')]/following::td[1]").extract_first()
        #     print(i_item)
        #     # 将数据yield到pipline
        #     yield metlin_item
        # # 解析下一页，取后一页的xpath
        metlin_item = SalieriItem()
        metlin_item["METLIN_ID"] = get_list.xpath(
            ".//th[contains(text(), 'METLIN ID')]/following::td[1]").extract_first()
        metlin_item["Mass"] = get_list.xpath(".//th[contains(text(), 'Mass')]/following::td[1]").extract_first()
        metlin_item["Name"] = get_list.xpath(".//th[contains(text(), 'Name')]/following::td[1]").extract_first()
        metlin_item["Synonym"] = get_list.xpath(".//th[contains(text(), 'Synonym')]/following::td[1]").extract_first()
        metlin_item["Systematic_Name"] = get_list.xpath(
            ".//th[contains(text(), 'Systematic Name')]/following::td[1]").extract_first()
        metlin_item["Formula"] = get_list.xpath(".//th[contains(text(), 'Formula')]/following::td[1]").extract_first()
        metlin_item["CAS"] = get_list.xpath(".//th[contains(text(), 'CAS')]/following::td[1]").extract_first()
        metlin_item["Purchase_Option"] = get_list.xpath(
            ".//th[contains(text(), 'Purchase Option')]/following::td[1]").extract_first()
        metlin_item["LMID"] = get_list.xpath(".//th[contains(text(), 'LMID')]/following::td[1]").extract_first()
        metlin_item["KEGG"] = get_list.xpath(".//th[contains(text(), 'KEGG')]/following::td[1]").extract_first()
        metlin_item["HMDB"] = get_list.xpath(".//th[contains(text(), 'HMDB')]/following::td[1]").extract_first()
        metlin_item["PubChem"] = get_list.xpath(".//th[contains(text(), 'PubChem')]/following::td[1]").extract_first()
        metlin_item["Notes"] = get_list.xpath(".//th[contains(text(), 'Notes')]/following::td[1]").extract_first()
        metlin_item["Drug"] = get_list.xpath(".//th[contains(text(), 'Drug')]/following::td[1]").extract_first()
        metlin_item["Structure"] = get_list.xpath(
            ".//th[contains(text(), 'Structure')]/following::td[1]").extract_first()
        metlin_item["Spectrum"] = get_list.xpath(".//th[contains(text(), 'Spectrum')]/following::td[1]").extract_first()
        print(get_list)
        # 将数据yield到pipline
        yield metlin_item
