def test1_demo():
    print('aaa')
    print('sss')
    print('zzz')
    print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
def test2_demo():
    print('bbb')
    print('sss')
    # print('zzz')
    # print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
def test3_demo():
    print('ccc')
    print('sss')
    print('zzz')
    print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww')
def int_demo():
    # 声明一个变量 = 前面的就是变量名 = 后面的是变量值
    aint = 5
    # 打印 aint变量
    print(aint)
    # type(aint) aint的变量类型
    # 打印aint的变量类型
    print(type(aint))
#
def snt_demo():
    # 声明一个变量 = 前面就是变量名 = 后面的是变量名
    asnt = '5'
    #打印变量
    print(asnt)
    # type(asnt) asnt的变量类型
    # 打印asnt的变量类型
    print(type(asnt))
#     小数类型的演示
def lfoad_demo():
    ant = 3.14
    print(ant)
    print(type(ant))
#     加法演示  （a,b）：括号里面的叫参数，多个参数用逗号隔开：参数等同于变量，只不过没有赋值：
def add_demo(a,b):
    print(a+b)
def types_dem():
    aint = 8
    print(type(aint))
    print(type(str(aint)))
    print(type(int(aint)))
def str_join():
    a = 123
    b = '我很壮'
    c = 3.14
    print(str(a)+b+str(c))
    print('a是%s b是%s c是%s'%(a,b,c) )
def jianfa_demo(a,b):
    c = a - b
    return c


if __name__ == '__main__':
    # types_dem()
    # str_join()
    c = jianfa_demo(100,500)
    print(c)
    e = add_demo(100,300)
    print(e)
    print(type(e))
