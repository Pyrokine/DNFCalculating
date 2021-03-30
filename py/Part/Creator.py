from py.base_char import *
import py.lite


class skill0(主动技能):
    名称 = '烈火燎原'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 420.0 / 70
    成长 = 280.0 / 70
    能量 = 140
    最小值 = 2
    CD = 5.0
    持续秒数 = 6.0
    TP成长 = 0.08
    TP上限 = 5
    硬直时长百分比 = 0

    def 觉醒模式(self, x):
        if x == 1:
            self.最小值 = 70
            self.基础 = self.基础 * 70 / 2
            self.成长 = self.成长 * 70 / 2


class skill1(主动技能):
    名称 = '炽炎星陨'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 119.0 / 7
    成长 = 252.0 / 7
    能量 = 140
    最小值 = 20
    CD = 5.0
    持续秒数 = 1.0
    TP成长 = 0.08
    TP上限 = 5
    硬直时长百分比 = 0

    def 觉醒模式(self, x):
        if x == 1:
            self.最小值 = 70
            self.基础 = self.基础 * 70 / 20
            self.成长 = self.成长 * 70 / 20


class skill2(主动技能):
    名称 = '冰霜之球'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 2960.0 / 7
    成长 = 400.0 / 7
    能量 = 140
    最小值 = 20
    CD = 10.0
    持续秒数 = 3.0
    TP成长 = 0.08
    TP上限 = 5
    硬直时长百分比 = 0

    def 觉醒模式(self, x):
        if x == 1:
            self.最小值 = 70
            self.基础 = self.基础 * 70 / 20
            self.成长 = self.成长 * 70 / 20


class skill3(主动技能):
    名称 = '冰天震地'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 2359.0 / 3
    成长 = 378.0 / 3
    能量 = 140
    最小值 = 40
    CD = 10.0
    持续秒数 = 1.0
    TP成长 = 0.08
    TP上限 = 5
    硬直时长百分比 = 0

    def 觉醒模式(self, x):
        if x == 1:
            self.最小值 = 140
            self.基础 = self.基础 * 140 / 40
            self.成长 = self.成长 * 140 / 40


class skill4(被动技能):
    名称 = '幻想之境'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        elif self.等级 <= 10:
            return round(1 + 0.01 * self.等级, 5)
        else:
            return round(1.1 + 0.015 * (self.等级 - 10), 5)

    def 独立攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class skill5(被动技能):
    名称 = '具象强化'
    所在等级 = 25
    等级上限 = 40
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.025 * self.等级, 5)


class skill6(主动技能):
    名称 = '烈焰飓风'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4560
    成长 = 504
    能量 = 140
    最小值 = 60
    CD = 20
    持续秒数 = 4.0
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0.05
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.倍率 *= 1.0
        elif x == 1:
            self.CD *= 0.85
            self.倍率 *= 1.09


class skill7(主动技能):
    名称 = '极冰护盾'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2342.0
    成长 = 261.0
    CD = 20.0
    持续秒数 = 1.0
    能量 = 140
    最小值 = 60
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0.1


class skill8(主动技能):
    名称 = '超能旋风波'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 9962.0 / 35
    成长 = 1190.0 / 35
    CD = 25.0
    持续秒数 = 5.0
    能量 = 140
    最小值 = 4
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.32

    def 觉醒模式(self, x):
        if x == 1:
            self.最小值 = 46
            self.基础 = self.基础 * 46 / 4
            self.成长 = self.成长 * 46 / 4


class skill9(主动技能):
    名称 = '风暴漩涡'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 9100.0 / 7
    成长 = 1015.0 / 7
    能量 = 140
    最小值 = 20
    CD = 25.0
    持续秒数 = 5.0
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.倍率 *= 1.22

    def 觉醒模式(self, x):
        if x == 1:
            self.最小值 = 70
            self.基础 = self.基础 * 70 / 20
            self.成长 = self.成长 * 70 / 20


class skill10(被动技能):
    名称 = '洞悉'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class skill11(主动技能):
    名称 = '末日虫洞'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 19
    基础 = 11434.00
    成长 = 2168.0
    CD = 45.0
    持续秒数 = 3.0
    能量 = 100
    最小值 = 100
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
        elif x == 1:
            self.倍率 *= 1.28


class skill12(主动技能):
    名称 = '冰雪降临'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 16
    基础 = 24544.8 / 2
    成长 = 4586.4 / 2
    CD = 31.5
    持续秒数 = 3.0
    能量 = 100
    最小值 = 50
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.最小值 = 2
            self.基础 = self.基础 / 25 * 1.28
            self.成长 = self.成长 / 25 * 1.28
            self.持续秒数 = 0.5
            self.硬直时长百分比 = 0.15
        elif x == 1:
            self.最小值 = 2
            self.基础 = self.基础 / 25 * 1.37
            self.成长 = self.成长 / 25 * 1.37
            self.持续秒数 = 0.5
            self.硬直时长百分比 = 0.15


class skill13(主动技能):
    名称 = '时空链接'
    所在等级 = 70
    等级上限 = 60
    基础等级 = 18
    基础 = 49744.72 / 2
    成长 = 5709.96 / 2
    CD = 54
    持续秒数 = 5.0
    能量 = 100
    最小值 = 50
    TP成长 = 0.10
    TP上限 = 5
    硬直时长百分比 = 0.05
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.32


class skill14(被动技能):
    名称 = '创世之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class skill15(主动技能):
    名称 = '时空禁制'
    所在等级 = 80
    等级上限 = 60
    基础等级 = 9
    基础 = 35205.00
    成长 = 6797.00
    CD = 45.0
    持续秒数 = 7.0
    能量 = 100
    最小值 = 100
    硬直时长百分比 = 0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 0.5 * 2.74


class skill16(主动技能):
    名称 = '创世'
    备注 = '(直接爆炸)'
    所在等级 = 85
    等级上限 = 60
    基础等级 = 5
    基础 = 84924.00
    成长 = 25632.0
    CD = 180.0
    持续秒数 = 1.0
    能量 = 100
    最小值 = 100
    硬直时长百分比 = 0


class skill17(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill18(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class skill19(被动技能):
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


class skill20(被动技能):
    名称 = '自我觉醒'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.11

    def 独立攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.11


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

skill_sn_awaking1 = 16
skill_sn_awaking2 = 16
skill_sn_awaking3 = 19

option_talismans = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        option_talismans.append(i.名称)

option_rune = ['无']
for i in skill_list:
    if 1 <= i.所在等级 <= 75 and i.是否有伤害 == 1:
        option_rune.append(i.名称)


class character(py.lite.CharBase):
    def 角色賦予(self):
        self.attr["实际名称"] = '缔造者'
        self.attr["角色"] = '缔造者'
        self.attr["职业"] = '缔造者'

        self.attr["武器选项"] = ['魔杖', '法杖', '棍棒', '矛', '扫把']

        self.attr["类型"] = '魔法固伤'
        self.attr["防具类型"] = '板甲'
        self.attr["防具精通属性"] = ['智力']

        self.attr["主BUFF"] = 1.66

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

        self.attr["远古记忆"] = 10

        self.attr["数据精算模式"] = 1
        self.attr["觉醒模式"] = 1

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [50, 50, 48, 48, 10, 10, 38, 38, 33, 33, 20, 19, 16, 18, 11, 9, 5, 4, 1, 2, 1]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ["/CD", "/CD", "/CD", "/CD", "", "", "/CD", "/CD", "/CD", "/CD", "", "/CD", "/CD", "/CD", "", "/CD", "/CD", "", "", "", ""]
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 50, 2, 0, 1, 1, 0, 0, 0, 0]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '火焰地狱']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "魔杖"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 10]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "具象强化"
        self.attr["右槽白金技能"] = "具象强化"
        self.attr["时装上衣技能"] = "具象强化"

        self.attr["三觉技能选择"] = "二觉序号"

        self.attr["护石栏"] = ["时空链接", "冰雪降临", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["时空链接", "时空链接", "时空链接", "时空链接", "时空链接", "时空链接", "无", "无", "无"]
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
        for i, 技能 in enumerate(self.attr["技能栏"]):
            if 技能.名称 == "觉醒之抉择":
                技能.关联技能 = [self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].名称]

    def skill_level_up_batched(self, 加成类型, minLV, maxLV, LV):
        LV = int(LV)
        if self.attr["远古记忆"] > 0:
            if minLV <= 15 <= maxLV:
                self.attr["远古记忆"] = min(20, self.attr["远古记忆"] + LV)

        for i in self.attr["技能栏"]:
            if minLV <= i.所在等级 <= maxLV:
                if 加成类型 == '所有':
                    i.等级加成(LV)

    def 技能释放次数计算(self):
        技能释放次数 = []
        次数输入 = self.attr["技能释放次数"]
        时间输入 = self.attr["时间输入"]
        武器类型 = self.attr["武器类型"]
        类型 = self.attr["类型"]
        数据精算模式 = self.attr["数据精算模式"]
        觉醒模式 = self.attr["觉醒模式"]

        for i in self.attr["技能栏"]:
            modelchange = '觉醒模式' in dir(i)
            if modelchange and 觉醒模式 == 1:
                i.觉醒模式(1)

            if i.是否有伤害 == 1:
                if 次数输入[skill_sn[i.名称]] == '/CD':
                    余数伤害时间 = ((int(i.能量 * (1 + (时间输入 * (1 - i.硬直时长百分比)) / i.等效CD(武器类型, 类型))) - int(int(i.能量 * (1 + 时间输入 / i.等效CD(武器类型, 类型))) / i.最小值) * i.最小值) / i.能量) * i.等效CD(武器类型, 类型)
                    余数次数 = 0
                    if 余数伤害时间 < i.持续秒数:
                        if 余数伤害时间 < 0.5:
                            余数次数 = -1
                        else:
                            余数次数 = -1 + 余数伤害时间 / i.持续秒数
                    else:
                        余数次数 = 0

                    if 数据精算模式 == 1 and 时间输入 != 1:
                        技能释放次数.append(round(int(int(i.能量 * (1 + (时间输入 * (1 - i.硬直时长百分比)) / i.等效CD(武器类型, 类型))) / i.最小值) + 余数次数, 2))
                    else:
                        余数次数 = 0
                        技能释放次数.append(round(int(int(i.能量 * (1 + (时间输入 * (1 - i.硬直时长百分比)) / i.等效CD(武器类型, 类型))) / i.最小值) + 余数次数, 2))
                elif 次数输入[skill_sn[i.名称]] != '0':
                    技能释放次数.append(int(次数输入[skill_sn[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)

        return 技能释放次数
