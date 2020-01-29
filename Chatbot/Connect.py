#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:03:27 2020

@author: cai
"""

#连接微信并阻塞进程


from wxpy import *
from respond import Respond


bot = Bot()
my_friend = bot.friends().search(u'TT')[0]

'''@bot.register()
def just_print(msg):
    # 打印消息
    print(msg)'''

(lastintent, lastartist) = (None, None)

@bot.register([my_friend, Group], TEXT)
def auto_reply(msg):
    # 如果是群聊，但没有被 @，则不回复
    global lastintent,lastartist
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        # 回复消息内容和类型
        (reply, lastintent, lastartist)  =  Respond(msg.text,lastintent, lastartist)
        return '{}'.format(reply)

embed()
