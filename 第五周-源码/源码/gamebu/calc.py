__Author__ = "Gamebu"

import re


def handle_special_occactions(jiajian_oper, cchu_oper):
    for i, m in enumerate(cchu_oper):
        j = m.strip()
        if j.endswith('*') or j.endswith('/'):
            cchu_oper[i+1] = m + jiajian_oper[i] + cchu_oper[i+1]
            del jiajian_oper[i]
            del cchu_oper[i]
    return jiajian_oper, cchu_oper

def cchu(formula):
    cchu_oper = re.findall('[*/]', formula)
    cchu_list = re.split('[*/]', formula)
    res = None
    for index, j in enumerate(cchu_list):
        if res:
            if cchu_oper[index - 1] == '*':
                res *= float(j)
            elif cchu_oper[index - 1] == '/':
                res /= float(j)
        else:
            res = float(j)
    return res
def compute(formula):
    formula = formula.replace("++", "+")
    formula = formula.replace("+-", "-")
    formula = formula.replace("-+", "-")
    formula = formula.replace("--", "+")
    formula = formula.replace("- -", "+")
    formula = formula.strip('()')
    jiajian_oper = re.findall('[+-]', formula)
    cchu_oper = re.split('[+-]', formula)
    if len(cchu_oper[0].strip()) == 0:
        cchu_oper[1] = jiajian_oper[0] + cchu_oper[1]
        del cchu_oper[0]
        del jiajian_oper[0]
    jiajian_oper, cchu_oper = handle_special_occactions(jiajian_oper, cchu_oper)
    for index, m in enumerate(cchu_oper):
        if re.search('[*/]', m):
            cchu_res = cchu(m)
            cchu_oper[index] = cchu_res

    jj_res = None
    for index, j in enumerate(cchu_oper):
        if jj_res:
            if jiajian_oper[index - 1] == '-':
                jj_res -= float(j)
            elif jiajian_oper[index -1] == '+':
                jj_res += float(j)
        else:
            jj_res = float(j)

    return jj_res
def calc(formula):
    formula = formula.strip()
    calc_res = None
    while True:
        i = re.search('\([^()]*\)', formula)
        if i:
            calc_res = compute(i.group())
            formula = formula.replace(i.group(), str(calc_res))
        else:
            calc_res = compute(formula)
            print("计算结果为：", calc_res)
            break


if __name__ == '__main__':
    back_flag = False
    while not back_flag:
        formula = input("输入:")
        if formula == 'b':
            back_flag = True
            continue
        calc(formula)