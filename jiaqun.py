from nonebot.plugin import on_request
from nonebot.adapters import Event, Bot
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters.cqhttp import Bot, Message
import nonebot, asyncio, pymysql

cljq = on_request(priority=1, block=True)


@cljq.handle()
async def cljq(bot: Bot, event: Event, state: T_State):
    post_type = event.post_type  # 获取请求-------------上报类型
    flag = event.flag
    if post_type == 'request':
        request_type = event.request_type  # 请求类型
        if request_type == 'group':  # 处理加群请求
            sub_type = event.sub_type  # 子类型(主动或者邀请)

        if sub_type == 'add':  # 主动主动申请
            userid = event.user_id  # 申请入群的QQ号
            groupid = event.group_id  # 群号
            comment = event.comment  # 验证信息
            state = sqlyz(userid)
            if state:
                print('已同意');
                await bot.set_group_add_request(approve=True, flag=flag, sub_type=sub_type)
            else:
                print('已拒绝');
                await bot.set_group_add_request(approve=False, flag=flag, sub_type=sub_type,
                                                reason='前往xxx.xxx.com付费后重新申请，请勿多次尝试，否则被风控无法加群')


def liansql():
    # 链接MYSQL获得db
    db = pymysql.connect(host="127.0.0.1", port=3306, user="fk", password="password", database="fk", )
    return db


def sqlyz(userid):
    try:
        db = liansql()  # 链接mysql
    except:
        print('-------------------------数据库链接失败------------------------')
    zz = db.cursor()
    sql = '''SELECT * FROM `orders` WHERE `shopid` = 1 AND `qq` = '%s' AND `state` = 1''' % (str(userid))
    zz.execute(sql)
    jilu = zz.fetchall()
    jilus = zz.rowcount
    print('jilu:', jilu)
    print('jilus:', jilus)
    if jilus > 0:
        print('if-true')
        for i in jilu:
            print('for:', i)
            dbid = i[0]
            gengsql = '''UPDATE `orders` SET `state` = 2 WHERE `orders`.`id` = %s;''' % (dbid)
            zz.execute(gengsql)
            print('已更新为2')
            print(dbid, '-------------找到记录id-------------')
        db.close()
        return True
    else:
        print('if-false')
        print('没有记录')
        db.close()
        return False
