from py.base_char import *
import py.lite


class 归元_街霸_男主动技能(主动技能):
    中毒基础 = 0
    中毒成长 = 0
    中毒倍率 = 1
    出血基础 = 0
    出血成长 = 0
    出血倍率 = 1
    灼伤基础 = 0
    灼伤成长 = 0
    灼伤倍率 = 1
    感电基础 = 0
    感电成长 = 0
    感电倍率 = 1
    基础2 = 0
    成长2 = 0
    攻击次数2 = 0

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级)
                        + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级)
                        + self.中毒倍率 * (self.中毒基础 + self.中毒成长 * self.等级)
                        + self.出血倍率 * (self.出血基础 + self.出血成长 * self.等级)
                        + self.灼伤倍率 * (self.灼伤基础 + self.灼伤成长 * self.等级)
                        + self.感电倍率 * (self.感电基础 + self.感电成长 * self.等级))
                       * (1 + self.TP成长 * self.TP等级) * self.倍率)

    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / self.恢复, 1)


class skill0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['罗网投掷']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)


class skill1(归元_街霸_男主动技能):
    名称 = '抛沙'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 751
    成长 = 108
    倍率 = 1.5  # 后街战术
    CD = 3.1
    TP成长 = 0.08
    TP上限 = 5


class skill2(归元_街霸_男主动技能):
    名称 = '毒瓶投掷'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 31
    基础 = 228 * 1.6  # 后街，下同
    成长 = 54 * 1.6
    中毒基础 = 232
    中毒成长 = 57
    灼烧基础 = 232
    灼烧成长 = 57
    CD = 2.0
    TP成长 = 0.10
    TP上限 = 5


class skill3(归元_街霸_男主动技能):
    名称 = '擒月炎'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 2003
    成长 = 216
    CD = 5.8
    TP成长 = 0.10
    TP上限 = 5


class skill4(被动技能):
    名称 = '爪精通'
    所在等级 = 25
    等级上限 = 30
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        return (1.31 + (self.等级 - 20) * 0.02) if self.等级 >= 20 else (1.11 + self.等级 * 0.01)

    def 物理攻击力倍率(self, 武器类型):
        return (1.31 + (self.等级 - 20) * 0.02) if self.等级 >= 20 else (1.11 + self.等级 * 0.01)

    def 魔法攻击力倍率(self, 武器类型):
        return (1.31 + (self.等级 - 20) * 0.02) if self.等级 >= 20 else (1.11 + self.等级 * 0.01)


class skill5(归元_街霸_男主动技能):
    名称 = '毒针投掷'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 303 * 1.9  # 后街，下同
    成长 = 29 * 1.9
    感电基础 = 236
    感电成长 = 26
    CD = 3
    TP成长 = 0.10
    TP上限 = 5


class skill6(归元_街霸_男主动技能):
    名称 = '砖块投掷'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 1200
    成长 = 126
    基础2 = 1972
    成长2 = 228
    倍率 = 1.6  # 后街战术
    CD = 4.0
    TP成长 = 0.10
    TP上限 = 5


class skill7(归元_街霸_男主动技能):
    名称 = '伏虎霸王拳'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 1200
    成长 = 128
    倍率 = 1.6  # 异常状态
    CD = 15.7
    TP成长 = 0.10
    TP上限 = 5


class skill8(归元_街霸_男主动技能):
    名称 = '挑衅'
    所在等级 = 35
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 5)


class skill9(归元_街霸_男主动技能):
    名称 = '螺旋滑铲'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    倍率 = 1.2  # 无法抓取
    基础 = 2758
    成长 = 318
    攻击次数 = 3
    CD = 21
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 1
            self.倍率 *= 3.62
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数 = 1
            self.倍率 *= 3.89
            self.CD *= 0.9


class skill10(归元_街霸_男主动技能):
    名称 = '罗网投掷'
    所在等级 = 35
    等级上限 = 11
    基础等级 = 1
    基础 = 1381
    成长 = 159
    CD = 15
    TP成长 = 0.10
    TP上限 = 3


class skill11(归元_街霸_男主动技能):
    名称 = '毒雷引爆'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 6823
    成长 = 775
    攻击次数 = 1
    基础2 = 3535
    成长2 = 393
    攻击次数2 = 1
    中毒基础 = 1682
    中毒成长 = 196
    CD = 25.2
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础2 = 0
            self.成长2 = 0
            self.倍率 *= 3
            self.基础 *= 0.52
            self.成长 *= 0.52
            self.中毒基础 *= 0.87
            self.中毒成长 *= 0.87
        elif x == 1:
            self.基础2 = 0
            self.成长2 = 0
            self.倍率 *= 3
            self.基础 *= 0.52
            self.成长 *= 0.52
            self.中毒基础 *= 1.08
            self.中毒成长 *= 1.08


class skill12(被动技能):
    名称 = '狂·霸王拳'
    所在等级 = 40
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['伏虎霸王拳']

    def 加成倍率(self, 武器类型):
        return 1.0

    def 技能加成倍率(self, 武器类型):
        return round(5.18 + 0.12 * self.等级, 5)


class skill13(归元_街霸_男主动技能):
    名称 = '血色风暴'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 8800
    成长 = 990
    出血基础 = 8800
    出血成长 = 990
    CD = 47.2
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.199
        elif x == 1:
            self.倍率 *= 1.276


class skill14(被动技能):
    名称 = '千手奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['血色风暴', '天崩地裂', '爆破污桶', '千锁乱舞']
    关联技能2 = ['抛沙', '毒瓶投掷', '毒针投掷', '擒月炎', '砖块投掷', '罗网投掷', '螺旋滑铲', '伏虎霸王拳', '毒雷引爆', '暗街夺命锁', '飞沙走石', '燃火轰天炮', '逆道·爆狱', '逆道·幽链之界']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.065 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.92 + 0.02 * self.等级, 5)


class skill15(归元_街霸_男主动技能):
    名称 = '天崩地裂'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 35891
    成长 = 10833
    灼烧基础 = 372
    灼伤成长 = 111.5
    中毒基础 = 372
    中毒成长 = 111.5
    出血基础 = 372
    出血成长 = 111.5
    CD = 152.3


class skill16(归元_街霸_男主动技能):
    名称 = '爆破污桶'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 10613
    成长 = 1197
    基础2 = 13827
    成长2 = 1558
    CD = 21
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.32


class skill17(归元_街霸_男主动技能):
    名称 = '千锁乱舞'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 11905
    成长 = 1340
    出血基础 = 11905
    出血成长 = 1340
    CD = 52.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
            self.CD *= 0.91
        elif x == 1:
            self.倍率 *= 1.2 * 1.07
            self.CD *= 0.91


class skill18(被动技能):
    名称 = '诡诈之道'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill19(归元_街霸_男主动技能):
    名称 = '暗街夺命锁'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 33880
    成长 = 3820
    出血基础 = 8703
    出血成长 = 985
    CD = 42.8
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.32


class skill20(归元_街霸_男主动技能):
    名称 = '飞沙走石'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 1427
    成长 = 161
    攻击次数 = 10
    基础2 = 8471
    成长2 = 956
    攻击次数2 = 2
    出血基础 = 13355
    出血成长 = 1511
    CD = 45
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.攻击次数 = 0
        self.攻击次数2 *= 2.8
        self.CD *= 0.9


class skill21(归元_街霸_男主动技能):
    名称 = '燃火轰天炮'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 109499.32
    成长 = 33063.86
    CD = 180.0


class skill22(被动技能):
    名称 = '逆道·皆允'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill23(归元_街霸_男主动技能):
    名称 = '逆道·爆狱'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 82114
    成长 = 9273
    攻击次数 = 1
    基础2 = 85125
    成长2 = 9610
    攻击次数2 = 0
    CD = 60.0


class skill24(归元_街霸_男主动技能):
    名称 = '逆道·幽链之界'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 276929
    成长 = 83592
    出血基础 = 2854
    出血成长 = 862
    中毒基础 = 2854
    中毒成长 = 862
    灼伤基础 = 2854
    灼伤成长 = 862
    CD = 290
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
        self.attr["实际名称"] = '归元_街霸_男'
        self.attr["角色"] = '格斗家(男)'
        self.attr["职业"] = '街霸'

        self.attr["武器选项"] = ['爪']

        self.attr["类型"] = '魔法百分比'
        self.attr["防具类型"] = '重甲'
        self.attr["防具精通属性"] = ['智力']

        self.attr["主BUFF"] = 1.79

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

        self.attr["远古记忆"] = 10

        self.attr["毒瓶强化"] = 0
        self.attr["毒针强化"] = 0
        self.attr["砖块强化"] = 0
        self.attr["污桶强化"] = 1
        self.attr["爆狱强化"] = 1

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [100, 46, 31, 43, 20, 41, 38, 38, 10, 36, 1, 33, 1, 31, 20, 12, 23, 18, 11, 16, 13, 5, 4, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 5, 0, 5, 0, 1, 0, 5, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '0', '0', '0', '', '0', '0', '/CD', '', '/CD', '/CD', '/CD', '', '/CD', '', '/CD', '/CD', '/CD', '', '/CD', '/CD', '/CD', '', '/CD', '/CD']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '痛苦之源']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "爪"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "爪精通"
        self.attr["右槽白金技能"] = "爪精通"
        self.attr["时装上衣技能"] = "诡诈之道"

        self.attr["三觉技能选择"] = "一觉序号"

        self.attr["护石栏"] = ["血色风暴", "螺旋滑铲", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["血色风暴", "血色风暴", "血色风暴", "血色风暴", "血色风暴", "血色风暴", "无", "无", "无"]
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

    def 技能等级初始化(self):
        super().技能等级初始化()
        技能栏 = self.attr["技能栏"]

        if self.attr["毒瓶强化"] == 1:
            技能栏[skill_sn['毒瓶投掷']].基础 = 0
            技能栏[skill_sn['毒瓶投掷']].成长 = 0
            技能栏[skill_sn['毒瓶投掷']].中毒基础 = 1034
            技能栏[skill_sn['毒瓶投掷']].中毒成长 = 184
            技能栏[skill_sn['毒瓶投掷']].灼烧基础 = 1034
            技能栏[skill_sn['毒瓶投掷']].灼烧成长 = 184
        if self.attr["毒针强化"] == 1:
            技能栏[skill_sn['毒针投掷']].基础 = 976
            技能栏[skill_sn['毒针投掷']].成长 = 92
            技能栏[skill_sn['毒针投掷']].出血基础 = 1276
            技能栏[skill_sn['毒针投掷']].出血成长 = 144
            技能栏[skill_sn['毒针投掷']].感电基础 = 0
            技能栏[skill_sn['毒针投掷']].感电成长 = 0
        if self.attr["砖块强化"] == 1:
            技能栏[skill_sn['砖块投掷']].攻击次数 = 0
            技能栏[skill_sn['砖块投掷']].攻击次数2 = 1
            技能栏[skill_sn['砖块投掷']].倍率 = 1
        if self.attr["污桶强化"] == 1:
            技能栏[skill_sn['爆破污桶']].攻击次数 = 0
            技能栏[skill_sn['爆破污桶']].攻击次数2 = 1
        if self.attr["爆狱强化"] == 1:
            技能栏[skill_sn['逆道·爆狱']].攻击次数 = 0
            技能栏[skill_sn['逆道·爆狱']].攻击次数2 = 1
            技能栏[skill_sn['逆道·爆狱']].灼伤基础 = 1889 * 5
            技能栏[skill_sn['逆道·爆狱']].灼伤成长 = 214 * 5

    def 计算伤害(self):
        self.预处理()
        # 初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算()
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        技能栏 = self.attr["技能栏"]
        武器类型 = self.attr["武器类型"]

        # 霸王拳
        if 技能栏[skill_sn['狂·霸王拳']].等级 != 0:
            if 技能总伤害[skill_sn['伏虎霸王拳']] != 0:
                temp = 技能总伤害[skill_sn['伏虎霸王拳']] * 技能栏[skill_sn['狂·霸王拳']].技能加成倍率(武器类型)
                if self.is_equip_exist('奔流不息之狂风'):
                    temp = temp / 0.7
                if self.is_equip_exist('奔流不息之伽蓝'):
                    temp *= 0.7
                技能总伤害[skill_sn['伏虎霸王拳']] += temp

        # 返回结果
        return sum(技能总伤害)