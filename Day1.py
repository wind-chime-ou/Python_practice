#结合input,if,字典做一个成语的字典程序
chengyu_dict = {"画蛇添足":"比喻做多余的事反而不必要，适得其反。",
                "一石二鸟":"比喻一次行动达到两个目的。",
                "三心二意":"形容意志不坚定，犹豫不决。",
                "心旷神怡":"形容心情舒畅，精神愉悦。",
                "杯弓蛇影":"比喻因疑虑而产生恐惧。"}
chengyu_dict["水滴石穿"] = "比喻只要有恒心，细小的力量也能产生巨大的效果。"
chengyu_dict["自相矛盾"] = "容自我发生冲突，前后不一致。"
chengyu_dict["求同存异"] = "在寻求共同点的同时，保留各自的不同观点。"
chengyu_dict["狼狈为奸"] = "形容坏人勾结在一起干坏事。"
chengyu_dict["如鱼得水"] = "比喻得到所需的环境或条件，生活得非常舒适。"

chengyu = input("请输入您需要查询的成语：")

if chengyu in chengyu_dict:
    print("您查询的"+chengyu+"含义如下：")
    print(chengyu_dict[chengyu])
else:
    print("该词典尚未收录您所查询的成语")
    print("该词典共收录了"+str(len(chengyu_dict))+"个成语")


#体温异常检测
temperature_dict = {"李华":"36.5","张三":"37","李四":"38","王五":"39"}

for temperature_name,temperature in temperature_dict.items():
    if float(temperature)>=38:
        print(temperature_name+"的温度是"+str(temperature))
        print("完球了")

#计算1到100的和
total = 0
for i in range(1,101):
    total = total + i
print(total)

#计算搜输入的数的平均值
print("我是一个计算所输入数字的平均值的程序")
num = input("请输入一个数字（输入q时停止输入）:")
total = 0
count = 0
while num != "q":
    user_num = float(num)
    total +=user_num
    count +=1
    num = input("请输入一个数字（输入q时停止输入）:")
if count==0:
    result = 0
else:
    result = total/count
print("您输入的平均值为："+str(result))

