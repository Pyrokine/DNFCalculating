from py.base_equip import *


# region  100SS特殊
class 装备212(装备):
    名称 = '军神的遗书'
    模式 = 0
    所属套装 = '军神的隐秘遗产'
    等级 = 100
    品质 = '史诗'
    部位 = '辅助装备'
    类型 = '特殊'
    力量 = 146
    智力 = 146
    体力 = 46
    精神 = 46
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.25
        character.attr["附加伤害"] += 0.14

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.05
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=208)
        # character.attr["被动"] += 转职被动智力=124)
        # character.attr["BUFF"] += BUFF魔攻per=1.06)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备213(装备):
    名称 = '末日之刻'
    模式 = 0
    所属套装 = '时间战争的残骸'
    等级 = 100
    品质 = '史诗'
    部位 = '辅助装备'
    类型 = '特殊'
    力量 = 146
    智力 = 146
    体力 = 46
    精神 = 46
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.15
        character.attr["技能攻击力"] *= 1.12
        character.skill_change_cooldown(1, 100, 0.114)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=195)
        # character.attr["被动"] += 转职被动智力=98)
        # character.attr["BUFF"] += BUFF魔攻per=1.06)
        # character.attr["被动"] += 一觉被动Lv=1)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备214(装备):
    名称 = '高贵之天'
    模式 = 0
    所属套装 = '灵宝：世间真理'
    等级 = 100
    品质 = '史诗'
    部位 = '辅助装备'
    类型 = '特殊'
    力量 = 146
    智力 = 146
    体力 = 46
    精神 = 46
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.12
        character.attr["技能攻击力"] *= 1.12

    def 进图属性(self, character):
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=195)
        # character.attr["被动"] += 转职被动智力=130)
        # character.attr["BUFF"] += BUFF魔攻per=1.06)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备215(装备):
    名称 = '能量回流控制者'
    模式 = 0
    所属套装 = '能量主宰'
    等级 = 100
    品质 = '史诗'
    部位 = '辅助装备'
    类型 = '特殊'
    力量 = 146
    智力 = 146
    体力 = 46
    精神 = 46
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["伤害增加"] += 0.2

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=208)
        # character.attr["被动"] += 转职被动智力=124)
        # character.attr["BUFF"] += BUFF魔攻per=1.06)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备216(装备):
    名称 = '暗黑术士亲笔古书'
    模式 = 0
    所属套装 = '深渊窥视者'
    等级 = 100
    品质 = '史诗'
    部位 = '辅助装备'
    类型 = '特殊'
    力量 = 146
    智力 = 146
    体力 = 46
    精神 = 46
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.42

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=208)
        # character.attr["被动"] += 转职被动智力=156)
        # character.attr["BUFF"] += BUFF魔攻per=1.06)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备217(装备):
    名称 = '引路者的旅行书'
    模式 = 0
    所属套装 = '圣者的黄昏'
    等级 = 100
    品质 = '史诗'
    部位 = '辅助装备'
    类型 = '特殊'
    力量 = 146
    智力 = 146
    体力 = 46
    精神 = 46
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.22
        character.attr["火属性强化"] += 64
        character.attr["冰属性强化"] += 64
        character.attr["光属性强化"] += 64
        character.attr["暗属性强化"] += 64

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
        # character.attr["被动"] += 守护恩赐体精=195)
        # character.attr["被动"] += 转职被动智力=108)
        # character.attr["BUFF"] += BUFF魔攻per=1.06)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备218(装备):
    名称 = '悲情者遗物'
    模式 = 0
    所属套装 = '坎坷命运'
    等级 = 100
    品质 = '史诗'
    部位 = '辅助装备'
    类型 = '特殊'
    力量 = 146
    智力 = 146
    体力 = 46
    精神 = 46
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["百分比三攻"] += 0.1
        character.attr["伤害增加"] += 0.11

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
        if character.is_equip_exist('悲痛者项链'):
            character.attr["攻击速度"] += -0.01
            character.attr["移动速度"] += -0.01
            character.attr["释放速度"] += -0.015

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=208)
        # character.attr["被动"] += 转职被动智力=124)
        # character.attr["BUFF"] += BUFF魔攻per=1.06)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备219(装备):
    名称 = '失控之怒'
    模式 = 0
    所属套装 = '吞噬愤怒'
    等级 = 100
    品质 = '史诗'
    部位 = '辅助装备'
    类型 = '特殊'
    力量 = 146
    智力 = 146
    体力 = 46
    精神 = 46
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["持续伤害"] += 0.1
        character.attr["最终伤害"] += 0.3

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=208)
        # character.attr["被动"] += 转职被动智力=124)
        # character.attr["BUFF"] += BUFF魔攻per=1.06)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备220(装备):
    名称 = '军神的庇护宝石'
    模式 = 0
    所属套装 = '军神的隐秘遗产'
    等级 = 100
    品质 = '史诗'
    部位 = '魔法石'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.21
        character.attr["技能攻击力"] *= 1.17

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=170)
        # character.attr["被动"] += 转职被动智力=73)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备221(装备):
    名称 = '时之漩涡'
    模式 = 0
    所属套装 = '时间战争的残骸'
    等级 = 100
    品质 = '史诗'
    部位 = '魔法石'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.24
        character.attr["最终伤害"] += 0.15

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=138)
        # character.attr["被动"] += 转职被动智力=48)
        # 批量技能等级提升('所有', 1, 50, 1)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        pass


class 装备222(装备):
    名称 = '智慧之地'
    模式 = 0
    所属套装 = '灵宝：世间真理'
    等级 = 100
    品质 = '史诗'
    部位 = '魔法石'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.12
        character.attr["最终伤害"] += 0.12

    def 进图属性(self, character):
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=150)
        # character.attr["被动"] += 转职被动智力=45)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        # character.attr["被动"] += 一觉被动Lv=1)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备223(装备):
    名称 = '电光能量支配者'
    模式 = 0
    所属套装 = '能量主宰'
    等级 = 100
    品质 = '史诗'
    部位 = '魔法石'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.13
        character.attr["技能攻击力"] *= 1.24

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=130)
        # character.attr["被动"] += 转职被动智力=36)
        # character.attr["BUFF"] += BUFF力量per=1.06)
        # character.attr["BUFF"] += BUFF智力per=1.06)
        # 批量技能等级提升('所有', 1, 50, 1)
        pass


class 装备224(装备):
    名称 = '暗黑术士的精髓'
    模式 = 0
    所属套装 = '黑魔法探求者'
    等级 = 100
    品质 = '史诗'
    部位 = '魔法石'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.35
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
        # character.attr["被动"] += 守护恩赐体精=195)
        # character.attr["被动"] += 转职被动智力=95)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备225(装备):
    名称 = '被困的时之沙'
    模式 = 0
    所属套装 = '时空旅行者'
    等级 = 100
    品质 = '史诗'
    部位 = '魔法石'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.17
        character.attr["火属性强化"] += 80
        character.attr["冰属性强化"] += 80
        character.attr["光属性强化"] += 80
        character.attr["暗属性强化"] += 80
        character.skill_change_cooldown(1, 45, 0.10)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=142)
        # character.attr["被动"] += 转职被动智力=48)
        # 批量技能等级提升('所有', 1, 50, 1)
        # character.attr["BUFF"] += BUFF力量per=1.06)
        # character.attr["BUFF"] += BUFF智力per=1.06)
        pass


class 装备226(装备):
    名称 = '寂寞的呼喊'
    模式 = 0
    所属套装 = '穿透命运的呐喊'
    等级 = 100
    品质 = '史诗'
    部位 = '魔法石'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.23
        character.attr["技能攻击力"] *= 1.13

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=155)
        # character.attr["被动"] += 转职被动智力=48)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        # character.attr["被动"] += 一觉被动Lv=1)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备227(装备):
    名称 = '狂乱之天灾降临'
    模式 = 0
    所属套装 = '狂乱追随者'
    等级 = 100
    品质 = '史诗'
    部位 = '魔法石'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.2
        character.attr["伤害增加"] += 0.2

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=170)
        # character.attr["被动"] += 转职被动智力=73)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08)
        # character.attr["BUFF"] += BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉Lv=1)
        pass


class 装备228(装备):
    名称 = '军神的古怪耳环'
    模式 = 0
    所属套装 = '军神的隐秘遗产'
    等级 = 100
    品质 = '史诗'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        if character.is_equip_exist('军神的遗书'):
            character.attr["百分比力智"] += 0.10
        character.attr["百分比三攻"] += 0.15
        character.attr["最终伤害"] += 0.17

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        if character.is_equip_exist('军神的遗书'):
            character.attr["移动速度"] += 0.10

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=158)
        # character.attr["被动"] += 转职被动智力=62)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        pass


class 装备229(装备):
    名称 = '时之矛盾'
    模式 = 0
    所属套装 = '时间战争的残骸'
    等级 = 100
    品质 = '史诗'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.15
        character.attr["暴击伤害"] += 0.24

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=143)
        # character.attr["被动"] += 转职被动智力=49)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        pass


class 装备230(装备):
    名称 = '宽容之海'
    模式 = 0
    所属套装 = '灵宝：世间真理'
    等级 = 100
    品质 = '史诗'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.16
        character.attr["附加伤害"] += 0.1

    def 进图属性(self, character):
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.05
        character.attr["移动速度"] += 0.05
        character.attr["释放速度"] += 0.225

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=143)
        # character.attr["被动"] += 转职被动智力=62)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        pass


class 装备231(装备):
    名称 = '电磁能量传送者'
    模式 = 0
    所属套装 = '能量主宰'
    等级 = 100
    品质 = '史诗'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.12
        if character.is_equip_exist('能量回流控制者'):
            character.attr["附加伤害"] += 0.1

    def 进图属性(self, character):
        if character.is_equip_exist('电光能量支配者'):
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
        # character.attr["被动"] += 守护恩赐体精=158)
        # character.attr["被动"] += 转职被动智力=62)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        pass


class 装备232(装备):
    名称 = '无尽地狱黑暗之印'
    模式 = 0
    所属套装 = '地狱求道者'
    等级 = 100
    品质 = '史诗'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.42

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=192)
        # character.attr["被动"] += 转职被动智力=95)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        pass


class 装备233(装备):
    名称 = '次元流星坠'
    模式 = 0
    所属套装 = '次元旅行者'
    等级 = 100
    品质 = '史诗'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.1
        character.attr["最终伤害"] += 0.19

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=178)
        # character.attr["被动"] += 转职被动智力=82)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        pass


class 装备234(装备):
    名称 = '命运挑战者'
    模式 = 0
    所属套装 = '天命无常'
    等级 = 100
    品质 = '史诗'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["暴击伤害"] += 0.22
        if '天命无常[2]' in character.attr["套装栏"]:
            character.attr["最终伤害"] += 0.05

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=146)
        # character.attr["被动"] += 转职被动智力=45)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        pass


class 装备235(装备):
    名称 = '悲剧人生的归寂'
    模式 = 0
    所属套装 = '悲剧的残骸'
    等级 = 100
    品质 = '史诗'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 169
    智力 = 169
    体力 = 69
    精神 = 69
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.15
        character.attr["暴击伤害"] += 0.1
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
        # character.attr["被动"] += 守护恩赐体精=166)
        # character.attr["被动"] += 转职被动智力=62)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        pass


class 装备236(装备):
    名称 = '军神的心之所念'
    模式 = 0
    所属套装 = '军神的隐秘遗产'
    等级 = 100
    品质 = '神话'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 171
    智力 = 171
    体力 = 70
    精神 = 70
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '附加伤害：'
    属性1范围 = [4, 1, 1]
    属性1选择 = 0
    属性2描述 = '百分比三攻：'
    属性2范围 = [9, 1, 1]
    属性2选择 = 0
    属性3描述 = '技能攻击力：'
    属性3范围 = [4, 1, 1]
    属性3选择 = 0
    属性4描述 = '最终伤害：'
    属性4范围 = [7, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.10
        character.attr["百分比三攻"] += 0.15
        character.attr["最终伤害"] += 0.17
        character.attr["附加伤害"] += 0.04
        character.attr["百分比三攻"] += 0.09
        character.attr["技能攻击力"] *= 1.04
        character.attr["最终伤害"] += 0.07

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.15

    # 专属属性
    属性1描述_BUFF = '一觉被动(160/140)+'
    属性1范围_BUFF = [60, 0, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [90, 10, 10]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '转职被动：'
    属性3范围_BUFF = [160, 100, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '一觉力智'
    属性4范围_BUFF = [7, 1, 1]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=158)
        # character.attr["被动"] += 转职被动智力=62)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 信念光环体精=220 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=200 - self.属性1选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智=90 - self.属性2选择_BUFF * 10)
        # character.attr["被动"] += 守护恩赐体精=160 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=160 - self.属性3选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智per=1.07 - self.属性4选择_BUFF / 100)
        pass


class 装备237(装备):
    名称 = '时之魅影'
    模式 = 0
    所属套装 = '时间战争的残骸'
    等级 = 100
    品质 = '神话'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 171
    智力 = 171
    体力 = 70
    精神 = 70
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '百分比三攻：'
    属性1范围 = [6, 1, 1]
    属性1选择 = 0
    属性2描述 = '技能攻击力：'
    属性2范围 = [4, 1, 1]
    属性2选择 = 0
    属性3描述 = '附加伤害：'
    属性3范围 = [8, 1, 1]
    属性3选择 = 0
    属性4描述 = '百分比力智：'
    属性4范围 = [5, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.15
        character.attr["暴击伤害"] += 0.24
        character.attr["百分比三攻"] += 0.06
        character.attr["技能攻击力"] *= 1.04
        character.attr["附加伤害"] += 0.08
        character.attr["百分比力智"] += 0.05

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = '一觉力智'
    属性1范围_BUFF = [70, 20, 10]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '转职被动：'
    属性2范围_BUFF = [200, 140, 20]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF力智：'
    属性3范围_BUFF = [11, 4, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '一觉力智'
    属性4范围_BUFF = [6, 2, 1]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=143)
        # character.attr["被动"] += 转职被动智力=49)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智=70 - self.属性1选择_BUFF * 10)
        # character.attr["被动"] += 守护恩赐体精=200 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=200 - self.属性2选择_BUFF * 20)
        # character.attr["BUFF"] += BUFF力量per=1.11 - self.属性3选择_BUFF / 100, BUFF智力per=1.11 - self.属性3选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智per=1.06 - self.属性4选择_BUFF / 100)
        pass


class 装备238(装备):
    名称 = '永恒之海'
    模式 = 0
    所属套装 = '灵宝：世间真理'
    等级 = 100
    品质 = '神话'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 171
    智力 = 171
    体力 = 70
    精神 = 70
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '所有属性强化 +'
    属性1范围 = [40, 20, 4]
    属性1选择 = 0
    属性2描述 = '最终伤害：'
    属性2范围 = [8, 1, 1]
    属性2选择 = 0
    属性3描述 = '百分比力智：'
    属性3范围 = [5, 1, 1]
    属性3选择 = 0
    属性4描述 = '伤害增加：'
    属性4范围 = [4, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.1
        character.attr["伤害增加"] += 0.16
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40
        character.attr["最终伤害"] += 0.08
        character.attr["百分比力智"] += 0.05
        character.attr["伤害增加"] += 0.04

    def 进图属性(self, character):
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.375

    # 专属属性
    属性1描述_BUFF = '一觉力智'
    属性1范围_BUFF = [6, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [80, 10, 10]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '转职被动：'
    属性3范围_BUFF = [300, 220, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '一觉被动(100/80）'
    属性4范围_BUFF = [60, 0, 20]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=143)
        # character.attr["被动"] += 转职被动智力=62)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智per=1.06 - self.属性1选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智=80 - self.属性2选择_BUFF * 10)
        # character.attr["被动"] += 守护恩赐体精=300 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=300 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 信念光环体精=160 - self.属性4选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=140 - self.属性4选择_BUFF * 20)
        pass


class 装备239(装备):
    名称 = '等离子操控者'
    模式 = 0
    所属套装 = '能量主宰'
    等级 = 100
    品质 = '神话'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 171
    智力 = 171
    体力 = 70
    精神 = 70
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '伤害增加：'
    属性1范围 = [12, 1, 1]
    属性1选择 = 0
    属性2描述 = '力量/智力 +'
    属性2范围 = [220, 100, 20]
    属性2选择 = 0
    属性3描述 = '附加伤害：'
    属性3范围 = [12, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.1
        character.attr["百分比三攻"] += 0.12
        if character.is_equip_exist('能量回流控制者'):
            character.attr["附加伤害"] += 0.1
        character.attr["伤害增加"] += 0.12
        character.attr["力量"] += 220
        character.attr["智力"] += 220
        character.attr["附加伤害"] += 0.12

    def 进图属性(self, character):
        if character.is_equip_exist('电光能量支配者'):
            character.attr["火属性强化"] += 40
            character.attr["冰属性强化"] += 40
            character.attr["光属性强化"] += 40
            character.attr["暗属性强化"] += 40

    def 其它属性(self, character):
        if character.is_equip_exist('能量回流控制者'):
            character.attr["移动速度"] += 0.1

    # 专属属性
    属性1描述_BUFF = 'BUFF三攻：'
    属性1范围_BUFF = [12, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '守护恩赐/力智：'
    属性2范围_BUFF = [220, 100, 20]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [120, 10, 10]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 转职被动智力=62)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        # character.attr["被动"] += 守护恩赐体精=158)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF物攻per=1.12 - self.属性1选择_BUFF / 100, BUFF魔攻per=1.12 - self.属性1选择_BUFF / 100, BUFF独立per=1.12 - self.属性1选择_BUFF / 100)
        # character.attr["力智固定"] += x=220 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 守护恩赐体精=220 - self.属性2选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智=120 - self.属性3选择_BUFF * 10)
        pass


class 装备240(装备):
    名称 = '永恒地狱黑暗之印'
    模式 = 0
    所属套装 = '地狱求道者'
    等级 = 100
    品质 = '神话'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 171
    智力 = 171
    体力 = 70
    精神 = 70
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '最终伤害：'
    属性1范围 = [12, 1, 1]
    属性1选择 = 0
    属性2描述 = '所有属性强化 +'
    属性2范围 = [40, 8, 4]
    属性2选择 = 0
    属性3描述 = '附加伤害：'
    属性3范围 = [9, 1, 1]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.42
        character.attr["最终伤害"] += 0.12
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40
        character.attr["附加伤害"] += 0.09

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = 'BUFF力智：'
    属性1范围_BUFF = [12, 1, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '转职被动：'
    属性2范围_BUFF = [240, 80, 20]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [90, 10, 10]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=192)
        # character.attr["被动"] += 转职被动智力=95)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF力量per=1.12 - self.属性1选择_BUFF / 100, BUFF智力per=1.12 - self.属性1选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐体精=240 - self.属性2选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=240 - self.属性2选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智=90 - self.属性3选择_BUFF * 10)
        pass


class 装备241(装备):
    名称 = '次元穿越者之星'
    模式 = 0
    所属套装 = '次元旅行者'
    等级 = 100
    品质 = '神话'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 171
    智力 = 171
    体力 = 70
    精神 = 70
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '力量/智力 +'
    属性1范围 = [300, 20, 20]
    属性1选择 = 0
    属性2描述 = '暴击伤害：'
    属性2范围 = [11, 1, 1]
    属性2选择 = 0
    属性3描述 = '技能等级Lv60 -'
    属性3范围 = [100, 70, 5]
    属性3选择 = 0
    属性4描述 = '无'
    属性4范围 = []
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.19
        character.attr["力量"] += 300
        character.attr["智力"] += 300
        character.attr["暴击伤害"] += 0.21
        character.skill_level_up_batched('所有', 60, 100, 1)

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15

    # 专属属性
    属性1描述_BUFF = '守护恩赐/力智：'
    属性1范围_BUFF = [300, 20, 20]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [110, 10, 10]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉被动(60/40)+'
    属性3范围_BUFF = [100, 0, 20]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '无'
    属性4范围_BUFF = [0, 0, 0]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 60, 100, 1)

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=178 - self.属性1选择_BUFF * 20)
        # character.attr["被动"] += 转职被动智力=82)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["被动"] += 守护恩赐体精=300 - self.属性1选择_BUFF * 20)
        # character.attr["力智固定"] += x=300 - self.属性1选择_BUFF * 20)
        # character.attr["觉醒"] += 一觉力智=110 - self.属性2选择_BUFF * 10)
        # character.attr["被动"] += 信念光环体精=160 - self.属性3选择_BUFF * 20)
        # character.attr["被动"] += 一觉被动力智=140 - self.属性3选择_BUFF * 20)
        pass


class 装备242(装备):
    名称 = '命运反抗者'
    模式 = 0
    所属套装 = '天命无常'
    等级 = 100
    品质 = '神话'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 171
    智力 = 171
    体力 = 70
    精神 = 70
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '物攻/魔攻/独立 +'
    属性1范围 = [120, 40, 10]
    属性1选择 = 0
    属性2描述 = '技能等级Lv25 -'
    属性2范围 = [45, 30, 5]
    属性2选择 = 0
    属性3描述 = '百分比力智：'
    属性3范围 = [4, 1, 1]
    属性3选择 = 0
    属性4描述 = '附加伤害：'
    属性4范围 = [7, 1, 1]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.22
        character.attr["百分比力智"] += 0.1
        if '天命无常[2]' in character.attr["套装栏"]:
            character.attr["最终伤害"] += 0.06
        character.attr["物理攻击力"] += 120
        character.attr["魔法攻击力"] += 120
        character.attr["独立攻击力"] += 120
        character.skill_level_up_batched('所有', 25, 45, 1)
        character.attr["百分比力智"] += 0.04
        character.attr["附加伤害"] += 0.07

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    # 专属属性
    属性1描述_BUFF = '一觉力智：'
    属性1范围_BUFF = [90, 10, 10]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = '一觉力智：'
    属性2范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = 'BUFF力智：'
    属性3范围_BUFF = [4, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = 'BUFF三攻：'
    属性4范围_BUFF = [7, 1, 1]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 25, 45, 1)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=146)
        # character.attr["被动"] += 转职被动智力=45)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["觉醒"] += 一觉力智=90 - self.属性1选择_BUFF * 10)
        # character.attr["觉醒"] += 一觉力智per=1.04 - self.属性2选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF力量per=1.04 - self.属性3选择_BUFF / 100, BUFF智力per=1.04 - self.属性3选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF物攻per=1.07 - self.属性4选择_BUFF / 100, BUFF魔攻per=1.07 - self.属性4选择_BUFF / 100, BUFF独立per=1.07 - self.属性4选择_BUFF / 100)
        pass


class 装备243(装备):
    名称 = '心痛如绞的诀别'
    模式 = 0
    所属套装 = '悲剧的残骸'
    等级 = 100
    品质 = '神话'
    部位 = '耳环'
    类型 = '特殊'
    力量 = 171
    智力 = 171
    体力 = 70
    精神 = 70
    物理攻击力 = 0
    魔法攻击力 = 0
    独立攻击力 = 0

    属性1描述 = '所有属性强化 +'
    属性1范围 = [16, 8, 4]
    属性1选择 = 0
    属性2描述 = '持续伤害：'
    属性2范围 = [10, 1, 1]
    属性2选择 = 0
    属性3描述 = '暴击伤害：'
    属性3范围 = [8, 1, 1]
    属性3选择 = 0
    属性4描述 = '力量/智力 +'
    属性4范围 = [140, 80, 20]
    属性4选择 = 0

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.106
        character.attr["伤害增加"] += 0.15
        character.attr["火属性强化"] += 16
        character.attr["冰属性强化"] += 16
        character.attr["光属性强化"] += 16
        character.attr["暗属性强化"] += 16
        character.attr["持续伤害"] += 0.1
        character.attr["暴击伤害"] += 0.18
        character.attr["力量"] += 140
        character.attr["智力"] += 140

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.0315

    # 专属属性
    属性1描述_BUFF = 'BUFF三攻：'
    属性1范围_BUFF = [5, 3, 1]  # 最大值 最小值 间隔
    属性1选择_BUFF = 0
    属性2描述_BUFF = 'BUFF力智：'
    属性2范围_BUFF = [10, 1, 1]  # 最大值 最小值 间隔
    属性2选择_BUFF = 0
    属性3描述_BUFF = '一觉力智：'
    属性3范围_BUFF = [8, 1, 1]  # 最大值 最小值 间隔
    属性3选择_BUFF = 0
    属性4描述_BUFF = '守护恩赐/力智：'
    属性4范围_BUFF = [140, 40, 20]  # 间隔
    属性4选择_BUFF = 0

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        # character.attr["被动"] += 守护恩赐体精=166)
        # character.attr["被动"] += 转职被动智力=62)
        # character.attr["BUFF"] += BUFF独立per=1.06)
        # self.属性描述 += '<font color="#00A2E8">神话属性：</font><br>'
        # character.attr["BUFF"] += BUFF物攻per=1.05 - self.属性1选择_BUFF / 100, BUFF魔攻per=1.05 - self.属性1选择_BUFF / 100, BUFF独立per=1.05 - self.属性1选择_BUFF / 100)
        # character.attr["BUFF"] += BUFF力量per=1.10 - self.属性2选择_BUFF / 100, BUFF智力per=1.10 - self.属性2选择_BUFF / 100)
        # character.attr["觉醒"] += 一觉力智per=1.08 - self.属性3选择_BUFF / 100)
        # character.attr["被动"] += 守护恩赐体精=140 - self.属性4选择_BUFF * 20)
        # character.attr["力智固定"] += x=140 - self.属性4选择_BUFF * 20)
        pass


# endregion
