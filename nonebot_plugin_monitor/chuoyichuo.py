# encoding: utf-8
# @Time : 2022/1/19 12:05
# @Author : Torres-圣君
# @File : chuoyichuo.py
# @Sofaware : PyCharm
import random

bot_name = "雷雨"

chuo_msg = [
    f"别戳了，{bot_name}怕疼QwQ",
    f"呜呜，再戳{bot_name}脸都要肿了",
    f"戳坏了{bot_name}，你赔得起吗？",
    f"再戳{bot_name}，我要叫我主人了",
    f"别老戳{bot_name}了，您歇会吧~",
    f"再戳{bot_name}，咬你了嗷~",
    f"想好了再戳，(*-`ω´-)✄",
    f"喂，110吗，有人老戳我",
    f"嗷呜嗷呜...恶龙咆哮┗|｀O′|┛",
    f"有事恁叫我，别天天一个劲戳戳戳！",
    f"再戳我让你变成女人，嘿嘿",
    f"不要戳我了 >_<",
    f"不要这样子啦(*/ω＼*)",
    f"不要再戳了(害怕ing)",
    f"还戳，哼(つд⊂)（生气）",
    f"再戳，小心我顺着网线找你.",
    f"咱要型气了o(>﹏<)o",
    f"嘿嘿，好舒服呀(bushi)",
    f"乖，好了好了，别戳了~",
    f"我爪巴爪巴，球球别再戳了",
    f"别再戳我了，行🐎？！",
    f"啊呜，你有什么事吗？"
]


def chuo_send_msg():
    rand_num = random.randint(0, len(chuo_msg) - 1)
    return chuo_msg[rand_num]
