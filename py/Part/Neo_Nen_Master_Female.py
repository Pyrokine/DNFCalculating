from py.base_char import *
import py.lite


# 蓄念炮
class skill0(被动技能):
    名称 = '蓄念炮'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    # 基础 = 226
    # 成长 = 5
    关联技能 = ['念气波蓄念炮']

    def 加成倍率(self, 武器类型):
        return round(2.26 + 0.05 * self.等级, 5)


# 分身
class skill1(主动技能):
    名称 = '分身'
    所在等级 = 5
    等级上限 = 20
    基础等级 = 10
    基础个数 = 0
    是否有伤害 = 0
    TP上限 = 0
    关联技能 = ['幻影爆碎']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round(self.基础个数 + self.等级, 5)


# 一觉被动
class skill2(被动技能):
    名称 = '乱舞千叶花'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.15 + 0.01 * self.等级, 5)


# 二觉被动
class skill3(被动技能):
    名称 = '心之念意'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.03 * self.等级, 5)


# 念气归元
class skill4(被动技能):
    名称 = '念气归元'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 分身0.01 最后被动倍率=幻爆百分比*100
class skill5(主动技能):
    名称 = '幻影爆碎'
    是否主动 = 0
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 386.6
    成长 = 43.8
    CD = 12
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.基础 + self.成长 * self.等级, 5)


# 念气波
class skill6(主动技能):
    名称 = '念气波'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 593
    成长 = 66.8
    CD = 1
    TP成长 = 0.08
    TP上限 = 5


# 念气波蓄念炮
class skill7(主动技能):
    名称 = '念气波蓄念炮'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 593
    成长 = 66.8
    CD = 3
    TP成长 = 0.08
    TP上限 = 5


# 念气环绕
class skill8(主动技能):
    名称 = '念气环绕'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    基础 = 322
    成长 = 36.5
    CD = 0.5
    TP成长 = 0.10
    TP上限 = 5
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.02 * self.等级, 3)


# 念兽龙虎啸
class skill9(主动技能):
    名称 = '念兽龙虎啸'
    所在等级 = 40
    等级上限 = 30
    基础等级 = 20
    基础 = 732
    成长 = 0
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 <= 19:
            return round(1.03 + 0.01 * self.等级, 5)
        else:
            return round(0.84 + 0.02 * self.等级, 5)


class skill10(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['念兽龙虎啸']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


# 气玉弹
class skill11(主动技能):
    名称 = '气玉弹'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2876.5
    成长 = 323.5
    CD = 8
    TP成长 = 0.08
    TP上限 = 5


# 狮子吼
class skill12(主动技能):
    名称 = '狮子吼'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 5659.1
    成长 = 638.9
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27
        elif x == 1:
            self.倍率 *= 1.27 + 0.09


# 螺旋念气场
class skill13(主动技能):
    名称 = '螺旋念气场'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 9336.7
    成长 = 1051.3
    # 实际CD为20秒
    演出时间 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.13
        elif x == 1:
            self.倍率 *= 1.13 + 0.09


# 念兽雷龙出海
class skill14(主动技能):
    名称 = '念兽雷龙出海'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 20572
    成长 = 2361
    攻击次数 = 1
    # 秒C
    基础2 = 15427
    成长2 = 1770.5
    攻击次数2 = 0

    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.13
        elif x == 1:
            self.倍率 *= 1.13 + 0.09


# 一觉
class skill15(主动技能):
    名称 = '千莲怒放'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 34236
    成长 = 10337
    CD = 145


# 奔雷掌
class skill16(主动技能):
    名称 = '奔雷掌'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 14808.2
    成长 = 1671.8
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20006759886
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.28807255611
            self.CD *= 0.90


# 狂狮怒吼
class skill17(主动技能):
    名称 = '狂狮怒吼'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 17450.5
    成长 = 1969.5
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.188
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.254
            self.CD *= 0.90


# 奇袭幻影
class skill18(主动技能):
    名称 = '奇袭幻影'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 38967.3
    成长 = 4400.7
    CD = 40
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33


# 聚能念气炮
class skill19(主动技能):
    名称 = '聚能念气炮'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 47986.6
    成长 = 5418.3
    CD = 45
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.26


# 二觉
class skill20(主动技能):
    名称 = '念帝旋天破'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 91535
    成长 = 27634
    CD = 180


# 天雷分身步
class skill21(主动技能):
    名称 = '天雷分身步'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    # 🐎测试9hit,游戏写的10hit
    基础 = 71859.4
    成长 = 8113.6
    倍率 = 1.10  # 加强
    CD = 60.0


# 三觉
class skill22(主动技能):
    名称 = '念印幻流破'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 229668
    成长 = 69341
    倍率 = 1.08  # 加强
    CD = 290.0
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


skill_list = []
i = 0
while i >= 0:
    try:
        exec('skill_list.append(skill' + str(i) + '())')
        i += 1
    except:
        i = -1

skill_sn = dict()
for i in range(len(skill_list)):
    skill_sn[skill_list[i].名称] = i

skill_sn_awaking1 = 0
skill_sn_awaking2 = 0
skill_sn_awaking3 = 0
for i in skill_list:
    if i.所在等级 == 50:
        skill_sn_awaking1 = skill_sn[i.名称]
    if i.所在等级 == 85:
        skill_sn_awaking2 = skill_sn[i.名称]
    if i.所在等级 == 100:
        skill_sn_awaking3 = skill_sn[i.名称]

option_talismans = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        option_talismans.append(i.名称)

option_rune = ['无']
for i in skill_list:
    if 20 <= i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        option_rune.append(i.名称)


class character(py.lite.CharBase):
    def 角色賦予(self):
        self.attr["实际名称"] = '归元_气功师_女'
        self.attr["角色"] = '格斗家(女)'
        self.attr["职业"] = '气功师'

        self.attr["武器选项"] = ['手套']

        self.attr["类型"] = '魔法百分比'
        self.attr["防具类型"] = '布甲'
        self.attr["防具精通属性"] = ['智力']

        self.attr["主BUFF"] = 1.57

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

        self.attr["BUFF属强"] = 86
        self.attr["远古记忆"] = 10

        self.attr["雷龙开关"] = 1

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [1, 10, 20, 11, 4, 43, 46, 46, 10, 20, 100, 46, 36, 33, 31, 12, 23, 18, 16, 13, 5, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 5, 0, 0, 0, 3, 0, 0, 5, 5, 5, 0, 0, 5, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '', '', '', '', '/CD', '0', '0', '72', '5', '', '0', '/CD', '/CD', '1', '1', '/CD', '/CD', '1', '1', '1', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 1, 0, 0, 40, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '无瑕之意志手套']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "手套"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "念兽龙虎啸"
        self.attr["右槽白金技能"] = "念兽龙虎啸"
        self.attr["时装上衣技能"] = "心之念意"

        self.attr["三觉技能选择"] = "一觉序号"

        self.attr["护石栏"] = ["狮子吼", "螺旋念气场", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["狮子吼", "狮子吼", "狮子吼", "狮子吼", "狮子吼", "狮子吼", "无", "无", "无"]
        self.attr["符文效果"] = ["攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%"]
        self.attr["辟邪玉栏"] = [
            ["无", 0],
            ["无", 0],
            ["无", 0],
            ["无", 0]
        ]
        self.attr["希洛克装备栏"] = ["无", "无", "无"]
        self.attr["希洛克武器栏"] = [
            ["无", 6],
            ["无", 3]
        ]

    def 三觉技能选择(self):
        self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].被动倍率 = 0

    def 被动倍率计算(self):
        技能栏 = self.attr["技能栏"]
        技能栏[skill_sn['分身']].基础个数 = 技能栏[skill_sn['幻影爆碎']].TP等级

        技能栏[skill_sn['念兽雷龙出海']].攻击次数 = (1 - self.attr["雷龙开关"])
        技能栏[skill_sn['念兽雷龙出海']].攻击次数2 = self.attr["雷龙开关"]

        if self.is_equip_exist('拥抱晨曦之温暖') or self.is_equip_exist('融化黑暗之温暖'):
            self.attr["技能栏"][skill_sn['幻影爆碎']].恢复 -= 0.3

        super().被动倍率计算()

    def 伤害指数计算(self):
        self.attr["光属性强化"] += self.attr["BUFF属强"]
        super().伤害指数计算()
