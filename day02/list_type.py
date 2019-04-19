alist = [1, 'shi', '我是', '谁', '123']

def list_sel(a):
    print(a[4])
    print(a[-3])
    print(a[0:3])
    print(a[3:3])
    print(a[0:-1])
def list_del():
    alist = [1, 'shi', '我是', '谁', '123']
    alist.pop()
    print(alist)
    alist.pop(2)
    print(alist)
    alist.pop('1')
    print(alist)
def list_add():
    alist = [1, 'shi', '我是', '谁', '123']
    alist.append('laozi')
    print(alist)
    blit = '123','456',[1,2,3]
    alist.append(blit)
    print(alist)
    blit = alist[3:8]
    alist.append(alist)
    print(blit)
    alist.pop(-1)
    alist[0] = alist.pop(-1)
    print(alist)
    alist[0] = 6
    print(alist)
    alist[2]
    b = 6
    alist[2] = b
    print(alist)

def a():
    alist[2] = 6
    print(alist)




if __name__ == '__main__':
    # alist = [1,'shi','我是','谁','123']
    # list_sel(alist)
    # list_del()
    # list_add()
    a()



