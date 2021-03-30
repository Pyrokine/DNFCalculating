from py.base_char import *
import py.lite


class 主动技能(主动技能):
    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / self.恢复, 1)


class skill0(主动技能):
    名称 = '崩拳'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2485.356
    成长 = 280.644
    CD = 6.0
    TP成长 = 0.1
    TP上限 = 5


class skill1(主动技能):
    名称 = '铁山靠'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3569.925
    成长 = 403.075
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 0.5


class skill2(主动技能):
    名称 = '碎骨'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3654.35
    成长 = 412.65
    CD = 7.0
    TP成长 = 0.1
    TP上限 = 5


class skill3(被动技能):
    名称 = '柔化肌肉'
    所在等级 = 30
    等级上限 = 15
    基础等级 = 5

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.125 + 0.015 * self.等级, 5)


class skill4(被动技能):
    名称 = '弱点感知'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1.01 + 0.01 * self.等级, 5)
            else:
                return round(1.11 + 0.02 * (self.等级 - 10), 5)


class skill5(主动技能):
    名称 = '寸拳'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8153.429
    成长 = 920.572
    CD = 15
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 0.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.09


class skill6(主动技能):
    名称 = '升龙拳'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 1762.0286
    成长 = 198.9714
    攻击次数 = 4
    基础2 = 1526.6286
    成长2 = 172.3714
    攻击次数2 = 1
    倍率 = 1.073
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 2.0


class skill7(主动技能):
    名称 = '闪电之舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1903.96875
    成长 = 215.03125
    攻击次数 = 7
    CD = 20
    TP成长 = 0.1
    TP上限 = 5
    演出时间 = 1
    是否有护石 = 1
    演出时间 = 2.2

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.92
            self.攻击次数 += 2
            self.CD *= 0.85
            self.演出时间 = 2.7
        elif x == 1:
            self.倍率 *= 0.99
            self.攻击次数 += 2
            self.CD *= 0.85
            self.演出时间 = 2.7


class skill8(主动技能):
    名称 = '纷影连环踢'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 526.5
    成长 = 59.5
    攻击次数 = 10
    基础2 = 11692
    成长2 = 1320.166666
    攻击次数2 = 1
    倍率 = 1.099
    CD = 40.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 4

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.演出时间 = 4.4
            self.倍率 *= 0.87
            self.攻击次数 = 20
        elif x == 1:
            self.演出时间 = 4.4
            self.倍率 *= 0.98
            self.攻击次数 = 20


class skill9(主动技能):
    名称 = '武神强踢'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 37261 * 1.1 * 1.007253
    成长 = 11248.5 * 1.1 * 1.007253
    CD = 145.0
    演出时间 = 0.5


class skill10(被动技能):
    名称 = '武神步'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.05 + 0.02 * self.等级, 5)


class skill11(主动技能):
    名称 = '破碎拳'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 18861.4546
    成长 = 2129.5454
    CD = 30
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.19 + 0.09


class skill12(主动技能):
    名称 = '回天连环击'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 2855.53
    成长 = 322.470
    攻击次数 = 1
    基础2 = 26260.765
    成长2 = 2965.234
    攻击次数2 = 1
    CD = 50
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.2

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 *= 1.34
        elif x == 1:
            self.攻击次数 = 0
            self.攻击次数2 *= 1.34 + 0.08


class skill13(被动技能):
    名称 = '神武之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        return round(1.22 + 0.02 * self.等级, 5)


class skill14(主动技能):
    名称 = '虎啸神拳'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 1581.4
    成长 = 178.6
    攻击次数 = 15
    基础2 = 15453.2
    成长2 = 1744.8
    攻击次数2 = 1
    基础3 = 4083.8667
    成长3 = 461.1333
    攻击次数3 = 1
    CD = 40.0
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 2 * 0.83


class skill15(主动技能):
    名称 = '无影脚'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 4892.76666
    成长 = 646.233333
    攻击次数 = 1
    基础2 = 2473.33333 + 2475.9  # 第二段+第三段
    成长2 = 326.666666 + 327.1
    攻击次数2 = 1
    基础3 = 38686.4
    成长3 = 5109.6
    攻击次数3 = 1
    CD = 45.0
    是否有护石 = 1
    演出时间 = 2

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 = 0
            self.攻击次数3 *= 1.66


class skill16(主动技能):
    名称 = '极尽霸皇断空拳'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 87153.5 * 1.006068
    成长 = 26310.5 * 1.006068
    CD = 180.0
    演出时间 = 1.2


class skill17(被动技能):
    名称 = '疾风劲'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill18(主动技能):
    名称 = '雷霆之舞'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 95264.6
    成长 = 10754.4
    CD = 60.0
    演出时间 = 6.2


class skill19(主动技能):
    名称 = '真烈空星鸣拳'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    基础 = 259160
    成长 = 78240
    CD = 290
    演出时间 = 6.1

    def 加成倍率(self, 武器类型):
        return 0


# CDR: 拳套精通(10%)
# 不包含觉醒
class skill20(被动技能):
    名称 = '拳套精通'
    所在等级 = 15
    等级上限 = 10
    基础等级 = 10
    # 拳套精通cd
    关联技能 = ['无']
    冷却关联技能 = ['崩拳', '铁山靠', '碎骨', '寸拳', '升龙拳', '闪电之舞', '纷影连环踢', '破碎拳', '回天连环击', '虎啸神拳', '无影脚', '雷霆之舞']

    def 加成倍率(self, 武器类型):
        return 1.0

    def CD缩减倍率(self, 武器类型):
        if 武器类型 == '拳套':
            if self.等级 == 0:
                return 1.0
            else:
                return 1 - 0.01 * self.等级
        else:
            return 1.0

    # 拳套自带全技能10cd
    冷却关联技能2 = ['所有']

    def CD缩减倍率2(self, 武器类型):
        if 武器类型 == '拳套':
            return 0.9
        elif 武器类型 == '臂铠':
            return 1.1
        else:
            return 1.0


# CDR 一觉cdr buff
class skill21(被动技能):
    名称 = '武神强踢buff'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['无']
    冷却关联技能 = ['所有']

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.9


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
        self.attr["实际名称"] = '归元_散打_女'
        self.attr["角色"] = '格斗家(女)'
        self.attr["职业"] = '散打'

        self.attr["武器选项"] = ['拳套', '臂铠']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '轻甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 2.13

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [46, 41, 41, 5, 10, 36, 36, 33, 31, 12, 20, 23, 18, 11, 16, 13, 5, 4, 6, 2, 10, 1]
        self.attr["技能TP等级"] = [0, 1, 5, 0, 0, 5, 0, 5, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['0', '/CD', '/CD', '', '', '/CD', '/CD', '/CD', '0', '1', '', '/CD', '/CD', '', '/CD', '/CD', '1', '', '1', '1', '', '']
        self.attr["技能宠物次数"] = [0, 2, 2, 0, 0, 2, 2, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '幻光绽放拳套']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "拳套"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "弱点感知"
        self.attr["右槽白金技能"] = "弱点感知"
        self.attr["时装上衣技能"] = "弱点感知"

        self.attr["三觉技能选择"] = "二觉序号"

        self.attr["护石栏"] = ["闪电之舞", "寸拳", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["闪电之舞", "闪电之舞", "闪电之舞", "闪电之舞", "闪电之舞", "闪电之舞", "无", "无", "无"]
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

    def CD倍率计算(self):
        if "武神强踢" in self.attr["技能栏"][skill_sn['真烈空星鸣拳']].关联技能:
            self.attr["技能栏"][skill_sn['武神强踢buff']].等级 = 0
        super().CD倍率计算()