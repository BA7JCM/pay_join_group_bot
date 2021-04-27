
QQ付费入群系统Nonebot2机器人插件
===============
## 使用：

1. 推荐将go-cqhttp协议更改为iPad，处理效率更高。
2. 放入Nonebot2机器人插件目录
3. 安装依赖
```shell
pip install pymysql
//可能需要将pip更改为pip3
```
4. 修改插件内的机器人数据库连接信息
```python
def liansql():
    # 链接MYSQL获得db
    db = pymysql.connect(host="127.0.0.1", port=3306, user="fk", password="password", database="fk", )
    return db
```
------

## 注意：

  + QQ付费入群系统是免费开源产品，所有程序均开放源代码，所以不会有收费计划，因此作者不可能教会每个人部署安装，请参考文档多百度谷歌，使用具有一定的技术门槛，请见谅！

## 版权信息

QQ付费入群系统遵循 MIT License 开源协议发布，并提供免费使用，请勿用于非法用途。