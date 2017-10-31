# Author:Gamebu

product = {}
cart = []
user = {}

product_file = open('product_file.txt', 'r')
product_list = product_file.readlines()
product_file.close()
for i in product_list:
    product[i.strip().split(':')[0]] = [i.strip().split(':')[1], int(i.strip().split(':')[2]), int(i.strip().split(':')[3])]

user_file = open('user_file.txt', 'r')
user_list = user_file.readlines()
user_file.close()
for j in user_list:
    user_cart = j.strip().split('|')
    user_product = {}
    if user_cart[0] != 'admin':
        for k in range(1, len(user_cart)-1):
            if user_cart[k].split(':')[0] != 'passwd':
                user_product[user_cart[k].split(':')[0]] = int(user_cart[k].split(':')[1])
            else:
                user_product[user_cart[k].split(':')[0]] = user_cart[k].split(':')[1]
            user[user_cart[0]] = [user_product, int(user_cart[-1])]
    else:
        user[user_cart[0]] = [{'passwd': user_cart[1]}]

username = ''
password = ''
grant = 0
count = 0
while count < 5:
    print("欢迎光临".center(30, '*'))
    username = input("请输入用户名:")
    password = input("请输入密码:")
    if username in user.keys():
        if user[username][0]['passwd'] == password:
            if username == 'admin':
                print("登陆成功，管理员！")
                grant = 1
                break
            else:
                print("登陆成功，祝您购物愉快！")
                break
        elif count == 4:
            print("登陆错误5次，系统退出！")
            count += 1
        else:
            print("密码不正确，请重试！")
            count += 1
    else:
        user_balance = input("您是第一次光临，请输入工资：")
        if user_balance.isdigit():
            user[username] = [{'passwd': password}, int(user_balance)]
            break
        else:
            print("输入错误，系统退出！")
            count = 5
else:
    exit(1)
if grant == 0:
    while True:
        print("商品一览表".center(30, '*'))
        print("%-6s %-20s %-6s" % ('编号', '名称', '单价'))
        for p in product:
            print("%-6s %-20s   %-6d" % (p+'.', product[p][0], product[p][1]))
        user_choice = input("请选购>>>:")
        if user_choice in product.keys():
            if user[username][1] < product[user_choice][1]:
                print("您的余额为“{_balance}”钱不够，请充值后再来！".format(_balance=user[username][1]))
                continue
            else:
                user[username][1] -= product[user_choice][1]
                cart.append([product[user_choice][0], product[user_choice][1]])
                if product[user_choice][0] not in user[username][0].keys():
                    user[username][0][product[user_choice][0]] = 1
                else:
                    user[username][0][product[user_choice][0]] += 1
                product[user_choice][2] -= 1
                print("已将“{_name}”放入购物车，您的余额为“{_balance}”".format(_name= product[user_choice][0], _balance=user[username][1]))
                continue
        elif user_choice == 'q':
            print("您的购物清单".center(30, '*'))
            z = 1
            for y in cart:
                print("%d. %s %d" % (z, y[0], y[1]))
                z += 1
            print("您的余额为：%d，再会" % user[username][1])
            break
        else:
            print("非法输入，请重新输入！")
else:
    while True:
        print("商品一览表".center(30, '*'))
        print("%-6s %-20s %-6s %-6s" % ('编号', '名称', '单价', '数量'))
        for p in product:
            print("%-6s %-20s   %-6d    %-6d" % (p+'.', product[p][0], product[p][1], product[p][2]))
        print("请选择要做的操作".center(30, '*'))
        print("1. 上货\n2. 下架\n3. 修改库存量")
        admin_choice = input("请选择>>>:")
        if admin_choice == '1':
            product_name = input("请输入新商品名称：")
            product_price = input("请输入新商品单价：")
            product_num = input("请输入新商品数量：")
            if product_price.isdigit() and product_num.isdigit():
                product[str(len(product)+1)] = [product_name, int(product_price), int(product_num)]
                print("新商品收入！")
            else:
                print("商品价格或数量输入错误！")
        elif admin_choice == '2':
            for q in product:
                print("%s. %s" % (q, product[q][0]))
            product_del = input("请输入下架产品的编号>>>:")
            if product_del.isdigit():
                if int(product_del) <= len(product):
                    for i in range(int(product_del), len(product)):
                        product[str(i)] = product[str(i+1)]
                    product.pop(str(len(product)))
                else:
                    print("输入的商品编号不存在！")
            else:
                print("非法输入！")
        elif admin_choice == '3':
            for q in product:
                print("%s. %s   %d" % (q, product[q][0], product[q][2]))
            product_chg = input("请输入修改产品的编号>>>:")
            product_chg_num = input("请输入产品新库存量>>>:")
            if product_chg.isdigit() and product_chg_num.isdigit():
                if int(product_chg) <= len(product):
                    product[product_chg][2] = int(product_chg_num)
                else:
                    print("输入的商品编号不存在！")
            else:
                print("非法输入！")
        elif admin_choice == 'q':
            break
        else:
            print("非法输入！")

product_file = open('product_file.txt', 'w')
for b in product:
    product_file.write('''{_id}:{_name}:{_price}:{_num}\n'''.format(_id=b, _name=product[b][0], _price=product[b][1], _num=product[b][2]))
product_file.close()

user_file = open("user_file.txt", 'w')
for c in user:
    if c == 'admin':
        user_file.write("{_user}|{_pass_wd}\n".format(_user=c, _pass_wd=user[c][0]['passwd']))
    else:
        user_file.write("{_user}|".format(_user=c))
        for d in user[c][0]:
            user_file.write("{_item}:{_item_num}|".format(_item=d, _item_num=user[c][0][d]))
        user_file.write("{_balance}\n".format(_balance=user[c][1]))
user_file.close()

