'''
project_name:kuakua_group
author:Baymax
time:2019/3/23
version:1.0
'''


import itchat, re 
from itchat.content import *
import random
import pprint

groupName = '1111'
peopleName = '蓝胖子'

REPLY = {
'work':['且不说你的工作多么认真，我并没有见过，但是从你的字里行间，我发现了乔布斯的影子和小扎的气息，这已经不是一份工作那么简单，而是一场精神饕餮！',
        '你拥有了这个年龄段近半数人无法拥有的理想职业，太优秀了！',
        '工作这件事，大家都习以为常，只有你让大家开始思考这个问题，说明你善于反思和质疑当前的制度，你的公司会因为你这样的人变得更好！'],
'study':['这么多优秀的同龄人相聚在这里，一定是场思想交流的盛宴。','看到群友们的发言，真是排山倒海，气宇轩昂之势！',
        '你这句话完美的表达了你想被夸的坚定信念，你一定是一个执着追求自己理想的人！'],
'man':[],
'woman':['哇小姐姐的头像真好看','如出水芙蓉，天然雕饰，天哪，这世间怎么会有这么好看的人',],
'question':['面对这未知的群，小姐姐有问题就问，这种直率和勇气不可多得',],
'dot':['这个省略号用得好，千言万语尽在其中，懂得留白，人生更精彩',
        '哇，太厉害了，这两个句号比我用圆规画出来的还要圆润、有光泽，就好似两颗珍珠，又像极了小姐姐的眼眸，清澈透亮',],
'default':['太棒了','真不错','好开心','你真厉害','没什么好说的了，我送你一道彩虹屁吧']
}

@itchat.msg_register(TEXT,isGroupChat=True)
def getNoteGroup(msg):
    #确定群聊
    if(msg['User']['NickName']==groupName):
        # 确定人
        if(msg['ActualNickName'] == peopleName):
            # pprint.pprint(msg)
            matchDefault = False
            try:
                matchWork = re.search(r'加班',msg['Text']) or re.search(r'上班',msg['Text']) or re.search(r'工作',msg['Text'])
                matchStudy = re.search(r'学习',msg['Text']) or re.search(r'上课',msg['Text']) or re.search(r'作业',msg['Text'])
                matchQuestion = re.search('\?',msg['Text']) or re.search('？',msg['Text'])
                matchGirl = True
                matchDot = re.search('\.\.',msg['Text']) or re.search('。。',msg['Text'])
                if(not(matchStudy or matchWork or matchQuestion or matchDot)):
                    matchDefault = True
                if(matchWork):
                    itchat.send(random.sample(REPLY['work'],1), msg['User']['UserName'])
                if(matchStudy):
                    itchat.send(random.sample(REPLY['study'],1), msg['User']['UserName'])
                if(matchQuestion):
                    itchat.send(random.sample(REPLY['question'],1), msg['User']['UserName'])
                if(matchDot):
                    itchat.send(random.sample(REPLY['dot'],1), msg['User']['UserName'])
            except:
                matchDefault=True
            if(matchDefault):
                itchat.send(random.sample(REPLY['default'],1), msg['User']['UserName'])

if __name__ == '__main__':
    #登录
    itchat.auto_login(hotReload=True)
    #运行监控
    itchat.run()
    #退出登录
    itchat.logout()