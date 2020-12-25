from py.base_equip import *


# region  防具套装
class 套装效果0(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.14
        character.attr["技能攻击力"] *= 1.14

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=135)


class 套装效果1(套装):
    名称 = '死亡阴影'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.14
        character.attr["火属性强化"] += 55
        character.attr["冰属性强化"] += 55
        character.attr["光属性强化"] += 55
        character.attr["暗属性强化"] += 55

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.10
        character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=190)
        # character.attr["被动"] += 转职被动智力=190)
        # character.attr["觉醒"] += 一觉力智=220)


class 套装效果2(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.22
        character.attr["技能攻击力"] *= 1.06

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["批量技能等级"] += '所有', 1, 30, 1)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉力智=175)


class 套装效果3(套装):
    名称 = '噩梦：地狱之路'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.16
        character.attr["最终伤害"] += 0.06
        character.attr["技能攻击力"] *= 1.06

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉力智=100)
        # character.attr["觉醒"] += 一觉力智per=1.04)


class 套装效果4(套装):
    名称 = '永恒不息之路'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.32
        character.skill_change_rate(60, 0.20)
        character.skill_change_cooldown(60, 60, -0.30)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["觉醒"] += 一觉力智=175)


class 套装效果5(套装):
    名称 = '天堂舞姬'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.17
        character.attr["最终伤害"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=105)
        # character.attr["被动"] += 转职被动智力=105)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["觉醒"] += 一觉力智=135)


class 套装效果6(套装):
    名称 = '皇家裁决者宣言'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.16
        character.attr["火属性强化"] += 52
        character.attr["冰属性强化"] += 52
        character.attr["光属性强化"] += 52
        character.attr["暗属性强化"] += 52

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["命中率"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["觉醒"] += 一觉力智=220)


class 套装效果7(套装):
    名称 = '炙炎之盛宴'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.18
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉力智=175)


class 套装效果8(套装):
    名称 = '传奇铁匠-封神'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.14
        character.attr["最终伤害"] += 0.14

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=80)
        # character.attr["被动"] += 转职被动智力=80)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉力智=120)


class 套装效果9(套装):
    名称 = '命运歧路'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.15
        character.attr["附加伤害"] += 0.13

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉力智=135)


class 套装效果10(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.08
        character.attr["伤害增加"] += 0.21

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["回避率"] += 0.06

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=3)
        # character.attr["觉醒"] += 一觉力智=230)


class 套装效果11(套装):
    名称 = '龙血玄黄'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.23

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.1
        character.attr["魔法暴击率"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=100)


class 套装效果12(套装):
    名称 = '擎天战甲'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.14
        character.attr["暴击伤害"] += 0.14

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.06, BUFF智力per=1.06)
        # character.attr["觉醒"] += 一觉力智=150)


class 套装效果13(套装):
    名称 = '荆棘漫天'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.12
        character.attr["暴击伤害"] += 0.11

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.10
        character.attr["魔法暴击率"] += 0.10

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["觉醒"] += 一觉力智=175)


class 套装效果14(套装):
    名称 = '大自然的呼吸'
    件数 = 2
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.16
        character.attr["暴击伤害"] += 0.15

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=145)
        # character.attr["被动"] += 转职被动智力=145)
        # character.attr["BUFF"] += BUFF力量per=1.15)
        # character.attr["BUFF"] += BUFF智力per=1.15)
        # character.attr["觉醒"] += 一觉力智=60)
        # character.attr["觉醒"] += 一觉力智per=1.05)


class 套装效果15(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.22
        character.attr["暴击伤害"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=50)
        # character.attr["被动"] += 转职被动智力=50)
        # character.attr["BUFF"] += BUFF力量per=1.24, BUFF智力per=1.24)
        # character.attr["觉醒"] += 一觉力智=153)


class 套装效果16(套装):
    名称 = '死亡阴影'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.14
        character.attr["技能攻击力"] *= 1.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=165)
        # character.attr["被动"] += 转职被动智力=165)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.25)
        # character.attr["BUFF"] += BUFF智力per=1.25)
        # character.attr["觉醒"] += 一觉力智=130)


class 套装效果17(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.15
        character.attr["火属性强化"] += 60
        character.attr["冰属性强化"] += 60
        character.attr["光属性强化"] += 60
        character.attr["暗属性强化"] += 60

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=113)
        # character.attr["被动"] += 转职被动智力=113)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.1, BUFF智力per=1.1)
        # character.attr["被动"] += 一觉被动Lv=2)
        # character.attr["觉醒"] += 一觉力智=150)


class 套装效果18(套装):
    名称 = '噩梦：地狱之路'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["火属性强化"] += 66
        character.attr["冰属性强化"] += 66
        character.attr["光属性强化"] += 66
        character.attr["暗属性强化"] += 66

        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=110)
        # character.attr["被动"] += 转职被动智力=110)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉力智=99)
        # character.attr["觉醒"] += 一觉力智per=1.04)


class 套装效果19(套装):
    名称 = '永恒不息之路'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.32
        character.skill_change_rate(70, 0.20)
        character.skill_change_cooldown(70, 70, -0.30)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=3)
        # character.attr["BUFF"] += BUFF力量per=1.15)
        # character.attr["BUFF"] += BUFF智力per=1.15)
        # character.attr["觉醒"] += 一觉力智=130)


class 套装效果20(套装):
    名称 = '天堂舞姬'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.11
        character.attr["伤害增加"] += 0.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.10
        character.attr["移动速度"] += 0.10
        character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=145)
        # character.attr["被动"] += 转职被动智力=145)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉力智=192)
        # character.attr["觉醒"] += 一觉力智per=1.05)


class 套装效果21(套装):
    名称 = '皇家裁决者宣言'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.15
        character.attr["火属性强化"] += 62
        character.attr["冰属性强化"] += 62
        character.attr["光属性强化"] += 62
        character.attr["暗属性强化"] += 62

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.05
        character.attr["移动速度"] += 0.05
        character.attr["释放速度"] += 0.08

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=280)
        # character.attr["被动"] += 转职被动智力=280)
        # character.attr["BUFF"] += BUFFLv=3)
        # character.attr["BUFF"] += BUFF力量per=1.2, BUFF智力per=1.2)


class 套装效果22(套装):
    名称 = '炙炎之盛宴'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.10
        character.attr["技能攻击力"] *= 1.20

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["批量技能等级"] += '所有', 1, 48, 2)
        # character.attr["BUFF"] += BUFF力量per=1.25)
        # character.attr["BUFF"] += BUFF智力per=1.25)
        # character.attr["觉醒"] += 一觉力智=100)


class 套装效果23(套装):
    名称 = '传奇铁匠-封神'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.21
        if character.is_equip_exist('天堂之翼'):
            character.skill_change_cooldown(1, 45, 0.30)
            character.skill_change_cooldown(60, 80, 0.30)
        else:
            character.skill_change_cooldown(1, 45, 0.20)
            character.skill_change_cooldown(60, 80, 0.20)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=250)
        # character.attr["被动"] += 转职被动智力=250)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.15, BUFF智力per=1.15)
        # character.attr["被动"] += 一觉被动Lv=2)
        # character.attr["觉醒"] += 一觉Lv=2)


class 套装效果24(套装):
    名称 = '命运歧路'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.12
        character.attr["暴击伤害"] += 0.17

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.21
        character.attr["移动速度"] += 0.21
        character.attr["释放速度"] += 0.315

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉力智=260)


class 套装效果25(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.08
        character.attr["附加伤害"] += 0.21

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=125)
        # character.attr["被动"] += 转职被动智力=125)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.32, BUFF智力per=1.32)


class 套装效果26(套装):
    名称 = '龙血玄黄'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.24
        character.attr["火属性强化"] += 24
        character.attr["冰属性强化"] += 24
        character.attr["光属性强化"] += 24
        character.attr["暗属性强化"] += 24

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=150)
        # character.attr["被动"] += 转职被动智力=150)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.09, BUFF智力per=1.09)
        # character.attr["觉醒"] += 一觉力智=155)
        # character.attr["觉醒"] += 一觉力智per=1.02)


class 套装效果27(套装):
    名称 = '擎天战甲'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.32

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=285)
        # character.attr["被动"] += 转职被动智力=285)
        # character.attr["BUFF"] += BUFF力量per=1.2, BUFF智力per=1.2)
        # character.attr["觉醒"] += 一觉Lv=2)


class 套装效果28(套装):
    名称 = '荆棘漫天'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.25
        character.skill_change_cooldown(1, 45, 0.15)
        character.skill_change_cooldown(60, 80, 0.15)
        character.skill_change_cooldown(90, 95, 0.15)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=200)
        # character.attr["被动"] += 转职被动智力=200)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.11, BUFF智力per=1.11)
        # character.attr["觉醒"] += 一觉力智=130)


class 套装效果29(套装):
    名称 = '大自然的呼吸'
    件数 = 3
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.15
        character.attr["技能攻击力"] *= 1.13

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.05
        character.attr["移动速度"] += 0.05
        character.attr["释放速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.05, BUFF智力per=1.05)
        # character.attr["觉醒"] += 一觉力智=248)


class 套装效果30(套装):
    名称 = '遗忘魔法师的馈赠'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.13
        character.skill_level_up_batched('所有', 1, 85, 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 85, 2)
        character.skill_level_up_batched('所有', 100, 100, 2)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFF力量per=1.06, BUFF智力per=1.06)
        # character.attr["觉醒"] += 一觉力智per=1.08)


class 套装效果31(套装):
    名称 = '死亡阴影'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.46

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["觉醒"] += 一觉力智=120)
        # character.attr["觉醒"] += 一觉力智per=1.08)
        # character.attr["批量技能等级"] += '所有', 1, 30, 1)


class 套装效果32(套装):
    名称 = '贫瘠沙漠的遗产'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.42
        character.attr["技能攻击力"] *= 1.04

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.14, BUFF智力per=1.14)
        # character.attr["被动"] += 一觉被动Lv=2)
        # character.attr["觉醒"] += 一觉Lv=2)
        # character.attr["觉醒"] += 一觉力智per=1.1)


class 套装效果33(套装):
    名称 = '噩梦：地狱之路'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.46

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=80)
        # character.attr["被动"] += 转职被动智力=80)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.15, BUFF智力per=1.15)
        # character.attr["觉醒"] += 一觉力智=185)


class 套装效果34(套装):
    名称 = '永恒不息之路'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.23
        character.attr["伤害增加"] += 0.20

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["释放速度"] += 0.225

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["觉醒"] += 一觉力智=150)
        # character.attr["觉醒"] += 一觉力智per=1.1)


class 套装效果35(套装):
    名称 = '天堂舞姬'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.12
        character.attr["技能攻击力"] *= 1.20

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.10
        character.attr["魔法暴击率"] += 0.10

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["被动"] += 一觉被动Lv=2)
        # character.attr["觉醒"] += 一觉Lv=2)
        # character.attr["觉醒"] += 一觉力智per=1.05)


class 套装效果36(套装):
    名称 = '皇家裁决者宣言'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.20

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["觉醒"] += 一觉力智=180)
        # character.attr["觉醒"] += 一觉力智per=1.1)


class 套装效果37(套装):
    名称 = '炙炎之盛宴'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.22
        character.skill_change_cooldown(1, 100, 0.15)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.05
        character.attr["攻击速度"] += 0.05
        character.attr["移动速度"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=300)
        # character.attr["被动"] += 转职被动智力=300)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["觉醒"] += 一觉力智=70)
        # character.attr["觉醒"] += 一觉力智per=1.08)


class 套装效果38(套装):
    名称 = '传奇铁匠-封神'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.27
        character.skill_change_cooldown(50, 50, 0.30)
        character.skill_change_cooldown(85, 85, 0.30)
        character.skill_change_cooldown(100, 100, 0.17)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.20

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.06, BUFF智力per=1.06)
        # character.attr["被动"] += 一觉被动Lv=2)
        # character.attr["觉醒"] += 一觉力智=20)
        # character.attr["觉醒"] += 一觉力智per=1.07)


class 套装效果39(套装):
    名称 = '命运歧路'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.11
        character.attr["最终伤害"] += 0.30

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=3)
        # character.attr["BUFF"] += BUFF力量per=1.17)
        # character.attr["BUFF"] += BUFF智力per=1.17)
        # character.attr["觉醒"] += 一觉力智per=1.07)


class 套装效果40(套装):
    名称 = '古代祭祀的神圣仪式'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.21
        character.attr["技能攻击力"] *= 1.25

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["觉醒"] += 一觉力智=305)


class 套装效果41(套装):
    名称 = '龙血玄黄'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        if character.is_equip_exist('战无不胜上衣'):
            character.attr["附加伤害"] += 0.41
        else:
            character.attr["附加伤害"] += 0.40

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.225

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.1, BUFF智力per=1.1)
        # character.attr["觉醒"] += 一觉力智=120)
        # character.attr["觉醒"] += 一觉力智per=1.06)


class 套装效果42(套装):
    名称 = '擎天战甲'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.12
        character.attr["技能攻击力"] *= 1.05

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.2
        character.attr["移动速度"] += 0.2
        character.attr["释放速度"] += 0.3

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFF力量per=1.07)
        # character.attr["BUFF"] += BUFF智力per=1.07)
        # character.attr["觉醒"] += 一觉力智=50)
        # character.attr["觉醒"] += 一觉力智per=1.1)
        # character.attr["批量技能等级"] += '所有', 1, 50, 2)


class 套装效果43(套装):
    名称 = '荆棘漫天'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.10
        character.attr["技能攻击力"] *= 1.28

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.1
        character.attr["移动速度"] += -0.02
        character.attr["释放速度"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.1, BUFF智力per=1.1)
        # character.attr["觉醒"] += 一觉力智=150)
        # character.attr["觉醒"] += 一觉力智per=1.08)


class 套装效果44(套装):
    名称 = '大自然的呼吸'
    件数 = 5
    类型 = '防具'

    def 城镇属性(self, character):
        character.attr["最终伤害"] += 0.11
        character.attr["技能攻击力"] *= 1.10
        character.attr["火属性强化"] += 64
        character.attr["冰属性强化"] += 64
        character.attr["光属性强化"] += 64
        character.attr["暗属性强化"] += 64

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.10
        character.attr["魔法暴击率"] += 0.10

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.15)
        # character.attr["BUFF"] += BUFF智力per=1.15)
        # character.attr["觉醒"] += 一觉力智=130)
        # character.attr["觉醒"] += 一觉力智per=1.04)


# endregion

# region  散搭套装
class 套装效果45(套装):
    名称 = '深渊窥视者'
    件数 = 2
    类型 = '上链左'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.09

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 48, 2)

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 48, 2)

    def BUFF属性(self, character):
        pass
        # character.attr["觉醒"] += 一觉力智per=1.02)


class 套装效果46(套装):
    名称 = '圣者的黄昏'
    件数 = 2
    类型 = '上链左'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.11
        character.attr["附加伤害"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉Lv=1)


class 套装效果47(套装):
    名称 = '坎坷命运'
    件数 = 2
    类型 = '上链左'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.14
        character.attr["技能攻击力"] *= 1.09

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.03
        character.attr["移动速度"] += 0.03
        character.attr["释放速度"] += 0.045
        if character.is_equip_exist('地狱边缘'):
            character.attr["攻击速度"] -= 0.01
            character.attr["移动速度"] -= 0.01
            character.attr["释放速度"] -= 0.015

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.02, BUFF智力per=1.02)
        # character.attr["觉醒"] += 一觉力智=45)


class 套装效果48(套装):
    名称 = '吞噬愤怒'
    件数 = 2
    类型 = '上链左'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.10
        character.attr["暴击伤害"] += 0.11

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        if character.is_equip_exist('灭世之怒'):
            character.attr["攻击速度"] += 0.15
            character.attr["移动速度"] += 0.15
            character.attr["释放速度"] += 0.225
        else:
            character.attr["攻击速度"] += 0.10
            character.attr["移动速度"] += 0.10
            character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=25)


class 套装效果49(套装):
    名称 = '黑魔法探求者'
    件数 = 2
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.12
        character.attr["技能攻击力"] *= 1.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉力智=48)


class 套装效果50(套装):
    名称 = '时空旅行者'
    件数 = 2
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.10
        character.attr["最终伤害"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=36)
        # character.attr["被动"] += 转职被动智力=46)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉Lv=1)


class 套装效果51(套装):
    名称 = '穿透命运的呐喊'
    件数 = 2
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.23

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉力智=25)


class 套装效果52(套装):
    名称 = '狂乱追随者'
    件数 = 2
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.18
        character.attr["火属性强化"] += 25
        character.attr["冰属性强化"] += 25
        character.attr["光属性强化"] += 25
        character.attr["暗属性强化"] += 25

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["释放速度"] += 0.225

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉力智=25)


class 套装效果53(套装):
    名称 = '地狱求道者'
    件数 = 2
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.10
        character.attr["最终伤害"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉力智=32)


class 套装效果54(套装):
    名称 = '次元旅行者'
    件数 = 2
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.22

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.10
        character.attr["魔法暴击率"] += 0.10

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=40)
        # character.attr["被动"] += 转职被动智力=60)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉力智=42)


class 套装效果55(套装):
    名称 = '天命无常'
    件数 = 2
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.attr["伤害增加"] += 0.07
        character.attr["附加伤害"] += 0.08
        character.attr["技能攻击力"] *= 1.05

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        if character.is_equip_exist('命运反抗者'):
            character.attr["移动速度"] += 0.08
            character.attr["攻击速度"] += 0.08
            character.attr["释放速度"] += 0.12
        else:
            character.attr["移动速度"] += 0.07
            character.attr["攻击速度"] += 0.07
            character.attr["释放速度"] += 0.105

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["被动"] += 一觉被动Lv=1)
        # character.attr["觉醒"] += 一觉力智=45)


class 套装效果56(套装):
    名称 = '悲剧的残骸'
    件数 = 2
    类型 = '环鞋指'

    def 城镇属性(self, character):
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
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉力智=25)


class 套装效果57(套装):
    名称 = '深渊窥视者'
    件数 = 3
    类型 = '上链左'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.13

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 60, 80, 2)
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 60, 80, 2)
        character.skill_level_up_batched('所有', 50, 50, 1)
        character.skill_level_up_batched('所有', 85, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=195)
        # character.attr["被动"] += 转职被动智力=230)
        # character.attr["BUFF"] += BUFF力量per=1.06, BUFF智力per=1.06)
        # character.attr["觉醒"] += 一觉力智=120)
        # character.attr["觉醒"] += 一觉力智per=1.03)


class 套装效果58(套装):
    名称 = '圣者的黄昏'
    件数 = 3
    类型 = '上链左'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.05
        character.attr["技能攻击力"] *= 1.12
        character.attr["火属性强化"] += 32
        character.attr["冰属性强化"] += 32
        character.attr["光属性强化"] += 32
        character.attr["暗属性强化"] += 32
        character.skill_change_cooldown(1, 45, 0.10)
        character.skill_change_cooldown(60, 80, 0.10)
        character.skill_change_cooldown(90, 95, 0.10)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["移动速度"] += 0.05
        character.attr["物理暴击率"] += 0.15
        character.attr["魔法暴击率"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=225)
        # character.attr["被动"] += 转职被动智力=258)
        # character.attr["BUFF"] += BUFF力量per=1.12, BUFF智力per=1.12)
        # character.attr["觉醒"] += 一觉力智=125)
        # character.attr["觉醒"] += 一觉力智per=1.03)


class 套装效果59(套装):
    名称 = '坎坷命运'
    件数 = 3
    类型 = '上链左'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.20
        character.attr["技能攻击力"] *= 1.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.03
        character.attr["移动速度"] += 0.03
        character.attr["释放速度"] += 0.045
        if character.is_equip_exist('地狱边缘'):
            character.attr["攻击速度"] -= 0.01
            character.attr["移动速度"] -= 0.01
            character.attr["释放速度"] -= 0.015

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=236)
        # character.attr["被动"] += 转职被动智力=255)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.06, BUFF智力per=1.06)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=74)
        # character.attr["觉醒"] += 一觉力智per=1.05)


class 套装效果60(套装):
    名称 = '吞噬愤怒'
    件数 = 3
    类型 = '上链左'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.30

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=236)
        # character.attr["被动"] += 转职被动智力=255)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.1, BUFF智力per=1.1)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=99)
        # character.attr["觉醒"] += 一觉力智per=1.04)


class 套装效果61(套装):
    名称 = '黑魔法探求者'
    件数 = 3
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.13

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.10
        character.attr["魔法暴击率"] += 0.1

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=38)
        # character.attr["觉醒"] += 一觉力智per=1.06)


class 套装效果62(套装):
    名称 = '时空旅行者'
    件数 = 3
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.17
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
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.1, BUFF智力per=1.1)
        # character.attr["觉醒"] += 一觉力智=45)
        # character.attr["觉醒"] += 一觉力智per=1.05)


class 套装效果63(套装):
    名称 = '穿透命运的呐喊'
    件数 = 3
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.14
        character.attr["技能攻击力"] *= 1.16

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=76)
        # character.attr["被动"] += 转职被动智力=68)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.06, BUFF智力per=1.06)
        # character.attr["被动"] += 一觉被动Lv=2)
        # character.attr["觉醒"] += 一觉Lv=2)
        # character.attr["觉醒"] += 一觉力智per=1.04)


class 套装效果64(套装):
    名称 = '狂乱追随者'
    件数 = 3
    类型 = '镯下右'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.16
        character.attr["技能攻击力"] *= 1.15

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=36)
        # character.attr["被动"] += 转职被动智力=38)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.1, BUFF智力per=1.1)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=85)
        # character.attr["觉醒"] += 一觉力智per=1.04)


class 套装效果65(套装):
    名称 = '地狱求道者'
    件数 = 3
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.16

    def 进图属性(self, character):
        character.attr["火属性强化"] += 40
        character.attr["冰属性强化"] += 40
        character.attr["光属性强化"] += 40
        character.attr["暗属性强化"] += 40

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.15
        character.attr["移动速度"] += 0.15
        character.attr["释放速度"] += 0.20

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=195)
        # character.attr["被动"] += 转职被动智力=188)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.06, BUFF智力per=1.06)
        # character.attr["觉醒"] += 一觉Lv=2)


class 套装效果66(套装):
    名称 = '次元旅行者'
    件数 = 3
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.10
        character.attr["技能攻击力"] *= 1.18

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=80)
        # character.attr["被动"] += 转职被动智力=120)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["觉醒"] += 一觉Lv=1)


class 套装效果67(套装):
    名称 = '天命无常'
    件数 = 3
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.10
        character.attr["技能攻击力"] *= 1.07
        character.attr["百分比力智"] += 0.07
        if character.is_equip_exist('命运反抗者'):
            character.attr["百分比力智"] += 0.056
        else:
            character.attr["百分比力智"] += 0.046666667

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        if character.is_equip_exist('命运反抗者'):
            character.attr["移动速度"] += 0.066
            character.attr["攻击速度"] += 0.066
        else:
            character.attr["移动速度"] += 0.055
            character.attr["攻击速度"] += 0.055

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.08, BUFF智力per=1.08)
        # character.attr["被动"] += 一觉被动Lv=2)
        # character.attr["觉醒"] += 一觉Lv=2)


class 套装效果68(套装):
    名称 = '悲剧的残骸'
    件数 = 3
    类型 = '环鞋指'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.29

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=171)
        # character.attr["被动"] += 转职被动智力=158)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.1, BUFF智力per=1.1)
        # character.attr["觉醒"] += 一觉Lv=1)


# endregion

# region  首饰套装
class 套装效果69(套装):
    名称 = '上古尘封术士'
    件数 = 2
    类型 = '首饰'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.10
        character.attr["百分比三攻"] += 0.14

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=60)
        # character.attr["被动"] += 转职被动智力=60)
        # character.attr["BUFF"] += BUFF力量per=1.02, BUFF智力per=1.02)
        # character.attr["觉醒"] += 一觉力智=45)


class 套装效果70(套装):
    名称 = '破晓曦光'
    件数 = 2
    类型 = '首饰'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.10
        character.attr["最终伤害"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFF力量per=1.03, BUFF智力per=1.03)
        # character.attr["觉醒"] += 一觉Lv=1)


class 套装效果71(套装):
    名称 = '幸运三角'
    件数 = 2
    类型 = '首饰'

    def 城镇属性(self, character):
        character.attr["火属性强化"] += 77
        character.attr["冰属性强化"] += 77
        character.attr["光属性强化"] += 77
        character.attr["暗属性强化"] += 77
        character.attr["物理攻击力"] += 77
        character.attr["魔法攻击力"] += 77
        character.attr["独立攻击力"] += 77

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.07
        character.attr["魔法暴击率"] += 0.07

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=140)
        # character.attr["被动"] += 转职被动智力=140)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["觉醒"] += 一觉力智=45)


class 套装效果72(套装):
    名称 = '精灵使的权能'
    件数 = 2
    类型 = '首饰'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.10
        character.attr["技能攻击力"] *= 1.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["被动"] += 转职被动智力=110)
        # character.attr["觉醒"] += 一觉力智=20)


class 套装效果73(套装):
    名称 = '上古尘封术士'
    件数 = 3
    类型 = '首饰'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.20

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=26)


class 套装效果74(套装):
    名称 = '破晓曦光'
    件数 = 3
    类型 = '首饰'

    def 城镇属性(self, character):
        character.attr["属性附加"] += 0.10
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.10
        character.attr["移动速度"] += 0.10
        character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["被动"] += 转职被动智力=100)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=45)


class 套装效果75(套装):
    名称 = '幸运三角'
    件数 = 3
    类型 = '首饰'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.2915

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.005
        character.attr["移动速度"] += 0.005
        character.attr["释放速度"] += 0.0075

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉Lv=2)


class 套装效果76(套装):
    名称 = '精灵使的权能'
    件数 = 3
    类型 = '首饰'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.10
        character.skill_change_cooldown(1, 100, 0.10)

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.03, BUFF智力per=1.03)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=26)


# endregion

# region  特殊套装
class 套装效果77(套装):
    名称 = '军神的隐秘遗产'
    件数 = 2
    类型 = '特殊'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.10
        character.attr["最终伤害"] += 0.08
        if character.is_equip_exist('军神的遗书'):
            if character.is_equip_exist('军神的心之所念'):
                character.attr["暴击伤害"] += 0.05
            if character.is_equip_exist('军神的古怪耳环'):
                character.attr["暴击伤害"] += 0.05

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        if character.is_equip_exist('军神的遗书'):
            if character.is_equip_exist('军神的心之所念'):
                character.attr["攻击速度"] += 0.05
                character.attr["移动速度"] += 0.10
                character.attr["释放速度"] += 0.075
            if character.is_equip_exist('军神的古怪耳环'):
                character.attr["移动速度"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=230)
        # character.attr["被动"] += 转职被动智力=230)
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.04)
        # character.attr["BUFF"] += BUFF智力per=1.04)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=35)


class 套装效果78(套装):
    名称 = '时间战争的残骸'
    件数 = 2
    类型 = '特殊'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.11
        character.attr["暴击伤害"] += 0.11

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["批量技能等级"] += '所有', 1, 30, 2)
        # character.attr["BUFF"] += BUFF力量per=1.02, BUFF智力per=1.02)
        # character.attr["觉醒"] += 一觉力智=35)


class 套装效果79(套装):
    名称 = '灵宝：世间真理'
    件数 = 2
    类型 = '特殊'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.15
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
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["BUFF"] += BUFF力量per=1.02, BUFF智力per=1.02)
        # character.attr["被动"] += 一觉被动Lv=1)
        # character.attr["觉醒"] += 一觉Lv=1)


class 套装效果80(套装):
    名称 = '能量主宰'
    件数 = 2
    类型 = '特殊'

    def 城镇属性(self, character):
        character.attr["百分比三攻"] += 0.12
        character.attr["伤害增加"] += 0.12

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        pass

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=95)
        # character.attr["被动"] += 转职被动智力=95)
        # character.attr["BUFF"] += BUFFLv=2)
        # character.attr["BUFF"] += BUFF力量per=1.02, BUFF智力per=1.02)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=35)


class 套装效果81(套装):
    名称 = '军神的隐秘遗产'
    件数 = 3
    类型 = '特殊'

    def 城镇属性(self, character):
        character.attr["技能攻击力"] *= 1.10
        character.attr["百分比力智"] += 0.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.10
        character.attr["释放速度"] += 0.15

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["BUFF"] += BUFFLv=1)
        # character.attr["觉醒"] += 一觉Lv=2)


class 套装效果82(套装):
    名称 = '时间战争的残骸'
    件数 = 3
    类型 = '特殊'

    def 城镇属性(self, character):
        character.attr["百分比力智"] += 0.10
        character.attr["技能攻击力"] *= 1.10

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=75)
        # character.attr["被动"] += 转职被动智力=85)
        # character.attr["被动"] += 一觉被动Lv=1)
        # character.attr["觉醒"] += 一觉Lv=2)


class 套装效果83(套装):
    名称 = '灵宝：世间真理'
    件数 = 3
    类型 = '特殊'

    def 城镇属性(self, character):
        character.attr["暴击伤害"] += 0.12

    def 进图属性(self, character):
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def 其它属性(self, character):
        character.attr["攻击速度"] += 0.10
        character.attr["移动速度"] += 0.10
        character.attr["释放速度"] += 0.15
        character.attr["物理暴击率"] += 0.05
        character.attr["魔法暴击率"] += 0.05

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        character.skill_level_up_batched('所有', 1, 85, 1)
        character.skill_level_up_batched('所有', 100, 100, 1)

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=100)
        # character.attr["被动"] += 转职被动智力=122)
        # character.attr["觉醒"] += 一觉Lv=1)
        # character.attr["觉醒"] += 一觉力智=39)


class 套装效果84(套装):
    名称 = '能量主宰'
    件数 = 3
    类型 = '特殊'

    def 城镇属性(self, character):
        character.attr["附加伤害"] += 0.10
        character.attr["技能攻击力"] *= 1.08

    def 进图属性(self, character):
        pass

    def 其它属性(self, character):
        character.attr["物理暴击率"] += 0.10
        character.attr["魔法暴击率"] += 0.10

    def 城镇属性_BUFF(self, character):
        pass

    def 进图属性_BUFF(self, character):
        pass

    def BUFF属性(self, character):
        pass
        # character.attr["被动"] += 守护恩赐体精=110)
        # character.attr["被动"] += 转职被动智力=110)
        # character.attr["BUFF"] += BUFF力量per=1.02, BUFF智力per=1.02)
        # character.attr["觉醒"] += 一觉Lv=2)
# endregion
