from py.base_equip import *


# region  防具套装

class 套装效果0(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.最终伤害加成(0.14)
        character.技能攻击力加成(0.14)


class 套装效果1(套装):
    名称 = '死亡阴影'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.16)
        character.所有属性强化加成(55)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)
        character.释放速度增加(0.15)


class 套装效果2(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.22)
        character.技能攻击力加成(0.06)


class 套装效果3(套装):
    名称 = '噩梦：地狱之路'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.16)
        character.最终伤害加成(0.06)
        character.技能攻击力加成(0.06)


class 套装效果4(套装):
    名称 = '永恒不息之路'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.31)


class 套装效果5(套装):
    名称 = '天堂舞姬'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.17)
        character.最终伤害加成(0.10)


class 套装效果6(套装):
    名称 = '皇家裁决者宣言'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.伤害增加加成(0.16)
        character.所有属性强化加成(52)

    def 其它属性(self, character):
        character.命中率增加(0.05)


class 套装效果7(套装):
    名称 = '炙炎之盛宴'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.18)
        character.所有属性强化加成(40)


class 套装效果8(套装):
    名称 = '传奇铁匠-封神'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.14)
        character.最终伤害加成(0.14)


class 套装效果9(套装):
    名称 = '命运歧路'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.伤害增加加成(0.15)
        character.附加伤害加成(0.13)


class 套装效果10(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.08)
        character.伤害增加加成(0.21)

    def 其它属性(self, character):
        character.回避率增加(0.06)


class 套装效果11(套装):
    名称 = '龙血玄黄'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.23)

    def 其它属性(self, character):
        character.物理暴击率增加(0.10)
        character.魔法暴击率增加(0.10)


class 套装效果12(套装):
    名称 = '擎天战甲'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.伤害增加加成(0.15)
        character.暴击伤害加成(0.15)


class 套装效果13(套装):
    名称 = '荆棘漫天'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.伤害增加加成(0.12)
        character.暴击伤害加成(0.11)

    def 其它属性(self, character):
        character.物理暴击率增加(0.10)
        character.魔法暴击率增加(0.10)


class 套装效果14(套装):
    名称 = '大自然的呼吸'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.16)
        character.暴击伤害加成(0.15)


class 套装效果15(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.伤害增加加成(0.22)
        character.暴击伤害加成(0.10)


class 套装效果16(套装):
    名称 = '死亡阴影'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.最终伤害加成(0.14)
        character.技能攻击力加成(0.16)


class 套装效果17(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.15)
        character.所有属性强化加成(60)


class 套装效果18(套装):
    名称 = '噩梦：地狱之路'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.所有属性强化加成(66)

        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)


class 套装效果19(套装):
    名称 = '永恒不息之路'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.最终伤害加成(0.32)


class 套装效果20(套装):
    名称 = '天堂舞姬'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.11)
        character.技能攻击力加成(0.15)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)
        character.移动速度增加(0.10)
        character.释放速度增加(0.15)


class 套装效果21(套装):
    名称 = '皇家裁决者宣言'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.15)
        character.所有属性强化加成(62)

    def 其它属性(self, character):
        character.攻击速度增加(0.05)
        character.移动速度增加(0.05)
        character.释放速度增加(0.08)


class 套装效果22(套装):
    名称 = '炙炎之盛宴'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.附加伤害加成(0.10)
        character.技能攻击力加成(0.20)

    def 其它属性(self, character):
        character.物理暴击率增加(0.05)
        character.魔法暴击率增加(0.05)


class 套装效果23(套装):
    名称 = '传奇铁匠-封神'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.21)
        if character.is_equip_exist('天堂之翼'):
            character.skill_change_cooldown(1, 45, 0.30)
            character.skill_change_cooldown(60, 80, 0.30)
        else:
            character.skill_change_cooldown(1, 45, 0.20)
            character.skill_change_cooldown(60, 80, 0.20)


class 套装效果24(套装):
    名称 = '命运歧路'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.12)
        character.暴击伤害加成(0.17)

    def 其它属性(self, character):
        character.攻击速度增加(0.21)
        character.移动速度增加(0.21)
        character.释放速度增加(0.315)


class 套装效果25(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.08)
        character.附加伤害加成(0.21)


class 套装效果26(套装):
    名称 = '龙血玄黄'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.24)
        character.所有属性强化加成(24)


class 套装效果27(套装):
    名称 = '擎天战甲'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.32)


class 套装效果28(套装):
    名称 = '荆棘漫天'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.附加伤害加成(0.25)
        character.skill_change_cooldown(1, 45, 0.15)
        character.skill_change_cooldown(60, 80, 0.15)
        character.skill_change_cooldown(90, 95, 0.15)


class 套装效果29(套装):
    名称 = '大自然的呼吸'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.伤害增加加成(0.15)
        character.技能攻击力加成(0.13)

    def 其它属性(self, character):
        character.攻击速度增加(0.05)
        character.移动速度增加(0.05)
        character.释放速度增加(0.10)


class 套装效果30(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.百分比力智加成(0.19)
        character.skill_level_up_batched('所有', 1, 85, 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 其它属性(self, character):
        character.物理暴击率增加(0.05)
        character.魔法暴击率增加(0.05)


class 套装效果31(套装):
    名称 = '死亡阴影'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.458)


class 套装效果32(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.44)
        character.技能攻击力加成(0.04)


class 套装效果33(套装):
    名称 = '噩梦：地狱之路'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.46)


class 套装效果34(套装):
    名称 = '永恒不息之路'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.22)
        character.百分比三攻加成(0.23)

    def 其它属性(self, character):
        character.攻击速度增加(0.15)
        character.释放速度增加(0.225)


class 套装效果35(套装):
    名称 = '天堂舞姬'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.40)

    def 其它属性(self, character):
        character.物理暴击率增加(0.10)
        character.魔法暴击率增加(0.10)


class 套装效果36(套装):
    名称 = '皇家裁决者宣言'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.属性附加加成(0.20)


class 套装效果37(套装):
    名称 = '炙炎之盛宴'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.最终伤害加成(0.26)
        character.skill_change_cooldown(1, 100, 0.15)
        character.技能攻击力加成(0.08)

    def 其它属性(self, character):
        character.攻击速度增加(0.05)
        character.攻击速度增加(0.05)
        character.移动速度增加(0.05)


class 套装效果38(套装):
    名称 = '传奇铁匠-封神'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.附加伤害加成(0.17)
        character.技能攻击力加成(0.20)
        character.skill_change_cooldown(50, 50, 0.30)
        character.skill_change_cooldown(85, 85, 0.30)
        character.skill_change_cooldown(100, 100, 0.17)

    def 其它属性(self, character):
        character.攻击速度增加(0.15)
        character.移动速度增加(0.15)
        character.释放速度增加(0.20)


class 套装效果39(套装):
    名称 = '命运歧路'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.12)
        character.技能攻击力加成(0.27)


class 套装效果40(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.45)


class 套装效果41(套装):
    名称 = '龙血玄黄'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.12)
        character.附加伤害加成(0.29)

    def 其它属性(self, character):
        character.攻击速度增加(0.15)
        character.移动速度增加(0.15)
        character.释放速度增加(0.225)


class 套装效果42(套装):
    名称 = '擎天战甲'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.属性附加加成(0.12)
        character.技能攻击力加成(0.10)

    def 其它属性(self, character):
        character.攻击速度增加(0.20)
        character.移动速度增加(0.20)
        character.释放速度增加(0.30)


class 套装效果43(套装):
    名称 = '荆棘漫天'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.伤害增加加成(0.10)
        character.技能攻击力加成(0.32)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)
        character.移动速度增加(-0.02 + 0.05)
        character.释放速度增加(0.1 + 0.12)


class 套装效果44(套装):
    名称 = '大自然的呼吸'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.最终伤害加成(0.11)
        character.技能攻击力加成(0.10)
        character.所有属性强化加成(64)

    def 其它属性(self, character):
        character.物理暴击率增加(0.10)
        character.魔法暴击率增加(0.10)


# endregion


# region  散搭套装

class 套装效果45(套装):
    名称 = '深渊窥视者'
    件数 = 2
    类型 = '上链左'

    def 城镇属性(self, character):
        character.伤害增加加成(0.09)

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 48, 2)


class 套装效果46(套装):
    名称 = '圣者的黄昏'
    件数 = 2
    类型 = '上链左'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.11)
        character.附加伤害加成(0.10)

    def 其它属性(self, character):
        character.移动速度增加(0.05)


class 套装效果47(套装):
    名称 = '坎坷命运'
    件数 = 2
    类型 = '上链左'

    def 城镇属性(self, character):
        character.伤害增加加成(0.14)
        character.技能攻击力加成(0.09)

    def 其它属性(self, character):
        character.攻击速度增加(0.03)
        character.移动速度增加(0.03)
        character.释放速度增加(0.045)
        if character.is_equip_exist('地狱边缘'):
            character.attr["攻击速度"] -= 0.01
            character.attr["移动速度"] -= 0.01
            character.attr["释放速度"] -= 0.015


class 套装效果48(套装):
    名称 = '吞噬愤怒'
    件数 = 2
    类型 = '上链左'

    def 城镇属性(self, character):
        character.伤害增加加成(0.10)
        character.暴击伤害加成(0.11)

    def 其它属性(self, character):
        if character.is_equip_exist('灭世之怒'):
            character.攻击速度增加(0.15)
            character.移动速度增加(0.15)
            character.释放速度增加(0.225)
        else:
            character.攻击速度增加(0.10)
            character.移动速度增加(0.10)
            character.释放速度增加(0.15)


class 套装效果49(套装):
    名称 = '黑魔法探求者'
    件数 = 2
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.伤害增加加成(0.12)
        character.技能攻击力加成(0.10)


class 套装效果50(套装):
    名称 = '时空旅行者'
    件数 = 2
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.10)
        character.最终伤害加成(0.10)


class 套装效果51(套装):
    名称 = '穿透命运的呐喊'
    件数 = 2
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.23)


class 套装效果52(套装):
    名称 = '狂乱追随者'
    件数 = 2
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.百分比力智加成(0.18)
        character.所有属性强化加成(25)

    def 其它属性(self, character):
        character.攻击速度增加(0.15)
        character.释放速度增加(0.225)


class 套装效果53(套装):
    名称 = '地狱求道者'
    件数 = 2
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.附加伤害加成(0.10)
        character.最终伤害加成(0.10)


class 套装效果54(套装):
    名称 = '次元旅行者'
    件数 = 2
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.附加伤害加成(0.22)

    def 其它属性(self, character):
        character.物理暴击率增加(0.10)
        character.魔法暴击率增加(0.10)


class 套装效果55(套装):
    名称 = '天命无常'
    件数 = 2
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.伤害增加加成(0.07)
        character.附加伤害加成(0.08)
        character.技能攻击力加成(0.05)

    def 其它属性(self, character):
        if character.is_equip_exist('命运反抗者'):
            character.移动速度增加(0.08)
            character.攻击速度增加(0.08)
            character.释放速度增加(0.12)
        else:
            character.移动速度增加(0.07)
            character.攻击速度增加(0.07)
            character.释放速度增加(0.105)


class 套装效果56(套装):
    名称 = '悲剧的残骸'
    件数 = 2
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.最终伤害加成(0.23)


class 套装效果57(套装):
    名称 = '深渊窥视者'
    件数 = 3
    类型 = '上链左'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.13)

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 60, 80, 2)
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)


class 套装效果58(套装):
    名称 = '圣者的黄昏'
    件数 = 3
    类型 = '上链左'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.05)
        character.技能攻击力加成(0.12)
        character.所有属性强化加成(32)
        character.skill_change_cooldown(1, 45, 0.10)
        character.skill_change_cooldown(60, 80, 0.10)
        character.skill_change_cooldown(90, 95, 0.10)

    def 其它属性(self, character):
        character.移动速度增加(0.05)
        character.物理暴击率增加(0.15)
        character.魔法暴击率增加(0.15)


class 套装效果59(套装):
    名称 = '坎坷命运'
    件数 = 3
    类型 = '上链左'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.21)
        character.技能攻击力加成(0.10)

    def 其它属性(self, character):
        character.攻击速度增加(0.03)
        character.移动速度增加(0.03)
        character.释放速度增加(0.045)
        if character.is_equip_exist('地狱边缘'):
            character.attr["攻击速度"] -= 0.01
            character.attr["移动速度"] -= 0.01
            character.attr["释放速度"] -= 0.015


class 套装效果60(套装):
    名称 = '吞噬愤怒'
    件数 = 3
    类型 = '上链左'

    def 城镇属性(self, character):
        character.百分比力智加成(0.30)


class 套装效果61(套装):
    名称 = '黑魔法探求者'
    件数 = 3
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.属性附加加成(0.13)

    def 其它属性(self, character):
        character.物理暴击率增加(0.10)
        character.魔法暴击率增加(0.10)


class 套装效果62(套装):
    名称 = '时空旅行者'
    件数 = 3
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.17)
        character.技能攻击力加成(0.14)


class 套装效果63(套装):
    名称 = '穿透命运的呐喊'
    件数 = 3
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.百分比力智加成(0.17)
        character.技能攻击力加成(0.19)


class 套装效果64(套装):
    名称 = '狂乱追随者'
    件数 = 3
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.16)
        character.技能攻击力加成(0.15)


class 套装效果65(套装):
    名称 = '地狱求道者'
    件数 = 3
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.16)

    def 进图属性(self, character):
        character.所有属性强化加成(40)

    def 其它属性(self, character):
        character.攻击速度增加(0.15)
        character.移动速度增加(0.15)
        character.释放速度增加(0.20)


class 套装效果66(套装):
    名称 = '次元旅行者'
    件数 = 3
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.10)
        character.技能攻击力加成(0.18)


class 套装效果67(套装):
    名称 = '天命无常'
    件数 = 3
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.附加伤害加成(0.10)
        character.技能攻击力加成(0.08)
        character.百分比力智加成(0.07)
        if character.is_equip_exist('命运反抗者'):
            character.百分比力智加成(0.052)
        else:
            character.百分比力智加成(0.046666667)

    def 其它属性(self, character):
        if character.is_equip_exist('命运反抗者'):
            character.移动速度增加(0.066)
            character.攻击速度增加(0.066)
        else:
            character.移动速度增加(0.055)
            character.攻击速度增加(0.055)


class 套装效果68(套装):
    名称 = '悲剧的残骸'
    件数 = 3
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.29)
        character.技能攻击力加成(0.10)


# endregion


# region  首饰套装

class 套装效果69(套装):
    名称 = '上古尘封术士'
    件数 = 2
    类型 = '首饰'

    def 城镇属性(self, character):
        character.百分比力智加成(0.10)
        character.百分比三攻加成(0.14)


class 套装效果70(套装):
    名称 = '破晓曦光'
    件数 = 2
    类型 = '首饰'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.10)
        character.最终伤害加成(0.10)

    def 其它属性(self, character):
        character.物理暴击率增加(0.05)
        character.魔法暴击率增加(0.05)


class 套装效果71(套装):
    名称 = '幸运三角'
    件数 = 2
    类型 = '首饰'

    def 城镇属性(self, character):
        character.所有属性强化加成(77)
        character.三攻固定加成(77)

    def 其它属性(self, character):
        character.物理暴击率增加(0.07)
        character.魔法暴击率增加(0.07)


class 套装效果72(套装):
    名称 = '精灵使的权能'
    件数 = 2
    类型 = '首饰'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.10)
        character.技能攻击力加成(0.12)


class 套装效果73(套装):
    名称 = '上古尘封术士'
    件数 = 3
    类型 = '首饰'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.20)


class 套装效果74(套装):
    名称 = '破晓曦光'
    件数 = 3
    类型 = '首饰'

    def 城镇属性(self, character):
        character.属性附加加成(0.10)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)
        character.移动速度增加(0.10)
        character.释放速度增加(0.15)


class 套装效果75(套装):
    名称 = '幸运三角'
    件数 = 3
    类型 = '首饰'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.2915)

    def 其它属性(self, character):
        character.攻击速度增加(0.005)
        character.移动速度增加(0.005)
        character.释放速度增加(0.0075)


class 套装效果76(套装):
    名称 = '精灵使的权能'
    件数 = 3
    类型 = '首饰'

    def 城镇属性(self, character):
        character.百分比力智加成(0.15)
        character.skill_change_cooldown(1, 100, 0.10)

    def 其它属性(self, character):
        character.物理暴击率增加(0.05)
        character.魔法暴击率增加(0.05)


# endregion


# region  特殊套装

class 套装效果77(套装):
    名称 = '军神的隐秘遗产'
    件数 = 2
    类型 = '特殊'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.10)
        character.最终伤害加成(0.08)
        if character.is_equip_exist('军神的遗书'):
            if character.is_equip_exist('军神的心之所念'):
                character.暴击伤害加成(0.05)
            if character.is_equip_exist('军神的古怪耳环'):
                character.暴击伤害加成(0.05)

    def 其它属性(self, character):
        if character.is_equip_exist('军神的遗书'):
            if character.is_equip_exist('军神的心之所念'):
                character.攻击速度增加(0.05)
                character.移动速度增加(0.10)
                character.释放速度增加(0.075)
            if character.is_equip_exist('军神的古怪耳环'):
                character.移动速度增加(0.05)


class 套装效果78(套装):
    名称 = '时间战争的残骸'
    件数 = 2
    类型 = '特殊'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.11)
        character.暴击伤害加成(0.11)


class 套装效果79(套装):
    名称 = '灵宝：世间真理'
    件数 = 2
    类型 = '特殊'

    def 城镇属性(self, character):
        character.附加伤害加成(0.15)
        character.技能攻击力加成(0.07)


class 套装效果80(套装):
    名称 = '能量主宰'
    件数 = 2
    类型 = '特殊'

    def 城镇属性(self, character):
        character.百分比三攻加成(0.12)
        character.伤害增加加成(0.12)


class 套装效果81(套装):
    名称 = '军神的隐秘遗产'
    件数 = 3
    类型 = '特殊'

    def 城镇属性(self, character):
        character.技能攻击力加成(0.10)
        character.百分比力智加成(0.10)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)
        character.释放速度增加(0.15)


class 套装效果82(套装):
    名称 = '时间战争的残骸'
    件数 = 3
    类型 = '特殊'

    def 城镇属性(self, character):
        character.百分比力智加成(0.10)
        character.技能攻击力加成(0.15)

    def 其它属性(self, character):
        character.物理暴击率增加(0.05)
        character.魔法暴击率增加(0.05)


class 套装效果83(套装):
    名称 = '灵宝：世间真理'
    件数 = 3
    类型 = '特殊'

    def 城镇属性(self, character):
        character.暴击伤害加成(0.12)

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        character.攻击速度增加(0.10)
        character.移动速度增加(0.10)
        character.释放速度增加(0.15)
        character.物理暴击率增加(0.05)
        character.魔法暴击率增加(0.05)


class 套装效果84(套装):
    名称 = '能量主宰'
    件数 = 3
    类型 = '特殊'

    def 城镇属性(self, character):
        character.附加伤害加成(0.10)
        character.技能攻击力加成(0.08)

    def 其它属性(self, character):
        character.物理暴击率增加(0.10)
        character.魔法暴击率增加(0.10)

# endregion
