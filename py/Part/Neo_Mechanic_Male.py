from py.base_char import *
import py.lite


class skill0(被动技能):
    名称 = '方舟反应堆'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 3)


class skill1(主动技能):
    名称 = 'G1科罗纳'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 245.75 / 0.50
    成长 = 16.52 / 0.50
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(1, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.59 + 0.01 * self.等级, 3)


class skill2(主动技能):
    名称 = 'G2旋雷者'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 800
    成长 = 100
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(6, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.50 + 0.01 * self.等级, 3)


class skill3(主动技能):
    名称 = '毒蛇炮'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2910
    成长 = 330
    CD = 2.975
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 5.5


class skill4(被动技能):
    名称 = '机械概论'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['RX78追击者', 'Ez8自爆者', 'RX60陷阱追击者', '毒蛇炮', '护石风暴', '空战机械：风暴', '空投支援', '拦截机工厂', '光反应能量模块', '盖波加之拳', 'EZ10反击者', 'EXSZero毒蛇炮', 'TN80终结者', 'TX-45特工队', '超时空行军', 'HS1全息机械猎手', 'GW16-瓦尔德斯坦']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.085 + 0.015 * self.等级, 3)


class skill5(主动技能):
    名称 = 'RX78追击者'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 1056.62
    成长 = 119.38
    CD = 2.125
    TP成长 = 0.08
    TP上限 = 5
    演出时间 = 5.5


class skill6(主动技能):
    名称 = 'Ez8自爆者'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1881.68
    成长 = 212.5
    CD = 5.525
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 5.5


class skill7(主动技能):
    名称 = 'G3捕食者'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 416.54
    成长 = 47.45
    CD = 1
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(1, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.48 + 0.01 * self.等级, 3)


class skill8(主动技能):
    名称 = 'RX60陷阱追击者'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4320.16
    成长 = 487.81
    CD = 10.2
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.5


class skill9(主动技能):
    名称 = '护石风暴'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 17488.8
    成长 = 1978.2
    CD = 25.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1
        elif x == 1:
            self.倍率 *= 1.0672


class skill10(主动技能):
    名称 = '空战机械：风暴'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 1729.09 / 3
    成长 = 215.91 / 3
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(1, 1)


class skill11(主动技能):
    名称 = '空投支援'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 14091.74
    成长 = 1430.35
    CD = 29.75
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.21
        elif x == 1:
            self.倍率 *= 1.30


class skill12(主动技能):
    名称 = '拦截机工厂'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 19110.96
    成长 = 2158.29
    CD = 38.25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.27


class skill13(主动技能):
    名称 = '光反应能量模块'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 21016.24
    成长 = 2373.05
    CD = 38.25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.27


class skill14(被动技能):
    名称 = '斗志之歌'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 < 17:
            return round(1.01 + 0.015 * self.等级, 3)
        else:
            return round(1.25 + 0.02 * (self.等级 - 16), 3)


class skill15(主动技能):
    名称 = '盖波加之拳'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 51094.05
    成长 = 15440.25
    CD = 145.0


class skill16(主动技能):
    名称 = 'EZ10反击者'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 13761.42
    成长 = 1554.16
    CD = 25.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.334


class skill17(主动技能):
    名称 = 'EXSZero毒蛇炮'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 40096.07
    成长 = 4526.3
    CD = 42.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.273


class skill18(被动技能):
    名称 = 'HS1机械助手'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 3)


class skill19(主动技能):
    名称 = 'TN80终结者'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 54607.2
    成长 = 6155.5
    CD = 34
    演出时间 = 2
    是否有护石 = 1
    演出时间 = 3

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.352


class skill20(主动技能):
    名称 = 'TX-45特工队'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 35274.11
    成长 = 3982.4
    CD = 38.25
    演出时间 = 1.5
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.29


class skill21(主动技能):
    名称 = '超时空行军'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 111387.67
    成长 = 35066.68
    CD = 180


class skill22(被动技能):
    名称 = 'SOPHIA'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill23(主动技能):
    名称 = 'HS1全息机械猎手'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 6
    基础 = 110647.6
    成长 = 12005.4
    CD = 51
    演出时间 = 3


class skill24(主动技能):
    名称 = 'GW16-瓦尔德斯坦'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 346641
    成长 = 104659
    CD = 290

    def 加成倍率(self, 武器类型):
        return 0.0


class skill25(被动技能):
    名称 = '机械引爆'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 5
    是否主动 = 1
    关联技能 = ['RX78追击者', 'Ez8自爆者', 'RX60陷阱追击者', '空投支援', '拦截机工厂', 'EZ10反击者', 'TX-45特工队']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.40


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
        self.attr["实际名称"] = '重霄_机械师_男'
        self.attr["角色"] = '神枪手(男)'
        self.attr["职业"] = '机械师'

        self.attr["武器选项"] = ['自动手枪']

        self.attr["类型"] = '魔法百分比'
        self.attr["防具类型"] = '布甲'
        self.attr["防具精通属性"] = ['智力']

        self.attr["主BUFF"] = 1.85

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

        self.attr["远古记忆"] = 10

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [10, 1, 0, 1, 1, 50, 1, 0, 12, 36, 0, 33, 31, 0, 20, 12, 23, 18, 11, 16, 13, 5, 4, 6, 2, 5]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 5, 0, 0, 0, 5, 0, 5, 5, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '/CD', '0', '/CD', '', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '0', '', '/CD', '/CD', '/CD', '', '/CD', '/CD', '/CD', '', '/CD', '/CD', '']
        self.attr["技能宠物次数"] = [0, 1, 0, 1, 0, 5, 3, 10, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '雷霆怒啸手枪']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "自动手枪"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "方舟反应堆"
        self.attr["右槽白金技能"] = "方舟反应堆"
        self.attr["时装上衣技能"] = "方舟反应堆"

        self.attr["三觉技能选择"] = "一觉序号"

        self.attr["护石栏"] = ["拦截机工厂", "护石风暴", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["拦截机工厂", "拦截机工厂", "拦截机工厂", "拦截机工厂", "拦截机工厂", "拦截机工厂", "无", "无", "无"]
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
        super().被动倍率计算()
        技能栏 = self.attr["技能栏"]
        技能栏[skill_sn['G1科罗纳']].被动倍率 *= 1 + 技能栏[skill_sn['G2旋雷者']].G系加成倍率() + 技能栏[skill_sn['G3捕食者']].G系加成倍率()
        技能栏[skill_sn['G2旋雷者']].被动倍率 *= 1 + 技能栏[skill_sn['G1科罗纳']].G系加成倍率() + 技能栏[skill_sn['G3捕食者']].G系加成倍率()
        技能栏[skill_sn['G3捕食者']].被动倍率 *= 1 + 技能栏[skill_sn['G1科罗纳']].G系加成倍率() + 技能栏[skill_sn['G2旋雷者']].G系加成倍率()
