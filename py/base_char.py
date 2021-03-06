from py import base_equip as py_base_equip


class 技能:
    名称 = ''
    备注 = ''
    所在等级 = 0
    等级上限 = 0
    等级 = 0
    基础等级 = 0
    等级溢出 = 0
    自定义描述 = 0

    关联技能 = ['无']
    关联技能2 = ['无']
    关联技能3 = ['无']
    非关联技能 = ['无']
    非关联技能2 = ['无']
    非关联技能3 = ['无']
    冷却关联技能 = ['无']
    冷却关联技能2 = ['无']
    冷却关联技能3 = ['无']
    非冷却关联技能 = ['无']
    非冷却关联技能2 = ['无']
    非冷却关联技能3 = ['无']

    版本 = "GF"

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
                if self.基础等级 != self.等级上限 and self.关联技能 != ['无']:
                    self.等级溢出 = 1
            else:
                self.等级 += x


class 主动技能(技能):
    # 只扩展了技能的三条属性，第一条技能hit默认1,2、3条hit默认为0，需要手动赋值
    # 如果需要继续扩展，可以在各自职业类内继承后自行扩展，同时需要重写下等效百分比函数
    # 固伤在填写基础及成长的时候需要注意，技能面板/独立得到的成长及数值需要*100
    基础 = 0.0
    成长 = 0.0
    攻击次数 = 1.0
    基础2 = 0.0
    成长2 = 0.0
    攻击次数2 = 0.0
    基础3 = 0.0
    成长3 = 0.0
    攻击次数3 = 0.0
    CD = 0.0
    TP成长 = 0.0
    TP上限 = 0
    TP等级 = 0
    是否主动 = 1
    是否有伤害 = 1
    恢复 = 1.0
    倍率 = 1.0
    被动倍率 = 1.0
    基础释放次数 = 0
    演出时间 = 0
    是否有护石 = 0
    护石选项 = ['魔界']

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return int((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                    self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率)

    def 等效CD(self, 武器类型, 输出类型):
        return round(self.CD / self.恢复 * py_base_equip.武器冷却惩罚(武器类型, 输出类型, self.版本), 1)


class 被动技能(技能):
    是否主动 = 0
    是否有伤害 = 0
    关联技能 = ['所有']


屬性 = {
    "实际名称": '',
    "角色": '',
    "职业": '',

    "武器选项": [],
    "类型选择": [],

    "类型": '',
    "防具类型": '',
    "防具精通属性": [],

    "基础力量": 0,
    "基础智力": 0,
    "基础体力": 0,
    "基础精神": 0,

    "力量": 0,
    "智力": 0,
    "体力": 0,
    "精神": 0,
    "物理攻击力": 65,
    "魔法攻击力": 65,
    "独立攻击力": 1045,
    "火属性强化": 13,
    "冰属性强化": 13,
    "光属性强化": 13,
    "暗属性强化": 13,

    "进图力量": 0.0,
    "进图智力": 0.0,
    "进图体力": 0.0,
    "进图精神": 0.0,
    "进图物理攻击力": 0,
    "进图魔法攻击力": 0,
    "进图独立攻击力": 0,
    "进图属强": 0,

    "技能栏": [],
    "技能序号": {},

    "装备栏": [],
    "套装栏": [],
    "武器类型": '',

    "是否增幅": [0] * 12,
    "强化等级": [12] * 12,
    "改造等级": [5] * 12,
    "武器锻造等级": 8,

    "护石栏": ["无", "无", "无"],
    "护石类型": ["魔界", "魔界", "魔界"],
    "符文栏": ["无", "无", "无", "无", "无", "无", "无", "无", "无"],
    "符文效果": ["攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%"],

    "职业分类": '输出',
    "主BUFF": 1.0,
    "希洛克BUFF": False,

    # 红阵，远古记忆 -1表示没有该技能
    "远古记忆": -1,
    "刀魂之卡赞": -1,

    "黄字": 0.0,
    "爆伤": 0.0,

    "伤害增加": 0.0,
    "暴击伤害": 0.0,
    "最终伤害": 0.0,
    "百分比力智": 0.0,
    "百分比三攻": 0.0,
    "附加伤害": 0.0,
    "属性附加": 0.0,
    "持续伤害": 0.0,
    "加算冷却缩减": 0.0,
    "技能攻击力": 1.0,

    "百分比减防": 0.0,
    "固定减防": 0,

    # 队友增幅系数
    "队友增幅系数": 1.0,

    "防御输入": 443243,
    "火抗输入": 0,
    "冰抗输入": 0,
    "光抗输入": 0,
    "暗抗输入": 0,

    "攻击速度": 0.00,
    "移动速度": 0.00,
    "释放速度": 0.00,
    "命中率": 0.0,
    "回避率": 0.0,
    "物理暴击率": 0.00,
    "魔法暴击率": 0.00,

    "时间输入": 25,
    "次数输入": [],
    "宠物次数": [],

    "希洛克武器词条": 0,
    "武器词条触发": 0,

    "攻击属性": 0,

    # 是否为图内状态
    "状态": 0,
    # 是否为输出装备描述
    "装备描述": 0,

    "持续伤害计算比例": 1.0,
    # 辟邪玉属性
    "附加伤害增加增幅": 1.0,
    "属性附加伤害增加增幅": 1.0,
    "技能伤害增加增幅": 1.0,
    "暴击伤害增加增幅": 1.0,
    "伤害增加增幅": 1.0,
    "最终伤害增加增幅": 1.0,
    "力量智力增加增幅": 1.0,
    "物理魔法攻击力增加增幅": 1.0,
    "所有属性强化增加": 1.0,

    "辟邪玉栏": [
        ["无", 0],
        ["无", 0],
        ["无", 0],
        ["无", 0]
    ],

    "一觉序号": 0,
    "二觉序号": 0,
    "三觉序号": 0,

    "护石选项": [],
    "符文选项": [],

    # 0武器，1首饰，2特殊，3防具
    "变换词条": [
        # 原词条类型，原词条数值，可洗最小值，可洗最大值，择优不考虑觉醒
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ],

    # 下装 戒指 辅助装备
    "希洛克装备栏": ["无", "无", "无"],
    "希洛克武器栏": [
        ["无", 6],
        ["无", 3]
    ],

    "词条属性映射": {},
    "黑鸦武器属性列表": []
}

细节1 = {
    #             力量  智力  物攻   魔攻   独立  属强
    "工会属性":    [120, 120,  0,    0,    0,    0],
    "训练官":     [0,    0,    0,    0,    0,   0],
    "婚戒":       [15,  15,   0,    0,    0,    0],
    "冒险团":     [290,  290,  0,    0,    0,   0],
    "收集箱":     [50,   50,   50,   50,  50,  10],
    "勋章":       [48,   48,   30,   30,  30,   7],
    "名称装饰卡":  [3,    3,    0,    0,   0,    0],
    "副武器/盾牌": [0,    0,    0,    0,   0,    0],
    "宠物装备-红": [0,    0,    0,    0,   0,    0],
    "宠物装备-蓝": [0,    0,    30,   30,  30,    0],
    "宠物装备-绿": [0,    0,    40,   40,  40,  20],
    "宠物附魔":    [0,    0,   0,     0,   0,   16],
    "站街修正":    [0,    0,   0,     0,   0,   0],
    "进图修正":    [0,    0,   0,     0,   0,   0]
}

细节3 = {
    "晶体契约":    [0,   0,    40,   40,   40,   0],
    "快捷栏纹章":  [0,    0,    20,   20,  20,   0]
}

细节4 = {
    "婚房":       [0,   0,    10,   10,   20,   8]
}

细节2 = {
    #         力智  三攻  属强 徽力智 徽三攻
    "上衣":    [40,  70,  0,   40,   0],
    "下装":    [40,  70,  0,   40,   0],
    "头肩":    [75,  20,  0,   0,    0],
    "腰带":    [0,   36,  0,   70,   0],
    "鞋":      [0,   36,  0,   0,    40],
    "手镯":    [0,   0,   30,  0,    40],
    "项链":    [0,   0,   30,  0,    0],
    "戒指":    [0,   0,   30,  70,   0],
    "左槽":    [0,   0,   12,  8,    0],
    "右槽":    [0,   0,   20,  8,    0],
    "耳环":    [150, 0,   0,   0,    0],
    "武器":    [0,   30,  15,  0,    0],
    "称号":    [0,   40,  15,  0,    0],
    "光环":    [0,   0,   0,   0,    40],
    "武器装扮": [0,   0,   0,   0,    40],
    "皮肤":    [0,   0,   6,   0,    40],
    "时装":    [230, 0,   10,  0,    0]
}

刀魂之卡赞数据 = [0, 31, 40, 48, 58, 67, 79, 90, 103, 116, 131, 145, 161, 178, 194, 212, 230, 250, 270, 292, 313]

角色基础系数 = {
    '魔枪士': [4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5],
    '格斗家(女)': [5, 5, 4, 4, 7.5, 7.5, 4.5, 4.5],
    '格斗家(男)': [5, 5, 4, 4, 7.5, 7.5, 4.5, 4.5],
    '枪剑士': [4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5],
    '神枪手(女)': [4.5, 4.5, 4.5, 4.5, 6.5, 6.5, 5.5, 5.5],
    '神枪手(男)': [4.5, 4.5, 4.5, 4.5, 6.5, 6.5, 5.5, 5.5],
    '守护者': [4.8, 4.8, 4.2, 4.2, 7, 7, 5, 5],
    '魔法师(女)': [4, 4, 5, 5, 4.5, 4.5, 7.5, 7.5],
    '魔法师(男)': [3.5, 4, 5.5, 5, 4, 4.5, 8, 7.5],
    '暗夜使者': [5, 4, 5, 4, 7.5, 5.5, 6.5, 4.5],
    '缔造者': [4, 4, 5, 5, 4.5, 4.5, 7.5, 7.5],
    '黑暗武士': [4.8, 4.8, 4.2, 4.2, 7.5, 7.5, 4.5, 4.5],
    '鬼剑士(男)': [4.8, 4.8, 4.2, 4.2, 7.5, 7.5, 4.5, 4.5],
    '鬼剑士(女)': [4.6, 4.6, 4.4, 4.4, 7, 7, 5, 5],
    '圣职者(男)': [4.7, 4.8, 4, 4.5, 6.5, 6.5, 4.5, 6.5],
    '圣职者(女)': [4.7, 4.8, 4, 4.5, 6.5, 6.5, 4.5, 6.5]
}

职业基础数据 = {
    '征战者-魔枪士': [5.5, 5.5, 3.5, 3.5],
    '决战者-魔枪士': [5, 5, 4, 4],
    '狩猎者-魔枪士': [3, 4.5, 6, 4.5],
    '暗枪士-魔枪士': [3.5, 3.5, 5.5, 5.5],
    '气功师-格斗家(女)': [3.5, 3.5, 5.5, 5.5],
    '散打-格斗家(女)': [5.5, 5.5, 3.5, 3.5],
    '街霸-格斗家(女)': [5, 4, 5, 4],
    '柔道家-格斗家(女)': [5, 6, 3.5, 3.5],
    '气功师-格斗家(男)': [3.5, 3.5, 5.5, 5.5],
    '散打-格斗家(男)': [5.5, 5.5, 3.5, 3.5],
    '街霸-格斗家(男)': [5, 4, 5, 4],
    '柔道家-格斗家(男)': [5, 6, 3.5, 3.5],
    '暗刃-枪剑士': [5.5, 5.5, 3.5, 3.5],
    '特工-枪剑士': [5, 5, 4, 4],
    '战线佣兵-枪剑士': [5.2, 5, 3.5, 4.3],
    '源能专家-枪剑士': [3.5, 3.5, 5.5, 5.5],
    '漫游枪手-神枪手(女)': [5.5, 5.5, 3.5, 3.5],
    '枪炮师-神枪手(女)': [5.5, 5.5, 3.5, 3.5],
    '机械师-神枪手(女)': [3.5, 3.5, 5.5, 5.5],
    '弹药专家-神枪手(女)': [4.7, 4.3, 4.7, 4.3],
    '漫游枪手-神枪手(男)': [5.5, 5.5, 3.5, 3.5],
    '枪炮师-神枪手(男)': [5.5, 5.5, 3.5, 3.5],
    '机械师-神枪手(男)': [3.5, 3.5, 5.5, 5.5],
    '弹药专家-神枪手(男)': [4.7, 4.3, 4.7, 4.3],
    '精灵骑士-守护者': [5, 5, 4, 4],
    '混沌魔灵-守护者': [3.5, 3.5, 5.5, 5.5],
    '帕拉丁-守护者': [5, 5.5, 2, 5.5],
    '龙骑士-守护者': [5, 5, 4, 4],
    '元素师-魔法师(女)': [3.5, 3.5, 5.5, 5.5],
    '召唤师-魔法师(女)': [3.8, 3.7, 5.3, 5.2],
    '战斗法师-魔法师(女)': [5, 4, 5, 4],
    '魔道学者-魔法师(女)': [4.5, 4, 5.2, 4.3],
    '小魔女-魔法师(女)': [4.7, 4.8, 5.5, 4.5],
    '元素爆破师-魔法师(男)': [3.5, 3.5, 5.5, 5.5],
    '冰结师-魔法师(男)': [3.5, 3.7, 5.5, 5.2],
    '血法师-魔法师(男)': [5.5, 5.5, 3.5, 3.5],
    '逐风者-魔法师(男)': [5.5, 5.2, 3.5, 3.8],
    '次元行者-魔法师(男)': [3.5, 3.5, 5.5, 5.5],
    '刺客-暗夜使者': [5.3, 4.5, 4.2, 4],
    '死灵术士-暗夜使者': [4.7, 3.5, 5.3, 4.5],
    '忍者-暗夜使者': [4.5, 3.5, 5.5, 4.5],
    '影舞者-暗夜使者': [5.5, 4.5, 4, 4],
    '缔造者-缔造者': [4, 4, 5, 5],
    '黑暗武士-黑暗武士': [4.8, 4.8, 4.2, 4.2],
    '剑魂-鬼剑士(男)': [5, 5, 4, 4],
    '鬼泣-鬼剑士(男)': [3.5, 3.5, 5.5, 5.5],
    '狂战士-鬼剑士(男)': [5.5, 5.5, 3.5, 3.5],
    '阿修罗-鬼剑士(男)': [3, 4.5, 6, 4.5],
    '剑影-鬼剑士(男)': [5, 5, 4, 4],
    '驭剑士-鬼剑士(女)': [5, 5, 4, 4],
    '暗殿骑士-鬼剑士(女)': [3.5, 3.5, 5.5, 5.5],
    '契魔者-鬼剑士(女)': [5.5, 5.5, 3.5, 3.5],
    '流浪武士-鬼剑士(女)': [5.5, 5.5, 3.5, 3.5],
    '圣骑士-圣职者(男)': [3.5, 5.5, 3.5, 5.5],
    '蓝拳圣使-圣职者(男)': [5.2, 5, 3.9, 3.9],
    '驱魔师-圣职者(男)': [5, 4, 5, 4],
    '复仇者-圣职者(男)': [3.5, 3.5, 5.5, 5.5],
    '圣骑士-圣职者(女)': [3.5, 5.5, 5.5, 3.5],
    '异端审判者-圣职者(女)': [5.2, 5, 3.5, 4.3],
    '巫女-圣职者(女)': [3.5, 3.5, 5.5, 5.5],
    '诱魔者-圣职者(女)': [3.5, 3.5, 5.5, 5.5]
}

map_EN_ZH = {
    "极诣_剑魂": "Neo_Blade_Master",
    "极诣_鬼泣": "Neo_Soul_Bender",
    "极诣_狂战士": "Neo_Berserker",
    "极诣_阿修罗": "Neo_Asura",
    "极诣_剑影": "Neo_Ghostblade",
    "极诣_驭剑士": "Neo_Sword_Master",
    "极诣_暗殿骑士": "Neo_Dark_Templar",
    "极诣_契魔者": "Neo_Demon_Slayer",
    "极诣_流浪武士": "Neo_Vagabond",
    "归元_气功师_男": "Neo_Nen_Master_Male",
    "归元_散打_男": "Neo_Striker_Male",
    "归元_街霸_男": "Neo_Brawler_Male",
    "归元_柔道家_男": "Neo_Grappler_Male",
    "归元_气功师_女": "Neo_Nen_Master_Female",
    "归元_散打_女": "Neo_Striker_Female",
    "归元_街霸_女": "Neo_Brawler_Female",
    "归元_柔道家_女": "Neo_Grappler_Female",
    "重霄_漫游枪手_男": "Neo_Ranger_Male",
    "重霄_枪炮师_男": "Neo_Launcher_Male",
    "重霄_机械师_男": "Neo_Mechanic_Male",
    "重霄_弹药专家_男": "Neo_Spitfire_Male",
    "重霄_漫游枪手_女": "Neo_Ranger_Female",
    "重霄_枪炮师_女": "Neo_Launcher_Female",
    "重霄_机械师_女": "Neo_Mechanic_Female",
    "重霄_弹药专家_女": "Neo_Spitfire_Female",
    "知源_元素爆破师": "Neo_Elemental_Bomber",
    "知源_冰结师": "Neo_Glacial_Master",
    "知源_血法师": "Neo_Blood_Mage",
    "知源_逐风者": "Neo_Swift_Master",
    "知源_次元行者": "Neo_Dimension_Walker",
    "知源_元素师": "Neo_Elementalist",
    "知源_召唤师": "Neo_Summoner",
    "知源_战斗法师": "Neo_Battle_Mage",
    "知源_魔道学者": "Neo_Witch",
    "神启_圣骑士_男_战斗": "Neo_Crusader_Male_Fight",
    "神启_蓝拳圣使": "Neo_Monk",
    "神启_驱魔师": "Neo_Exorcist",
    "神启_复仇者": "Neo_Avenger",
    "神启_异端审判者": "Neo_Inquisitor",
    "神启_巫女": "Neo_Shaman",
    "神启_诱魔者": "Neo_Mistress",
    "隐夜_刺客": "Neo_Rogue",
    "隐夜_死灵术士": "Neo_Necromancer",
    "隐夜_忍者": "Neo_Kunoichi",
    "隐夜_影舞者": "Neo_Shadow_Dancer",
    "皓曦_精灵骑士": "Neo_Elven_Knight",
    "皓曦_混沌魔灵": "Neo_Chaos",
    "皓曦_帕拉丁": "Neo_Lightbringer",
    "皓曦_龙骑士": "Neo_Dragon_Knight",
    "不灭战神": "Warlord",
    "圣武枪魂": "Durandal",
    "屠戮之魂": "Deimos",
    "幽影夜神": "Erebus",
    "铁血统帅": "Godfather",
    "弑心镇魂者": "Executioner",
    "巅峰狂徒": "Renegade",
    "未来开拓者": "Pathfinder",
    "缔造者": "Creator",
    "黑暗武士": "Dark_Knight",
}

value_range = {
    0: [],
    1: list(range(101)),  # SP等级
    2: list(range(6)),  # TP等级
    3: ["/CD"] + [str(i) for i in range(11)],  # 技能释放次数
    4: list(range(11)),  # 技能宠物次数
    5: list(range(32)),  # 强化等级
    6: list(range(9)),  # 锻造等级
    7: ["无", "攻击+2%,CD+1%", "攻击+3%,CD+2%", "攻击+5%,CD+3%", "攻击+6%,CD+4%",
        "攻击-1%,CD-3%", "攻击-2%,CD-4%", "攻击-3%,CD-6%", "攻击-4%,CD-7%",
        "攻击+1%", "攻击+2%", "攻击+3%", "攻击+4%",
        "CD-2%", "CD-3%", "CD-4%", "CD-5%"],  # 符文
    8: ["无", "奈克斯", "暗杀者", "卢克西", "守门人", "洛多斯"],  # 希洛克装备
    9: ["强化", "增幅"],
    10: ["无", "力智", "三攻", "黄字", "白字", "爆伤", "终伤"],  # 希洛克武器属性
    11: [[6, 8, 10], [3, 4, 5]],  # 希洛克武器数值
}
