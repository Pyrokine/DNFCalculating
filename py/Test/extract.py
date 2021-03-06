import importlib
import json
import py.lite
import py.base_char
import py.Test.json_formatter

char_list = [
    '极诣_剑魂', '极诣_鬼泣', '极诣_狂战士', '极诣_阿修罗', '极诣_剑影', '极诣_驭剑士', '极诣_暗殿骑士', '极诣_契魔者', '极诣_流浪武士', '归元_气功师_男', '归元_散打_男', '归元_街霸_男', '归元_柔道家_男', '归元_气功师_女', '归元_散打_女', '归元_街霸_女', '归元_柔道家_女',
    '重霄_漫游枪手_男', '重霄_枪炮师_男', '重霄_机械师_男', '重霄_弹药专家_男', '重霄_漫游枪手_女', '重霄_枪炮师_女', '重霄_机械师_女', '重霄_弹药专家_女', '知源_元素爆破师', '知源_冰结师', '知源_血法师', '知源_逐风者', '知源_次元行者', '知源_元素师', '知源_召唤师', '知源_战斗法师', '知源_魔道学者',
    '神启_圣骑士_男_战斗', '神启_蓝拳圣使', '神启_驱魔师', '神启_复仇者', '神启_异端审判者', '神启_巫女', '神启_诱魔者', '隐夜_刺客', '隐夜_死灵术士', '隐夜_忍者', '隐夜_影舞者', '皓曦_精灵骑士', '皓曦_混沌魔灵', '皓曦_帕拉丁', '皓曦_龙骑士', '不灭战神', '圣武枪魂', '屠戮之魂', '幽影夜神',
    '铁血统帅', '弑心镇魂者', '巅峰狂徒', '未来开拓者', '缔造者', '黑暗武士'
]

equip_list = [
    '大祭司的神启礼服', '大祭司的星祈礼袍', '大祭司的星祈披肩', '大祭司的星祈长裙', '大祭司的星祈凉鞋', '大祭司的星祈腰带',
    '大魔法师[???]的长袍', '魔法师[???]的长袍', '魔法师[???]的披风', '魔法师[???]的护腿', '魔法师[???]的长靴', '魔法师[???]的腰带',
    '浪漫旋律华尔兹', '优雅旋律华尔兹', '性感洒脱探戈', '魅惑律动伦巴', '激烈欢动踢踏', '热情舞动桑巴',
    '掌管生死之影夹克', '死亡阴影夹克', '死亡阴影护肩', '死亡阴影短裤', '死亡阴影长靴', '死亡阴影腰带',
    '皇家裁决者审判外套', '首席执行官裁决夹克', '首席执行官裁决肩甲', '首席执行官裁决短裤', '首席执行官裁决长靴', '首席执行官裁决腰带',
    '战无不胜上衣', '冲锋陷阵胸甲', '枪林弹雨护肩', '破釜沉舟护腿', '赤地千里战靴', '浴血奋战腰带',
    '爆裂大地之勇猛', '燃烧烈焰之勇气', '艰难求生之斗志', '肆虐狂风之意志', '寂静寒夜之忍耐', '守护战士之苦难',
    '炙炎：霸王树', '炙炎：火龙果', '炙炎：榴莲', '炙炎：荔枝', '炙炎：木瓜', '炙炎：山竹',
    '摧枯拉朽胸甲', '气吞山河战甲', '排山倒海护肩', '雷霆万钧护腿', '遮天蔽日长靴', '风起云涌腰带',
    '撒旦：愤怒之王', '撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '巴尔：堕落之魂', '亚巴顿：绝望地狱',
    '天堂之翼', '妖精之姿', '魔龙之心', '邪恶之角', '自然之核', '碎钢之牙',
    '千链万化战甲', '千链锁灵战甲', '千链锁灵肩甲', '千链锁灵护腿', '千链锁灵战靴', '千链锁灵腰带',
    '英明循环之生命', '奔流不息之岁月', '奔流不息之山川', '奔流不息之伽蓝', '奔流不息之银河', '奔流不息之狂风',
    '神赐的抉择', '人性的抉择', '矛盾的抉择', '命运的抉择', '守护的抉择', '正义的抉择',
    '生命脉动之地', '宽恕坚韧之地', '猛烈燃烧之炎', '蚕食新绿之息', '交织烈日之风', '宁静苍翠之水',
    '莱多：秩序创造者', '肯那兹：精神燎原之火', '莱多：变幻的规律', '盖柏：完美的均衡',
    '融化黑暗之温暖', '驱散月光之黎明', '拥抱晨曦之温暖', '寂静无言之露珠',
    '伽内什的永恒庇护', '四叶草之初心', '白象之庇护', '红兔之祝福',
    '至高之炎-伊弗利特', '冷焰之冰-温蒂妮', '火魔之焰-沙罗曼达', '祝福之风-西尔芙',
    '军神的心之所念', '军神的遗书', '军神的庇护宝石', '军神的古怪耳环',
    '永恒之海', '高贵之天', '智慧之地', '宽容之海',
    '时之魅影', '末日之刻', '时之漩涡', '时之矛盾',
    '等离子操控者', '能量回流控制者', '电光能量支配者', '电磁能量传送者',
    '深渊囚禁者长袍', '堕落深渊黑魔法衬衫', '暗黑术士亲笔古书', '堕落世界树之生命',
    '无尽的探求', '驱散黑暗短裤', '执着的探求', '暗黑术士的精髓',
    '永恒地狱黑暗之印', '堕入地狱之脚', '支配黑暗之环', '无尽地狱黑暗之印',
    '圣者的黄昏披风', '引路者的黄昏披风', '引路者的四季项链', '引路者的旅行书',
    '时间回溯之针', '时空漩涡护腿', '时间指引之针', '被困的时之沙',
    '次元穿越者之星', '次元漫步者长靴', '次元穿越者之印', '次元流星坠',
    '逆转结局', '地狱边缘', '悲痛者项链', '悲情者遗物',
    '响彻天地的咆哮', '灵魂的呐喊', '支配战场的呐喊', '寂寞的呼喊',
    '命运反抗者', '悲喜交加', '命运的捉弄', '命运挑战者',
    '灭世之怒', '泣血之恨', '激狂之怒', '失控之怒',
    '狂乱之逆转宿命', '疯狂之如影随形', '狂乱之坚如磐石', '狂乱之天灾降临',
    '心痛如绞的诀别', '崩溃世界的忧伤', '蓬勃生命的落幕', '悲剧人生的归寂'
]


equip_dict = {}
for i in equip_list:
    equip_dict[i] = 0

for char_name in char_list:
    print(char_name)
    char_name_en = py.base_char.map_EN_ZH[char_name]
    importlib.import_module("py.Part." + char_name_en)
    character = eval("py.Part.{0}.character()".format(char_name_en))
    character.初始化()
    character.角色基础数据生成()

    data = {
        "attr": {},
        "equip": {}
    }

    array = ["实际名称", "技能SP等级", "技能TP等级", "技能释放次数", "技能宠物次数", "强化等级", "是否增幅", "武器锻造等级", "左槽白金技能", "右槽白金技能",
             "时装上衣技能", "三觉技能选择", "辟邪玉栏", "希洛克装备栏", "希洛克武器栏", "护石栏", "护石类型", "符文栏", "符文效果", "符文选项"]
    for i in array:
        data["attr"][i] = character.attr[i]

    data["attr"]["护石选项"] = ["无"]
    for i in character.attr["技能栏"]:
        try:
            if i.是否有护石 and "魔界" in i.护石选项:
                data["attr"]["护石选项"].append("魔界 - " + i.名称)
        except:
            pass
    for i in character.attr["技能栏"]:
        try:
            if i.是否有护石 and "圣痕" in i.护石选项:
                data["attr"]["护石选项"].append("圣痕 - " + i.名称)
        except:
            pass

    data["attr"]["技能列表"] = [
        [i.名称 for i in character.attr["技能栏"]],
        [1 if i.是否有伤害 else 0 for i in character.attr["技能栏"]],
        [1 if i.是否有伤害 and i.TP上限 > 0 else 0 for i in character.attr["技能栏"]]
    ]

    data["attr"]["武器"] = character.attr["装备栏"][-1]

    data["attr"]["细节1"] = py.base_char.细节1
    data["attr"]["细节2"] = py.base_char.细节2
    data["attr"]["细节3"] = py.base_char.细节3
    data["attr"]["细节4"] = py.base_char.细节4

    data["equip"] = equip_dict

    with open("../user_data_default/{0}.json".format(char_name_en), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)

    with open("../user_data_default/{0}.json".format(char_name_en), "r", encoding="utf-8") as f:
        content = f.read()

    content = py.Test.json_formatter.handle(content)

    with open("../user_data_default/{0}.json".format(char_name_en), "w", encoding="utf-8") as f:
        f.write(content)
