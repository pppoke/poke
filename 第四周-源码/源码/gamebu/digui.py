# author:Game_bu
num = 1
def move(n, a, b, c):
    global num
    if n == 1:
        print("{_a}->{_c}, num={_num}".format(_a=a, _c=c, _num=num))
        num +=1
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
