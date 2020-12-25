from math import *
from py.base_char import *
import py.lite


class skill0(被动技能):
    名称 = '战戟精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        return 1.0

    def 武器倍率(self):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.02 * self.等级, 5)


# 霸王戟=猛攻  有TP0.1
class skill1(被动技能):
    名称 = '战戟猛攻'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 20:
            return round(1 + 0.005 * self.等级, 5)
        else:
            return round(1.1 + 0.02 * (self.等级 - 20), 5)

    def 物理攻击力倍率进图(self, 武器类型):
        return self.加成倍率(武器类型)


class skill2(被动技能):
    名称 = '战戟之魂'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class skill3(被动技能):
    名称 = '战神之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


class skill4(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill5(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class skill6(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


# 霸王机吃精通吗？
class skill7(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class skill8(主动技能):
    名称 = '霸王戟'
    所在等级 = 25
    等级上限 = 1
    基础等级 = 1
    是否主动 = 0
    基础 = 2281
    成长 = 311
    CD = 0.5
    TP成长 = 0.10
    TP上限 = 5


# 果体测试就2段+1段
class skill9(主动技能):
    名称 = '破军突击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2476  # 2585 3次  #测试只有2段+1
    成长 = 291  # 307
    CD = 5.5
    # TP成长 = 0.10
    # TP上限 = 5


class skill10(主动技能):
    名称 = '追魂斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3172
    成长 = 360
    CD = 6.6
    TP成长 = 0.10
    TP上限 = 5


class skill11(主动技能):
    名称 = '落月斩'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4292
    成长 = 483
    CD = 7.7
    TP成长 = 0.10
    TP上限 = 5


class skill12(主动技能):
    名称 = '冷血突刺'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8672
    成长 = 963
    CD = 17.6
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
        elif x == 1:
            self.倍率 *= 1.29


class skill13(主动技能):
    名称 = '破灭斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7081
    成长 = 799
    CD = 15.4
    TP成长 = 0.10
    TP上限 = 5


class skill14(主动技能):
    名称 = '夺命乱舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 10134
    成长 = 1133
    CD = 19.8
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27
        elif x == 1:
            self.倍率 *= 1.36


class skill15(主动技能):
    名称 = '横扫八荒'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 18970
    成长 = 2130
    CD = 44
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2587
        elif x == 1:
            self.倍率 *= 1.4187


class skill16(主动技能):
    名称 = '长虹贯日'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 17551
    成长 = 1979
    CD = 27.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.232
        elif x == 1:
            self.倍率 *= 1.323


# 下劈中了，就不中冲击波。下劈。冲击波不计算伤害
class skill17(主动技能):
    名称 = '穿云裂地斩-下劈'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 33760  # 125368
    成长 = 3813  # 3813
    # 冲击波
    # 基础= 30210
    # 成长 = 3411
    CD = 55
    TP成长 = 0.10
    TP上限 = 5

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.22
        elif x == 1:
            self.倍率 *= 1.30


class skill18(主动技能):
    名称 = '破灭轮回刺'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 43816
    成长 = 4948
    CD = 44
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33


class skill19(主动技能):
    名称 = '断魂裂岩斩'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 48000
    成长 = 5433
    CD = 49.5
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35


class skill20(主动技能):
    名称 = '千魂弑'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 44019
    成长 = 13283
    CD = 159.5


class skill21(主动技能):
    名称 = '血战天狱'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 109081
    成长 = 32931
    CD = 198


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

不灭战神护石选项 = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        不灭战神护石选项.append(i.名称)

不灭战神符文选项 = ['无']
for i in skill_list:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        不灭战神符文选项.append(i.名称)


class character(py.lite.char_base):
    def 角色賦予(self):
        self.attr["实际名称"] = '不灭战神'
        self.attr["角色"] = '魔枪士'
        self.attr["职业"] = '征战者'

        self.attr["武器选项"] = ['战戟']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '重甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 1.8

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [10, 20, 20, 11, 4, 1, 2, 100, 1, 43, 41, 38, 36, 36, 33, 31, 23, 18, 16, 13, 12, 5]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 5, 1, 0, 5, 0, 5, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '', '', '', '', '', '', '', '10', '0', '0', '/CD', '/CD', '/CD', '1', '1', '1', '1', '1', '1', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 0, 5, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '万夫之勇']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "战戟"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "战戟猛攻"
        self.attr["右槽白金技能"] = "战戟猛攻"
        self.attr["时装上衣技能"] = "战戟猛攻"

        self.attr["三觉技能选择"] = "二觉序号"

    def 三觉技能选择(self):
        for i, 技能 in enumerate(self.attr["技能栏"]):
            if 技能.名称 == "觉醒之抉择":
                技能.关联技能 = [self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].名称]

    def 被动倍率计算(self):
        技能栏 = self.attr["技能栏"]
        技能栏[8].等级 = 技能栏[1].等级
        self.attr["物理攻击力"] = int((self.attr["物理攻击力"] - 65) * 技能栏[0].武器倍率() + 65)
        super().被动倍率计算()

    def 伤害指数计算(self):
        self.attr["进图物理攻击力"] = int((self.attr["进图物理攻击力"] - 40) * self.attr["技能栏"][0].武器倍率() + 40)
        super().伤害指数计算()
