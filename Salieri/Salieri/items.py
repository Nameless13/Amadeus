# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SalieriItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    METLIN_ID = scrapy.Field()
    Mass = scrapy.Field()
    Name = scrapy.Field()
    Synonym = scrapy.Field()
    Systematic_Name = scrapy.Field()
    Formula = scrapy.Field()
    CAS = scrapy.Field()
    Purchase_Option = scrapy.Field()
    LMID = scrapy.Field()
    KEGG = scrapy.Field()
    HMDB = scrapy.Field()
    PubChem = scrapy.Field()
    Notes = scrapy.Field()
    Drug = scrapy.Field()
    Structure = scrapy.Field()
    Spectrum = scrapy.Field()