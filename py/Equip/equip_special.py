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
        character.附加伤害加成(0.14)

    def 其它属性(self, character):
        character.移动速度增加(0.05)

    def 变换属性(self, character):
        character.伤害增加加成(0.25, 3)


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
        character.技能攻击力加成(0.12)
        character.skill_change_cooldown(1, 100, 0.114)

    def 变换属性(self, character):
        character.百分比力智加成(0.15, 3)


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
        character.技能攻击力加成(0.12)

    def 进图属性(self, character):
        character.所有属性强化加成(40)

    def 其它属性(self, character):
        character.移动速度增加(0.10)

    def 变换属性(self, character):
        character.最终伤害加成(0.12, 3)


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
        character.伤害增加加成(0.20)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)

    def 变换属性(self, character):
        character.百分比力智加成(0.16, 3)


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

    def 进图属性(self, character):
        character.百分比三攻加成(0.24)

    def 变换属性(self, character):
        character.百分比三攻加成(0.18, 3)


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
        character.所有属性强化加成(64)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)
        character.释放速度增加(0.15)

    def 变换属性(self, character):
        character.暴击伤害加成(0.22, 3)


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
        character.百分比力智加成(0.16)
        character.百分比三攻加成(0.10)

    def 其它属性(self, character):
        character.攻击速度增加(0.04)
        character.移动速度增加(0.04)
        character.释放速度增加(0.06)
        if character.is_equip_exist('地狱边缘'):
            character.攻击速度增加(-0.01)
            character.移动速度增加(-0.01)
            character.释放速度增加(-0.015)
        if character.is_equip_exist('悲痛者项链'):
            character.攻击速度增加(-0.01)
            character.移动速度增加(-0.01)
            character.释放速度增加(-0.015)

    def 变换属性(self, character):
        character.伤害增加加成(0.11, 3)


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
        character.持续伤害加成(0.10)

    def 变换属性(self, character):
        character.最终伤害加成(0.30, 3)


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
        character.暴击伤害加成(0.21)
        character.技能攻击力加成(0.17)


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
        character.百分比三攻加成(0.24)
        character.最终伤害加成(0.15)


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
        character.百分比力智加成(0.12)
        character.最终伤害加成(0.12)

    def 进图属性(self, character):
        character.所有属性强化加成(40)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)


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
        character.最终伤害加成(0.13)
        character.技能攻击力加成(0.24)

    def 其它属性(self, character):
        character.释放速度增加(0.15)


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
        character.暴击伤害加成(0.35)
        character.技能攻击力加成(0.07)


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
        character.百分比力智加成(0.17)
        character.所有属性强化加成(80)
        character.skill_change_cooldown(1, 45, 0.10)


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
        character.暴击伤害加成(0.23)
        character.技能攻击力加成(0.13)


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
        character.百分比三攻加成(0.20)
        character.伤害增加加成(0.20)


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
            character.百分比力智加成(0.10)
        character.百分比三攻加成(0.15)
        character.最终伤害加成(0.17)

    def 其它属性(self, character):
        if character.is_equip_exist('军神的遗书'):
            character.移动速度增加(0.10)


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
        character.伤害增加加成(0.15)
        character.暴击伤害加成(0.24)


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
        character.伤害增加加成(0.16)
        character.附加伤害加成(0.10)

    def 进图属性(self, character):
        character.所有属性强化加成(40)

    def 其它属性(self, character):
        character.攻击速度增加(0.05)
        character.移动速度增加(0.05)
        character.释放速度增加(0.225)


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
        character.百分比力智加成(0.10)
        character.百分比三攻加成(0.12)
        if character.is_equip_exist('能量回流控制者'):
            character.附加伤害加成(0.10)

    def 进图属性(self, character):
        if character.is_equip_exist('电光能量支配者'):
            character.所有属性强化加成(40)


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
        character.最终伤害加成(0.42)


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
        character.暴击伤害加成(0.10)
        character.最终伤害加成(0.19)

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)


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
        character.百分比力智加成(0.10)
        character.暴击伤害加成(0.22)
        if '天命无常[2]' in character.attr["套装栏"]:
            character.最终伤害加成(0.091666667)


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
        character.伤害增加加成(0.15)
        character.暴击伤害加成(0.10)
        character.附加伤害加成(0.10)

    def 其它属性(self, character):
        character.攻击速度增加(0.021)


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

    def 城镇属性(self, character):
        character.技能攻击力加成(0.10)
        character.百分比三攻加成(0.15)
        character.最终伤害加成(0.17)
        character.附加伤害加成(0.04)
        character.百分比三攻加成(0.09)
        character.技能攻击力加成(0.04)
        character.最终伤害加成(0.07)

    def 其它属性(self, character):
        character.移动速度增加(0.15)


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

    def 城镇属性(self, character):
        character.伤害增加加成(0.15)
        character.暴击伤害加成(0.14)
        character.技能攻击力加成(0.10)
        character.百分比三攻加成(0.06)
        character.技能攻击力加成(0.04)
        character.附加伤害加成(0.08)
        character.百分比力智加成(0.05)


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

    def 城镇属性(self, character):
        character.附加伤害加成(0.10)
        character.伤害增加加成(0.16)
        character.所有属性强化加成(40)
        character.最终伤害加成(0.08)
        character.百分比力智加成(0.05)
        character.伤害增加加成(0.04)

    def 进图属性(self, character):
        character.所有属性强化加成(40)

    def 其它属性(self, character):
        character.攻击速度增加(0.15)
        character.移动速度增加(0.15)
        character.释放速度增加(0.375)


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

    def 城镇属性(self, character):
        character.百分比力智加成(0.10)
        character.百分比三攻加成(0.12)
        if character.is_equip_exist('能量回流控制者'):
            character.附加伤害加成(0.10)
        character.伤害增加加成(0.12)
        character.力智固定加成(220)
        character.附加伤害加成(0.12)

    def 进图属性(self, character):
        if character.is_equip_exist('电光能量支配者'):
            character.所有属性强化加成(40)

    def 其它属性(self, character):
        if character.is_equip_exist('能量回流控制者'):
            character.移动速度增加(0.10)


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

    def 城镇属性(self, character):
        character.最终伤害加成(0.42)
        character.最终伤害加成(0.12)
        character.所有属性强化加成(40)
        character.附加伤害加成(0.09)


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

    def 城镇属性(self, character):
        character.最终伤害加成(0.19)
        character.暴击伤害加成(0.10)
        character.力智固定加成(300)
        character.暴击伤害加成(0.11)
        character.skill_level_up_batched('所有', 60, 100, 1)

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        character.攻击速度增加(0.15)


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

    def 城镇属性(self, character):
        character.暴击伤害加成(0.22)
        character.百分比力智加成(0.10)
        if '天命无常[2]' in character.attr["套装栏"]:
            character.最终伤害加成(0.10)
        character.三攻固定加成(120)
        character.skill_level_up_batched('所有', 25, 45, 1)
        character.百分比力智加成(0.04)
        character.附加伤害加成(0.07)


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

    def 城镇属性(self, character):
        character.附加伤害加成(0.106)
        character.伤害增加加成(0.15)
        character.所有属性强化加成(16)
        character.持续伤害加成(0.10)
        character.暴击伤害加成(0.10)
        character.暴击伤害加成(0.08)
        character.力智固定加成(140)

    def 其它属性(self, character):
        character.移动速度增加(0.0315)

# endregion
