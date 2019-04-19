from day01 import base_type
def int_demo():
    aint=1
    print(aint)
    print(type(aint))
def zhun_huan():
    a=1
    print(type(str(a)))
    print(type(float(a)))
def chuan_lian():
    a=123
    b='他骂死了'
    print(str(a)+b)
    print('%s %s '% (a,b))
def add_demo(a,d):
    print(a+d)


def jian_fa(a,b):
    c = a-b
    return c







if __name__ == '__main__':
    zhun_huan()
    # c = jian_fa(3,1)
    # print (c)
    # add_demo(3,4)
    chuan_lian()
    # int_demo()

    # base_type.add_demo(32, 32)
    #
    # d = base_type.jianfa_demo(30, 15)
    # print(d)






