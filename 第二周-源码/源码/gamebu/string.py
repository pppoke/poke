# Author:game_bu

game_bu = "   \tg\ta建gg波%s{_name}me bgg%d{_age}uDDD"
game_bu1 = b'222ga\xe5\xbb\xba\xe6\xb3\xa2me bu'


print(game_bu.zfill(50))  # 补位
print(game_bu.swapcase())  # 字符串大小写转换
print(game_bu.strip())  # 去除两段的空字符
print(game_bu.lstrip())  # 去除两段的空字符
print(game_bu.rstrip())  # 去除两段的空字符
print(game_bu.split('me'))  # 以给出的关键字切割字符串
print(game_bu.splitlines())  # 以行切割
print(game_bu.replace('gg', '00'))  # 替换字符
joinstr = "123"
joinstr1 = '+-'
print(joinstr1.join(joinstr))  # 将joinstr1插入到joinstr中
print(game_bu.ljust(50, '*'))  # 左靠齐，右侧补充*
print(game_bu.rjust(50, '*'))  # 右靠齐，左侧补充*

transtr = str.maketrans('abcdefg', '1234567')  # 创建替换规则
print(game_bu.translate(transtr))  # 将替换规则应用到字符串中



# is类的函数，多用于判断，用处广
game_bu2 = "Ada123 s43"
print(game_bu2.isdigit())  # 是否整数
print(game_bu2.isdecimal())
print(game_bu2.isnumeric())
print(game_bu2.isalnum())  # 是否包含特殊字符
print(game_bu2.isalpha())  # 是否包含特殊字符或数字
print(game_bu2.isidentifier())  # 是否能作为变量名
print(game_bu2.islower())  # 判断是否不包含大写字母
print(game_bu2.isupper())  # 判断是否不包含小写字母
print(game_bu2.isprintable())  # 是否可打印
print(game_bu2.isspace())  # 是否只包含空格之类的字符
print(game_bu2.istitle())  # 字符串中每个单词首字母是否大些



# 常规打印方法
print(game_bu.format(_name="大圣", _age=9999))
print(game_bu.format_map({"_name": "美猴王", "_age": 18000}))
print(game_bu % ("孙猴子", 23333))

# 查找字符串中出现制定参数的位置下标并返回
print(game_bu.find('gg'))
print(game_bu.rfind('gg'))
print(game_bu.index('a'))
print(game_bu.rindex('a'))

# 将字符串中的转义符'\t'替换为指定个空字符
print(game_bu.expandtabs(20))

# 将字符串转换为二进制编码，将二进制编码转换为UTF-8编码
print(game_bu.encode())
print(game_bu1.decode())

# 判断字符串是否以指定的参数结尾，返回布尔型
print(game_bu.endswith('e bu'))
print(game_bu1.endswith(b'\xa2me bu'))

# 输出第一个字符大写
print(game_bu.capitalize())

# 输出40个字符，如果game_bu长度不组40，则将game_bu居中打印，两边补充'-'
# 如果指定的长度比game_bu长度短，则忽略这个方法，直接打印game_bu
print(game_bu.center(100, '-'))

# 统计指定字符或字符串出现的次数
print(game_bu.count('222'))
