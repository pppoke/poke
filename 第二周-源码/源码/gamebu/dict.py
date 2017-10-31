# Author:Gamebu

info = {
    'stu1101': "TengLan Wu",
    'stu1102': "LongZe Luola",
    'stu1103': "XiaoZe Maliya",
}

print(info.get('stu1101', "不存在"))  # 获取指定key的值，如果不存在，则返回defualt值

print(info.pop('stu1105', 'fsfds'))  # 删除指定key的item，如果不存在这个key，则返回defualt值，否则返回item的value
# info.clear()
#print(info.popitem())  # 删除一个item，并将删除的item以tuple返回

info1 = {'师徒104': '西天取经', 'stu1103': '苍老师'}

info.update(info1)  # 将info1的key更新到info，key相同则更新value
print("%s" % info.values())

a = info.values()
print(type(a))