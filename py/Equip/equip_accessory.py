from py.base_equip import *


# region  100SS首饰
class 装备180(装备):
    名称 = '莱多：变幻的规律'
    模式 = 0
    所属套装 = '上古尘封术士'
    等级 = 100
    品质 = '史诗'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 147
    智力 = 100
    体力 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.12
        character.attr["技能攻击力"] *= 1.2
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备181(装备):
    名称 = '拥抱晨曦之温暖'
    模式 = 0
    所属套装 = '破晓曦光'
    等级 = 100
    品质 = '史诗'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 147
    体力 = 117
    智力 = 100
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.06
        character.attr["技能攻击力"] *= 1.04 + 0.01 * min(13, character.fetch_strengthen_level(self.部位))
        character.attr["火属性强化"] += 28
        character.attr["冰属性强化"] += 28
        character.attr["光属性强化"] += 28
        character.attr["暗属性强化"] += 28

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 48, 1)
        character.skill_change_recovery(15, 30, 0.30)

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 48, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["BUFF"] += BUFF力量per=1.05)
        # character.attr["BUFF"] += BUFF智力per=1.05)
        pass


class 装备182(装备):
    名称 = '白象之庇护'
    模式 = 0
    所属套装 = '幸运三角'
    等级 = 100
    品质 = '史诗'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 147
    智力 = 100
    体力 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.07
        character.attr["伤害增加"] += 0.07
        character.attr["暴击伤害"] += 0.07
        character.attr["附加伤害"] += 0.07
        character.attr["技能攻击力"] *= 1.07

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=220)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备183(装备):
    名称 = '火魔之焰-沙罗曼达'
    模式 = 0
    所属套装 = '精灵使的权能'
    等级 = 100
    品质 = '史诗'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 147
    智力 = 100
    体力 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["火属性强化"] += 38
        character.attr["冰属性强化"] += 38
        character.attr["光属性强化"] += 38
        character.attr["暗属性强化"] += 38
        character.attr["附加伤害"] += 0.3

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=220)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备184(装备):
    名称 = '执着的探求'
    模式 = 0
    所属套装 = '黑魔法探求者'
    等级 = 100
    品质 = '史诗'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 147
    智力 = 100
    体力 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.28

    def 进图属性(self, character):
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=245)
        # character.attr["被动"] += 转职被动智力=270)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备185(装备):
    名称 = '时间指引之针'
    模式 = 0
    所属套装 = '时空旅行者'
    等级 = 100
    品质 = '史诗'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 147
    智力 = 100
    体力 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.2
        character.attr["技能攻击力"] *= 1.14
        character.skill_change_cooldown(50, 50, 0.10)
        character.skill_change_cooldown(85, 85, 0.10)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=242)
        # character.attr["BUFF"] += BUFF力量per=1.07)
        # character.attr["BUFF"] += BUFF智力per=1.07)
        pass


class 装备186(装备):
    名称 = '支配战场的呐喊'
    模式 = 0
    所属套装 = '穿透命运的呐喊'
    等级 = 100
    品质 = '史诗'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 147
    智力 = 100
    体力 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.12
        character.attr["最终伤害"] += 0.23

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=220)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备187(装备):
    名称 = '狂乱之坚如磐石'
    模式 = 0
    所属套装 = '狂乱追随者'
    等级 = 100
    品质 = '史诗'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 147
    智力 = 100
    体力 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.3
        character.attr["技能攻击力"] *= 1.11

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=220)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备188(装备):
    名称 = '莱多：秩序创造者'
    模式 = 0
    所属套装 = '上古尘封术士'
    等级 = 100
    品质 = '神话'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 149
    智力 = 100
    体力 = 120
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '百分比三攻：'
    属性1范围 = [3, 1, 1]
    属性1选择 = 0
    属性2描述 = '技能攻击力：'
    属性2范围 = [6, 1, 1]
    属性2选择 = 0
    属性3描述 = '暴击伤害：'
    属性3范围 = [9, 1, 1]
    属性3选择 = 0
    属性4描述 = '百分比力智：'
    属性4范围 = [6, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.06
        character.attr["百分比三攻"] += 0.03
        character.attr["暴击伤害"] += 0.09
        character.attr["附加伤害"] += 0.12
        character.attr["技能攻击力"] *= 1.20
        character.attr["技能攻击力"] *= 1.06
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.1
        character.attr["释放速度"] += 0.15
        # 专属属性

    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [60, 40, 10]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '转职被动：'
    属性2范围_BUFF = [200, 100, 20]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [9, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = 'BUFF三攻：'
    属性4范围_BUFF = [7, 2, 1]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智=60 - self.属性1选择_BUFF * 10)
        # character.attr["被动"] += 守护恩赐体精=200 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=200 - self.属性2选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智per=1.09 - self.属性3选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF物攻per=1.07 - self.属性4选择_BUFF / 100, BUFF魔攻per=1.07 - self.属性4选择_BUFF / 100, BUFF独立per=1.07 - self.属性4选择_BUFF / 100)
        pass


class 装备189(装备):
    名称 = '融化黑暗之温暖'
    模式 = 0
    所属套装 = '破晓曦光'
    等级 = 100
    品质 = '神话'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 149
    智力 = 100
    体力 = 120
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '物理/魔法/独立 +'
    属性1范围 = [110, 30, 10]
    属性1选择 = 0
    属性2描述 = '暴击伤害：'
    属性2范围 = [10, 1, 1]
    属性2选择 = 0
    属性3描述 = '伤害增加：'
    属性3范围 = [11, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.06
        character.attr["火属性强化"] += 28
        character.attr["冰属性强化"] += 28
        character.attr["光属性强化"] += 28
        character.attr["暗属性强化"] += 28
        character.attr["技能攻击力"] *= 1.04 + 0.01 * min(13, character.fetch_strengthen_level(self.部位))
        character.attr["物理攻击力"] += 110
        character.attr["魔法攻击力"] += 110
        character.attr["独立攻击力"] += 110
        character.attr["伤害增加"] += 0.11
        character.attr["暴击伤害"] += 0.1

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 48, 1)
        character.skill_change_recovery(15, 30, 0.30)

    def 其它属性(self, character):
        x = min(sum(character.attr["强化等级"]), 150) // 6
        character.attr["物理暴击率"] += 0.005 * x
        character.attr["魔法暴击率"] += 0.005 * x
        character.attr["攻击速度"] += 0.008 * x
        character.attr["移动速度"] += 0.008 * x
        character.attr["释放速度"] += 0.012 * x
        # 专属属性

    属性1描述_BUFF = 'BUFF三攻：'
    属性1范围_BUFF = [9, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [10, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF力智：'
    属性3范围_BUFF = [11, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 48, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["BUFF"] += BUFF力量per=1.05, BUFF智力per=1.05)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF物攻per=1.09 - self.属性1选择_BUFF / 100, BUFF魔攻per=1.09 - self.属性1选择_BUFF / 100, BUFF独立per=1.09 - self.属性1选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智per=1.10 - self.属性2选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF力量per=1.11 - self.属性3选择_BUFF / 100, BUFF智力per=1.11 - self.属性3选择_BUFF / 100)
        pass


class 装备190(装备):
    名称 = '伽内什的永恒庇护'
    模式 = 0
    所属套装 = '幸运三角'
    等级 = 100
    品质 = '神话'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 149
    智力 = 100
    体力 = 120
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '暴击伤害：'
    属性1范围 = [4, 1, 1]
    属性1选择 = 0
    属性2描述 = '百分比力智：'
    属性2范围 = [10, 1, 1]
    属性2选择 = 0
    属性3描述 = '伤害增加：'
    属性3范围 = [3, 1, 1]
    属性3选择 = 0
    属性4描述 = '百分比三攻：'
    属性4范围 = [8, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.07
        character.attr["技能攻击力"] *= 1.07
        character.attr["暴击伤害"] += 0.07
        character.attr["伤害增加"] += 0.07
        character.attr["百分比力智"] += 0.07
        character.attr["暴击伤害"] += 0.04
        character.attr["百分比力智"] += 0.1
        character.attr["伤害增加"] += 0.03
        character.attr["百分比三攻"] += 0.08

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.07
        character.attr["移动速度"] += 0.07
        character.attr["释放速度"] += 0.07

    # 专属属性
    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [50, 20, 10]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [10, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉被动(120/100)+'
    属性3范围_BUFF = [40, 0, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = 'BUFF力智：'
    属性4范围_BUFF = [9, 2, 1]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=220)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智=50 - self.属性1选择_BUFF * 10)
        # character.attr["觉醒"] += 一觉力智per=1.1 - self.属性2选择_BUFF / 100)
        # character.attr["被动"] += 信念光环体精=160 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=140 - self.属性3选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF力量per=1.09 - self.属性4选择_BUFF / 100, BUFF智力per=1.09 - self.属性4选择_BUFF / 100)
        pass


class 装备191(装备):
    名称 = '至高之炎-伊弗利特'
    模式 = 0
    所属套装 = '精灵使的权能'
    等级 = 100
    品质 = '神话'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 149
    智力 = 100
    体力 = 120
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '力量/智力 +'
    属性1范围 = [160, 40, 20]
    属性1选择 = 0
    属性2描述 = '最终伤害：'
    属性2范围 = [12, 1, 1]
    属性2选择 = 0
    属性3描述 = '百分比三攻：'
    属性3范围 = [12, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.3
        character.attr["火属性强化"] += 38
        character.attr["冰属性强化"] += 38
        character.attr["光属性强化"] += 38
        character.attr["暗属性强化"] += 38
        character.attr["力量"] += 160
        character.attr["智力"] += 160
        character.attr["最终伤害"] += 0.12
        character.attr["百分比三攻"] += 0.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = '守护恩赐/力智：'
    属性1范围_BUFF = [160, 40, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [120, 10, 10]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF三攻：'
    属性3范围_BUFF = [12, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=220)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 守护恩赐体精=160 - self.属性1选择_BUFF * 20)
        # character.attr["力智固定"] += x=160 - self.属性1选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智=120 - self.属性2选择_BUFF * 10)
        # character.attr["BUFF"] += BUFF物攻per=1.12 - self.属性3选择_BUFF / 100, BUFF魔攻per=1.12 - self.属性3选择_BUFF / 100, BUFF独立per=1.12 - self.属性3选择_BUFF / 100)
        pass


class 装备192(装备):
    名称 = '无尽的探求'
    模式 = 0
    所属套装 = '黑魔法探求者'
    等级 = 100
    品质 = '神话'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 149
    智力 = 100
    体力 = 120
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '力量/智力 +'
    属性1范围 = [240, 20, 20]
    属性1选择 = 0
    属性2描述 = '附加伤害：'
    属性2范围 = [7, 1, 1]
    属性2选择 = 0
    属性3描述 = '百分比三攻：'
    属性3范围 = [12, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.2
        character.attr["力量"] += 240
        character.attr["智力"] += 240
        character.attr["附加伤害"] += 0.07
        character.attr["百分比三攻"] += 0.12

    def 进图属性(self, character):
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 其它属性(self, character):
        pass
        # 专属属性

    属性1描述_BUFF = '守护恩赐/力智：'
    属性1范围_BUFF = [240, 20, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [10, 4, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [120, 10, 10]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=245)
        # character.attr["被动"] += 转职被动智力=270)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 守护恩赐体精=240 - self.属性1选择_BUFF * 20)
        # character.attr["力智固定"] += x=240 - self.属性1选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF物攻per=1.1 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.1 - self.属性2选择_BUFF / 100, BUFF独立per=1.1 - self.属性2选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智=120 - self.属性3选择_BUFF * 10)
        pass


class 装备193(装备):
    名称 = '时间回溯之针'
    模式 = 0
    所属套装 = '时空旅行者'
    等级 = 100
    品质 = '神话'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 149
    智力 = 100
    体力 = 120
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '百分比力智：'
    属性1范围 = [4, 1, 1]
    属性1选择 = 0
    属性2描述 = '所有属性强化 +'
    属性2范围 = [20, 12, 4]
    属性2选择 = 0
    属性3描述 = '物理/魔法/独立 +'
    属性3范围 = [100, 10, 10]
    属性3选择 = 0
    属性4描述 = '最终伤害：'
    属性4范围 = [8, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.14
        character.attr["百分比力智"] += 0.2
        character.skill_change_cooldown(50, 50, 0.15)
        character.skill_change_cooldown(85, 85, 0.15)
        character.attr["百分比力智"] += 0.04
        character.attr["火属性强化"] += 20
        character.attr["冰属性强化"] += 20
        character.attr["光属性强化"] += 20
        character.attr["暗属性强化"] += 20
        character.attr["物理攻击力"] += 100
        character.attr["魔法攻击力"] += 100
        character.attr["独立攻击力"] += 100
        character.attr["最终伤害"] += 0.08

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["释放速度"] += 0.15

    # 专属属性
    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '转职被动Lv+'
    属性2范围_BUFF = [5, 3, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [110, 20, 10]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = 'BUFF三攻：'
    属性4范围_BUFF = [10, 3, 1]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=242)
        # character.attr["BUFF"] += BUFF力量per=1.07, BUFF智力per=1.07)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智per=1.04 - self.属性1选择_BUFF / 100)
        # character.attr["被动"] += 转职被动Lv=5 - self.属性2选择_BUFF)
        # character.attr["被动"] += 守护恩赐Lv=5 - self.属性2选择_BUFF)
        # character.attr["觉醒"] += 一觉力智=110 - self.属性3选择_BUFF * 10)
        # character.attr["BUFF"] += BUFF物攻per=1.1 - self.属性4选择_BUFF / 100, BUFF魔攻per=1.1 - self.属性4选择_BUFF / 100, BUFF独立per=1.1 - self.属性4选择_BUFF / 100)
        pass


class 装备194(装备):
    名称 = '响彻天地的咆哮'
    模式 = 0
    所属套装 = '穿透命运的呐喊'
    等级 = 100
    品质 = '神话'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 149
    智力 = 100
    体力 = 120
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '技能攻击力：'
    属性1范围 = [3, 1, 1]
    属性1选择 = 0
    属性2描述 = '附加伤害：'
    属性2范围 = [4, 1, 1]
    属性2选择 = 0
    属性3描述 = '百分比力智：'
    属性3范围 = [7, 1, 1]
    属性3选择 = 0
    属性4描述 = '百分比三攻：'
    属性4范围 = [12, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.12
        character.attr["最终伤害"] += 0.23
        character.attr["技能攻击力"] *= 1.03
        character.attr["附加伤害"] += 0.04
        character.attr["百分比力智"] += 0.07
        character.attr["百分比三攻"] += 0.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.08
        character.attr["移动速度"] += 0.08
        character.attr["释放速度"] += 0.12

    # 专属属性
    属性1描述_BUFF = '转职被动：'
    属性1范围_BUFF = [160, 120, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF三攻：'
    属性3范围_BUFF = [7, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = 'BUFF力智：'
    属性4范围_BUFF = [12, 1, 1]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=220 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=250 - self.属性1选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 守护恩赐体精=160 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=160 - self.属性1选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智per=1.04 - self.属性2选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF物攻per=1.07 - self.属性3选择_BUFF / 100, BUFF魔攻per=1.07 - self.属性3选择_BUFF / 100, BUFF独立per=1.07 - self.属性3选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF力量per=1.12 - self.属性4选择_BUFF / 100, BUFF智力per=1.12 - self.属性4选择_BUFF / 100)
        pass


class 装备195(装备):
    名称 = '狂乱之逆转宿命'
    模式 = 0
    所属套装 = '狂乱追随者'
    等级 = 100
    品质 = '神话'
    部位 = '手镯'
    类型 = '首饰'
    力量 = 149
    智力 = 100
    体力 = 120
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '伤害增加：'
    属性1范围 = [10, 1, 1]
    属性1选择 = 0
    属性2描述 = '所有属性强化 +'
    属性2范围 = [32, 4, 4]
    属性2选择 = 0
    属性3描述 = '暴击伤害：'
    属性3范围 = [12, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.3
        character.attr["技能攻击力"] *= 1.11
        character.attr["伤害增加"] += 0.1
        character.attr["火属性强化"] += 32
        character.attr["冰属性强化"] += 32
        character.attr["光属性强化"] += 32
        character.attr["暗属性强化"] += 32
        character.attr["暴击伤害"] += 0.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass
        # 专属属性

    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [110, 20, 10]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [8, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF力智：'
    属性3范围_BUFF = [12, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=220)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智=110 - self.属性1选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF物攻per=1.08 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.08 - self.属性2选择_BUFF / 100, BUFF独立per=1.08 - self.属性2选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF力量per=1.12 - self.属性3选择_BUFF / 100, BUFF智力per=1.12 - self.属性3选择_BUFF / 100)
        pass


class 装备196(装备):
    名称 = '肯那兹：精神燎原之火'
    模式 = 0
    所属套装 = '上古尘封术士'
    等级 = 100
    品质 = '史诗'
    部位 = '项链'
    类型 = '首饰'
    力量 = 100
    智力 = 147
    精神 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.2
        character.attr["附加伤害"] += 0.12
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=277)
        # character.attr["被动"] += 转职被动智力=151)
        # character.attr["BUFF"] += BUFF物攻per=1.06)
        pass


class 装备197(装备):
    名称 = '驱散月光之黎明'
    模式 = 0
    所属套装 = '破晓曦光'
    等级 = 100
    品质 = '史诗'
    部位 = '项链'
    类型 = '首饰'
    力量 = 100
    智力 = 147
    精神 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.04 + 0.01 * min(13, character.fetch_strengthen_level(self.部位))
        character.attr["百分比三攻"] += 0.06
        character.attr["火属性强化"] += 28
        character.attr["冰属性强化"] += 28
        character.attr["光属性强化"] += 28
        character.attr["暗属性强化"] += 28

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 50, 70, 1)
        character.skill_change_recovery(35, 45, 0.30)

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 50, 70, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=154)
        # character.attr["被动"] += 转职被动智力=151)
        # character.attr["BUFF"] += BUFF物攻per=1.06)
        pass


class 装备198(装备):
    名称 = '四叶草之初心'
    模式 = 0
    所属套装 = '幸运三角'
    等级 = 100
    品质 = '史诗'
    部位 = '项链'
    类型 = '首饰'
    力量 = 100
    智力 = 147
    精神 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.07
        character.attr["百分比三攻"] += 0.07
        character.attr["伤害增加"] += 0.07
        character.attr["暴击伤害"] += 0.07
        character.attr["最终伤害"] += 0.07

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=264)
        # character.attr["被动"] += 转职被动智力=151)
        # character.attr["BUFF"] += BUFF物攻per=1.06)
        pass


class 装备199(装备):
    名称 = '冷焰之冰-温蒂妮'
    模式 = 0
    所属套装 = '精灵使的权能'
    等级 = 100
    品质 = '史诗'
    部位 = '项链'
    类型 = '首饰'
    力量 = 100
    智力 = 147
    精神 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["火属性强化"] += 38
        character.attr["冰属性强化"] += 38
        character.attr["光属性强化"] += 38
        character.attr["暗属性强化"] += 38
        character.attr["百分比三攻"] += 0.27

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=264)
        # character.attr["被动"] += 转职被动智力=151)
        # character.attr["BUFF"] += BUFF物攻per=1.06)
        pass


class 装备200(装备):
    名称 = '堕落世界树之生命'
    模式 = 0
    所属套装 = '深渊窥视者'
    等级 = 100
    品质 = '史诗'
    部位 = '项链'
    类型 = '首饰'
    力量 = 100
    智力 = 147
    精神 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.4

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=134)
        # character.attr["被动"] += 转职被动智力=48)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF物攻per=1.06)
        pass


class 装备201(装备):
    名称 = '引路者的四季项链'
    模式 = 0
    所属套装 = '圣者的黄昏'
    等级 = 100
    品质 = '史诗'
    部位 = '项链'
    类型 = '首饰'
    力量 = 100
    智力 = 147
    精神 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.35
        character.skill_change_cooldown(1, 45, 0.10)
        character.skill_change_cooldown(60, 80, 0.10)
        character.skill_change_cooldown(90, 95, 0.10)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=248)
        # character.attr["被动"] += 转职被动智力=128)
        # character.attr["BUFF"] += BUFF物攻per=1.06)
        pass


class 装备202(装备):
    名称 = '悲痛者项链'
    模式 = 0
    所属套装 = '坎坷命运'
    等级 = 100
    品质 = '史诗'
    部位 = '项链'
    类型 = '首饰'
    力量 = 100
    智力 = 147
    精神 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.1
        character.attr["最终伤害"] += 0.28

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.04
        character.attr["移动速度"] += 0.04
        character.attr["释放速度"] += 0.06
        if character.is_equip_exist('地狱边缘'):
            character.attr["攻击速度"] += -0.01
            character.attr["移动速度"] += -0.01
            character.attr["释放速度"] += -0.015
        if character.is_equip_exist('悲情者遗物'):
            character.attr["攻击速度"] += -0.01
            character.attr["移动速度"] += -0.01
            character.attr["释放速度"] += -0.015

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=264)
        # character.attr["被动"] += 转职被动智力=151)
        # character.attr["BUFF"] += BUFF物攻per=1.06)
        pass

    def 装备描述_BUFF(self, character):
        # temp = ''
        # if character.attr["角色"] == '圣职者(女)':
        #     temp += '智力 +147<br>'
        #     temp += '[勇气祝福]物理攻击力增加量 +6%<br>'
        #     temp += '[启示：圣歌]智力 +151<br>'
        # elif character.attr["角色"] == '圣职者(男)':
        #     temp += '精神 +117<br>'
        #     temp += '[荣誉祝福]物理攻击力增加量 +6%<br>'
        #     temp += '[守护恩赐]体力、精神 +264<br>'
        # elif character.attr["角色"] == '魔法师(女)':
        #     temp += '智力 +147<br>'
        #     temp += '[禁忌诅咒]物理攻击力增加量 +6%<br>'
        #     temp += '[人偶操纵者]智力 +151<br>'
        # return temp
        pass


class 装备203(装备):
    名称 = '激狂之怒'
    模式 = 0
    所属套装 = '吞噬愤怒'
    等级 = 100
    品质 = '史诗'
    部位 = '项链'
    类型 = '首饰'
    力量 = 100
    智力 = 147
    精神 = 117
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.3
        character.attr["持续伤害"] += 0.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=264)
        # character.attr["被动"] += 转职被动智力=151)
        # character.attr["BUFF"] += BUFF物攻per=1.06)
        pass


class 装备204(装备):
    名称 = '盖柏：完美的均衡'
    模式 = 0
    所属套装 = '上古尘封术士'
    等级 = 100
    品质 = '史诗'
    部位 = '戒指'
    类型 = '首饰'
    力量 = 171
    智力 = 171
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.2
        character.attr["附加伤害"] += 0.12
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=266)
        # character.attr["被动"] += 转职被动智力=86)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备205(装备):
    名称 = '寂静无言之露珠'
    模式 = 0
    所属套装 = '破晓曦光'
    等级 = 100
    品质 = '史诗'
    部位 = '戒指'
    类型 = '首饰'
    力量 = 171
    智力 = 171
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.04 + 0.01 * min(13, character.fetch_strengthen_level(self.部位))
        character.attr["火属性强化"] += 30
        character.attr["冰属性强化"] += 30
        character.attr["光属性强化"] += 30
        character.attr["暗属性强化"] += 30

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 75, 85, 1)
        character.skill_change_recovery(60, 80, 0.30)

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 75, 85, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=181)
        # character.attr["被动"] += 转职被动智力=86)
        # character.attr["BUFF"] += BUFF力量per=1.06)
        # character.attr["BUFF"] += BUFF智力per=1.06)
        pass


class 装备206(装备):
    名称 = '红兔之祝福'
    模式 = 0
    所属套装 = '幸运三角'
    等级 = 100
    品质 = '史诗'
    部位 = '戒指'
    类型 = '首饰'
    力量 = 171
    智力 = 171
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.07
        character.attr["百分比三攻"] += 0.07
        character.attr["伤害增加"] += 0.07
        character.attr["暴击伤害"] += 0.07
        character.attr["最终伤害"] += 0.07

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=266)
        # character.attr["被动"] += 转职被动智力=86)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备207(装备):
    名称 = '祝福之风-西尔芙'
    模式 = 0
    所属套装 = '精灵使的权能'
    等级 = 100
    品质 = '史诗'
    部位 = '戒指'
    类型 = '首饰'
    力量 = 171
    智力 = 171
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.27
        character.attr["火属性强化"] += 38
        character.attr["冰属性强化"] += 38
        character.attr["光属性强化"] += 38
        character.attr["暗属性强化"] += 38

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.04
        character.attr["移动速度"] += 0.04
        character.attr["释放速度"] += 0.06

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=266)
        # character.attr["被动"] += 转职被动智力=86)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备208(装备):
    名称 = '支配黑暗之环'
    模式 = 0
    所属套装 = '地狱求道者'
    等级 = 100
    品质 = '史诗'
    部位 = '戒指'
    类型 = '首饰'
    力量 = 171
    智力 = 171
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.4

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=299)
        # character.attr["被动"] += 转职被动智力=115)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备209(装备):
    名称 = '次元穿越者之印'
    模式 = 0
    所属套装 = '次元旅行者'
    等级 = 100
    品质 = '史诗'
    部位 = '戒指'
    类型 = '首饰'
    力量 = 171
    智力 = 171
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.14
        character.attr["技能攻击力"] *= 1.18

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 60, 80, 1)

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 60, 80, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=246)
        # character.attr["被动"] += 转职被动智力=92)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备210(装备):
    名称 = '命运的捉弄'
    模式 = 0
    所属套装 = '天命无常'
    等级 = 100
    品质 = '史诗'
    部位 = '戒指'
    类型 = '首饰'
    力量 = 171
    智力 = 171
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        if '天命无常[2]' in character.attr["套装栏"]:
            if character.is_equip_exist('命运反抗者'):
                character.attr["伤害增加"] += 0.12
            else:
                character.attr["伤害增加"] += 0.10
        character.attr["最终伤害"] += 0.06
        character.attr["技能攻击力"] *= 1.19

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=253)
        # character.attr["被动"] += 转职被动智力=70)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备211(装备):
    名称 = '蓬勃生命的落幕'
    模式 = 0
    所属套装 = '悲剧的残骸'
    等级 = 100
    品质 = '史诗'
    部位 = '戒指'
    类型 = '首饰'
    力量 = 171
    智力 = 171
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.27
        if character.is_equip_exist('心痛如绞的诀别'):
            character.attr["附加伤害"] += 0.106
        else:
            character.attr["附加伤害"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.021

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=266)
        # character.attr["被动"] += 转职被动智力=86)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass

# endregion
