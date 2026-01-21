#encoding:utf-8
#!/usr/bin/python

#统计奥林匹克的各个国家的金牌，银牌，铜牌榜单，实现


#统计奥林匹克的各个国家的金牌，银牌，铜牌榜单，实现
class olympic_nums:
    def __init__(self, name, jin, yin, tong):
        #初始化属性，‘定义数据类型’
        self.name = name
        self.jin = jin
        self.yin = yin
        self.tong = tong

    def add_medals(self):
        #新增奖牌
        self.jin += 1
        self.yin += 1
        self.tong += 1
        return self.jin, self.yin, self.tong


    def total_medals(self):
        #计算返回所有的奖牌总数
        return self.jin + self.yin + self.tong


    def display(self):
        #展示金牌，银牌，铜牌，总奖牌
        total = self.jin + self.yin + self.tong
        #return f"{self.name}: 金牌 {self.jin}, 银牌 {self.yin}, 铜牌 {self.tong}"
        return f"{self.name}: 金牌 {self.jin}, 银牌 {self.yin}, 铜牌 {self.tong}, 总奖牌 {total}"



if __name__ == '__main__':
    # 创建对象,这是典型的面向对象的写法，创建对象，赋数值
    china = olympic_nums("cn", 7, 8, 6)
    us = olympic_nums("us2", 8, 3, 7)
    jp = olympic_nums("jp2", 3, 9, 9)

    #china = olympic_nums("中国", 38, 32, 18)
    print(china.add_medals())  # 新增奖牌
    print(china.total_medals())   #奖牌总数
    print(china.display())    #展示金牌，银牌，铜牌，总奖牌

    #根据国家的奖牌总数排序
    #计算单个国家的奖牌总数
    china_zong = china.total_medals()
    us_zong = us.total_medals()
    jp_zong = us.total_medals()
    print('china_zong', type(china_zong))

    #创建列表，把奖牌总数和国家存进去
    medallist = [china_zong, us_zong, jp_zong]
    print('medallist', type(medallist), medallist)
    sorted_medallist = sorted(medallist, reverse=True)
    print('sorted_medallist', type(sorted_medallist), sorted_medallist)


    def __init__(self, name, jin, yin, tong):
        #初始化属性，‘定义数据类型’
        self.name = name
        self.jin = jin
        self.yin = yin
        self.tong = tong

    def add_medals(self):
        #新增奖牌
        self.jin += 1
        self.yin += 1
        self.tong += 1
        return self.jin, self.yin, self.tong


    def total_medals(self):
        #计算返回所有的奖牌总数
        return self.jin + self.yin + self.tong


    def display(self):
        #展示金牌，银牌，铜牌，总奖牌
        total = self.jin + self.yin + self.tong
        #return f"{self.name}: 金牌 {self.jin}, 银牌 {self.yin}, 铜牌 {self.tong}"
        return f"{self.name}: 金牌 {self.jin}, 银牌 {self.yin}, 铜牌 {self.tong}, 总奖牌 {total}"



if __name__ == '__main__':
    # 创建对象,这是典型的面向对象的写法，创建对象，赋数值
    china = olympic_nums("cn", 7, 8, 6)
    us = olympic_nums("us2", 8, 3, 7)
    jp = olympic_nums("jp2", 3, 9, 9)

    #china = olympic_nums("中国", 38, 32, 18)
    print(china.add_medals())  # 新增奖牌
    print(china.total_medals())   #奖牌总数
    print(china.display())    #展示金牌，银牌，铜牌，总奖牌

    #根据国家的奖牌总数排序
    #计算单个国家的奖牌总数
    china_zong = china.total_medals()
    us_zong = us.total_medals()
    jp_zong = us.total_medals()
    print('china_zong', type(china_zong))

    #创建列表，把奖牌总数和国家存进去
    medallist = [china_zong, us_zong, jp_zong]
    print('medallist', type(medallist), medallist)
    sorted_medallist = sorted(medallist, reverse=True)
    print('sorted_medallist', type(sorted_medallist), sorted_medallist)


    #根据单个奖牌排序，根据金牌排序



''' 
# 创建奖牌数据
countries = [
   # olympic_nums("中国", 38, 32, 18),
    olympic_nums("美国", 39, 41, 33),
    olympic_nums("日本", 27, 14, 17),
    olympic_nums("英国", 22, 21, 23),
]
'''

