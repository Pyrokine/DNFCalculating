from py.base_equip import *


# region  100SS武器
class 装备0(装备):
    名称 = '信念徽章：自由'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '短剑'
    力量 = 0
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.26
        character.attr["百分比三攻"] += 0.22
        character.attr["伤害增加"] += 0.22
        character.attr["技能攻击力"] *= 1.3

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.1
        character.attr["释放速度"] += 0.15


class 装备1(装备):
    名称 = '太极天帝剑'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '太刀'
    力量 = 81
    智力 = 122
    物理攻击力 = 1167
    魔法攻击力 = 1290
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.4
        character.attr["技能攻击力"] *= 1.3
        character.attr["技能攻击力"] *= 1.23

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += -0.5
        character.attr["移动速度"] += -0.5
        character.attr["释放速度"] += -0.5


class 装备2(装备):
    名称 = '哈蒂-赎月者'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '钝器'
    力量 = 122
    智力 = 0
    物理攻击力 = 1352
    魔法攻击力 = 1167
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.16
        character.attr["暴击伤害"] += 0.41
        character.attr["附加伤害"] += 0.12
        character.attr["技能攻击力"] *= 1.32

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15


class 装备3(装备):
    名称 = '卡西姆的大剑'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '巨剑'
    力量 = 81
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.2
        character.attr["最终伤害"] += 0.43
        character.attr["技能攻击力"] *= 1.3
        character.skill_change_cooldown(1, 45, 0.20)
        character.skill_change_cooldown(60, 80, 0.20)
        character.skill_change_cooldown(90, 95, 0.20)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.225


class 装备4(装备):
    名称 = '星之海：巴德纳尔'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '光剑'
    力量 = 81
    智力 = 0
    物理攻击力 = 1143
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.26
        character.attr["属性附加"] += 0.2
        character.attr["技能攻击力"] *= 1.22
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.225


class 装备5(装备):
    名称 = '白虎啸魂手套'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '手套'
    力量 = 0
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.5
        if character.attr["职业"] == '气功师':
            character.attr["技能攻击力"] *= 1.4
            character.skill_change_attr('狮子吼', 1.20, 0.70)

    def 进图属性(self, character):
        if character.attr["职业"] == '气功师':
            character.attr["火属性强化"] += 56
            character.attr["冰属性强化"] += 56
            character.attr["光属性强化"] += 56
            character.attr["暗属性强化"] += 56

    def 其它属性(self, character):
        if character.attr["职业"] == '气功师':
            character.attr["攻击速度"] += 0.1
            character.attr["移动速度"] += 0.1
            character.attr["释放速度"] += 0.15


class 装备6(装备):
    名称 = '太阴神：灵龟'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '臂铠'
    力量 = 122
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.14
        character.attr["暴击伤害"] += 0.25
        character.attr["最终伤害"] += 0.26
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15


class 装备7(装备):
    名称 = '疯狂飓风'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '爪'
    力量 = 81
    智力 = 41
    物理攻击力 = 1229
    魔法攻击力 = 1229
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["伤害增加"] += 0.47
        character.attr["持续伤害"] += 0.1
        character.attr["技能攻击力"] *= 1.22
        character.skill_level_up_specified('爪精通', 3)
        character.skill_level_up_specified('万毒噬心诀', 1)
        character.skill_level_up_specified('燃火轰天炮', 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.15


class 装备8(装备):
    名称 = '猎焰追魂拳套'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '拳套'
    力量 = 81
    智力 = 0
    物理攻击力 = 1290
    魔法攻击力 = 1167
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.35
        character.attr["伤害增加"] += 0.24
        character.attr["最终伤害"] += 0.12
        character.attr["技能攻击力"] *= 1.3

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备9(装备):
    名称 = '青沙棍'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '东方棍'
    力量 = 81
    智力 = 122
    物理攻击力 = 1167
    魔法攻击力 = 1229
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.4
        character.attr["附加伤害"] += 0.34
        character.attr["技能攻击力"] *= 1.3

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.06
        character.attr["魔法暴击率"] += 0.06


class 装备10(装备):
    名称 = '午夜生死轮盘'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '左轮枪'
    力量 = 81
    智力 = 0
    物理攻击力 = 1238
    魔法攻击力 = 1042
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.18
        character.attr["暴击伤害"] += 0.54
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备11(装备):
    名称 = '雷霆怒啸手枪'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '自动手枪'
    力量 = 0
    智力 = 81
    物理攻击力 = 868
    魔法攻击力 = 1273
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.29
        character.attr["最终伤害"] += 0.22
        character.attr["技能攻击力"] *= 1.38
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40
        character.skill_change_attr('光反应能量模块', 1.2, 1)
        character.skill_level_up_specified('TN80终结者', 3)
        character.skill_level_up_specified('GSP猎鹰捕食者形态', 3)
        character.skill_level_up_specified('GSP猎鹰科罗纳形态', 3)
        character.skill_level_up_specified('GSP猎鹰旋雷者形态', 3)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备12(装备):
    名称 = '强力打击-X'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '步枪'
    力量 = 81
    智力 = 122
    物理攻击力 = 1331
    魔法攻击力 = 1157
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.27
        character.attr["伤害增加"] += 0.2
        character.attr["暴击伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.3
        character.skill_level_up_specified('战地勋章', 2)
        character.skill_level_up_specified('重火力支援', 2)
        character.skill_level_up_specified('制空掌握', 2)
        character.skill_level_up_specified('开火', 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备13(装备):
    名称 = '绝杀：无人生还'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '手炮'
    力量 = 122
    智力 = 0
    物理攻击力 = 1447
    魔法攻击力 = 868
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.32
        character.attr["百分比三攻"] += 0.16
        character.attr["技能攻击力"] *= 1.3
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40
        character.skill_level_up_batched('所有', 50, 50, 2)
        character.skill_level_up_batched('所有', 85, 85, 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备14(装备):
    名称 = '激光流星弓'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '手弩'
    力量 = 81
    智力 = 41
    物理攻击力 = 1042
    魔法攻击力 = 1157
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.36
        character.attr["附加伤害"] += 0.35
        character.attr["技能攻击力"] *= 1.3
        character.skill_level_up_specified('弹夹改装', 1)
        character.skill_level_up_specified('单兵推进器', 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["命中率"] += 0.03
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05


class 装备15(装备):
    名称 = '歼灵灭魂矛'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '矛'
    力量 = 122
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1045
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.15
        character.attr["最终伤害"] += 0.33
        character.attr["技能攻击力"] *= 1.35
        if character.attr["职业"] == '战斗法师':
            character.attr["技能栏"][character.attr["技能序号"]['碎霸']].额外倍率 = 5
        elif character.attr["职业"] == '血法师':
            character.attr["技能栏"][character.attr["技能序号"]['狱血之牙']].额外倍率 = 5

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备16(装备):
    名称 = '混沌之种'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '棍棒'
    力量 = 81
    智力 = 81
    物理攻击力 = 1328
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.35
        character.attr["附加伤害"] += 0.35
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备17(装备):
    名称 = '火焰地狱'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '魔杖'
    力量 = 0
    智力 = 122
    物理攻击力 = 1106
    魔法攻击力 = 1352
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.15
        character.attr["最终伤害"] += 0.34
        character.attr["技能攻击力"] *= 1.33

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备18(装备):
    名称 = '世界树的根须'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '法杖'
    力量 = 0
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1475
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.24
        character.attr["百分比三攻"] += 0.2
        character.attr["附加伤害"] += 0.1
        character.attr["技能攻击力"] *= 1.32
        character.skill_change_cooldown(1, 100, 0.1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.2


class 装备19(装备):
    名称 = '纯白的祈祷'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '扫把'
    力量 = 0
    智力 = 81
    物理攻击力 = 1229
    魔法攻击力 = 1352
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.15
        character.attr["百分比三攻"] += 0.15
        character.attr["伤害增加"] += 0.15
        character.attr["暴击伤害"] += 0.15
        character.attr["技能攻击力"] *= 1.3

    def 进图属性(self, character):
        character.attr["火属性强化"] += 26
        character.attr["冰属性强化"] += 26
        character.attr["光属性强化"] += 26
        character.attr["暗属性强化"] += 26

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.225

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 转职被动智力=127)
        # character.attr["BUFF"] += BUFFLv=5)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["BUFF"] += BUFF物攻per=1.2, BUFF魔攻per=1.2, BUFF独立per=1.2)
        # character.attr["觉醒"] += 一觉Lv=2)
        # character.attr["觉醒"] += 一觉力智=68)
        pass


class 装备20(装备):
    名称 = '圣者的慈悲'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '十字架'
    力量 = 0
    智力 = 81
    体力 = 97
    精神 = 97
    物理攻击力 = 1229
    魔法攻击力 = 1167
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.36
        character.attr["百分比三攻"] += 0.36
        character.attr["技能攻击力"] *= 1.31

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.16
        character.attr["移动速度"] += 0.16
        character.attr["释放速度"] += 0.24
        character.attr["物理暴击率"] += 0.08
        character.attr["魔法暴击率"] += 0.08

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=152)
        # character.attr["被动"] += 转职被动智力=152)
        # character.attr["BUFF"] += BUFFLv=5)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["BUFF"] += BUFF物攻per=1.2, BUFF魔攻per=1.2, BUFF独立per=1.2)
        # character.attr["觉醒"] += 一觉Lv=3)
        # character.attr["觉醒"] += 一觉力智=26)
        pass


class 装备21(装备):
    名称 = '轮回之环：桓龙'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '念珠'
    力量 = 0
    智力 = 122
    物理攻击力 = 1106
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.34
        character.attr["伤害增加"] += 0.2
        character.attr["技能攻击力"] *= 1.34
        character.skill_change_cooldown(1, 100, 0.1)
        if character.attr["职业"] in ['驱魔师', '巫女']:
            character.skill_level_up_batched('所有', 48, 80, 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备22(装备):
    名称 = '暗战终结者'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '图腾'
    力量 = 122
    智力 = 0
    物理攻击力 = 1290
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.12
        character.attr["暴击伤害"] += 0.16
        character.attr["附加伤害"] += 0.38
        character.attr["技能攻击力"] *= 1.36

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备23(装备):
    名称 = '泯灭之灵'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '镰刀'
    力量 = 81
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1229
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.28
        character.attr["附加伤害"] += 0.18
        character.attr["最终伤害"] += 0.18
        character.attr["技能攻击力"] *= 1.38
        pass

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备24(装备):
    名称 = '弗卡奴斯的第二个痕迹'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '战斧'
    力量 = 81
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1045
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.41
        character.attr["持续伤害"] += 0.1
        character.attr["最终伤害"] += 0.17
        character.attr["技能攻击力"] *= 1.28
        character.skill_level_up_specified('苍龙逐日', 3)
        character.skill_level_up_specified('火刑', 3)
        character.skill_change_attr('无双击', 1.40, 1)
        character.skill_change_attr('行刑', 1.40, 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备25(装备):
    名称 = '匿影'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '匕首'
    力量 = 81
    智力 = 0
    物理攻击力 = 1167
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.18
        character.attr["最终伤害"] += 0.26
        character.attr["技能攻击力"] *= 1.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.225
        character.attr["命中率"] += 0.15
        character.attr["回避率"] += 0.15


class 装备26(装备):
    名称 = '一叶障目'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '双剑'
    力量 = 81
    智力 = 0
    物理攻击力 = 1343
    魔法攻击力 = 983
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.32
        character.attr["最终伤害"] += 0.32
        character.attr["技能攻击力"] *= 1.32
        技能倍率提升(40, 0.32)
        技能倍率提升(45, 0.32)
        技能倍率提升(70, 0.32)
        character.skill_change_attr('忍法：影分身', 0.68, 0.68)
        character.skill_change_attr('弧光闪', 0.68, 0.68)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备27(装备):
    名称 = '绿色生命的面容'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '手杖'
    力量 = 0
    智力 = 81
    物理攻击力 = 1086
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.19
        character.attr["附加伤害"] += 0.19
        character.attr["最终伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.4
        character.attr["最终伤害"] += 0.1

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.21


class 装备28(装备):
    名称 = '血腥红宝石之眼'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '苦无'
    力量 = 0
    智力 = 122
    物理攻击力 = 1029
    魔法攻击力 = 1352
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.3
        character.attr["暴击伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.35
        character.attr["火属性强化"] += 40
        character.skill_level_up_specified('火遁·蟾蜍油炎弹', 5)
        character.skill_level_up_specified('八岐大蛇', 5)
        character.skill_level_up_specified('天照', 5)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备29(装备):
    名称 = '幻影狂欢长枪'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '长枪'
    力量 = 122
    智力 = 0
    物理攻击力 = 1290
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.4
        character.attr["附加伤害"] += 0.12
        character.attr["最终伤害"] += 0.12
        character.attr["技能攻击力"] *= 1.28
        character.skill_level_up_specified('行云：沐', 2)
        character.skill_level_up_specified('行云：启', 2)
        character.skill_level_up_specified('行云：冥', 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备30(装备):
    名称 = '万夫之勇'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '战戟'
    力量 = 81
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1045
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.14
        character.attr["最终伤害"] += 0.29
        character.attr["技能攻击力"] *= 1.16
        character.skill_level_up_specified('战戟之魂', 3)
        character.skill_level_up_specified('战神之力', 3)
        character.skill_level_up_specified('千魂弑', 2)
        character.skill_level_up_specified('血战天狱', 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备31(装备):
    名称 = '千芒闪爆枪'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '光枪'
    力量 = 81
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.18
        character.attr["百分比三攻"] += 0.16
        character.attr["附加伤害"] += 0.32
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备32(装备):
    名称 = '寂灭剧毒矛'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '暗矛'
    力量 = 81
    智力 = 122
    物理攻击力 = 1167
    魔法攻击力 = 1290
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.24
        character.attr["最终伤害"] += 0.4
        character.attr["技能攻击力"] *= 1.3
        character.skill_level_up_specified('黑暗本源', 3)
        character.skill_level_up_specified('坠蚀之雨', 2)
        character.skill_level_up_specified('冥夜裂空', 2)
        character.skill_level_up_specified('冥蚀脉冲', 2)
        character.skill_change_attr('幽影暗蚀：寂灭', 1.114000616, 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备33(装备):
    名称 = '金刚密藏刀'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '长刀'
    力量 = 81
    智力 = 81
    物理攻击力 = 1328
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.1
        character.attr["伤害增加"] += 0.1
        character.attr["暴击伤害"] += 0.1
        character.attr["技能攻击力"] *= 1.28
        character.attr["火属性强化"] += 50
        character.attr["冰属性强化"] += 50
        character.attr["光属性强化"] += 50
        character.attr["暗属性强化"] += 50
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.225
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05


class 装备34(装备):
    名称 = '冰洁的红焰'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '小太刀'
    力量 = 81
    智力 = 41
    物理攻击力 = 1229
    魔法攻击力 = 1229
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.11
        character.attr["伤害增加"] += 0.21
        character.attr["最终伤害"] += 0.3
        character.attr["技能攻击力"] *= 1.4

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15


class 装备35(装备):
    名称 = '聚能擎天剑'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '重剑'
    力量 = 81
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.15
        character.attr["暴击伤害"] += 0.55
        character.attr["技能攻击力"] *= 1.3
        character.attr["火属性强化"] += 22
        character.attr["冰属性强化"] += 22
        character.attr["光属性强化"] += 22
        character.attr["暗属性强化"] += 22

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.40
        character.attr["移动速度"] += 0.3


class 装备36(装备):
    名称 = '远古御神战剑'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '源力剑'
    力量 = 0
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.23
        character.attr["附加伤害"] += 0.24
        character.attr["最终伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.33

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15


class 装备37(装备):
    名称 = '战场的热血：安格巴迪'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '短剑'
    力量 = 0
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.3
        character.attr["附加伤害"] += 0.34
        character.attr["技能攻击力"] *= 1.4

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.05
        character.attr["移动速度"] += 0.05
        character.attr["释放速度"] += 0.1


class 装备38(装备):
    名称 = '前瞻守卫者'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '太刀'
    力量 = 81
    智力 = 122
    物理攻击力 = 1167
    魔法攻击力 = 1290
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.25
        character.attr["伤害增加"] += 0.14
        character.attr["暴击伤害"] += 0.26
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.3


class 装备39(装备):
    名称 = '骚动的冥焰'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '钝器'
    力量 = 122
    智力 = 0
    物理攻击力 = 1352
    魔法攻击力 = 1167
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.2
        character.attr["附加伤害"] += 0.32
        character.attr["技能攻击力"] *= 1.36
        character.attr["火属性强化"] += 55
        character.attr["冰属性强化"] += 55
        character.attr["光属性强化"] += 55
        character.attr["暗属性强化"] += 55

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备40(装备):
    名称 = '神之意象'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '巨剑'
    力量 = 81
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.35
        character.attr["技能攻击力"] *= 1.24
        character.attr["火属性强化"] += 50
        character.attr["冰属性强化"] += 50
        character.attr["光属性强化"] += 50
        character.attr["暗属性强化"] += 50
        character.skill_level_up_batched('所有', 1, 85, 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备41(装备):
    名称 = '赤光剑路易纳斯'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '光剑'
    力量 = 81
    智力 = 0
    物理攻击力 = 1143
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.17
        character.attr["百分比三攻"] += 0.2
        character.attr["最终伤害"] += 0.22
        character.attr["技能攻击力"] *= 1.33

    def 进图属性(self, character):
        character.attr["火属性强化"] += 31
        character.attr["冰属性强化"] += 31
        character.attr["光属性强化"] += 31
        character.attr["暗属性强化"] += 31

    def 其它属性(self, character):
        pass


class 装备42(装备):
    名称 = '无瑕之意志手套'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '手套'
    力量 = 0
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.11
        character.attr["属性附加"] += 0.15
        character.attr["最终伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.15
        character.skill_level_up_batched('所有', 1, 48, 2)
        character.skill_level_up_batched('所有', 60, 80, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备43(装备):
    名称 = '毁灭之碾压'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '臂铠'
    力量 = 122
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.4
        character.attr["附加伤害"] += 0.34
        character.attr["技能攻击力"] *= 1.3

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["命中率"] += 0.05
        character.attr["物理暴击率"] += 0.1
        character.attr["魔法暴击率"] += 0.1


class 装备44(装备):
    名称 = '痛苦之源'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '爪'
    力量 = 81
    智力 = 41
    物理攻击力 = 1229
    魔法攻击力 = 1229
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.17
        character.attr["附加伤害"] += 0.5
        character.attr["技能攻击力"] *= 1.4

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备45(装备):
    名称 = '幻光绽放拳套'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '拳套'
    力量 = 81
    智力 = 0
    物理攻击力 = 1290
    魔法攻击力 = 1167
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.2
        character.attr["附加伤害"] += 0.35
        character.attr["持续伤害"] += 0.1
        character.attr["技能攻击力"] *= 1.26
        character.attr["火属性强化"] += 35
        character.attr["冰属性强化"] += 35
        character.attr["光属性强化"] += 35
        character.attr["暗属性强化"] += 35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备46(装备):
    名称 = '鸣鸿破影棍'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '东方棍'
    力量 = 81
    智力 = 122
    物理攻击力 = 1167
    魔法攻击力 = 1229
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.4
        character.attr["伤害增加"] += 0.3
        character.attr["技能攻击力"] *= 1.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["释放速度"] += 0.15


class 装备47(装备):
    名称 = '血枪之脉'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '左轮枪'
    力量 = 81
    智力 = 0
    物理攻击力 = 1238
    魔法攻击力 = 1042
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.4
        character.attr["附加伤害"] += 0.32
        character.attr["技能攻击力"] *= 1.32

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.2


class 装备48(装备):
    名称 = '寻觅海石竹'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '自动手枪'
    力量 = 0
    智力 = 81
    物理攻击力 = 868
    魔法攻击力 = 1273
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.35
        character.attr["百分比三攻"] += 0.35
        character.attr["技能攻击力"] *= 1.34

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1


class 装备49(装备):
    名称 = '湍流'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '步枪'
    力量 = 81
    智力 = 122
    物理攻击力 = 1331
    魔法攻击力 = 1157
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.23
        character.attr["暴击伤害"] += 0.23
        character.attr["附加伤害"] += 0.23
        character.attr["技能攻击力"] *= 1.31

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备50(装备):
    名称 = '乾坤极电炮'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '手炮'
    力量 = 122
    智力 = 0
    物理攻击力 = 1447
    魔法攻击力 = 868
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.32
        character.attr["暴击伤害"] += 0.16
        character.attr["附加伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.3
        character.skill_change_attr('激光炮', 1.2, 0.7)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备51(装备):
    名称 = '吟游诗人的轻吟'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '手弩'
    力量 = 81
    智力 = 41
    物理攻击力 = 1042
    魔法攻击力 = 1157
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.34
        character.attr["最终伤害"] += 0.4
        character.attr["技能攻击力"] *= 1.3

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.1
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05


class 装备52(装备):
    名称 = '吟唱：不灭之魂'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '矛'
    力量 = 122
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1045
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.15
        character.attr["伤害增加"] += 0.25
        character.attr["暴击伤害"] += 0.25
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备53(装备):
    名称 = '精灵浮风棍'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '棍棒'
    力量 = 81
    智力 = 81
    物理攻击力 = 1328
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.26
        character.attr["附加伤害"] += 0.15
        character.attr["最终伤害"] += 0.21
        character.attr["技能攻击力"] *= 1.33
        character.skill_level_up_specified('斗神意志', 4)
        character.skill_level_up_specified('御风之力', 4)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.10


class 装备54(装备):
    名称 = '魔力之泉：加斯达利亚'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '魔杖'
    力量 = 0
    智力 = 122
    物理攻击力 = 1106
    魔法攻击力 = 1352
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.21
        character.attr["百分比三攻"] += 0.21
        character.attr["最终伤害"] += 0.21
        character.attr["技能攻击力"] *= 1.38

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.1
        character.attr["释放速度"] += 0.15


class 装备55(装备):
    名称 = '银月的祝福'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '法杖'
    力量 = 0
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1475
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.13
        character.attr["暴击伤害"] += 0.13
        character.attr["最终伤害"] += 0.25
        character.attr["技能攻击力"] *= 1.36
        character.skill_level_up_batched('所有', 50, 50, 2)
        character.skill_level_up_batched('所有', 85, 85, 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.1
        character.attr["魔法暴击率"] += 0.05


class 装备56(装备):
    名称 = '世界树之精灵'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '扫把'
    力量 = 0
    智力 = 81
    物理攻击力 = 1229
    魔法攻击力 = 1352
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.15
        character.attr["最终伤害"] += 0.26
        character.attr["技能攻击力"] *= 1.26
        character.skill_level_up_batched('所有', 50, 50, 2)
        character.skill_level_up_batched('所有', 85, 85, 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 50, 50, 2)
        character.skill_level_up_batched('所有', 85, 85, 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 转职被动智力=152)
        # character.attr["BUFF"] += BUFFLv=5)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["BUFF"] += BUFF物攻per=1.2, BUFF魔攻per=1.2, BUFF独立per=1.2)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=26)
        pass


class 装备57(装备):
    名称 = '闪耀的神威'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '十字架'
    力量 = 0
    智力 = 81
    体力 = 97
    精神 = 97
    物理攻击力 = 1229
    魔法攻击力 = 1167
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.3
        character.attr["暴击伤害"] += 0.3
        character.attr["技能攻击力"] *= 1.32
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=127)
        # character.attr["被动"] += 转职被动智力=127)
        # character.attr["BUFF"] += BUFFLv=5)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["BUFF"] += BUFF物攻per=1.2, BUFF魔攻per=1.2, BUFF独立per=1.2)
        # character.attr["觉醒"] += 一觉Lv=2)
        # character.attr["觉醒"] += 一觉力智=68)
        pass


class 装备58(装备):
    名称 = '古代神兽的记忆'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '念珠'
    力量 = 0
    智力 = 122
    物理攻击力 = 1106
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.33
        character.attr["暴击伤害"] += 0.36
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备59(装备):
    名称 = '拓荒者之路'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '图腾'
    力量 = 122
    智力 = 0
    物理攻击力 = 1290
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.31
        character.attr["百分比三攻"] += 0.24
        character.attr["暴击伤害"] += 0.1
        character.attr["技能攻击力"] *= 1.36

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.2


class 装备60(装备):
    名称 = '异教主的审判'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '镰刀'
    力量 = 81
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1229
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.2
        character.attr["暴击伤害"] += 0.24
        character.attr["附加伤害"] += 0.25
        character.attr["技能攻击力"] *= 1.31

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.14
        character.attr["移动速度"] += 0.14
        character.attr["释放速度"] += 0.21


class 装备61(装备):
    名称 = '信念之重量'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '战斧'
    力量 = 81
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1045
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.12
        character.attr["最终伤害"] += 0.55
        character.attr["技能攻击力"] *= 1.4

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.1


class 装备62(装备):
    名称 = '暗杀团长的玉妆刀'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '匕首'
    力量 = 81
    智力 = 0
    物理攻击力 = 1167
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.22
        character.attr["百分比三攻"] += 0.22
        character.attr["最终伤害"] += 0.22
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.1
        character.attr["释放速度"] += 0.15


class 装备63(装备):
    名称 = '血色舞会'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '双剑'
    力量 = 81
    智力 = 0
    物理攻击力 = 1343
    魔法攻击力 = 983
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.2
        character.attr["附加伤害"] += 0.21
        character.attr["最终伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.16
        pass

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["命中率"] += 0.05
        character.attr["回避率"] += 0.05


class 装备64(装备):
    名称 = '圣洁的精灵遗物'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '手杖'
    力量 = 0
    智力 = 81
    物理攻击力 = 1086
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.27
        character.attr["伤害增加"] += 0.13
        character.attr["暴击伤害"] += 0.27
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.12
        character.attr["命中率"] += 0.05


class 装备65(装备):
    名称 = '天幕道火扇'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '苦无'
    力量 = 0
    智力 = 122
    物理攻击力 = 1029
    魔法攻击力 = 1352
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.13
        character.attr["技能攻击力"] *= 1.28

    def 进图属性(self, character):
        character.attr["百分比三攻"] += 0.45
        character.skill_level_up_batched('所有', 1, 45, 3)
        character.skill_level_up_specified('烈焰印记', 3)
        character.skill_level_up_specified('火遁·冥炎业火阵', 2)

    def 其它属性(self, character):
        pass


class 装备66(装备):
    名称 = '彪悍冲锋者'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '长枪'
    力量 = 122
    智力 = 0
    物理攻击力 = 1290
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.26
        character.attr["百分比三攻"] += 0.13
        character.attr["伤害增加"] += 0.24
        character.attr["技能攻击力"] *= 1.38

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15


class 装备67(装备):
    名称 = '沙岩幻戟'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '战戟'
    力量 = 81
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1045
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.3
        character.attr["最终伤害"] += 0.24
        character.attr["技能攻击力"] *= 1.16
        character.skill_level_up_batched('所有', 1, 48, 2)
        character.skill_level_up_batched('所有', 60, 80, 2)
        character.skill_change_cooldown(1, 48, 0.19)
        character.skill_change_cooldown(60, 80, 0.19)
        character.skill_change_cooldown(90, 95, 0.19)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.2
        character.attr["移动速度"] += 0.2


class 装备68(装备):
    名称 = '天将军：传承之光'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '光枪'
    力量 = 81
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.1
        character.attr["暴击伤害"] += 0.34
        character.attr["最终伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.38

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备69(装备):
    名称 = '魅影飞龙'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '暗矛'
    力量 = 81
    智力 = 122
    物理攻击力 = 1167
    魔法攻击力 = 1290
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.26
        character.attr["暴击伤害"] += 0.35
        character.attr["技能攻击力"] *= 1.38
        character.skill_change_attr('暗蚀螺旋枪', 1.315316871, 1)
        character.skill_change_attr('暗蚀爆雷杀', 1.144086022, 1)
        character.skill_change_attr('无尽侵蚀：缚魂', 1.134989433, 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.1
        character.attr["释放速度"] += 0.1


class 装备70(装备):
    名称 = '夜天刀'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '长刀'
    力量 = 81
    智力 = 81
    物理攻击力 = 1328
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.14
        character.attr["最终伤害"] += 0.29
        character.attr["技能攻击力"] *= 1.16
        character.skill_level_up_specified('B.G枪刃改造', 3)
        character.skill_level_up_specified('B.C精锐特训', 3)
        character.skill_level_up_specified('电光飞掠', 2)
        character.skill_level_up_specified('集结·暮光之翼', 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备71(装备):
    名称 = '冥焰黑暗之触'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '小太刀'
    力量 = 81
    智力 = 41
    物理攻击力 = 1229
    魔法攻击力 = 1229
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.23
        character.attr["暴击伤害"] += 0.3
        character.attr["附加伤害"] += 0.14
        character.attr["技能攻击力"] *= 1.35

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.06
        character.attr["魔法暴击率"] += 0.06


class 装备72(装备):
    名称 = '爆烈红焰'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '重剑'
    力量 = 81
    智力 = 0
    物理攻击力 = 1475
    魔法攻击力 = 1106
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.17
        character.attr["属性附加"] += 0.2
        character.attr["最终伤害"] += 0.15
        character.attr["技能攻击力"] *= 1.28

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


class 装备73(装备):
    名称 = '谍影：超级核心'
    模式 = 0
    所属套装 = '无'
    等级 = 100
    品质 = '史诗'
    部位 = '武器'
    类型 = '源力剑'
    力量 = 0
    智力 = 81
    物理攻击力 = 1167
    魔法攻击力 = 1414
    独立攻击力 = 770

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.22
        character.attr["暴击伤害"] += 0.2
        character.attr["最终伤害"] += 0.2
        character.attr["技能攻击力"] *= 1.08
        character.skill_level_up_specified('源力剑精通', 3)
        try:
            character.attr["技能栏"][character.attr["技能序号"]['源力剑精通']].谍影专用倍率 = 2
        except:
            pass
        pass

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass


# endregion
