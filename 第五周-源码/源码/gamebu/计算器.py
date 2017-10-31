# -*- coding:utf-8 -*-
# Author:Game_bu

import re


def jjcc(formula_list):
    while True:
        if '*' in formula_list or '/' in formula_list:
            for index in range(1, len(formula_list)-1):
                if formula_list[index] == '*' and formula_list[index-1] != 'd':
                    formula_list[index-1] = str(float(formula_list[index-1])*float(formula_list[index+1]))
                    formula_list[index] = 'd'
                    formula_list[index+1] = 'd'
                if formula_list[index] == '/' and formula_list[index-1] != 'd':
                    formula_list[index-1] = str(float(formula_list[index-1])/float(formula_list[index+1]))
                    formula_list[index] = 'd'
                    formula_list[index+1] = 'd'
        elif '+' in formula_list or '-' in formula_list:
            for index in range(1, len(formula_list)-1):
                if formula_list[index] == '+' and formula_list[index-1] != 'd':
                    formula_list[index-1] = str(float(formula_list[index-1])+float(formula_list[index+1]))
                    formula_list[index] = 'd'
                    formula_list[index+1] = 'd'
                if formula_list[index] == '-' and formula_list[index-1] != 'd':
                    formula_list[index-1] = str(float(formula_list[index-1])-float(formula_list[index+1]))
                    formula_list[index] = 'd'
                    formula_list[index+1] = 'd'
        else:
            #print(formula_list)
            return str(formula_list[0])
        while True:
            if 'd' in formula_list:
                formula_list.remove('d')
                continue
            break


def chuli(str_data):
    j = 0
    formula_list = []
    for i in range(0, len(str_data)):
        if str_data[i] in "+-*/":
            if i == 0:
                continue
            if i != j:
                formula_list.append(str_data[j:i])
                formula_list.append(str_data[i])
            else:
                continue
            j = i + 1
    else:
        formula_list.append(str_data[j:i + 1])
    #print(formula_list)
    jie_guo = jjcc(formula_list)
    if jie_guo:
        return jie_guo



back_flag = False
while not back_flag:
    formula = input("输入:")
    if formula == 'b':
        back_flag = True
        continue
    fma_tmp = re.sub('[0-9]', '', re.sub('[+-/*() ]', '0', formula))
    if fma_tmp:
        print("非法输入:", fma_tmp)
        back_flag = True
        continue
    break
while True:
    lit = re.findall(r'\([^()]+\)', formula)
    if lit:
        lit_cp = lit.copy()
        for i in range(0, len(lit)):
            lit[i] = chuli(lit[i][1:-1])
        for j in lit_cp:
            #print(formula)
            formula = formula[0:formula.index(j)] + lit[lit_cp.index(j)] + formula[formula.index(j)+len(j):]
            #formula = re.sub(j, lit[lit_cp.index(j)], formula)
            #print(formula)
            #input()
    else:
        print("结果为：%-52.8f" % float(chuli(formula)))
        break