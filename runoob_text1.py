#match...case...练习
age = int(input("欢迎登录相亲系统，请填写您的年龄，我将为您匹配年龄适合的候选人:"))
def xq(age):
    match age:
        case 18|19|20|21|22|23|24|25:
            return "年轻好啊"
        case 26|27|28|29|30|31|32|33|34|35|36|37:
            return "老大不小了，抓紧点吧"
        case 38|39|40:
            return "快别挑了，找个人搭伙过吧"
        case _:
            return "大人的事，小孩别掺和" #暂时忽略大龄青年

print(xq(age))
