from py.base_char import *
import py.lite


class 主动技能(主动技能):
    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / self.恢复, 1)


class skill0(主动技能):
    名称 = '致命射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1044.9
    成长 = 118.1
    攻击次数 = 1
    CD = 6.9
    TP成长 = 0.1
    TP上限 = 7


class skill1(被动技能):
    名称 = '左轮奥义'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 10:
            return round(1.1 + 0.01 * self.等级, 5)
        else:
            return round(1.2 + 0.02 * (self.等级 - 10), 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class skill2(被动技能):
    名称 = '花式枪术'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)


class skill3(主动技能):
    名称 = '三连发'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 475.2
    成长 = 53.8
    基础2 = 951.5
    成长2 = 107.5
    攻击次数2 = 2
    基础3 = 2380.3
    成长3 = 268.7
    攻击次数3 = 1
    CD = 8.0
    TP成长 = 0.1
    TP上限 = 7


class skill4(主动技能):
    名称 = '致命回射'
    所在等级 = 30
    等级上限 = 1
    基础等级 = 1
    CD = 8.7


class skill5(主动技能):
    名称 = '乱射'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 441.11
    成长 = 49.89
    攻击次数 = 20
    CD = 17.6
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 1.14
            self.成长 *= 1.14
            self.攻击次数 = 22
        elif x == 1:
            self.基础 *= 1.14 + 0.08
            self.成长 *= 1.14 + 0.08
            self.攻击次数 = 22


class skill6(主动技能):
    名称 = '移动射击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 404.3
    成长 = 45.7
    攻击次数 = 30
    CD = 24.3
    TP成长 = 0.10
    TP上限 = 7


class skill7(主动技能):
    名称 = '多重射击'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1998.3
    成长 = 225.7
    攻击次数 = 5
    CD = 19.8
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础 *= 6.1
            self.成长 *= 6.1
            self.攻击次数 = 1
        elif x == 1:
            self.基础 *= 6.1 + 0.45
            self.成长 *= 6.1 + 0.45
            self.攻击次数 = 1


class skill8(主动技能):
    名称 = '双鹰回旋'
    备注 = '(20/24/37 & 34/54)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 460.85
    成长 = 52.15
    基础2 = 531
    成长2 = 53.9
    基础3 = 558
    成长3 = 56.6
    攻击次数 = 16
    攻击次数2 = 18
    攻击次数3 = 29
    攻击间隔 = 1
    CD = 44.6
    TP成长 = 0.05
    TP基础 = 5
    TP上限 = 7
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        攻击次数 = int((self.攻击次数 + (4 / 5) * self.TP等级) / self.攻击间隔)
        攻击次数2 = int((self.攻击次数2 + (6 / 5) * self.TP等级) / self.攻击间隔)
        攻击次数3 = int((self.攻击次数3 + (8 / 5) * self.TP等级) / self.攻击间隔)

        if self.等级 == 0:
            return 0
        else:
            return int((攻击次数 * (self.基础 + self.成长 * self.等级) + 攻击次数2 * (
                    self.基础2 + self.成长2 * self.等级) + 攻击次数3 * (
                                self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.09  # COLG百科
            # self.攻击间隔 = 0.7
            # self.攻击次数 = 0
            # self.基础2 *= 1.08
            # self.成长2 *= 1.08
        elif x == 1:
            self.倍率 *= 1.09 + 0.07  # COLG百科
            # self.攻击间隔 = 0.7
            # self.攻击次数 = 0
            # self.基础2 *= 1.08
            # self.成长2 *= 1.08


class skill9(被动技能):
    名称 = '死亡印记'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class skill10(主动技能):
    名称 = '疯狂屠戮'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 456.4
    成长 = 155.3
    基础2 = 422.6
    成长2 = 127.7
    基础3 = 787.2
    成长3 = 214.4
    攻击次数 = 3
    攻击次数2 = 70
    攻击次数3 = 25
    CD = 145


class skill11(主动技能):
    名称 = '死亡突袭'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 6046.3
    成长 = 682.7
    攻击次数 = 3
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.22
            self.CD *= 0.90
        elif x == 1:
            self.倍率 *= 1.22 + 0.09
            self.CD *= 0.90


class skill12(主动技能):
    名称 = '压制射击'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 1378.5
    成长 = 155.5
    基础2 = 3061.2
    成长2 = 345.8
    攻击次数 = 20
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 7
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 24
            self.基础2 *= 1.52
            self.成长2 *= 1.52
        elif x == 1:
            self.攻击次数 = 24
            self.基础2 *= 1.52 + 0.9
            self.成长2 *= 1.52 + 0.9


class skill13(被动技能):
    名称 = '射击掌握'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能2 = ['致命射击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round((1.305 + 0.045 * self.等级) / (1.22 + 0.02 * self.等级), 5)


class skill14(主动技能):
    名称 = '疾风骤雨'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 2059.4 / 1.126 * 1.136
    成长 = 232.6 / 1.126 * 1.136
    攻击次数 = 24
    CD = 40.0
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.36275


class skill15(主动技能):
    名称 = '抹杀'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 6679.7
    成长 = 754.3
    攻击次数 = 7
    CD = 45.0
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3338


class skill16(主动技能):
    名称 = '第七翼动'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 5112.2
    成长 = 1543.8
    基础2 = 28489.4
    成长2 = 8600.6
    攻击次数 = 13
    攻击次数2 = 1
    CD = 180


class skill17(被动技能):
    名称 = '卓尔不群'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill18(主动技能):
    名称 = '爆燃突击'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 9325.5
    成长 = 1053.5
    基础2 = 37304.4
    成长2 = 4212.2
    攻击次数 = 6
    攻击次数2 = 1
    CD = 60


class skill19(主动技能):
    名称 = '鹰眸·致命危机'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 271532
    成长 = 81964
    CD = 290

    def 加成倍率(self, 武器类型):
        return 0.0


class skill20(主动技能):
    名称 = '烟尘弹'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 342.4
    成长 = 38.6
    攻击次数 = 6
    CD = 6
    TP成长 = 0.08
    TP上限 = 7


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
        self.attr["实际名称"] = '重霄_漫游枪手_男'
        self.attr["角色"] = '神枪手(男)'
        self.attr["职业"] = '漫游枪手'

        self.attr["武器选项"] = ['左轮枪']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '皮甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 2.25

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [46, 10, 10, 38, 1, 36, 0, 33, 31, 20, 12, 23, 18, 11, 16, 13, 6, 4, 6, 2, 48]
        self.attr["技能TP等级"] = [1, 0, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['3', '', '', '3', '3', '2', '0', '2', '1', '', '1', '0', '1', '', '1', '1', '1', '', '1', '1', '0']
        self.attr["技能宠物次数"] = [1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '血枪之脉']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "左轮枪"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "花式枪术"
        self.attr["右槽白金技能"] = "花式枪术"
        self.attr["时装上衣技能"] = "花式枪术"

        self.attr["三觉技能选择"] = "二觉序号"

        self.attr["护石栏"] = ["双鹰回旋", "多重射击", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["双鹰回旋", "双鹰回旋", "双鹰回旋", "双鹰回旋", "双鹰回旋", "双鹰回旋", "无", "无", "无"]
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
        技能栏[skill_sn['致命回射']].基础 = 技能栏[skill_sn['致命射击']].等效百分比(self.attr["武器类型"]) * 1.5
        技能栏[skill_sn['致命回射']].被动倍率 = 技能栏[skill_sn['致命射击']].被动倍率
