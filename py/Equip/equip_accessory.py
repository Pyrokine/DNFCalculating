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
        character.attr["技能攻击力"] *= 1.20
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1


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
        character.attr["技能攻击力"] *= 1.05 + 0.01 * min(13, character.fetch_strengthen_level(self.部位))
        character.attr["火属性强化"] += 28
        character.attr["冰属性强化"] += 28
        character.attr["光属性强化"] += 28
        character.attr["暗属性强化"] += 28

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 48, 1)
        character.skill_change_recovery(15, 30, 0.30)


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

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["释放速度"] += 0.15


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

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.06
        character.attr["百分比三攻"] += 0.03
        character.attr["暴击伤害"] += 0.09
        character.attr["附加伤害"] += 0.06
        character.attr["技能攻击力"] *= 1.25
        character.attr["技能攻击力"] *= 1.06
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += 0.1
        character.attr["释放速度"] += 0.15


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

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.06
        character.attr["火属性强化"] += 28
        character.attr["冰属性强化"] += 28
        character.attr["光属性强化"] += 28
        character.attr["暗属性强化"] += 28
        character.attr["技能攻击力"] *= 1.05 + 0.01 * min(13, character.fetch_strengthen_level(self.部位))
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

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.07
        character.attr["移动速度"] += 0.07
        character.attr["释放速度"] += 0.07


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

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.20
        character.attr["火属性强化"] += 38
        character.attr["冰属性强化"] += 38
        character.attr["光属性强化"] += 38
        character.attr["暗属性强化"] += 38
        character.attr["技能攻击力"] *= 1.13
        character.attr["力量"] += 160
        character.attr["智力"] += 160
        character.attr["最终伤害"] += 0.12
        character.attr["百分比三攻"] += 0.12


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

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.20
        character.attr["技能攻击力"] *= 1.10
        character.attr["力量"] += 240
        character.attr["智力"] += 240
        character.attr["附加伤害"] += 0.07
        character.attr["百分比三攻"] += 0.12

    def 进图属性(self, character):
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40


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

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.28
        character.attr["百分比力智"] += 0.12
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

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["释放速度"] += 0.15


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

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.12
        character.attr["最终伤害"] += 0.18
        character.attr["技能攻击力"] *= 1.06
        character.attr["技能攻击力"] *= 1.03
        character.attr["附加伤害"] += 0.04
        character.attr["百分比力智"] += 0.07
        character.attr["百分比三攻"] += 0.12

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.08
        character.attr["移动速度"] += 0.08
        character.attr["释放速度"] += 0.12


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

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.3
        character.attr["技能攻击力"] *= 1.11
        character.attr["伤害增加"] += 0.1
        character.attr["火属性强化"] += 32
        character.attr["冰属性强化"] += 32
        character.attr["光属性强化"] += 32
        character.attr["暗属性强化"] += 32
        character.attr["暴击伤害"] += 0.12


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
        character.attr["百分比力智"] += 0.05 + 0.01 * min(13, character.fetch_strengthen_level(self.部位))
        character.attr["百分比三攻"] += 0.06
        character.attr["火属性强化"] += 28
        character.attr["冰属性强化"] += 28
        character.attr["光属性强化"] += 28
        character.attr["暗属性强化"] += 28

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 50, 70, 1)
        character.skill_change_recovery(35, 45, 0.30)


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

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.1


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
        character.attr["附加伤害"] += 0.12
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["释放速度"] += 0.15

    def 变换属性(self, character):
        character.attr["百分比力智"] += 0.20


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
        character.attr["伤害增加"] += 0.01 * min(13, character.fetch_strengthen_level(self.部位))
        character.attr["火属性强化"] += 30
        character.attr["冰属性强化"] += 30
        character.attr["光属性强化"] += 30
        character.attr["暗属性强化"] += 30

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 75, 85, 1)
        character.skill_change_recovery(60, 80, 0.30)

    def 变换属性(self, character):
        character.attr["伤害增加"] += 0.05


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
        character.attr["最终伤害"] += 0.07

    def 变换属性(self, character):
        character.attr["暴击伤害"] += 0.07


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
        character.attr["火属性强化"] += 38
        character.attr["冰属性强化"] += 38
        character.attr["光属性强化"] += 38
        character.attr["暗属性强化"] += 38

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.04
        character.attr["移动速度"] += 0.04
        character.attr["释放速度"] += 0.06

    def 变换属性(self, character):
        character.attr["最终伤害"] += 0.27


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

    def 进图属性(self, character):
        character.attr["暴击伤害"] += 0.20

    def 变换属性(self, character):
        character.attr["暴击伤害"] += 0.20


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
        character.attr["技能攻击力"] *= 1.18

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 60, 80, 1)

    def 其它属性(self, character):
        character.attr["释放速度"] += 0.15

    def 变换属性(self, character):
        character.attr["百分比力智"] += 0.14


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
                character.attr["伤害增加"] += 0.11
            else:
                character.attr["伤害增加"] += 0.10
        character.attr["最终伤害"] += 0.06
        character.attr["技能攻击力"] *= 1.19

    def 变换属性(self, character):
        character.attr["最终伤害"] += 0.06


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
        if character.is_equip_exist('心痛如绞的诀别'):
            character.attr["附加伤害"] += 0.106
        else:
            character.attr["附加伤害"] += 0.10

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.021

    def 变换属性(self, character):
        character.attr["暴击伤害"] += 0.27

# endregion
