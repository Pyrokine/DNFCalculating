from math import *
from py.base_char import *
import py.lite


# 武器钝器
class 破晓女神主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '钝器':
            return round(self.CD / self.恢复 * 1.05, 1)


# 天使光翼
class skill0(被动技能):
    名称 = '天使光翼'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.00 + 0.01 * self.等级, 5)
        else:
            return round(0.90 + 0.02 * self.等级, 5)
    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95

# 天使降临
class skill1(被动技能):
    名称 = '天使降临'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.08 + 0.01 * self.等级, 5)
        else:
            return round(0.98 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 <= 10:
            return round(1.08 + 0.01 * self.等级, 5)
        else:
            return round(0.98 + 0.02 * self.等级, 5)

# 一觉被动
class skill2(被动技能):
    名称 = '荣耀之光'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105+0.015 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.105 + 0.015 * self.等级, 5)

# 二觉被动
class skill3(被动技能):
    名称 = '戒律'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


# 卓越之力
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


# 超卓之心
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


# 觉醒之抉择
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

# 神光冲击
class skill7(破晓女神主动技能):
    名称 = '神光冲击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1596.7
    成长 = 180.3
    CD = 4
    TP成长 = 0.10
    TP上限 = 5

# 神光连斩
class skill8(破晓女神主动技能):
    名称 = '神光连斩'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 2109.7
    成长 = 238.3
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

# 圣盾突击
class skill9(破晓女神主动技能):
    名称 = '圣盾突击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2756.7
    成长 = 311.3
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


# 神光喷涌
class skill10(破晓女神主动技能):
    名称 = '神光喷涌'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4451.9
    成长 = 503.1
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 神光盾击
class skill11(破晓女神主动技能):
    名称 = '神光盾击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4908.2
    成长 = 554.8
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 烈光
class skill12(破晓女神主动技能):
    名称 = '烈光'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4966.2
    成长 = 560.8
    CD = 8
    TP成长 = 0.10
    TP上限 = 5

# 神光闪耀
class skill13(破晓女神主动技能):
    名称 = '神光闪耀'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 7816.3
    成长 = 882.7
    CD = 16
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 2

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.09

# 神光闪影击
class skill14(破晓女神主动技能):
    名称 = '神光闪影击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 10235.5
    成长 = 1155.5
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


# 神罚之锤
class skill15(破晓女神主动技能):
    名称 = '神罚之锤'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 11383.6
    成长 = 1285.4
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.27
        elif x == 1:
            self.倍率 *= 1.27 + 0.09


# 神光之跃
class skill16(破晓女神主动技能):
    名称 = '神光之跃'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 19198.4
    成长 = 2167.6
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.08


# 一觉
class skill17(破晓女神主动技能):
    名称 = '信仰聚合神光惩戒'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 46241.6
    成长 = 13959.2
    CD = 152.3


# 圣盾裁决
class skill18(破晓女神主动技能):
    名称 = '圣盾裁决'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 14912.3
    成长 = 1683.7
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.24 + 0.08

# 破晓之光
class skill19(破晓女神主动技能):
    名称 = '破晓之光'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 29092.3
    成长 = 3284.7
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.11
        self.CD *= 0.90

# 神光回旋斩
class skill20(破晓女神主动技能):
    名称 = '神光回旋斩'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 46139.6
    成长 = 5209.4
    CD = 40
    是否有护石 = 1

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
           self.倍率 *= 1.368

# 神圣信约
class skill21(破晓女神主动技能):
    名称 = '神圣信约'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 50250.4
    成长 = 5673.6
    CD = 45
    是否有护石 = 1

    护石选项 = ['圣痕','（蓄力）']
    def 装备护石(self, x):
        if x == 0:
           self.倍率 *= 1.18 + 0.14
        elif x == 1:
           self.倍率 *= 1.32 * (11+0.23)/11

# 二觉
class skill22(破晓女神主动技能):
    名称 = '神圣意志大天使降临'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 106483
    成长 = 32147
    CD = 189

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

破晓女神护石选项 = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        破晓女神护石选项.append(i.名称)

破晓女神符文选项 = ['无']
for i in skill_list:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        破晓女神符文选项.append(i.名称)


class character(py.lite.char_base):
    def 角色賦予(self):
        self.attr["实际名称"] = '破晓女神'
        self.attr["角色"] = '守护者'
        self.attr["职业"] = '帕拉丁'

        self.attr["武器选项"] = ['太刀', '短剑', '巨剑', '钝器']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '板甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 1.89

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [10, 10, 20, 11, 4, 1, 2, 1, 1, 1, 1, 38, 38, 36, 36, 33, 31, 12, 16, 18, 16, 13, 5]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 5, 5, 0, 0, 5, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '', '', '', '', '', '', '1', '0', '0', '0', '/CD', '/CD', '/CD', '0', '/CD', '1', '1', '/CD', '1', '1', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '骚动的冥焰']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "钝器"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "天使光翼"
        self.attr["右槽白金技能"] = "天使光翼"
        self.attr["时装上衣技能"] = "天使光翼"

        self.attr["三觉技能选择"] = "二觉序号"

    def 三觉技能选择(self):
        for i, 技能 in enumerate(self.attr["技能栏"]):
            if 技能.名称 == "觉醒之抉择":
                技能.关联技能 = [self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].名称]
