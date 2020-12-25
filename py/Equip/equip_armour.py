from py.base_equip import *


# region  100SS防具
class 装备74(装备):
    名称 = '魔法师[???]的长袍'
    模式 = 0
    所属套装 = '遗忘魔法师的馈赠'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.05
        character.attr["百分比三攻"] += 0.1
        character.attr["最终伤害"] += 0.12

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 45, 1)

    def 其它属性(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 45, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=150)
        # character.attr["被动"] += 转职被动智力=50)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备75(装备):
    名称 = '死亡阴影夹克'
    模式 = 0
    所属套装 = '死亡阴影'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.04
        character.attr["伤害增加"] += 0.18
        character.attr["暴击伤害"] += 0.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=150)
        # character.attr["被动"] += 转职被动智力=50)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备76(装备):
    名称 = '燃烧烈焰之勇气'
    模式 = 0
    所属套装 = '贫瘠沙漠的遗产'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.06
        character.attr["暴击伤害"] += 0.28

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备77(装备):
    名称 = '撒旦：沸腾之怒'
    模式 = 0
    所属套装 = '噩梦：地狱之路'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.16
        character.attr["暴击伤害"] += 0.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备78(装备):
    名称 = '奔流不息之岁月'
    模式 = 0
    所属套装 = '永恒不息之路'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.3
        if character.attr["职业"] == '缔造者':
            character.skill_change_rate(50, -0.3)
            character.skill_change_recovery(50, 50, 1.00)
        else:
            character.skill_change_rate(45, -0.3)
            character.skill_change_recovery(45, 45, 1.00)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备79(装备):
    名称 = '优雅旋律华尔兹'
    模式 = 0
    所属套装 = '天堂舞姬'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.17
        character.attr["暴击伤害"] += 0.14
        character.skill_change_cooldown(1, 45, 0.10)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备80(装备):
    名称 = '首席执行官裁决夹克'
    模式 = 0
    所属套装 = '皇家裁决者宣言'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.19
        character.attr["暴击伤害"] += 0.14

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备81(装备):
    名称 = '炙炎：火龙果'
    模式 = 0
    所属套装 = '炙炎之盛宴'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["暴击伤害"] += 0.15

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF力量per=1.02)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # character.attr["BUFF"] += BUFF智力per=1.02)
        pass


class 装备82(装备):
    名称 = '妖精之姿'
    模式 = 0
    所属套装 = '传奇铁匠-封神'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=241)
        # character.attr["被动"] += 转职被动智力=141)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备83(装备):
    名称 = '人性的抉择'
    模式 = 0
    所属套装 = '命运歧路'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.11
        character.attr["伤害增加"] += 0.21

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=280)
        # character.attr["被动"] += 转职被动智力=180)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备84(装备):
    名称 = '大祭司的星祈礼袍'
    模式 = 0
    所属套装 = '古代祭祀的神圣仪式'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.1
        character.attr["最终伤害"] += 0.12
        pass

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备85(装备):
    名称 = '冲锋陷阵胸甲'
    模式 = 0
    所属套装 = '龙血玄黄'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=263)
        # character.attr["被动"] += 转职被动智力=163)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备86(装备):
    名称 = '气吞山河战甲'
    模式 = 0
    所属套装 = '擎天战甲'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.34
        if character.attr["职业"] == '缔造者':
            character.skill_level_up_batched('所有', 50, 50, 2)
        else:
            character.skill_level_up_batched('所有', 45, 45, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 45, 45, 2)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=263)
        # character.attr["被动"] += 转职被动智力=163)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备87(装备):
    名称 = '千链锁灵战甲'
    模式 = 0
    所属套装 = '荆棘漫天'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备88(装备):
    名称 = '宽恕坚韧之地'
    模式 = 0
    所属套装 = '大自然的呼吸'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.28

    def 进图属性(self, character):
        character.attr["火属性强化"] += 24
        character.attr["冰属性强化"] += 24
        character.attr["光属性强化"] += 24
        character.attr["暗属性强化"] += 24

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=242)
        # character.attr["被动"] += 转职被动智力=142)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备89(装备):
    名称 = '堕落深渊黑魔法衬衫'
    模式 = 0
    所属套装 = '深渊窥视者'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=173)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备90(装备):
    名称 = '引路者的黄昏披风'
    模式 = 0
    所属套装 = '圣者的黄昏'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.2
        character.attr["百分比三攻"] += 0.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=236)
        # character.attr["被动"] += 转职被动智力=136)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备91(装备):
    名称 = '地狱边缘'
    模式 = 0
    所属套装 = '坎坷命运'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.04
        character.attr["移动速度"] += 0.04
        character.attr["释放速度"] += 0.06
        if character.is_equip_exist('悲痛者项链'):
            character.attr["攻击速度"] += -0.01
            character.attr["移动速度"] += -0.01
            character.attr["释放速度"] += -0.015
        if character.is_equip_exist('悲情者遗物'):
            character.attr["攻击速度"] += -0.01
            character.attr["移动速度"] += -0.01
            character.attr["释放速度"] += -0.015

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备92(装备):
    名称 = '泣血之恨'
    模式 = 0
    所属套装 = '吞噬愤怒'
    等级 = 100
    品质 = '史诗'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.23
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
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        pass


class 装备93(装备):
    名称 = '大魔法师[???]的长袍'
    模式 = 0
    所属套装 = '遗忘魔法师的馈赠'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '布甲'

    属性1描述 = '伤害增加：'
    属性1范围 = [11, 1, 1]
    属性1选择 = 0
    属性2描述 = '技能等级Lv1 -'
    属性2范围 = [45, 5, 5]
    属性2选择 = 0
    属性3描述 = '百分比力智：'
    属性3范围 = [12, 3, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    # 专属属性
    属性1描述_BUFF = 'BUFF力智：'
    属性1范围_BUFF = [11, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [90, 10, 10]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '转职被动：'
    属性3范围_BUFF = [200, 20, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.1
        character.attr["最终伤害"] += 0.12
        character.attr["百分比力智"] += 0.05 + 0.12
        character.attr["伤害增加"] += 0.11
        character.skill_level_up_batched('所有', 1, 45, 1)

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 45, 1)

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 45, 1)

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 45, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=150)
        # character.attr["被动"] += 转职被动智力=50)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF力量per=1.11 - self.属性1选择_BUFF / 100, BUFF智力per=1.11 - self.属性1选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智=90 - self.属性2选择_BUFF * 10)
        # character.attr["被动"] += 守护恩赐体精=200 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=100 - self.属性3选择_BUFF * 20)
        pass


class 装备94(装备):
    名称 = '掌管生死之影夹克'
    模式 = 0
    所属套装 = '死亡阴影'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '皮甲'

    属性1描述 = '百分比力智：'
    属性1范围 = [10, 1, 1]
    属性1选择 = 0
    属性2描述 = '暴击伤害：'
    属性2范围 = [10, 1, 1]
    属性2选择 = 0
    属性3描述 = '物攻/魔攻/独立 +'
    属性3范围 = [170, 80, 10]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    # 专属属性
    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [100, 10, 10]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF力智：'
    属性2范围_BUFF = [10, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉被动(120/100)+'
    属性3范围_BUFF = [180, 0, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.04
        character.attr["伤害增加"] += 0.18
        character.attr["百分比力智"] += 0.10
        character.attr["暴击伤害"] += 0.2
        character.attr["物理攻击力"] += 170
        character.attr["魔法攻击力"] += 170
        character.attr["独立攻击力"] += 170

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=150)
        # character.attr["被动"] += 转职被动智力=50)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智=100 - self.属性1选择_BUFF * 10)
        # character.attr["BUFF"] += BUFF力量per=1.1 - self.属性2选择_BUFF / 100, BUFF智力per=1.1 - self.属性2选择_BUFF / 100)
        # character.attr["被动"] += 信念光环体精=300 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=280 - self.属性3选择_BUFF * 20)
        pass


class 装备95(装备):
    名称 = '爆裂大地之勇猛'
    模式 = 0
    所属套装 = '贫瘠沙漠的遗产'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '轻甲'

    属性1描述 = '百分比三攻：'
    属性1范围 = [8, 1, 1]
    属性1选择 = 0
    属性2描述 = '百分比力智：'
    属性2范围 = [8, 1, 1]
    属性2选择 = 0
    属性3描述 = '暴击伤害：'
    属性3范围 = [15, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    属性1描述_BUFF = '转职被动：'
    属性1范围_BUFF = [240, 100, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [8, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [150, 10, 10]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.06
        character.attr["百分比三攻"] += 0.08
        character.attr["百分比力智"] += 0.08
        character.attr["暴击伤害"] += 0.43

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=150 - self.属性1选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 守护恩赐体精=240 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=240 - self.属性1选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF物攻per=1.08 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.08 - self.属性2选择_BUFF / 100, BUFF独立per=1.08 - self.属性2选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智=150 - self.属性3选择_BUFF * 10)
        pass


class 装备96(装备):
    名称 = '撒旦：愤怒之王'
    模式 = 0
    所属套装 = '噩梦：地狱之路'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '重甲'

    属性1描述 = '持续伤害：'
    属性1范围 = [5, 2, 1]
    属性1选择 = 0
    属性2描述 = '暴击伤害：'
    属性2范围 = [7, 1, 1]
    属性2选择 = 0
    属性3描述 = '附加伤害：'
    属性3范围 = [4, 1, 1]
    属性3选择 = 0
    属性4描述 = '伤害增加：'
    属性4范围 = [9, 1, 1]
    属性4选择 = 0

    属性1描述_BUFF = '一觉被动(160/140)+'
    属性1范围_BUFF = [60, 0, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [7, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [50, 20, 10]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = 'BUFF力智：'
    属性4范围_BUFF = [9, 1, 1]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.16
        character.attr["暴击伤害"] += 0.16
        character.attr["持续伤害"] += 0.05
        character.attr["暴击伤害"] += 0.07
        character.attr["附加伤害"] += 0.04
        character.attr["伤害增加"] += 0.09

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 信念光环体精=220 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=200 - self.属性1选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF物攻per=1.07 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.07 - self.属性2选择_BUFF / 100, BUFF独立per=1.07 - self.属性2选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智=50 - self.属性3选择_BUFF * 10)
        # character.attr["BUFF"] += BUFF力量per=1.09 - self.属性4选择_BUFF / 100, BUFF智力per=1.09 - self.属性4选择_BUFF / 100)
        pass


class 装备97(装备):
    名称 = '英明循环之生命'
    模式 = 0
    所属套装 = '永恒不息之路'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '板甲'

    属性1描述 = '技能等级Lv25 -'
    属性1范围 = [45, 30, 5]
    属性1选择 = 0
    属性2描述 = '附加伤害：'
    属性2范围 = [5, 1, 1]
    属性2选择 = 0
    属性3描述 = '百分比力智：'
    属性3范围 = [8, 1, 1]
    属性3选择 = 0
    属性4描述 = '最终伤害：'
    属性4范围 = [6, 1, 1]
    属性4选择 = 0

    属性1描述_BUFF = 'BUFF力智：'
    属性1范围_BUFF = [6, 3, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [60, 20, 10]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF三攻：'
    属性3范围_BUFF = [9, 2, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '转职被动Lv+'
    属性4范围_BUFF = [6, 1, 1]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.3
        if character.attr["职业"] == '缔造者':
            character.skill_change_rate(50, -0.3)
            character.skill_change_recovery(50, 50, 1.00)
        else:
            character.skill_change_rate(45, -0.3)
            character.skill_change_recovery(45, 45, 1.00)
        character.skill_level_up_batched('所有', 25, 45, 1)
        character.attr["附加伤害"] += 0.05
        character.attr["百分比力智"] += 0.08
        character.attr["最终伤害"] += 0.06

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 25, 45, 1)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF力量per=1.06 - self.属性1选择_BUFF / 100, BUFF智力per=1.06 - self.属性1选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智=60 - self.属性2选择_BUFF * 10)
        # character.attr["BUFF"] += BUFF物攻per=1.09 - self.属性3选择_BUFF / 100, BUFF魔攻per=1.09 - self.属性3选择_BUFF / 100, BUFF独立per=1.09 - self.属性3选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐Lv=6 - self.属性4选择_BUFF)
        # character.attr["被动"] += 转职被动Lv=6 - self.属性4选择_BUFF)
        pass


class 装备98(装备):
    名称 = '浪漫旋律华尔兹'
    模式 = 0
    所属套装 = '天堂舞姬'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '布甲'

    属性1描述 = '百分比三攻：'
    属性1范围 = [3, 1, 1]
    属性1选择 = 0
    属性2描述 = '最终伤害：'
    属性2范围 = [10, 1, 1]
    属性2选择 = 0
    属性3描述 = '伤害增加：'
    属性3范围 = [8, 1, 1]
    属性3选择 = 0
    属性4描述 = '所有属性强化 +'
    属性4范围 = [24, 12, 4]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.14
        character.attr["伤害增加"] += 0.17
        character.skill_change_cooldown(1, 45, 0.10)
        character.attr["百分比三攻"] += 0.03
        character.attr["最终伤害"] += 0.1
        character.attr["伤害增加"] += 0.08
        character.attr["火属性强化"] += 24
        character.attr["冰属性强化"] += 24
        character.attr["光属性强化"] += 24
        character.attr["暗属性强化"] += 24

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    属性1描述_BUFF = '一觉被动(120/100)+'
    属性1范围_BUFF = [40, 0, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [100, 10, 10]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF三攻：'
    属性3范围_BUFF = [8, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '转职被动：'
    属性4范围_BUFF = [140, 80, 20]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 一觉被动力智=140 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 信念光环体精=160 - self.属性1选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智=100 - self.属性2选择_BUFF * 10)
        # character.attr["BUFF"] += BUFF物攻per=1.08 - self.属性3选择_BUFF / 100, BUFF魔攻per=1.08 - self.属性3选择_BUFF / 100, BUFF独立per=1.08 - self.属性3选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐体精=140 - self.属性4选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=140 - self.属性4选择_BUFF * 20)
        pass


class 装备99(装备):
    名称 = '皇家裁决者审判外套'
    模式 = 0
    所属套装 = '皇家裁决者宣言'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '皮甲'

    属性1描述 = '暴击伤害：'
    属性1范围 = [7, 1, 1]
    属性1选择 = 0
    属性2描述 = '伤害增加：'
    属性2范围 = [5, 1, 1]
    属性2选择 = 0
    属性3描述 = '附加伤害：'
    属性3范围 = [6, 1, 1]
    属性3选择 = 0
    属性4描述 = '最终伤害：'
    属性4范围 = [5, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.19
        character.attr["暴击伤害"] += 0.14
        character.attr["暴击伤害"] += 0.07
        character.attr["伤害增加"] += 0.05
        character.attr["附加伤害"] += 0.06
        character.attr["最终伤害"] += 0.05

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = 'BUFF力智：'
    属性1范围_BUFF = [8, 2, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [5, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [60, 10, 10]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '一觉被动(220/200)+'
    属性4范围_BUFF = [80, 0, 20]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF力量per=1.08 - self.属性1选择_BUFF / 100, BUFF智力per=1.08 - self.属性1选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF物攻per=1.05 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.05 - self.属性2选择_BUFF / 100, BUFF独立per=1.05 - self.属性2选择_BUFF / 100)
        # character.attr["被动"] += 信念光环体精=300 - self.属性4选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智=60 - self.属性3选择_BUFF * 10)
        # character.attr["被动"] += 一觉被动力智=280 - self.属性4选择_BUFF * 20)
        pass


class 装备100(装备):
    名称 = '炙炎：霸王树'
    模式 = 0
    所属套装 = '炙炎之盛宴'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '轻甲'

    属性1描述 = '最终伤害：'
    属性1范围 = [10, 1, 1]
    属性1选择 = 0
    属性2描述 = '暴击伤害：'
    属性2范围 = [8, 1, 1]
    属性2选择 = 0
    属性3描述 = '伤害增加：'
    属性3范围 = [4, 1, 1]
    属性3选择 = 0
    属性4描述 = '百分比力智：'
    属性4范围 = [3, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.16
        character.attr["暴击伤害"] += 0.15
        character.attr["最终伤害"] += 0.1
        character.attr["暴击伤害"] += 0.08
        character.attr["伤害增加"] += 0.04
        character.attr["百分比力智"] += 0.03

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15

    # 专属属性
    属性1描述_BUFF = 'BUFF力智：'
    属性1范围_BUFF = [10, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [80, 10, 10]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF三攻：'
    属性3范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '一觉被动(180/160)+'
    属性4范围_BUFF = [40, 0, 20]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF力量per=1.02, BUFF智力per=1.02)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF力量per=1.10 - self.属性1选择_BUFF / 100, BUFF智力per=1.10 - self.属性1选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智=80 - self.属性2选择_BUFF * 10)
        # character.attr["BUFF"] += BUFF物攻per=1.04 - self.属性3选择_BUFF / 100, BUFF魔攻per=1.04 - self.属性3选择_BUFF / 100, BUFF独立per=1.04 - self.属性3选择_BUFF / 100)
        # character.attr["被动"] += 一觉被动力智=200 - self.属性4选择_BUFF * 20)
        # character.attr["被动"] += 信念光环体精=220 - self.属性4选择_BUFF * 20)
        pass


class 装备101(装备):
    名称 = '天堂之翼'
    模式 = 0
    所属套装 = '传奇铁匠-封神'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '重甲'

    属性1描述 = '附加伤害：'
    属性1范围 = [9, 1, 1]
    属性1选择 = 0
    属性2描述 = '百分比力智：'
    属性2范围 = [4, 1, 1]
    属性2选择 = 0
    属性3描述 = '最终伤害：'
    属性3范围 = [4, 1, 1]
    属性3选择 = 0
    属性4描述 = '百分比三攻：'
    属性4范围 = [7, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.34
        character.attr["附加伤害"] += 0.09
        character.attr["百分比力智"] += 0.04
        character.attr["最终伤害"] += 0.04
        character.attr["百分比三攻"] += 0.07

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.5
        # 专属属性

    属性1描述_BUFF = '一觉力智'
    属性1范围_BUFF = [90, 10, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '转职被动：'
    属性2范围_BUFF = [200, 140, 20]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉被动(140/120)+'
    属性3范围_BUFF = [60, 0, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = 'BUFF力智：'
    属性4范围_BUFF = [7, 1, 1]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=241)
        # character.attr["被动"] += 转职被动智力=141)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智=90 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=200 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 守护恩赐体精=200 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 信念光环体精=200 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=180 - self.属性3选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF力量per=1.07 - self.属性4选择_BUFF / 100, BUFF智力per=1.07 - self.属性4选择_BUFF / 100)
        pass


class 装备102(装备):
    名称 = '神赐的抉择'
    模式 = 0
    所属套装 = '命运歧路'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '板甲'

    属性1描述 = '伤害增加：'
    属性1范围 = [5, 1, 1]
    属性1选择 = 0
    属性2描述 = '暴击伤害：'
    属性2范围 = [7, 1, 1]
    属性2选择 = 0
    属性3描述 = '最终伤害：'
    属性3范围 = [6, 1, 1]
    属性3选择 = 0
    属性4描述 = '附加伤害：'
    属性4范围 = [5, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.21
        character.attr["百分比三攻"] += 0.11
        character.attr["伤害增加"] += 0.05
        character.attr["暴击伤害"] += 0.07
        character.attr["最终伤害"] += 0.06
        character.attr["附加伤害"] += 0.05

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = 'BUFF力智：'
    属性1范围_BUFF = [5, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [7, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '转职被动：'
    属性3范围_BUFF = [200, 100, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '一觉被动(140/120)+'
    属性4范围_BUFF = [80, 0, 20]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=280)
        # character.attr["被动"] += 转职被动智力=180)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF力量per=1.05 - self.属性1选择_BUFF / 100, BUFF智力per=1.05 - self.属性1选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF物攻per=1.07 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.07 - self.属性2选择_BUFF / 100, BUFF独立per=1.07 - self.属性2选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐体精=200 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=200 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=200 - self.属性4选择_BUFF * 20)
        # character.attr["被动"] += 信念光环体精=220 - self.属性4选择_BUFF * 20)
        pass


class 装备103(装备):
    名称 = '大祭司的神启礼服'
    模式 = 0
    所属套装 = '古代祭祀的神圣仪式'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '布甲'

    属性1描述 = '附加伤害：'
    属性1范围 = [10, 2, 1]
    属性1选择 = 0
    属性2描述 = '百分比力智：'
    属性2范围 = [10, 1, 1]
    属性2选择 = 0
    属性3描述 = '百分比三攻：'
    属性3范围 = [11, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.1
        character.attr["最终伤害"] += 0.12
        character.attr["附加伤害"] += 0.1
        character.attr["百分比力智"] += 0.10
        character.attr["百分比三攻"] += 0.11

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass
        # 专属属性

    属性1描述_BUFF = 'BUFF三攻：'
    属性1范围_BUFF = [10, 2, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '转职被动Lv+'
    属性2范围_BUFF = [12, 3, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [150, 50, 10]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF物攻per=1.10 - self.属性1选择_BUFF / 100, BUFF魔攻per=1.10 - self.属性1选择_BUFF / 100, BUFF独立per=1.10 - self.属性1选择_BUFF / 100)
        # character.attr["被动"] += 转职被动Lv=12 - self.属性2选择_BUFF)
        # character.attr["被动"] += 守护恩赐Lv=12 - self.属性2选择_BUFF)
        # character.attr["觉醒"] += 一觉力智=150 - self.属性3选择_BUFF * 10)
        pass


class 装备104(装备):
    名称 = '战无不胜上衣'
    模式 = 0
    所属套装 = '龙血玄黄'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '皮甲'

    属性1描述 = '伤害增加：'
    属性1范围 = [4, 1, 1]
    属性1选择 = 0
    属性2描述 = '百分比三攻：'
    属性2范围 = [3, 1, 1]
    属性2选择 = 0
    属性3描述 = '暴击伤害：'
    属性3范围 = [10, 1, 1]
    属性3选择 = 0
    属性4描述 = '百分比力智：'
    属性4范围 = [8, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.35
        character.attr["伤害增加"] += 0.04
        character.attr["百分比三攻"] += 0.03
        character.attr["暴击伤害"] += 0.1
        character.attr["百分比力智"] += 0.08

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉被动(120/100)+'
    属性2范围_BUFF = [40, 0, 20]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF三攻：'
    属性3范围_BUFF = [10, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '转职被动：'
    属性4范围_BUFF = [200, 60, 20]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=263)
        # character.attr["被动"] += 转职被动智力=163)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智per=1.04 - self.属性1选择_BUFF / 100)
        # character.attr["被动"] += 信念光环体精=160 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=140 - self.属性2选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF物攻per=1.10 - self.属性3选择_BUFF / 100, BUFF魔攻per=1.10 - self.属性3选择_BUFF / 100, BUFF独立per=1.10 - self.属性3选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐体精=200 - self.属性4选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=200 - self.属性4选择_BUFF * 20)
        pass


class 装备105(装备):
    名称 = '摧枯拉朽胸甲'
    模式 = 0
    所属套装 = '擎天战甲'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '轻甲'

    属性1描述 = '技能攻击力：'
    属性1范围 = [4, 1, 1]
    属性1选择 = 0
    属性2描述 = '最终伤害：'
    属性2范围 = [4, 1, 1]
    属性2选择 = 0
    属性3描述 = '伤害增加：'
    属性3范围 = [9, 1, 1]
    属性3选择 = 0
    属性4描述 = '暴击伤害：'
    属性4范围 = [7, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.34
        if character.attr["职业"] == '缔造者':
            character.skill_level_up_batched('所有', 50, 50, 2)
        else:
            character.skill_level_up_batched('所有', 45, 45, 2)
        character.attr["技能攻击力"] *= 1.04
        character.attr["最终伤害"] += 0.04
        character.attr["伤害增加"] += 0.09
        character.attr["暴击伤害"] += 0.07

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉被动(100/80)+'
    属性3范围_BUFF = [160, 0, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = 'BUFF力智：'
    属性4范围_BUFF = [7, 1, 1]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 45, 45, 2)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=263)
        # character.attr["被动"] += 转职被动智力=163)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智per=1.04 - self.属性1选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF物攻per=1.04 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.04 - self.属性2选择_BUFF / 100, BUFF独立per=1.04 - self.属性2选择_BUFF / 100)
        # character.attr["被动"] += 信念光环体精=260 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=240 - self.属性3选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF力量per=1.07 - self.属性4选择_BUFF / 100, BUFF智力per=1.07 - self.属性4选择_BUFF / 100)
        pass


class 装备106(装备):
    名称 = '千链万化战甲'
    模式 = 0
    所属套装 = '荆棘漫天'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '重甲'

    属性1描述 = '暴击伤害：'
    属性1范围 = [10, 1, 1]
    属性1选择 = 0
    属性2描述 = '百分比三攻：'
    属性2范围 = [10, 1, 1]
    属性2选择 = 0
    属性3描述 = '附加伤害：'
    属性3范围 = [10, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.35
        character.attr["暴击伤害"] += 0.1
        character.attr["百分比三攻"] += 0.1
        character.attr["附加伤害"] += 0.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = 'BUFF力智：'
    属性1范围_BUFF = [11, 2, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '转职被动Lv+'
    属性2范围_BUFF = [10, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智'
    属性3范围_BUFF = [12, 3, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        #
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF力量per=1.11 - self.属性1选择_BUFF / 100, BUFF智力per=1.11 - self.属性1选择_BUFF / 100)
        # character.attr["被动"] += 转职被动Lv=10 - self.属性2选择_BUFF)
        # character.attr["被动"] += 守护恩赐Lv=10 - self.属性2选择_BUFF)
        # character.attr["觉醒"] += 一觉力智per=1.12 - self.属性3选择_BUFF / 100)
        pass


class 装备107(装备):
    名称 = '生命脉动之地'
    模式 = 0
    所属套装 = '大自然的呼吸'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '板甲'

    属性1描述 = '百分比力智：'
    属性1范围 = [12, 1, 1]
    属性1选择 = 0
    属性2描述 = '伤害增加：'
    属性2范围 = [9, 1, 1]
    属性2选择 = 0
    属性3描述 = '最终伤害：'
    属性3范围 = [9, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.28
        character.attr["百分比力智"] += 0.12
        character.attr["伤害增加"] += 0.09
        character.attr["最终伤害"] += 0.09

    def 进图属性(self, character):
        character.attr["火属性强化"] += 24
        character.attr["冰属性强化"] += 24
        character.attr["光属性强化"] += 24
        character.attr["暗属性强化"] += 24

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = 'BUFF力智：'
    属性1范围_BUFF = [13, 2, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [10, 2, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '转职被动Lv+'
    属性3范围_BUFF = [9, 2, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=242)
        # character.attr["被动"] += 转职被动智力=142)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF力量per=1.13 - self.属性1选择_BUFF / 100, BUFF智力per=1.13 - self.属性1选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF物攻per=1.1 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.1 - self.属性2选择_BUFF / 100, BUFF独立per=1.1 - self.属性2选择_BUFF / 100)
        # character.attr["被动"] += 转职被动Lv=10 - self.属性3选择_BUFF)
        # character.attr["被动"] += 守护恩赐Lv=10 - self.属性3选择_BUFF)
        pass


class 装备108(装备):
    名称 = '深渊囚禁者长袍'
    模式 = 0
    所属套装 = '深渊窥视者'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '布甲'

    属性1描述 = '技能等级Lv5 -'
    属性1范围 = [100, 10, 5]
    属性1选择 = 0
    属性2描述 = '百分比三攻：'
    属性2范围 = [7, 1, 1]
    属性2选择 = 0
    属性3描述 = '物攻/魔攻/独立 +'
    属性3范围 = [80, 10, 10]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.35
        character.skill_level_up_batched('所有', 5, 100, 1)
        character.attr["百分比三攻"] += 0.07
        character.attr["物理攻击力"] += 80
        character.attr["魔法攻击力"] += 80
        character.attr["独立攻击力"] += 80

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass
        # 专属属性

    属性1描述_BUFF = '转职被动Lv+'
    属性1范围_BUFF = [17, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉被动(40/20)+'
    属性2范围_BUFF = [120, 0, 20]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '转职被动：'
    属性3范围_BUFF = [200, 60, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 5, 100, 1)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=173)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 转职被动Lv=17 - self.属性1选择_BUFF)
        # character.attr["被动"] += 守护恩赐Lv=17 - self.属性1选择_BUFF)
        # character.attr["被动"] += 信念光环体精=160 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=140 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 守护恩赐体精=200 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=200 - self.属性3选择_BUFF * 20)
        pass


class 装备109(装备):
    名称 = '圣者的黄昏披风'
    模式 = 0
    所属套装 = '圣者的黄昏'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '皮甲'

    属性1描述 = '所有属性强化 +'
    属性1范围 = [40, 4, 4]
    属性1选择 = 0
    属性2描述 = '伤害增加：'
    属性2范围 = [10, 1, 1]
    属性2选择 = 0
    属性3描述 = '附加伤害：'
    属性3范围 = [10, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.2
        character.attr["百分比三攻"] += 0.12
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40
        character.attr["伤害增加"] += 0.1
        character.attr["附加伤害"] += 0.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass
        # 专属属性

    属性1描述_BUFF = '一觉被动(40/20)+'
    属性1范围_BUFF = [180, 0, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF三攻：'
    属性2范围_BUFF = [10, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '转职被动：'
    属性3范围_BUFF = [240, 60, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=236)
        # character.attr["被动"] += 转职被动智力=136)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 信念光环体精=220 - self.属性1选择_BUFF)
        # character.attr["被动"] += 一觉被动力智=200 - self.属性1选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF物攻per=1.1 - self.属性2选择_BUFF / 100, BUFF魔攻per=1.1 - self.属性2选择_BUFF / 100, BUFF独立per=1.1 - self.属性2选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐体精=240 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=240 - self.属性3选择_BUFF * 20)
        pass


class 装备110(装备):
    名称 = '逆转结局'
    模式 = 0
    所属套装 = '坎坷命运'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '轻甲'

    属性1描述 = '技能等级Lv30 -'
    属性1范围 = [48, 35, 5]
    属性1选择 = 0
    属性2描述 = '物攻/魔攻/独立 +'
    属性2范围 = [70, 10, 10]
    属性2选择 = 0
    属性3描述 = '最终伤害：'
    属性3范围 = [5, 1, 1]
    属性3选择 = 0
    属性4描述 = '力量/智力 +'
    属性4范围 = [160, 40, 20]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.35
        if character.is_equip_exist('悲痛者项链'):
            character.attr["百分比三攻"] += -0.10
            character.attr["附加伤害"] += 0.10
        if character.is_equip_exist('悲情者遗物'):
            character.attr["百分比三攻"] += -0.10
            character.attr["附加伤害"] += 0.10
        character.skill_level_up_batched('所有', 30, 48, 1)
        character.attr["物理攻击力"] += 70
        character.attr["魔法攻击力"] += 70
        character.attr["独立攻击力"] += 70
        character.attr["最终伤害"] += 0.05
        character.attr["力量"] += 160
        character.attr["智力"] += 160

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.06
        character.attr["移动速度"] += 0.06
        character.attr["释放速度"] += 0.09
        # 专属属性

    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '转职被动Lv+'
    属性2范围_BUFF = [7, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF三攻：'
    属性3范围_BUFF = [5, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '转职被动：'
    属性4范围_BUFF = [160, 40, 20]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 30, 48, 1)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智per=1.04 - self.属性1选择_BUFF / 100)
        # character.attr["被动"] += 转职被动Lv=7 - self.属性2选择_BUFF)
        # character.attr["被动"] += 守护恩赐Lv=7 - self.属性2选择_BUFF)
        # character.attr["BUFF"] += BUFF物攻per=1.05 - self.属性3选择_BUFF / 100, BUFF魔攻per=1.05 - self.属性3选择_BUFF / 100, BUFF独立per=1.05 - self.属性3选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐体精=160 - self.属性4选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=160 - self.属性4选择_BUFF * 20)
        pass


class 装备111(装备):
    名称 = '灭世之怒'
    模式 = 0
    所属套装 = '吞噬愤怒'
    等级 = 100
    品质 = '神话'
    部位 = '上衣'
    力量 = {'布甲': 100, '皮甲': 150, '轻甲': 160, '重甲': 155, '板甲': 150}
    智力 = {'布甲': 160, '皮甲': 150, '轻甲': 140, '重甲': 140, '板甲': 150}
    类型 = '重甲'

    属性1描述 = '最终伤害：'
    属性1范围 = [4, 1, 1]
    属性1选择 = 0
    属性2描述 = '百分比三攻：'
    属性2范围 = [13, 1, 1]
    属性2选择 = 0
    属性3描述 = '百分比力智：'
    属性3范围 = [4, 1, 1]
    属性3选择 = 0
    属性4描述 = '技能攻击力：'
    属性4范围 = [5, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.23
        character.attr["持续伤害"] += 0.1
        character.attr["最终伤害"] += 0.04
        character.attr["百分比三攻"] += 0.13
        character.attr["百分比力智"] += 0.04
        character.attr["技能攻击力"] *= 1.05

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass
        # 专属属性

    属性1描述_BUFF = '一觉被动(100/80)+'
    属性1范围_BUFF = [60, 0, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF力智：'
    属性2范围_BUFF = [13, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '转职被动：'
    属性3范围_BUFF = [200, 140, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '一觉力智：'
    属性4范围_BUFF = [50, 10, 10]  # 最大值 最小值 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF物攻per=1.25)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 信念光环体精=160 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=140 - self.属性1选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF力量per=1.13 - self.属性2选择_BUFF / 100, BUFF智力per=1.13 - self.属性2选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐体精=200 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=200 - self.属性3选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智=50 - self.属性4选择_BUFF * 10)
        pass


class 装备112(装备):
    名称 = '魔法师[???]的护腿'
    模式 = 0
    所属套装 = '遗忘魔法师的馈赠'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.05
        character.attr["百分比三攻"] += 0.1
        character.attr["伤害增加"] += 0.12

    def 进图属性(self, character):
        character.attr["火属性强化"] += 18
        character.attr["冰属性强化"] += 18
        character.attr["光属性强化"] += 18
        character.attr["暗属性强化"] += 18

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备113(装备):
    名称 = '死亡阴影短裤'
    模式 = 0
    所属套装 = '死亡阴影'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.04
        character.attr["伤害增加"] += 0.18
        character.attr["暴击伤害"] += 0.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=150)
        # character.attr["被动"] += 转职被动智力=50)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备114(装备):
    名称 = '肆虐狂风之意志'
    模式 = 0
    所属套装 = '贫瘠沙漠的遗产'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.06
        character.attr["暴击伤害"] += 0.16
        character.attr["附加伤害"] += 0.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备115(装备):
    名称 = '亚蒙：谎言之力'
    模式 = 0
    所属套装 = '噩梦：地狱之路'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["最终伤害"] += 0.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备116(装备):
    名称 = '奔流不息之伽蓝'
    模式 = 0
    所属套装 = '永恒不息之路'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.31
        character.skill_change_rate(40, -0.3)
        character.skill_change_recovery(40, 40, 1.0)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备117(装备):
    名称 = '魅惑律动伦巴'
    模式 = 0
    所属套装 = '天堂舞姬'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.14
        character.attr["最终伤害"] += 0.17
        character.skill_change_cooldown(35, 45, 0.15)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备118(装备):
    名称 = '首席执行官裁决短裤'
    模式 = 0
    所属套装 = '皇家裁决者宣言'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["最终伤害"] += 0.17

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备119(装备):
    名称 = '炙炎：荔枝'
    模式 = 0
    所属套装 = '炙炎之盛宴'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.33

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF力量per=1.02)
        # character.attr["BUFF"] += BUFF智力per=1.02)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备120(装备):
    名称 = '邪恶之角'
    模式 = 0
    所属套装 = '传奇铁匠-封神'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=241)
        # character.attr["被动"] += 转职被动智力=141)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备121(装备):
    名称 = '命运的抉择'
    模式 = 0
    所属套装 = '命运歧路'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.07
        character.attr["暴击伤害"] += 0.07
        character.attr["附加伤害"] += 0.07
        character.attr["最终伤害"] += 0.07
        character.attr["百分比三攻"] += 0.07

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=280)
        # character.attr["被动"] += 转职被动智力=180)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备122(装备):
    名称 = '大祭司的星祈长裙'
    模式 = 0
    所属套装 = '古代祭祀的神圣仪式'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.1
        character.attr["伤害增加"] += 0.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备123(装备):
    名称 = '破釜沉舟护腿'
    模式 = 0
    所属套装 = '龙血玄黄'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '皮甲'

    def 城镇属性(self, character):
        if character.is_equip_exist('战无不胜上衣'):
            character.attr["暴击伤害"] += 0.35
        else:
            character.attr["暴击伤害"] += 0.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=263)
        # character.attr["被动"] += 转职被动智力=163)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备124(装备):
    名称 = '雷霆万钧护腿'
    模式 = 0
    所属套装 = '擎天战甲'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.34
        character.skill_level_up_batched('所有', 35, 35, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 35, 35, 2)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=263)
        # character.attr["被动"] += 转职被动智力=163)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备125(装备):
    名称 = '千链锁灵护腿'
    模式 = 0
    所属套装 = '荆棘漫天'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备126(装备):
    名称 = '蚕食新绿之息'
    模式 = 0
    所属套装 = '大自然的呼吸'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.32

    def 进图属性(self, character):
        character.attr["暗属性强化"] += 24

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.1
        character.attr["魔法暴击率"] += 0.1

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=242)
        # character.attr["被动"] += 转职被动智力=142)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备127(装备):
    名称 = '驱散黑暗短裤'
    模式 = 0
    所属套装 = '黑魔法探求者'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=275)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备128(装备):
    名称 = '时空漩涡护腿'
    模式 = 0
    所属套装 = '时空旅行者'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.32
        character.skill_change_cooldown(60, 80, 0.10)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=242)
        # character.attr["被动"] += 转职被动智力=142)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备129(装备):
    名称 = '灵魂的呐喊'
    模式 = 0
    所属套装 = '穿透命运的呐喊'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.14
        character.attr["附加伤害"] += 0.17

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备130(装备):
    名称 = '疯狂之如影随形'
    模式 = 0
    所属套装 = '狂乱追随者'
    等级 = 100
    品质 = '史诗'
    部位 = '下装'
    力量 = {'布甲': 100, '皮甲': 149, '轻甲': 158, '重甲': 154, '板甲': 149}
    智力 = {'布甲': 158, '皮甲': 149, '轻甲': 139, '重甲': 139, '板甲': 149}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.1
        character.attr["暴击伤害"] += 0.22

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF魔攻per=1.25)
        pass


class 装备131(装备):
    名称 = '魔法师[???]的披风'
    模式 = 0
    所属套装 = '遗忘魔法师的馈赠'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.05
        character.attr["百分比三攻"] += 0.1
        character.attr["技能攻击力"] *= 1.13

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备132(装备):
    名称 = '死亡阴影护肩'
    模式 = 0
    所属套装 = '死亡阴影'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.04
        character.attr["暴击伤害"] += 0.18
        character.attr["技能攻击力"] *= 1.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备133(装备):
    名称 = '艰难求生之斗志'
    模式 = 0
    所属套装 = '贫瘠沙漠的遗产'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.06
        character.attr["附加伤害"] += 0.16
        character.attr["技能攻击力"] *= 1.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备134(装备):
    名称 = '贝利亚尔：毁灭之种'
    模式 = 0
    所属套装 = '噩梦：地狱之路'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.16
        character.attr["技能攻击力"] *= 1.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备135(装备):
    名称 = '奔流不息之山川'
    模式 = 0
    所属套装 = '永恒不息之路'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.1
        character.attr["技能攻击力"] *= 1.2
        character.skill_change_rate(35, -0.3)
        character.skill_change_recovery(35, 35, 1.0)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备136(装备):
    名称 = '性感洒脱探戈'
    模式 = 0
    所属套装 = '天堂舞姬'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.17
        character.attr["技能攻击力"] *= 1.14
        character.skill_change_cooldown(75, 80, 0.15)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=260)
        # character.attr["被动"] += 转职被动智力=160)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备137(装备):
    名称 = '首席执行官裁决肩甲'
    模式 = 0
    所属套装 = '皇家裁决者宣言'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.12
        character.attr["技能攻击力"] *= 1.2

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备138(装备):
    名称 = '炙炎：榴莲'
    模式 = 0
    所属套装 = '炙炎之盛宴'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.33

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.05)
        # character.attr["BUFF"] += BUFF智力per=1.05)
        pass


class 装备139(装备):
    名称 = '魔龙之心'
    模式 = 0
    所属套装 = '传奇铁匠-封神'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.12
        character.attr["技能攻击力"] *= 1.2

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.16

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=312)
        # character.attr["被动"] += 转职被动智力=212)
        # character.attr["BUFF"] += BUFF力量per=1.03)
        # character.attr["BUFF"] += BUFF智力per=1.03)
        pass


class 装备140(装备):
    名称 = '矛盾的抉择'
    模式 = 0
    所属套装 = '命运歧路'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=320)
        # character.attr["被动"] += 转职被动智力=220)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备141(装备):
    名称 = '大祭司的星祈披肩'
    模式 = 0
    所属套装 = '古代祭祀的神圣仪式'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.1
        character.attr["技能攻击力"] *= 1.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        if character.is_equip_exist('大祭司的神启礼服'):
            character.attr["释放速度"] += 0.24
        else:
            character.attr["释放速度"] += 0.18

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备142(装备):
    名称 = '枪林弹雨护肩'
    模式 = 0
    所属套装 = '龙血玄黄'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '皮甲'

    def 城镇属性(self, character):
        if character.is_equip_exist('战无不胜上衣'):
            character.attr["技能攻击力"] *= 1.35
        else:
            character.attr["技能攻击力"] *= 1.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.05)
        # character.attr["BUFF"] += BUFF智力per=1.05)
        pass


class 装备143(装备):
    名称 = '排山倒海护肩'
    模式 = 0
    所属套装 = '擎天战甲'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.34
        character.skill_level_up_batched('所有', 60, 60, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 60, 60, 2)
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备144(装备):
    名称 = '千链锁灵肩甲'
    模式 = 0
    所属套装 = '荆棘漫天'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += -0.1

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备145(装备):
    名称 = '猛烈燃烧之炎'
    模式 = 0
    所属套装 = '大自然的呼吸'
    等级 = 100
    品质 = '史诗'
    部位 = '头肩'
    力量 = {'布甲': 100, '皮甲': 139, '轻甲': 146, '重甲': 143, '板甲': 139}
    智力 = {'布甲': 146, '皮甲': 139, '轻甲': 131, '重甲': 131, '板甲': 139}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.32
        pass

    def 进图属性(self, character):
        character.attr["火属性强化"] += 24

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=270)
        # character.attr["被动"] += 转职被动智力=170)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.02)
        # character.attr["BUFF"] += BUFF智力per=1.02)
        pass


class 装备146(装备):
    名称 = '魔法师[???]的长靴'
    模式 = 0
    所属套装 = '遗忘魔法师的馈赠'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.05
        character.attr["百分比三攻"] += 0.1
        character.attr["暴击伤害"] += 0.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.14
        character.attr["释放速度"] += 0.15

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备147(装备):
    名称 = '死亡阴影长靴'
    模式 = 0
    所属套装 = '死亡阴影'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.04
        character.attr["暴击伤害"] += 0.1
        character.attr["附加伤害"] += 0.18

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["被动"] += 一觉被动Lv=2)
        pass


class 装备148(装备):
    名称 = '寂静寒夜之忍耐'
    模式 = 0
    所属套装 = '贫瘠沙漠的遗产'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.28
        character.attr["伤害增加"] += 0.06

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=268)
        # character.attr["被动"] += 转职被动智力=168)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备149(装备):
    名称 = '巴尔：堕落之魂'
    模式 = 0
    所属套装 = '噩梦：地狱之路'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["伤害增加"] += 0.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备150(装备):
    名称 = '奔流不息之银河'
    模式 = 0
    所属套装 = '永恒不息之路'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.28
        character.skill_change_rate(25, -0.3)
        character.skill_change_recovery(25, 25, 1.0)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.06)
        # character.attr["BUFF"] += BUFF智力per=1.06)
        pass


class 装备151(装备):
    名称 = '激烈欢动踢踏'
    模式 = 0
    所属套装 = '天堂舞姬'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.17
        character.attr["附加伤害"] += 0.14
        character.skill_change_cooldown(1, 30, 0.15)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=180)
        # character.attr["被动"] += 转职被动智力=80)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["被动"] += 一觉被动Lv=2)
        pass


class 装备152(装备):
    名称 = '首席执行官裁决长靴'
    模式 = 0
    所属套装 = '皇家裁决者宣言'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.11
        character.attr["最终伤害"] += 0.21

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备153(装备):
    名称 = '炙炎：木瓜'
    模式 = 0
    所属套装 = '炙炎之盛宴'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.3

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.19
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.05)
        # character.attr["BUFF"] += BUFF智力per=1.05)
        pass


class 装备154(装备):
    名称 = '自然之核'
    模式 = 0
    所属套装 = '传奇铁匠-封神'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["火属性强化"] += 70
        character.attr["冰属性强化"] += 70
        character.attr["光属性强化"] += 70
        character.attr["暗属性强化"] += 70
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["BUFF"] += BUFF力量per=1.05)
        # character.attr["BUFF"] += BUFF智力per=1.05)
        pass


class 装备155(装备):
    名称 = '守护的抉择'
    模式 = 0
    所属套装 = '命运歧路'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.17
        if character.attr["护石第一栏"] != '无':
            单技能修改(character.attr["护石第一栏"], 1.55, 0.7)
        if character.attr["护石第二栏"] != '无':
            单技能修改(character.attr["护石第二栏"], 1.45, 0.75)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=280)
        # character.attr["被动"] += 转职被动智力=180)
        # if 属性.护石第一栏 != '无':
        #     character.attr["BUFF"] += BUFF力量per=1.04)
        #     character.attr["BUFF"] += BUFF智力per=1.04)
        # if 属性.护石第二栏 != '无':
        #     character.attr["BUFF"] += BUFF力量per=1.02)
        #     character.attr["BUFF"] += BUFF智力per=1.02)
        pass


class 装备156(装备):
    名称 = '大祭司的星祈凉鞋'
    模式 = 0
    所属套装 = '古代祭祀的神圣仪式'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.1
        character.attr["附加伤害"] += 0.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        if character.is_equip_exist('大祭司的神启礼服'):
            character.attr["移动速度"] += 0.18
        else:
            character.attr["移动速度"] += 0.12

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备157(装备):
    名称 = '赤地千里战靴'
    模式 = 0
    所属套装 = '龙血玄黄'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '皮甲'

    def 城镇属性(self, character):
        if character.is_equip_exist('战无不胜上衣'):
            character.attr["百分比力智"] += 0.35
        else:
            character.attr["百分比力智"] += 0.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.05)
        # character.attr["BUFF"] += BUFF智力per=1.05)
        pass


class 装备158(装备):
    名称 = '遮天蔽日长靴'
    模式 = 0
    所属套装 = '擎天战甲'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.34
        character.skill_level_up_batched('所有', 70, 70, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 70, 70, 2)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.05)
        # character.attr["BUFF"] += BUFF智力per=1.05)
        pass


class 装备159(装备):
    名称 = '千链锁灵战靴'
    模式 = 0
    所属套装 = '荆棘漫天'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += -0.06

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备160(装备):
    名称 = '交织烈日之风'
    模式 = 0
    所属套装 = '大自然的呼吸'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.32

    def 进图属性(self, character):
        character.attr["光属性强化"] += 24

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.14

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["被动"] += 一觉被动Lv=1)
        pass


class 装备161(装备):
    名称 = '堕入地狱之脚'
    模式 = 0
    所属套装 = '地狱求道者'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '布甲'

    def 城镇属性(self, character):
        pass

    def 进图属性(self, character):
        character.attr["火属性强化"] += 70
        character.attr["冰属性强化"] += 70
        character.attr["光属性强化"] += 70
        character.attr["暗属性强化"] += 70
        character.skill_level_up_batched('所有', 1, 90, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 90, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=263)
        # character.attr["被动"] += 转职被动智力=163)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["被动"] += 一觉被动Lv=2)
        pass


class 装备162(装备):
    名称 = '次元漫步者长靴'
    模式 = 0
    所属套装 = '次元旅行者'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.1
        character.attr["伤害增加"] += 0.19

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 45, 1)

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.14

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 45, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF力量per=1.02)
        # character.attr["BUFF"] += BUFF智力per=1.02)
        pass


class 装备163(装备):
    名称 = '悲喜交加'
    模式 = 0
    所属套装 = '天命无常'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.29

    def 进图属性(self, character):
        if '天命无常[2]' in character.attr["套装栏"]:
            if character.is_equip_exist('命运反抗者'):
                character.attr["火属性强化"] += 24
                character.attr["冰属性强化"] += 24
                character.attr["光属性强化"] += 24
                character.attr["暗属性强化"] += 24
            else:
                character.attr["火属性强化"] += 20
                character.attr["冰属性强化"] += 20
                character.attr["光属性强化"] += 20
                character.attr["暗属性强化"] += 20

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.04

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=270)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        pass


class 装备164(装备):
    名称 = '崩溃世界的忧伤'
    模式 = 0
    所属套装 = '悲剧的残骸'
    等级 = 100
    品质 = '史诗'
    部位 = '鞋'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.17
        if character.is_equip_exist('心痛如绞的诀别'):
            character.attr["附加伤害"] += 0.106
        else:
            character.attr["附加伤害"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.021

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["被动"] += 一觉被动Lv=2)
        pass


class 装备165(装备):
    名称 = '魔法师[???]的腰带'
    模式 = 0
    所属套装 = '遗忘魔法师的馈赠'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.05
        character.attr["百分比三攻"] += 0.1
        character.attr["附加伤害"] += 0.14

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备166(装备):
    名称 = '死亡阴影腰带'
    模式 = 0
    所属套装 = '死亡阴影'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.04
        character.attr["暴击伤害"] += 0.10
        character.attr["附加伤害"] += 0.18

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=150)
        # character.attr["被动"] += 转职被动智力=50)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备167(装备):
    名称 = '守护战士之苦难'
    模式 = 0
    所属套装 = '贫瘠沙漠的遗产'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["伤害增加"] += 0.06
        character.attr["附加伤害"] += 0.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备168(装备):
    名称 = '亚巴顿：绝望地狱'
    模式 = 0
    所属套装 = '噩梦：地狱之路'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["暴击伤害"] += 0.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备169(装备):
    名称 = '奔流不息之狂风'
    模式 = 0
    所属套装 = '永恒不息之路'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.32
        character.skill_change_rate(30, -0.3)
        character.skill_change_recovery(30, 30, 1.0)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备170(装备):
    名称 = '热情舞动桑巴'
    模式 = 0
    所属套装 = '天堂舞姬'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.17
        character.attr["最终伤害"] += 0.14
        character.skill_change_cooldown(60, 70, 0.15)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备171(装备):
    名称 = '首席执行官裁决腰带'
    模式 = 0
    所属套装 = '皇家裁决者宣言'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.18
        character.attr["暴击伤害"] += 0.15

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备172(装备):
    名称 = '炙炎：山竹'
    模式 = 0
    所属套装 = '炙炎之盛宴'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["火属性强化"] += 60
        character.attr["冰属性强化"] += 60
        character.attr["光属性强化"] += 60
        character.attr["暗属性强化"] += 60
        character.attr["百分比三攻"] += 0.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.15

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFF力量per=1.02)
        # character.attr["BUFF"] += BUFF智力per=1.02)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备173(装备):
    名称 = '碎钢之牙'
    模式 = 0
    所属套装 = '传奇铁匠-封神'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=241)
        # character.attr["被动"] += 转职被动智力=141)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备174(装备):
    名称 = '正义的抉择'
    模式 = 0
    所属套装 = '命运歧路'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.2
        character.skill_change_rate(50, 0.25)
        character.skill_change_rate(85, 0.45)
        character.skill_change_cooldown(85, 85, 0.20)
        character.skill_change_rate(100, 0.13)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=280)
        # character.attr["被动"] += 转职被动智力=180)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备175(装备):
    名称 = '大祭司的星祈腰带'
    模式 = 0
    所属套装 = '古代祭祀的神圣仪式'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '布甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.1
        character.attr["暴击伤害"] += 0.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        if character.is_equip_exist('大祭司的神启礼服'):
            character.attr["攻击速度"] += 0.18
        else:
            character.attr["攻击速度"] += 0.12

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备176(装备):
    名称 = '浴血奋战腰带'
    模式 = 0
    所属套装 = '龙血玄黄'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '皮甲'

    def 城镇属性(self, character):
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性(self, character):
        if character.is_equip_exist('战无不胜上衣'):
            character.attr["火属性强化"] += 72
            character.attr["冰属性强化"] += 72
            character.attr["光属性强化"] += 72
            character.attr["暗属性强化"] += 72
        else:
            character.attr["火属性强化"] += 68
            character.attr["冰属性强化"] += 68
            character.attr["光属性强化"] += 68
            character.attr["暗属性强化"] += 68

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备177(装备):
    名称 = '风起云涌腰带'
    模式 = 0
    所属套装 = '擎天战甲'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '轻甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.34
        character.skill_level_up_batched('所有', 40, 40, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 40, 40, 2)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=263)
        # character.attr["被动"] += 转职被动智力=163)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备178(装备):
    名称 = '千链锁灵腰带'
    模式 = 0
    所属套装 = '荆棘漫天'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '重甲'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["释放速度"] += -0.15

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass


class 装备179(装备):
    名称 = '宁静苍翠之水'
    模式 = 0
    所属套装 = '大自然的呼吸'
    等级 = 100
    品质 = '史诗'
    部位 = '腰带'
    力量 = {'布甲': 100, '皮甲': 130, '轻甲': 135, '重甲': 132, '板甲': 130}
    智力 = {'布甲': 135, '皮甲': 130, '轻甲': 123, '重甲': 123, '板甲': 130}
    类型 = '板甲'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.32

    def 进图属性(self, character):
        character.attr["冰属性强化"] += 24

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.15

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=242)
        # character.attr["被动"] += 转职被动智力=142)
        # character.attr["BUFF"] += BUFF独立per=1.25)
        pass

# endregion
