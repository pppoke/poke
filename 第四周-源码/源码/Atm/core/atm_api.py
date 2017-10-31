# Author:Game_bu
import os, functools, pickle, time, json

user_state = False
user_name = ''
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def login(user_type=False):
    def out_wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            global user_state
            if not user_state:
                with open(BASE_DIR + "/conf/db.bat", 'rb') as fp:
                    user_dict = pickle.load(fp)
                username = input("请输入用户名：")
                password = input("请输入密码：")
                if user_type:
                    if username in user_dict['admin'] and password == user_dict['admin'][username]['passwd']:
                        user_state = True
                        print("欢迎您，管理员：{_name}".format(_name=username))
                        global user_name
                        user_name = username
                    else:
                        print("管理员用户名或密码错误！")
                        return 1
                else:
                    if username in user_dict['user'] and password == user_dict['user'][username]['passwd']:
                        user_state = True
                        print("欢迎您，会员用户：{_name}".format(_name=username))
                        user_name = username
                    else:
                        print("用户名或密码错误！")
                        return 1
            else:
                pass
            wrap_ret = func(*args, **kwargs)
            return wrap_ret
        return wrapper
    return out_wrapper


@login(user_type=True)
def admin():
    admin_navi = ["添加账户", "额度管理", "冻结账户", "会员列表", "注销"]
    while True:
        for i in range(len(admin_navi)):
            print("{_id}. {_navi}".format(_id=i+1, _navi=admin_navi[i]))
        admin_navi_choice = input("请选择>>>:")
        if admin_navi_choice.isdigit():
            admin_navi_choice = int(admin_navi_choice)
        if admin_navi_choice in range(1, len(admin_navi)+1):
            if admin_navi_choice == 1:
                admin_adduser()
            elif admin_navi_choice == 2:
                admin_quota()
            elif admin_navi_choice == 3:
                admin_freeze()
            elif admin_navi_choice == 4:
                all_user()
            elif admin_navi_choice == 5:
                global user_state
                user_state = False
                print("再见")
                return 0
            else:
                pass
        else:
            print("非法输入!")


@login(user_type=False)
def query():
    with open(BASE_DIR + "/conf/db.bat", 'rb') as fp:
        query_user_dict = pickle.load(fp)
    print(" 用户名     余额    总额度          状态   ")
    q = query_user_dict['user'][user_name]
    print("%-8s %-8.2f %-8.1f %10s" % (user_name, q['balance'], q['limit'], q['state']))
    print("\n当前已用额度：%8.2f\n" % (q['limit'] - q['balance']))


@login(user_type=False)
def transfer():
    with open(BASE_DIR + "/conf/db.bat", 'rb') as fp:
        transfer_dict = pickle.load(fp)
    count3 = 0
    while count3 < 3:
        tf_user = input("请输入转账用户名：")
        if tf_user.strip() == user_name:
            print("不能向同一账户转账！")
            count3 += 1
            continue
        elif tf_user.strip() not in transfer_dict['user'].keys():
            print("账户不存在！")
            count3 += 1
            continue
        elif  transfer_dict['user'][tf_user.strip()]['state'] == 'freeze':
            print("该账户被冻结，请联系管理员！")
            count3 += 1
            continue
        else:
            tf_user = tf_user.strip()
            break
    else:
        print("错误过多，请冷静重试")
        return 1
    count2 = 0
    while count2 < 3:
        ft_cash = input("请输入转账数额：")
        ft_cash_list = ft_cash.strip().split('.')
        if len(ft_cash_list) == 1:
            if not ft_cash.isdigit() or ft_cash.startswith('0'):
                print("非法输入，请重新输入！")
                count2 += 1
                continue
            else:
                ft_cash = float(ft_cash_list[0])
                break
        elif len(ft_cash_list) == 2:
            if not ft_cash_list[0].isdigit() or not ft_cash_list[1].isdigit():
                print("非法输入，请重新输入！")
                count2 += 1
                continue
            elif ft_cash.startswith('0') and len(ft_cash_list[0]) > 1:
                print("非法输入，请重新输入！")
                count2 += 1
                continue
            else:
                ft_cash = float(ft_cash_list[0] + '.' + ft_cash_list[1][0:2])
                break
        else:
            print("非法输入，请重新输入！")
            count2 += 1
            continue
    if count2 == 3:
        print("错误过多，请冷静重试")
        return 1
    if transfer_dict['user'][user_name]['balance'] < ft_cash:
        print("您的余额不足，转账失败！")
        return 2
    else:
        transfer_dict['user'][user_name]['balance'] -= ft_cash
        transfer_dict['user'][tf_user]['balance'] += ft_cash
        with open(BASE_DIR + "/conf/db.bat", 'wb') as fp:
            pickle.dump(transfer_dict, fp)
        logger(user_name, '转账转出', '转出给' + tf_user, ft_cash)
        logger(tf_user, '转账转入', '转自于' + user_name, ft_cash)
        print("转账已完成！")
    return 0


@login(user_type=False)
def repayment():
    with open(BASE_DIR + "/conf/db.bat", 'rb') as fp:
        repayment_dict = pickle.load(fp)
    count2 = 0
    while count2 < 3:
        repay_cash = input("请输入还款数额：")
        if not repay_cash.isdigit() or repay_cash.startswith('0'):
            print("非法输入，请重输！")
            count2 += 1
            continue
        else:
            repay_authent = input("请输入还款口令码:")
            if repay_authent == '123456':
                repay_cash = int(repay_cash)
                break
            else:
                print("口令码错误，还款失败！")
                return 2
    if count2 == 3:
        print("错误过多，请冷静重试")
        return 1
    repayment_dict['user'][user_name]['balance'] += repay_cash
    with open(BASE_DIR + "/conf/db.bat", 'wb') as fp:
        pickle.dump(repayment_dict, fp)
    logger(user_name, '还款', '主动还款', repay_cash)
    print("还款完成")
    return 0


@login(user_type=True)
def all_user():
    with open(BASE_DIR + "/conf/db.bat", 'rb') as fp:
        all_user_dict = pickle.load(fp)
        print(" 用户名     余额    总额度          状态   ")
        user_list = list(all_user_dict['user'].keys())
        user_list.sort()
        for i in user_list:
            q = all_user_dict['user'][i]
            print("%-8s %-8.2f %-8.1f %10s" % (i, q['balance'], q['limit'], q['state']))
        return 0


@login(user_type=True)
def admin_freeze():
    with open(BASE_DIR + "/conf/db.bat", 'rb') as fp:
        freeze_user_dict = pickle.load(fp)
    count = 0
    while count < 3:
        freeze_user = input("请输入操作会员用户名：")
        if freeze_user.strip() in freeze_user_dict['user']:
            freeze_user = freeze_user.strip()
            break
        else:
            print("不存在该会员信息，请重试！")
            count += 1
            continue
    if count == 3:
        print("错误过多，请冷静重试")
        return 1
    old_state = freeze_user_dict['user'][freeze_user]['state']
    if old_state == 'freeze':
        freeze_user_dict['user'][freeze_user]['state'] = 'active'
    else:
        freeze_user_dict['user'][freeze_user]['state'] = 'freeze'
    with open(BASE_DIR + "/conf/db.bat", 'wb') as fp:
        pickle.dump(freeze_user_dict, fp)
    global user_name
    logger(user_name, '用户冻结/解冻', '用户' + freeze_user+'状态已由' + old_state + '调整为' + freeze_user_dict['user'][freeze_user]['state'])
    print("会员:{_user}的额度已由{_old_state}调整为{_new_state}".format(_user=freeze_user, _old_state=old_state, _new_state=freeze_user_dict['user'][freeze_user]['state']))


@login(user_type=True)
def admin_quota():
    with open(BASE_DIR + "/conf/db.bat", 'rb') as fp:
        quota_user_dict = pickle.load(fp)
    count = 0
    while count < 3:
        quota_user = input("请输入操作会员用户名：")
        if quota_user.strip() in quota_user_dict['user']:
            if quota_user_dict['user'][quota_user]['state'] == 'active':
                quota_user = quota_user.strip()
                break
            else:
                print("该会员被冻结，请先解冻！")
                count += 1
                continue
        else:
            print("不存在该会员信息，请重试！")
            count += 1
            continue
    if count == 3:
        print("错误过多，请冷静重试")
        return 1
    count1 = 0
    while count1 < 3:
        quota_limit = input("请输入会员信用卡额度(最高30000)：")
        if quota_limit.startswith('0') or not quota_limit.isdigit():
            print("非法输入，请重新输入！")
            count1 += 1
            continue
        elif int(quota_limit) > 30000:
            print("额度过高，请重新输入！")
            count1 += 1
            continue
        else:
            quota_limit = float(quota_limit)
            break
    if count1 == 3:
        print("错误过多，请冷静重试")
        return 1
    old_limit = quota_user_dict['user'][quota_user]['limit']
    quota_user_dict['user'][quota_user]['limit'] = quota_limit
    quota_user_dict['user'][quota_user]['balance'] -= (old_limit - quota_limit)
    with open(BASE_DIR + "/conf/db.bat", 'wb') as fp:
        pickle.dump(quota_user_dict, fp)
    global user_name
    logger(user_name, '额度调整', '用户' + quota_user+'额度已由' + str(old_limit) + '调整为' + str(quota_limit))
    print("会员:{_user}的额度已由{_old_limit}调整为{_limit}".format(_old_limit=old_limit, _user=quota_user, _limit=quota_limit))


@login(user_type=True)
def admin_adduser():
    with open(BASE_DIR + "/conf/db.bat", 'rb') as fp:
        adm_add_user_dict = pickle.load(fp)
    count3 = 0
    while count3 < 3:
        add_user = input("请输入新会员用户名：")
        if add_user.strip() in adm_add_user_dict['user']:
            print("用户名已存在，请先注销该用户！")
            count3 += 1
        else:
            add_user = add_user.strip()
            break
    if count3 == 3:
        print("错误过多，请冷静重试")
        return 1
    count = 0
    while count < 3:
        add_passwd = input("请输入会员密码：")
        add_passwd1 = input("请再次输入会员密码：")
        if add_passwd.strip() != add_passwd1.strip():
            print("两次输入密码不相同，请重新输入！")
            count += 1
            continue
        else:
            add_passwd = add_passwd.strip()
            break
    if count == 3:
        print("错误过多，请冷静重试")
        return 1
    count2 = 0
    while count2 < 3:
        add_limit = input("请输入会员信用卡额度(最高12000)：")
        if add_limit.startswith('0') or not add_limit.isdigit():
            print("非法输入，请重新输入！")
            count2 += 1
            continue
        elif int(add_limit) > 12000:
            print("额度过高，请重新输入！")
            count2 += 1
            continue
        else:
            add_limit = float(add_limit)
            break
    if count2 == 3:
        print("错误过多，请冷静重试")
        return 1
    count1 = 0
    while count1 < 3:
        add_interest = input("请输入信用卡提现费率(0.01-0.09)：")
        if len(add_interest) >= 4 and add_interest[0:4].startswith('0.0') and add_interest[3].isdigit():
            add_interest = float(add_interest)
            break
        else:
            print("非法输入，请重新输入！")
            count1 += 1
    if count1 == 3:
        print("错误过多，请冷静重试")
        return 1
    adm_add_user_dict['user'][add_user] = {'passwd': add_passwd, 'limit': add_limit, 'balance': add_limit, 'interest': add_interest, 'state': 'active'}
    with open(BASE_DIR + "/conf/db.bat", 'wb') as fp:
        pickle.dump(adm_add_user_dict, fp)
    global user_name
    logger(user_name, '添加用户', add_user)
    print("新会员：{_user}已添加到后台！".format(_user=add_user))


def user_logout():
    global user_state, user_name
    user_state = False
    user_name = ''
    return 0


def logger(user_log, action, event, money=0.0):
    log_time = time.strftime('%Y-%m-%d %X')
    with open(BASE_DIR + "/conf/atm.log", 'a+', encoding='utf-8') as fp:
        fp.write('{_log_time}|用户名:{_user_name}|动作:{_action}|事件:{_event}|钱款:{_money}\n'.format(_log_time=log_time, _user_name=user_log, _action=action, _event=event, _money=money))
