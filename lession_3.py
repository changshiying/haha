# money= int (input('请输入你们的工zi：'))
# if money>=20000:
#     print("我要去旅游")
# elif money>=15200:
#     print("woquchifan")
# else:
#     print("banzhuan")

a='ahasjdh我是好人！'
# for item in a:
#     print(item)
# for item in a:
#     if item == 'a':
#         continue
#     print(item)
#
# for item in a :
#     if item =='j':
#         break
#     print(item)

# for a in  range(1,10,1):
#     print(a)

# gongzi=10000
# jiangji=500
# sum1=gongzi+jiangji
# print(sum1)

# 无参函数
# def haohuo():
#     gongzi=10000
#     jiangjin=500
#     chifan=600
#     sum1=gongzi+jiangjin+chifan
#     print(sum1)
# haohuo()

# 有参函数
# def haohuo(gongzi,jiangjin,chifan):
#     sum1=gongzi+jiangjin+chifan
#     print(sum1)
# haohuo(1000,5000,3000)

# 默认参数
# def haohuo(gongzi,jiangjin,chifan=300):
# #     sum1=gongzi+jiangjin+chifan
# #     print(sum1)
# # haohuo(5000,3000,6000)
# # haohuo(6000,100)

# 不定长参数
# def haohuo(gongzi,jiangjin,chifan,*args,**kwargs):
#     print(args)
#     print(kwargs)
#     sum1=gongzi+jiangjin+chifan
#     for i in args:
#         sum1 +=i
#     for j in kwargs:
#         sum1 +=kwargs[j]   #sum1  +=kwargs.get(j)
#     print(sum1)
#
# haohuo(1000,5000,6000,300,2000,1000,fuli=802,chefei=300)


# str1='woshizhutou'
# list1=str1.split()
# print(list1)

# for n in range(1,10,1):
#     print(n)
#
name = input("Please input your name:")
sex = input("Please input your sex:")
dic = {}
dic["name"] = name
dic["sex"] = sex
print(dic)