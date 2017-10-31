# Author:Gamebu
topmenu = ['A', 'B']
Atwomenu = ['A1', 'A2', 'A3']
A1_threemenu = ['A11', 'A12', 'A13']
A2_threemenu = ['A21', 'A22', 'A23']
A3_threemenu = ['A31', 'A32', 'A33']
Btwomenu = ['B1', 'B2', 'B3']
B1_threemenu = ['B11', 'B12', 'B13']
B2_threemenu = ['B21', 'B22', 'B23']
B3_threemenu = ['B31', 'B32', 'B33']


Atwo_dict = {Atwomenu[0]: A1_threemenu, Atwomenu[1]: A2_threemenu, Atwomenu[2]: A3_threemenu}
Btwo_dict = {Btwomenu[0]: B1_threemenu, Btwomenu[1]: B2_threemenu, Btwomenu[2]: B3_threemenu}
top_dict = {topmenu[0]: Atwo_dict, topmenu[1]: Btwo_dict}

while True:
    for i in topmenu:
        print("%s" % i)
    ask = input("Please select:")
    if ask == 'q':
        print("top menu,can't q")
        continue
    elif ask == 'exit':
        print("Bye")
        exit(0)
    elif ask not in top_dict.keys():
        print("error ask")
        continue
    else:
        while True:
            for j in top_dict[ask].keys():
                print("%s" % j)
            ask1 = input("Please select:")
            if ask1 == 'q':
                break
            elif ask1 == 'exit':
                print("Bye")
                exit(0)
            elif ask1 not in top_dict[ask].keys():
                print("error ask1")
            else:
                while True:
                    for p in top_dict[ask][ask1]:
                        print("%s" % p)
                    ask2 = input("Please select:")
                    if ask2 == 'q':
                        break
                    elif ask2 == 'exit':
                        print("Bye")
                        exit(0)
                    else:
                        print("error ask2,it three_menu")