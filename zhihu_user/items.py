# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class UserItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = Field()
    name = Field()
    articles_count = Field()
    answer_count = Field()
    follower_count = Field()
    avatar_url = Field()
    avatar_url_template = Field()
    badge = Field()
    gender = Field()
    headline = Field()
    is_advertiser = Field()
    is_followed = Field()
    is_following = Field()
    is_org = Field()
    type = Field()
    url = Field()
    url_token = Field()
    user_type = Field()
