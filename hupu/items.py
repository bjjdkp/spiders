# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from py2neo.ogm import GraphObject, Property, RelatedTo


class UserItem(scrapy.Item):

    puid = scrapy.Field()
    nickname = scrapy.Field()
    header_url = scrapy.Field()
    level = scrapy.Field()
    register_date = scrapy.Field()
    gender = scrapy.Field()  # 0：未设置   1：男   2：女
    location = scrapy.Field()
    follow_count = scrapy.Field()  # 关注人数
    fans_count = scrapy.Field()  # 粉丝人数
    be_light_count = scrapy.Field()  # 被点亮数
    be_recommend_count = scrapy.Field()  # 被推荐数
    bbs_msg_count = scrapy.Field()  # 发帖数
    bbs_post_count = scrapy.Field()  # 回帖数
    bbs_recommend_count = scrapy.Field()  # 推荐数
    news_comment_count = scrapy.Field()  # 新闻评论数
    bbs_msg_url = scrapy.Field()
    bbs_post_url = scrapy.Field()
    bbs_recommend_url = scrapy.Field()
    news_comment_url = scrapy.Field()
    bbs_follow_url = scrapy.Field()
    bbs_fans_url = scrapy.Field()
    bbs_job = scrapy.Field()
    reputation = scrapy.Field()
    update_time = scrapy.Field()


class TopicItem(scrapy.Item):
    tid = scrapy.Field()
    launch_time = scrapy.Field()
    title = scrapy.Field()
    user_name = scrapy.Field()
    update_time = scrapy.Field()


class User(GraphObject):
    __primarykey__ = 'puid'

    puid = Property()
    name = Property()
    follow = RelatedTo('User', 'follow')





