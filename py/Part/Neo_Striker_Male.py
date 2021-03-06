from py.base_char import *
import py.lite
from py.base_equip import 武器冷却惩罚


class 觉醒技能(主动技能):
    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / 0.9 * 0.85 / self.恢复 * 武器冷却惩罚(武器类型, 输出类型, self.版本), 1)


# CDR: 拳套精通(10%) + 烈焰焚步(15%)
# 不包含觉醒
class 拳套精通(主动技能):
    def 等效CD(self, 武器类型, 输出类型):
        if 武器类型 == '拳套':
            return round(self.CD / 0.9 * 0.9 * 0.85 / self.恢复 * 武器冷却惩罚(武器类型, 输出类型, self.版本), 1)
        if 武器类型 == '臂铠':
            return round(self.CD / 0.9 * 0.85 / self.恢复 * 武器冷却惩罚(武器类型, 输出类型, self.版本), 1)


class skill0(拳套精通):
    名称 = '下段踢'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 737.65306122449
    成长 = 83.3469387755102
    CD = 1.8
    TP成长 = 0.08
    TP上限 = 5


class skill1(拳套精通):
    名称 = '碎骨'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3004.85
    成长 = 339.15
    CD = 6.3
    TP成长 = 0.08
    TP上限 = 5


class skill2(拳套精通):
    名称 = '铁山靠'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2892.2
    成长 = 326.8
    CD = 6.3
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
        else:
            return round(1.125 + 0.015 * self.等级, 5)


class skill4(拳套精通):
    名称 = '闪击快打'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 4565.54054054054
    成长 = 515.459459459459
    CD = 10.8
    TP成长 = 0.1
    TP上限 = 5


class skill5(拳套精通):
    名称 = '冲膝'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 6663.62857142857
    成长 = 752.371428571429
    CD = 13.5
    TP成长 = 0.1
    TP上限 = 5


class skill6(拳套精通):
    名称 = '炽焰旋风腿'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 8101.2
    成长 = 915.8
    CD = 18
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.28718046004268
        elif x == 1:
            self.倍率 *= 1.41682229824914


class skill7(拳套精通):
    名称 = '闪电之舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 7933.9375
    成长 = 896.0625
    CD = 18
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.24 + 0.09


class skill8(拳套精通):
    名称 = '瞬影连环踢'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 15717.3
    成长 = 1774.7
    CD = 40.5
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.23 + 0.08


class skill9(被动技能):
    名称 = '烈焰燃烧'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.01 * self.等级, 5)

    # 仅作用于面板显示
    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.03 + 0.01 * self.等级, 5)


# 不适用拳套掌握CDR
class skill10(觉醒技能):
    名称 = '烈焰焚步'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 31307
    成长 = 9452
    CD = 130.5
    关联技能 = ['所有']

    # 手搓 -5% CD
    def 等效CD(self, 武器类型, 输出类型):
        if 武器类型 == '拳套':
            return round(self.CD / self.恢复 * (1 - 0.05), 1)

    # 被动技能攻击力加成
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.02 + 0.04 * (self.等级 - 1), 5)


class skill11(拳套精通):
    名称 = '飞燕旋风'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 13039.6363636364
    成长 = 1472.36363636364
    CD = 27
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.224166749577
        elif x == 1:
            self.倍率 *= 1.313739926375


# 碎心修炼场实测有伤害丢失的BUG
class skill12(拳套精通):
    名称 = '旋风碎心踢'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 23332.9411764706
    成长 = 2635.05882352941
    CD = 45
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.16
        elif x == 1:
            self.倍率 *= 1.16 + 0.08


class skill13(被动技能):
    名称 = '烈火支配'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)


class skill14(拳套精通):
    名称 = '烈火强踢'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 38181.3333333333
    成长 = 4310.66666666667
    CD = 40.5
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35


class skill15(拳套精通):
    名称 = '烈火强拳'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 47826.3333333333
    成长 = 5399.66666666667
    CD = 49.5
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35


# 不适用拳套掌握CDR
class skill16(觉醒技能):
    名称 = '极武霸皇踢'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 82676.3333333337
    成长 = 24957.3333333333
    CD = 162


class skill17(被动技能):
    名称 = '千锤百炼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill18(拳套精通):
    名称 = '炼狱坠星腿'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 79841.4
    成长 = 9014.6
    CD = 54


# 不适用拳套掌握CDR
class skill19(觉醒技能):
    名称 = '焚火逐日拳'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 251118.333333333
    成长 = 75810.6666666667
    CD = 261
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
        self.attr["实际名称"] = '归元_散打_男'
        self.attr["角色"] = '格斗家(男)'
        self.attr["职业"] = '散打'

        self.attr["武器选项"] = ['拳套', '臂铠']

        self.attr["类型"] = '物理百分比'
        self.attr["防具类型"] = '轻甲'
        self.attr["防具精通属性"] = ['力量']

        self.attr["主BUFF"] = 2.04

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

        self.attr["二挡关联"] = "二挡：瞬影连环踢"

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [50, 41, 41, 5, 0, 36, 1, 33, 31, 20, 12, 23, 18, 11, 16, 13, 5, 4, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 5, 0, 0, 5, 0, 1, 5, 0, 0, 5, 5, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['0', '4', '4', '', '0', '2', '0', '2', '1', '', '1', '2', '1', '', '1', '1', '1', '', '1', '1']
        self.attr["技能宠物次数"] = [0, 2, 2, 0, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '幻光绽放拳套']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "拳套"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "柔化肌肉"
        self.attr["右槽白金技能"] = "柔化肌肉"
        self.attr["时装上衣技能"] = "烈焰焚步"

        self.attr["三觉技能选择"] = "二觉序号"

        self.attr["护石栏"] = ["瞬影连环踢", "旋风碎心踢", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["瞬影连环踢", "瞬影连环踢", "瞬影连环踢", "瞬影连环踢", "瞬影连环踢", "瞬影连环踢", "无", "无", "无"]
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

    def 面板物理攻击力(self):
        面板物理攻击 = (self.attr["物理攻击力"] + self.attr["进图物理攻击力"])
        武器类型 = self.attr["武器类型"]

        for i in self.attr["技能栏"]:
            try:
                面板物理攻击 *= i.物理攻击力倍率(武器类型)
            except:
                pass
        # 武极48级被动的运算取整必须在其他物攻提升率之前
        面板物理攻击 = int(面板物理攻击) * (1 + self.attr["百分比三攻"]) * 1.22
        return 面板物理攻击

    def 站街物理攻击力(self):
        站街物理攻击 = self.attr["物理攻击力"]
        武器类型 = self.attr["武器类型"]

        for i in self.attr["技能栏"]:
            try:
                站街物理攻击 *= i.物理攻击力倍率(武器类型)
            except:
                pass
        站街物理攻击 = int(站街物理攻击)
        return 站街物理攻击

    def 希洛克属性计算(self):
        pass
        # TODO

    def 计算伤害(self):
        self.预处理()
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算()
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        # 整合二挡伤害
        总伤害 = 0
        二挡关联 = self.attr["二挡关联"]
        for i in self.attr["技能栏"]:
            if 二挡关联 != '无':
                if (i.名称 == '瞬影连环踢' and 二挡关联 == '二挡：瞬影连环踢') or (i.名称 == '烈火强拳' and 二挡关联 == '二挡：烈火强拳') or (i.名称 == '炼狱坠星腿' and 二挡关联 == '二挡：炼狱坠星腿'):
                    技能总伤害[skill_sn[i.名称]] += 技能总伤害[skill_sn['烈焰焚步']]
                    技能总伤害[skill_sn['烈焰焚步']] *= 0

            if i.名称 != '烈焰焚步':
                总伤害 += 技能总伤害[skill_sn[i.名称]]

        # 返回结果
        return sum(技能总伤害)
