from py.Equip.equ_list import *
from py.Equip.辟邪玉 import *
from py import base_char as py_base_char
import copy


class CharBase:
    attr = []

    def printDetail(self):
        print("力量: {0}".format(self.站街力量()))
        print("智力: {0}".format(self.站街智力()))
        print("体力: {0}".format(self.attr["体力"]))
        print("精神: {0}".format(self.attr["精神"]))
        print("物理攻击力: {0}".format(int(self.站街物理攻击力())))
        print("魔法攻击力: {0}".format(int(self.站街魔法攻击力())))
        print("独立攻击力: {0}".format(int(self.站街独立攻击力())))
        print("火属性强化: {0}".format(self.attr["火属性强化"]))
        print("伤害增加: {0}".format(self.attr["伤害增加"]))
        print("暴击伤害: {0}".format(self.attr["暴击伤害"]))
        print("最终伤害: {0}".format(self.attr["最终伤害"]))
        print("百分比力智: {0}".format(self.attr["百分比力智"]))
        print("百分比三攻: {0}".format(self.attr["百分比三攻"]))
        print("附加伤害: {0}".format(self.attr["附加伤害"]))
        print("加算冷却缩减: {0}".format(self.attr["加算冷却缩减"]))
        print("技能攻击力: {0}".format(self.attr["技能攻击力"]))

    def printSkills(self):
        for i in self.attr["技能栏"]:
            try:
                print(i.名称, i.等级, i.TP等级)
            except:
                print(i.名称, i.等级)

    def 附加伤害加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '附加伤害 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["附加伤害"] += self.attr["附加伤害增加增幅"] * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.attr["变换词条"][可变 - 1] = [3, round(x * 100), round(x * 100) + (2 if 可变 > 1 else 4), round(x * 100) + (8 if 可变 > 1 else 16)]
        return ''

    def 三攻固定加成(self, x=0, y=0, z=0):
        if self.attr["装备描述"] == 1:
            return '物攻/魔攻/独立 +{}<br>'.format(x)
        else:
            if y == 0 or z == 0:
                y = x
                z = x
            self.attr["物理攻击力"] += x
            self.attr["魔法攻击力"] += y
            self.attr["独立攻击力"] += z
        return ''

    def 力智固定加成(self, x=0, y=0):
        if self.attr["装备描述"] == 1:
            return '力量、智力 +{}<br>'.format(x)
        else:
            if y == 0:
                y = x
            self.attr["力量"] += x
            self.attr["智力"] += y
        return ''

    def 持续伤害加成(self, x):
        if self.attr["装备描述"] == 1:
            return '持续伤害 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["持续伤害"] += x
        return ''

    def 属性附加加成(self, x):
        if self.attr["装备描述"] == 1:
            return '属性附加伤害 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["属性附加"] += self.attr["属性附加伤害增加增幅"] * x
        return ''

    def 技能攻击力加成(self, x, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '技能攻击力 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["技能攻击力"] *= 1 + self.attr["技能伤害增加增幅"] * x if 辟邪玉加成 == 1 else x
        return ''

    def 暴击伤害加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '暴击伤害 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["暴击伤害"] += self.attr["暴击伤害增加增幅"] * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.attr["变换词条"][可变 - 1] = [4, round(x * 100), round(x * 100) + (2 if 可变 > 1 else 4), round(x * 100) + (8 if 可变 > 1 else 16)]
        return ''

    def 伤害增加加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '伤害增加 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["伤害增加"] += self.attr["伤害增加增幅"] * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.attr["变换词条"][可变 - 1] = [2, round(x * 100), round(x * 100) + (2 if 可变 > 1 else 4), round(x * 100) + (8 if 可变 > 1 else 16)]
        return ''

    def 最终伤害加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '最终伤害 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["最终伤害"] += self.attr["最终伤害增加增幅"] * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.attr["变换词条"][可变 - 1] = [5, round(x * 100), round(x * 100) + (2 if 可变 > 1 else 4), round(x * 100) + (8 if 可变 > 1 else 16)]
        return ''

    def 百分比力智加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '力量、智力 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["百分比力智"] += self.attr["力量智力增加增幅"] * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.attr["变换词条"][可变 - 1] = [0, round(x * 100), round(x * 100) + (2 if 可变 > 1 else 4), round(x * 100) + (8 if 可变 > 1 else 16)]
        return ''

    def 百分比三攻加成(self, x, 可变=0, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '百分比三攻 {}%<br>'.format(('+' if x > 0 else '') + str(round(x * 100)))
        else:
            self.attr["百分比三攻"] += self.attr["物理魔法攻击力增加增幅"] * x if 辟邪玉加成 == 1 else x
            if 可变 > 0:
                self.attr["变换词条"][可变 - 1] = [1, round(x * 100), round(x * 100) + (2 if 可变 > 1 else 4), round(x * 100) + (8 if 可变 > 1 else 16)]
        return ''

    def 火属性强化加成(self, x, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '火属性强化 +{}<br>'.format(x)
        else:
            if self.attr["状态"] == 0:
                self.attr["火属性强化"] += self.attr["所有属性强化增加"] * x if 辟邪玉加成 == 1 else x
            else:
                self.attr["火属性强化"] += int(self.attr["所有属性强化增加"] * x)
        return ''

    def 冰属性强化加成(self, x, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '冰属性强化 +{}<br>'.format(x)
        else:
            if self.attr["状态"] == 0:
                self.attr["冰属性强化"] += self.attr["所有属性强化增加"] * x if 辟邪玉加成 == 1 else x
            else:
                self.attr["冰属性强化"] += int(self.attr["所有属性强化增加"] * x)
        return ''

    def 光属性强化加成(self, x, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '光属性强化 +{}<br>'.format(x)
        else:
            if self.attr["状态"] == 0:
                self.attr["光属性强化"] += self.attr["所有属性强化增加"] * x if 辟邪玉加成 == 1 else x
            else:
                self.attr["光属性强化"] += int(self.attr["所有属性强化增加"] * x)
        return ''

    def 暗属性强化加成(self, x, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '暗属性强化 +{}<br>'.format(x)
        else:
            if self.attr["状态"] == 0:
                self.attr["暗属性强化"] += self.attr["所有属性强化增加"] * x if 辟邪玉加成 == 1 else x
            else:
                self.attr["暗属性强化"] += int(self.attr["所有属性强化增加"] * x)
        return ''

    def 所有属性强化加成(self, x, 辟邪玉加成=1):
        if self.attr["装备描述"] == 1:
            return '所有属性强化 +{}<br>'.format(x)
        else:
            if self.attr["状态"] == 0:
                temp = self.attr["所有属性强化增加"] * x if 辟邪玉加成 == 1 else x
            else:
                temp = int(self.attr["所有属性强化增加"] * x)
            self.所有属性强化(temp)
        return ''

    def 所有属性强化(self, x):
        self.attr["火属性强化"] += x
        self.attr["冰属性强化"] += x
        self.attr["光属性强化"] += x
        self.attr["暗属性强化"] += x

    def 攻击速度增加(self, x):
        if self.attr["装备描述"] == 1:
            return '攻击速度 {}%<br>'.format(("+" if x > 0 else '') + str(round(x * 100, 2)))
        else:
            self.attr["攻击速度"] += x
        return ''

    def 移动速度增加(self, x):
        if self.attr["装备描述"] == 1:
            return '移动速度 {}%<br>'.format(("+" if x > 0 else '') + str(round(x * 100, 2)))
        else:
            self.attr["移动速度"] += x
        return ''

    def 释放速度增加(self, x):
        if self.attr["装备描述"] == 1:
            return '释放速度 {}%<br>'.format(("+" if x > 0 else '') + str(round(x * 100, 2)))
        else:
            self.attr["释放速度"] += x
        return ''

    def 命中率增加(self, x):
        if self.attr["装备描述"] == 1:
            return '命中率 {}%<br>'.format(("+" if x > 0 else '') + str(round(x * 100)))
        else:
            self.attr["命中率"] += x
        return ''

    def 回避率增加(self, x):
        if self.attr["装备描述"] == 1:
            return '回避率 {}%<br>'.format(("+" if x > 0 else '') + str(round(x * 100)))
        else:
            self.attr["回避率"] += x
        return ''

    def 物理暴击率增加(self, x):
        if self.attr["装备描述"] == 1:
            return '物理暴击率 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["物理暴击率"] += x
        return ''

    def 魔法暴击率增加(self, x):
        if self.attr["装备描述"] == 1:
            return '魔法暴击率 +{}%<br>'.format(round(x * 100))
        else:
            self.attr["魔法暴击率"] += x
        return ''

    # 检测装备
    def is_equip_exist(self, 装备名称):
        for i in self.attr["装备栏"]:
            if i == 装备名称:
                return True
        return False

    # 技能等级加成
    def skill_level_up_batched(self, 加成类型, minLV, maxLV, LV, 可变=0):
        LV = int(LV)
        if self.attr["远古记忆"] > 0:
            if minLV <= 15 <= maxLV:
                self.attr["远古记忆"] = min(20, self.attr["远古记忆"] + LV)

        if self.attr["刀魂之卡赞"] > 0:
            if minLV <= 5 <= maxLV:
                self.attr["刀魂之卡赞"] = min(20, self.attr["刀魂之卡赞"] + LV)

        for i in self.attr["技能栏"]:
            if minLV <= i.所在等级 <= maxLV:
                if 加成类型 == '所有':
                    i.等级加成(LV)
                else:
                    if i.是否主动 == 1:
                        i.等级加成(LV)

        if 可变 > 0:
            self.attr["变换词条"][可变 - 1] = [6, 2, 14 + (2 if 可变 > 1 else 4), 14 + (8 if 可变 > 1 else 16)]

    # 单技能等级加成
    def skill_level_up_specified(self, 技能名, LV):
        for i in self.attr["技能栏"]:
            if 技能名 == i.名称:
                i.等级加成(LV)
                break

    # 单技能修改
    def skill_change_attr(self, 名称, 倍率, CD):
        for i in self.attr["技能栏"]:
            if i.是否有伤害 == 1:
                if i.名称 == 名称:
                    i.倍率 *= 倍率
                    i.CD *= CD

    # 技能倍率加成
    def skill_change_rate(self, LV, x):
        for i in self.attr["技能栏"]:
            if i.所在等级 == LV and i.是否有伤害 == 1:
                i.倍率 *= (1 + x * self.attr["技能伤害增加增幅"])

    # 技能冷却缩减
    def skill_change_cooldown(self, minLV, maxLV, x):
        for i in self.attr["技能栏"]:
            if minLV <= i.所在等级 <= maxLV and i.是否有伤害 == 1:
                i.CD *= (1 - x)

    # 技能恢复加成
    def skill_change_recovery(self, minLV, maxLV, x):
        for i in self.attr["技能栏"]:
            if minLV <= i.所在等级 <= maxLV and i.是否有伤害 == 1:
                i.恢复 += x

    # 获取装备等级
    def fetch_strengthen_level(self, 部位):
        return self.attr["强化等级"][部位列表.index(部位)]

    def 站街物理攻击力倍率(self):
        站街物理攻击倍率 = 1.0
        武器类型 = self.attr["武器类型"]
        for i in self.attr["技能栏"]:
            try:
                站街物理攻击倍率 *= i.物理攻击力倍率(武器类型)
            except:
                pass
        return 站街物理攻击倍率

    def 站街魔法攻击力倍率(self):
        站街魔法攻击力倍率 = 1.0
        武器类型 = self.attr["武器类型"]
        for i in self.attr["技能栏"]:
            try:
                站街魔法攻击力倍率 *= i.魔法攻击力倍率(武器类型)
            except:
                pass
        return 站街魔法攻击力倍率

    def 站街独立攻击力倍率(self):
        站街独立攻击力倍率 = 1.0
        武器类型 = self.attr["武器类型"]
        for i in self.attr["技能栏"]:
            try:
                站街独立攻击力倍率 *= i.独立攻击力倍率(武器类型)
            except:
                pass
        return 站街独立攻击力倍率

    def 站街力量(self):
        return int(self.attr["力量"])

    def 站街智力(self):
        return int(self.attr["智力"])

    def 站街物理攻击力(self):
        return self.attr["物理攻击力"] * self.站街物理攻击力倍率()

    def 站街魔法攻击力(self):
        return self.attr["魔法攻击力"] * self.站街魔法攻击力倍率()

    def 站街独立攻击力(self):
        return self.attr["独立攻击力"] * self.站街独立攻击力倍率()

    def 面板力量(self):
        pass

    def 面板智力(self):
        pass

    def 面板物理攻击力(self):
        pass

    def 面板魔法攻击力(self):
        pass

    def 面板独立攻击力(self):
        pass

    def 三觉技能选择(self):
        # 由每个角色重写，填写的为游戏里选择的技能（未三觉为增强，已三觉为替换）
        for i, 技能 in enumerate(self.attr["技能栏"]):
            if 技能.名称 == "觉醒之抉择":
                技能.关联技能 = [self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].名称]
            elif i == self.attr["二觉序号"]:
                技能.被动倍率 = 0

    def 技能等级初始化(self):
        技能SP等级 = self.attr["技能SP等级"]
        技能TP等级 = self.attr["技能TP等级"]

        for i, 技能 in enumerate(self.attr["技能栏"]):
            技能.等级 = 技能SP等级[i]
            if 技能TP等级[i] > 0:
                技能.TP等级 = 技能TP等级[i]

        self.三觉技能选择()

    def 角色賦予(self):
        self.attr["实际名称"] = ''
        self.attr["角色"] = ''
        self.attr["职业"] = ''

        self.attr["武器选项"] = ['']

        self.attr["类型"] = ''
        self.attr["防具类型"] = ''
        self.attr["防具精通属性"] = ['']

        self.attr["主BUFF"] = 1

        self.attr["远古记忆"] = 0
        self.attr["刀魂之卡赞"] = 0

    def 角色基础数据生成(self):
        角色数据 = py_base_char.角色基础系数[self.attr["角色"]]
        职业数据 = py_base_char.职业基础数据[self.attr["职业"] + '-' + self.attr["角色"]]

        当前等级 = 100
        唤醒 = 275

        self.attr["基础力量"] = int(角色数据[4] + 角色数据[0] * min(14, 当前等级 - 1) + 职业数据[0] * max(当前等级 - 15, 0) + 唤醒 + 2.1 * min(71, 当前等级))
        self.attr["基础体力"] = int(角色数据[5] + 角色数据[1] * min(14, 当前等级 - 1) + 职业数据[1] * max(当前等级 - 15, 0) + 唤醒 + 2.0 * min(71, 当前等级))
        self.attr["基础智力"] = int(角色数据[6] + 角色数据[2] * min(14, 当前等级 - 1) + 职业数据[2] * max(当前等级 - 15, 0) + 唤醒 + 2.1 * min(71, 当前等级))
        self.attr["基础精神"] = int(角色数据[7] + 角色数据[3] * min(14, 当前等级 - 1) + 职业数据[3] * max(当前等级 - 15, 0) + 唤醒 + 2.0 * min(71, 当前等级))

        self.attr["力量"] = self.attr["基础力量"]
        self.attr["体力"] = self.attr["基础体力"]
        self.attr["智力"] = self.attr["基础智力"]
        self.attr["精神"] = self.attr["基础精神"]

        self.attr["词条属性映射"] = 词条属性映射
        self.attr["黑鸦武器属性列表"] = 黑鸦武器属性列表

        self.技能等级初始化()

    def 角色数据输入(self):
        self.attr["技能SP等级"] = []
        self.attr["技能TP等级"] = []
        self.attr["技能释放次数"] = []
        self.attr["技能宠物次数"] = []

        self.attr["装备栏"] = []
        self.attr["套装栏"] = []
        self.attr["武器类型"] = ""

        self.attr["左槽白金技能"] = ""
        self.attr["右槽白金技能"] = ""
        self.attr["时装上衣技能"] = ""

    def 用户数据覆盖(self, data):
        attr = data["attr"]
        for i in attr:
            self.attr[i] = attr[i]

        if not "细节1" in self.attr:
            self.attr["细节1"] = py_base_char.细节1
            self.attr["细节2"] = py_base_char.细节2
            self.attr["细节3"] = py_base_char.细节3
            self.attr["细节4"] = py_base_char.细节4

    def 获取武器类型(self, weapon_name):
        武器序号 = 装备序号[weapon_name]
        武器类型 = 装备列表[武器序号].类型
        return 武器类型

    def 称号基础(self):
        self.力智固定加成(100)
        self.三攻固定加成(65)
        self.所有属性强化加成(22)
        self.百分比三攻加成(0.12)
        self.附加伤害加成(0.10)

        self.attr["进图力量"] += 35
        self.attr["进图智力"] += 35

    def 宠物基础(self):
        self.力智固定加成(160)
        self.所有属性强化加成(25)
        self.skill_level_up_batched("所有", 1, 80, 1)
        self.attr["加算冷却缩减"] += 0.05
        self.暴击伤害加成(0.20, 辟邪玉加成=0)
        self.百分比力智加成(0.12, 辟邪玉加成=0)

    def 额外细节(self):
        pass

    def 细节基础(self):
        for i in self.attr["细节1"].values():
            self.attr["力量"] += i[0]
            self.attr["智力"] += i[1]
            self.attr["物理攻击力"] += i[2]
            self.attr["魔法攻击力"] += i[3]
            self.attr["独立攻击力"] += i[4]
            self.所有属性强化加成(i[5])

        for i in self.attr["细节3"].values():
            self.attr["进图力量"] += i[0]
            self.attr["进图智力"] += i[1]
            self.attr["进图物理攻击力"] += i[2]
            self.attr["进图魔法攻击力"] += i[3]
            self.attr["进图独立攻击力"] += i[4]
            self.attr["进图属强"] += i[5]

        for i in self.attr["细节4"].values():
            self.attr["力量"] += i[0]
            self.attr["智力"] += i[1]
            self.attr["物理攻击力"] += i[2]
            self.attr["魔法攻击力"] += i[3]
            self.attr["独立攻击力"] += i[4]
            self.所有属性强化(i[5])

        for i in self.attr["细节2"].values():
            self.attr["力量"] += i[0] + i[3]
            self.attr["智力"] += i[0] + i[3]
            self.attr["物理攻击力"] += i[1] + i[4]
            self.attr["魔法攻击力"] += i[1] + i[4]
            self.attr["独立攻击力"] += i[1] + i[4]
            self.所有属性强化加成(i[2])

        # 勋章强化
        self.attr["力量"] += 17
        self.attr["智力"] += 17
        self.attr["体力"] += 17
        self.attr["精神"] += 17

        # 宠物装备 - 红
        self.附加伤害加成(0.08)

        # 左槽
        self.最终伤害加成(0.03)

        # 腰带、鞋
        self.skill_level_up_batched("主动", 1, 50, 1)
        self.skill_level_up_batched("主动", 1, 50, 1)

        # 头肩
        self.技能攻击力加成(0.03)
        # self.skill_level_up_batched("主动", 1, 50, 1)

        # 称号
        self.技能攻击力加成(0.03)
        # self.skill_level_up_batched("主动", 1, 50, 1)

        # 光环
        self.百分比三攻加成(0.05)
        self.skill_level_up_batched("所有", 1, 80, 1)

        # 白金、时装上衣
        self.skill_level_up_specified(self.attr["左槽白金技能"], 1)
        self.skill_level_up_specified(self.attr["右槽白金技能"], 1)
        self.skill_level_up_specified(self.attr["时装上衣技能"], 1)

        # 顶级秘药、特挑酷饮、魔界秘药
        self.attr["进图力量"] += 150 + 175
        self.attr["进图智力"] += 150 + 175
        self.attr["进图属强"] += 5

        self.额外细节()

    def 精通计算(self, 装备等级, 品质, 强化等级, 部位):
        return round((20 + 2.5 * (装备等级 + 品级加分[品质] + int(强化等级 / 3))) * 部位系数[部位], 2)

    def 防具基础(self):
        for i in [0, 1, 2, 3, 4]:
            装备名称 = self.attr["装备栏"][i]
            if 装备名称:
                装备属性 = 装备列表[装备序号[装备名称]]
                self.attr["力量"] += 装备属性.力量[self.attr["防具类型"]]
                self.attr["智力"] += 装备属性.智力[self.attr["防具类型"]]

                精通数值 = self.精通计算(装备属性.等级, 装备属性.品质, self.attr["强化等级"][i], 部位列表[i])
                if "力量" in self.attr["防具精通属性"]:
                    self.attr["力量"] += 精通数值
                if "智力" in self.attr["防具精通属性"]:
                    self.attr["智力"] += 精通数值

    def 首饰基础(self):
        for i in [5, 6, 7]:
            装备名称 = self.attr["装备栏"][i]
            if 装备名称:
                装备属性 = 装备列表[装备序号[装备名称]]
                self.attr["力量"] += 装备属性.力量
                self.attr["智力"] += 装备属性.智力
                self.attr["物理攻击力"] += 装备属性.物理攻击力
                self.attr["魔法攻击力"] += 装备属性.魔法攻击力
                self.attr["独立攻击力"] += 装备属性.独立攻击力

    def 特殊基础(self):
        for i in [8, 9, 10]:
            装备名称 = self.attr["装备栏"][i]
            if 装备名称:
                装备属性 = 装备列表[装备序号[装备名称]]
                self.attr["力量"] += 装备属性.力量
                self.attr["智力"] += 装备属性.智力
                self.attr["物理攻击力"] += 装备属性.物理攻击力
                self.attr["魔法攻击力"] += 装备属性.魔法攻击力
                self.attr["独立攻击力"] += 装备属性.独立攻击力

        装备名称 = self.attr["装备栏"][8]
        if 装备名称:
            装备属性 = 装备列表[装备序号[装备名称]]
            三攻 = 耳环计算(装备属性.等级, 装备属性.品质, self.attr["强化等级"][8])
            self.attr["物理攻击力"] += 三攻
            self.attr["魔法攻击力"] += 三攻
            self.attr["独立攻击力"] += 三攻

        for i in [9, 10]:
            装备名称 = self.attr["装备栏"][i]
            if 装备名称:
                装备属性 = 装备列表[装备序号[装备名称]]
                力智 = 左右计算(装备属性.等级, 装备属性.品质, self.attr["强化等级"][i])
                self.attr["力量"] += 力智
                self.attr["智力"] += 力智

    def 武器基础(self):
        装备名称 = self.attr["装备栏"][11]
        if 装备名称:
            装备属性 = 装备列表[装备序号[装备名称]]
            self.attr["力量"] += 装备属性.力量
            self.attr["智力"] += 装备属性.智力
            self.attr["物理攻击力"] += 装备属性.物理攻击力
            self.attr["魔法攻击力"] += 装备属性.魔法攻击力
            self.attr["独立攻击力"] += 装备属性.独立攻击力

            self.attr["物理攻击力"] += 武器计算(装备属性.等级, 装备属性.品质, self.attr["强化等级"][11], self.attr["武器类型"], "物理")
            self.attr["魔法攻击力"] += 武器计算(装备属性.等级, 装备属性.品质, self.attr["强化等级"][11], self.attr["武器类型"], "魔法")
            self.attr["独立攻击力"] += 锻造计算(装备属性.等级, 装备属性.品质, self.attr["武器锻造等级"])

    def 增幅基础(self):
        for i in range(12):
            if self.attr["是否增幅"][i]:
                装备名称 = self.attr["装备栏"][i]
                if 装备名称:
                    装备属性 = 装备列表[装备序号[装备名称]]
                    x = 增幅计算(装备属性.等级, 装备属性.品质, self.attr["强化等级"][i])
                    if "物理" in self.attr["类型"] or "力量" in self.attr["类型"]:
                        self.attr["力量"] += x
                    else:
                        self.attr["智力"] += x

    def 装备基础(self):
        self.称号基础()
        self.宠物基础()
        self.细节基础()
        self.防具基础()
        self.首饰基础()
        self.特殊基础()
        self.武器基础()
        self.增幅基础()

    def 装备词条计算(self):
        for i in range(12):
            装备名称 = self.attr["装备栏"][i]
            if 装备名称:
                装备列表[装备序号[装备名称]].城镇属性(self)
                装备列表[装备序号[装备名称]].变换属性(self)

        for i in self.attr["套装栏"]:
            套装列表[套装序号[i]].城镇属性(self)
            套装列表[套装序号[i]].进图属性(self)

        self.attr["状态"] = 1
        for i in range(12):
            装备名称 = self.attr["装备栏"][i]
            if 装备名称:
                装备列表[装备序号[装备名称]].进图属性(self)

        for i in self.attr["套装栏"]:
            套装列表[套装序号[i]].进图属性(self)
        self.attr["状态"] = 0

    def 辟邪玉计算(self):
        for i in range(4):
            [name, value] = self.attr["辟邪玉栏"][i]
            if "无" != name:
                辟邪玉列表[辟邪玉序号[name]].当前值 = value
                辟邪玉列表[辟邪玉序号[name]].穿戴属性(self)

    def 护石符文计算(self):
        for i in range(3):
            if self.attr["护石栏"][i] != '无':
                self.attr["技能栏"][self.attr["技能序号"][self.attr["护石栏"][i]]].装备护石(0 if self.attr["护石类型"][i] == "魔界" else 1)

        for i in range(9):
            if self.attr["护石栏"][i // 3] != '无' and self.attr["符文栏"][i] != '无' and self.attr["符文效果"][i] != '无':
                for j in self.attr["符文效果"][i].split(","):
                    if "攻击" in j:
                        self.attr["技能栏"][self.attr["技能序号"][self.attr["符文栏"][i]]].倍率 *= 1 + int(j.replace("攻击", "").replace("%", "")) / 100
                    elif "CD" in j:
                        self.attr["技能栏"][self.attr["技能序号"][self.attr["符文栏"][i]]].CD *= 1 + int(j.replace("CD", "").replace("%", "")) / 100

    def 进图属性强化(self):
        进图属强提升 = self.attr["进图属强"]
        self.attr["火属性强化"] += 进图属强提升
        self.attr["冰属性强化"] += 进图属强提升
        self.attr["光属性强化"] += 进图属强提升
        self.attr["暗属性强化"] += 进图属强提升

    def CD倍率计算(self):
        for i in self.attr["技能栏"]:
            if i.冷却关联技能 != ["无"]:
                if i.冷却关联技能 == ["所有"]:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率(self.attr["武器类型"])
                else:
                    for j in i.冷却关联技能:
                        self.attr["技能栏"][self.attr["技能序号"][j]].CD *= i.CD缩减倍率(self.attr["武器类型"])

            if i.非冷却关联技能 != ['无']:
                if i.非冷却关联技能 == ['所有']:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率(self.attr["武器类型"])
                else:
                    for k in i.非冷却关联技能:
                        self.attr["技能栏"][self.attr["技能序号"][k]].CD /= i.CD缩减倍率(self.attr["武器类型"])

            if i.冷却关联技能2 != ["无"]:
                if i.冷却关联技能2 == ["所有"]:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率2(self.attr["武器类型"])
                else:
                    for j in i.冷却关联技能2:
                        self.attr["技能栏"][self.attr["技能序号"][j]].CD *= i.CD缩减倍率2(self.attr["武器类型"])

            if i.非冷却关联技能2 != ['无']:
                if i.非冷却关联技能2 == ['所有']:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率2(self.attr["武器类型"])
                else:
                    for k in i.非冷却关联技能2:
                        self.attr["技能栏"][self.attr["技能序号"][k]].CD /= i.CD缩减倍率2(self.attr["武器类型"])

            if i.冷却关联技能3 != ["无"]:
                if i.冷却关联技能3 == ["所有"]:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.CD *= i.CD缩减倍率3(self.attr["武器类型"])
                else:
                    for j in i.冷却关联技能3:
                        self.attr["技能栏"][self.attr["技能序号"][j]].CD *= i.CD缩减倍率3(self.attr["武器类型"])

            if i.非冷却关联技能3 != ['无']:
                if i.非冷却关联技能3 == ['所有']:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.CD /= i.CD缩减倍率3(self.attr["武器类型"])
                else:
                    for k in i.非冷却关联技能3:
                        self.attr["技能栏"][self.attr["技能序号"][k]].CD /= i.CD缩减倍率3(self.attr["武器类型"])

    def 加算冷却计算(self):
        for i in self.attr["技能栏"]:
            if i.是否有伤害 == 1:
                i.CD *= (1 - self.attr["加算冷却缩减"])

    def 被动倍率计算(self):
        if self.attr["远古记忆"] > 0:
            self.attr["进图智力"] += self.attr["远古记忆"] * 15

        if self.attr["刀魂之卡赞"] > 0:
            self.attr["进图力量"] += py_base_char.刀魂之卡赞数据[self.attr["刀魂之卡赞"]]
            self.attr["进图智力"] += py_base_char.刀魂之卡赞数据[self.attr["刀魂之卡赞"]]

        for i in self.attr["技能栏"]:
            if i.关联技能 != ["无"]:
                if i.关联技能 == ["所有"]:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率(self.attr["武器类型"])
                else:
                    for j in i.关联技能:
                        self.attr["技能栏"][self.attr["技能序号"][j]].被动倍率 *= i.加成倍率(self.attr["武器类型"])

            if i.非关联技能 != ['无']:
                if i.非关联技能 == ['所有']:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率(self.attr["武器类型"])
                else:
                    for k in i.非关联技能:
                        self.attr["技能栏"][self.attr["技能序号"][k]].被动倍率 /= i.加成倍率(self.attr["武器类型"])

            if i.关联技能2 != ["无"]:
                if i.关联技能2 == ["所有"]:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率2(self.attr["武器类型"])
                else:
                    for j in i.关联技能2:
                        self.attr["技能栏"][self.attr["技能序号"][j]].被动倍率 *= i.加成倍率2(self.attr["武器类型"])

            if i.非关联技能2 != ['无']:
                if i.非关联技能2 == ['所有']:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率2(self.attr["武器类型"])
                else:
                    for k in i.非关联技能2:
                        self.attr["技能栏"][self.attr["技能序号"][k]].被动倍率 /= i.加成倍率2(self.attr["武器类型"])

            if i.关联技能3 != ["无"]:
                if i.关联技能3 == ["所有"]:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.被动倍率 *= i.加成倍率3(self.attr["武器类型"])
                else:
                    for j in i.关联技能3:
                        self.attr["技能栏"][self.attr["技能序号"][j]].被动倍率 *= i.加成倍率3(self.attr["武器类型"])

            if i.非关联技能3 != ['无']:
                if i.非关联技能3 == ['所有']:
                    for j in self.attr["技能栏"]:
                        if j.是否有伤害 == 1:
                            j.被动倍率 /= i.加成倍率3(self.attr["武器类型"])
                else:
                    for k in i.非关联技能3:
                        self.attr["技能栏"][self.attr["技能序号"][k]].被动倍率 /= i.加成倍率3(self.attr["武器类型"])

    def 属性倍率计算(self):
        属性倍率组 = [
            self.attr["火属性强化"] - self.attr["火抗输入"],
            self.attr["冰属性强化"] - self.attr["冰抗输入"],
            self.attr["光属性强化"] - self.attr["光抗输入"],
            self.attr["暗属性强化"] - self.attr["暗抗输入"]
        ]
        self.attr["属性倍率"] = 1.05 + 0.0045 * int(max(属性倍率组))

    def 希洛克武器提升计算(self):
        pass
        # TODO

    def 希洛克属性计算(self):
        # 0下装 1戒指 2辅助装备
        # 属性1
        if self.attr["希洛克装备栏"][0] != "无":
            self.最终伤害加成(0.05)
        if self.attr["希洛克装备栏"][1] != "无":
            self.百分比三攻加成(0.05)
        if self.attr["希洛克装备栏"][2] != "无":
            self.技能攻击力加成(0.05)

        # 属性2
        if self.attr["希洛克装备栏"][0] == "奈克斯" and self.attr["希洛克装备栏"][1] == "奈克斯":
            self.伤害增加加成(0.05)
        if self.attr["希洛克装备栏"][1] == "奈克斯" and self.attr["希洛克装备栏"][2] == "奈克斯":
            self.暴击伤害加成(0.05)
        if self.attr["希洛克装备栏"][0] == "奈克斯" and self.attr["希洛克装备栏"][2] == "奈克斯":
            self.百分比力智加成(0.05)

        if self.attr["希洛克装备栏"][0] == "暗杀者" and self.attr["希洛克装备栏"][1] == "暗杀者":
            self.伤害增加加成(0.02)
            self.skill_change_cooldown(1, 45, 0.2)
        if self.attr["希洛克装备栏"][1] == "暗杀者" and self.attr["希洛克装备栏"][2] == "暗杀者":
            self.暴击伤害加成(0.03)
            self.skill_change_cooldown(60, 70, 0.2)
        if self.attr["希洛克装备栏"][0] == "暗杀者" and self.attr["希洛克装备栏"][2] == "暗杀者":
            self.百分比力智加成(0.03)
            self.skill_change_cooldown(75, 80, 0.17)

        if self.attr["希洛克装备栏"][0] == "卢克西" and self.attr["希洛克装备栏"][1] == "卢克西":
            self.skill_change_rate(50, 0.17)
            self.skill_change_rate(85, 0.17)
            self.skill_change_rate(100, 0.10)
        if self.attr["希洛克装备栏"][1] == "卢克西" and self.attr["希洛克装备栏"][2] == "卢克西":
            self.skill_change_rate(50, 0.17)
            self.skill_change_rate(85, 0.17)
            self.skill_change_rate(100, 0.10)
        if self.attr["希洛克装备栏"][0] == "卢克西" and self.attr["希洛克装备栏"][2] == "卢克西":
            self.skill_change_rate(50, 0.17)
            self.skill_change_rate(85, 0.17)
            self.skill_change_rate(100, 0.10)

        more_than_two = False
        if self.attr["希洛克装备栏"][0] == "守门人" and self.attr["希洛克装备栏"][1] == "守门人":
            more_than_two = True
            self.attr["进图属强"] += int(self.attr["所有属性强化增加"] * 30)
        if self.attr["希洛克装备栏"][1] == "守门人" and self.attr["希洛克装备栏"][2] == "守门人":
            more_than_two = True
            self.attr["进图属强"] += int(self.attr["所有属性强化增加"] * 30)
        if self.attr["希洛克装备栏"][0] == "守门人" and self.attr["希洛克装备栏"][2] == "守门人":
            more_than_two = True
            self.attr["进图属强"] += int(self.attr["所有属性强化增加"] * 30)
        if more_than_two:
            self.attr["细节1"]["宠物附魔"] = [0, 0, 60, 60, 60, 0]
            self.attr["细节2"]["手镯"][2] = 25
            self.attr["细节2"]["项链"][2] = 25
            self.attr["细节2"]["戒指"][2] = 25

        if self.attr["希洛克装备栏"][0] == "洛多斯" and self.attr["希洛克装备栏"][1] == "洛多斯":
            self.伤害增加加成(0.04)
        if self.attr["希洛克装备栏"][1] == "洛多斯" and self.attr["希洛克装备栏"][2] == "洛多斯":
            self.暴击伤害加成(0.04)
        if self.attr["希洛克装备栏"][0] == "洛多斯" and self.attr["希洛克装备栏"][2] == "洛多斯":
            self.百分比力智加成(0.04)

        # 武器
        self.attr["词条属性映射"][self.attr["希洛克武器栏"][0][0]].加成属性(self, int(self.attr["希洛克武器栏"][0][1]) * 0.01)
        if "无" not in self.attr["希洛克装备栏"]:
            self.attr["词条属性映射"][self.attr["希洛克武器栏"][1][0]].加成属性(self, int(self.attr["希洛克武器栏"][1][1]) * 0.01)

    def 面板系数计算(self):
        面板力量 = int(int((self.attr["力量"] + self.attr["进图力量"])) * (1 + self.attr["百分比力智"]))
        面板智力 = int(int((self.attr["智力"] + self.attr["进图智力"])) * (1 + self.attr["百分比力智"]))

        if self.attr["类型"] == '物理百分比':
            return int((面板力量 / 250 + 1) * (self.attr["物理攻击力"] + self.attr["进图物理攻击力"]) * (1 + self.attr["百分比三攻"]))
        elif self.attr["类型"] == '魔法百分比':
            return int((面板智力 / 250 + 1) * (self.attr["魔法攻击力"] + self.attr["进图魔法攻击力"]) * (1 + self.attr["百分比三攻"]))
        elif self.attr["类型"] == '物理固伤':
            return int((面板力量 / 250 + 1) * (self.attr["独立攻击力"] + self.attr["进图独立攻击力"]) * (1 + self.attr["百分比三攻"]))
        elif self.attr["类型"] == '魔法固伤':
            return int((面板智力 / 250 + 1) * (self.attr["独立攻击力"] + self.attr["进图独立攻击力"]) * (1 + self.attr["百分比三攻"]))

    def 增伤倍率计算(self):
        增伤倍率 = 1 + int(self.attr["伤害增加"] * 100) / 100
        增伤倍率 *= 1 + self.attr["暴击伤害"]
        增伤倍率 *= 1 + self.attr["最终伤害"]
        增伤倍率 *= self.attr["技能攻击力"]
        增伤倍率 *= 1 + self.attr["持续伤害"] * self.attr["持续伤害计算比例"]
        增伤倍率 *= 1 + self.attr["附加伤害"] + self.attr["属性附加"] * self.attr["属性倍率"]
        return 增伤倍率

    def 伤害指数计算(self):
        防御 = max(self.attr["防御输入"] - self.attr["固定减防"], 0) * (1 - self.attr["百分比减防"])
        基准倍率 = 1.5 * self.attr["主BUFF"] * (1 - 防御 / (防御 + 20000))

        self.属性倍率计算()
        self.希洛克武器提升计算()
        面板 = self.面板系数计算()
        增伤倍率 = self.增伤倍率计算()

        self.attr["伤害指数"] = 面板 * self.attr["属性倍率"] * 增伤倍率 * 基准倍率 / 100 * (1 + self.attr["希洛克BUFF"] * 0.15)

    def 装备属性计算(self):
        self.装备基础()
        self.装备词条计算()

    def 预处理(self):
        self.辟邪玉计算()
        self.希洛克属性计算()
        self.护石符文计算()
        self.装备属性计算()
        self.进图属性强化()
        self.CD倍率计算()
        self.加算冷却计算()
        self.被动倍率计算()
        self.伤害指数计算()

    def 技能释放次数计算(self):
        技能释放次数 = []
        初始释放次数 = self.attr["技能释放次数"]
        技能序号 = self.attr["技能序号"]
        时间输入 = self.attr["时间输入"]
        武器类型 = self.attr["武器类型"]
        类型 = self.attr["类型"]

        for i in self.attr["技能栏"]:
            if i.是否有伤害 == 1:
                if 初始释放次数[技能序号[i.名称]] == "/CD":
                    技能释放次数.append(int((时间输入 - i.演出时间) / i.等效CD(武器类型, 类型) + 1 + i.基础释放次数))
                elif 初始释放次数[技能序号[i.名称]] != 0:
                    技能释放次数.append(int(初始释放次数[技能序号[i.名称]]))
                else:
                    技能释放次数.append(0)
            else:
                技能释放次数.append(0)
        return 技能释放次数

    def 技能单次伤害计算(self):
        技能单次伤害 = []
        武器类型 = self.attr["武器类型"]
        伤害指数 = self.attr["伤害指数"]
        for i in self.attr["技能栏"]:
            if i.是否有伤害:
                技能单次伤害.append(i.等效百分比(武器类型) * 伤害指数 * i.被动倍率)
            else:
                技能单次伤害.append(0)
        return 技能单次伤害

    def 技能总伤害计算(self, 技能释放次数, 技能单次伤害):
        技能总伤害 = []
        for i in self.attr["技能栏"]:
            index = self.attr["技能序号"][i.名称]
            if i.是否有伤害 == 1 and 技能释放次数[index]:
                # 宠物10% 斗神12%
                技能总伤害.append(技能释放次数[index] * 技能单次伤害[index] *
                             (1.12 + 0.1 * self.attr["技能宠物次数"][index] / 技能释放次数[index]))
            else:
                技能总伤害.append(0)
        return 技能总伤害

    def 计算伤害(self):
        self.预处理()
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算()
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        # pprint(技能总伤害)
        return sum(技能总伤害)

    def 初始化(self):
        self.attr = copy.deepcopy(py_base_char.屬性)
        self.角色賦予()
        self.角色数据输入()
