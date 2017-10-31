# Author:Game_bu
import os

def get_conf(backend_record):
    with open('haproxy.conf', 'r') as fp:
        line_dict = {'record': []}
        for i in fp:
            i = i.strip()
            line_list = i.split(' ')
            if len(line_list) == 2 and i.startswith('backend'):
                if len(line_dict) == 2:
                    backend_record.append(line_dict)
                    line_dict = {'record': []}
                line_dict[line_list[0]] = line_list[1]
            elif len(line_list) == 6 and i.startswith('server'):
                line_dict['record'].append({line_list[0]: line_list[1], line_list[2]: int(line_list[3]), line_list[4]: int(line_list[5])})
            else:
                pass
        backend_record.append(line_dict)
        return 0


def put_conf(backend_record):
    with open('haproxy.conf', 'r') as rf, open('haproxy1.conf', 'w+') as wf:
        for i in rf:
            if i.strip().startswith('backend'):
                break
            else:
                wf.write(i)
        for q in backend_record:
            wf.write("backend {_ip}\n".format(_ip=q['backend']))
            for j in q['record']:
                wf.write("\t\tserver {_ip} weight {_weight} maxconn {_maxconn}\n".format(_ip=j['server'], _weight=j['weight'], _maxconn=j['maxconn']))
    os.remove('haproxy.conf')
    os.rename('haproxy1.conf', 'haproxy.conf')
    print("配置信息已更新值本地！")
    return 0

def show_backend(backend_record):
    if backend_record == []:
        print("没有服务配置信息！")
        return 1
    for i in range(1, len(backend_record)+1):
        print("{_id}.  backend: {_addr}".format(_id=i, _addr=backend_record[i-1]['backend']))
        for j in backend_record[i-1]['record']:
            print("\tserver {_ip} weight {_weight} maxconn {_maxconn}".format(_ip=j['server'], _weight=j['weight'], _maxconn=j['maxconn']))
    return 0


def chg_backend(backend_record):
    chg_id = input("请输入修改的配置编号>>>：")
    if chg_id in str(list(range(1, len(backend_record)+1))):
        chg_msg = input("请输入更新的json信息>>>：")
        backend_record[int(chg_id)-1] = eval(chg_msg)
        print("信息已修改！")
    elif chg_id == 'q':
        pass
    else:
        print("非法输入！")
        return 1
    return 0


def add_backend(backend_record):
    add_msg = input("请输入新增配置的json信息>>>：")
    add_dict = eval(add_msg)
    add_flag = True
    for i in backend_record:
        if add_dict['backend'].strip() == i['backend'].strip():
            print("网站配置已存在，请选择修改动作！")
            add_flag = False
    if add_flag:
        backend_record.append(eval(add_msg))
        print("信息已新增！")
        return 0
    else:
        return 1


def del_backend(backend_record):
    del_msg = input("请输入删除的配置信息>>>：")
    del_dict = eval(del_msg)
    del_flag = True
    for i in backend_record:
        if del_dict['backend'].strip() == i['backend'].strip():
            backend_record.pop(backend_record.index(i))
            print("信息已删除！")
            del_flag = False
            break
    if del_flag:
        print("网站配置不存在，删除失败！")
        return 1
    else:
        return 0




conf_list = []

get_conf(conf_list)

while True:
    show_backend(conf_list)
    user_choice = input("\n1. 新增    2. 删除   3. 修改\n请选择动作>>>：")
    if user_choice in ['1', '2', '3', 'q']:
        if user_choice == '3':
            chg_ret = chg_backend(conf_list)
            if chg_ret == 1:
                break
            input()
        elif user_choice == '2':
            del_ret = del_backend(conf_list)
            input()
        elif user_choice == '1':
            add_ret = add_backend(conf_list)
            input()
        else:
            put_ret = put_conf(conf_list)
            print("再见")
            break
    else:
        print("非法输入！")
        break

