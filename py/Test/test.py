# 这是一个测试文件
import copy
import json
import py.base_char
import py.lite
import importlib
import sys


array1_1 = [
    ["大祭司的星祈礼袍", "大祭司的星祈披肩", "大祭司的星祈长裙", "大祭司的星祈腰带", "大祭司的星祈凉鞋", "", "", "", "", "", ""],
    ["魔法师[???]的长袍", "魔法师[???]的披风", "魔法师[???]的护腿", "魔法师[???]的腰带", "魔法师[???]的长靴", "", "", "", "", "", ""],
    ["优雅旋律华尔兹", "性感洒脱探戈", "魅惑律动伦巴", "热情舞动桑巴", "激烈欢动踢踏", "", "", "", "", "", ""],
    ["死亡阴影夹克", "死亡阴影护肩", "死亡阴影短裤", "死亡阴影腰带", "死亡阴影长靴", "", "", "", "", "", ""],
    ["首席执行官裁决夹克", "首席执行官裁决肩甲", "首席执行官裁决短裤", "首席执行官裁决腰带", "首席执行官裁决长靴", "", "", "", "", "", ""],
    ["冲锋陷阵胸甲", "枪林弹雨护肩", "破釜沉舟护腿", "浴血奋战腰带", "赤地千里战靴", "", "", "", "", "", ""],
    ["燃烧烈焰之勇气", "艰难求生之斗志", "肆虐狂风之意志", "守护战士之苦难", "寂静寒夜之忍耐", "", "", "", "", "", ""],
    ["炙炎：火龙果", "炙炎：榴莲", "炙炎：荔枝", "炙炎：山竹", "炙炎：木瓜", "", "", "", "", "", ""],
    ["气吞山河战甲", "排山倒海护肩", "雷霆万钧护腿", "风起云涌腰带", "遮天蔽日长靴", "", "", "", "", "", ""],
    ["撒旦：沸腾之怒", "贝利亚尔：毁灭之种", "亚蒙：谎言之力", "亚巴顿：绝望地狱", "巴尔：堕落之魂", "", "", "", "", "", ""],
    ["妖精之姿", "魔龙之心", "邪恶之角", "碎钢之牙", "自然之核", "", "", "", "", "", ""],
    ["千链锁灵战甲", "千链锁灵肩甲", "千链锁灵护腿", "千链锁灵腰带", "千链锁灵战靴", "", "", "", "", "", ""],
    ["奔流不息之岁月", "奔流不息之山川", "奔流不息之伽蓝", "奔流不息之狂风", "奔流不息之银河", "", "", "", "", "", ""],
    ["人性的抉择", "矛盾的抉择", "命运的抉择", "正义的抉择", "守护的抉择", "", "", "", "", "", ""],
    ["宽恕坚韧之地", "猛烈燃烧之炎", "蚕食新绿之息", "宁静苍翠之水", "交织烈日之风", "", "", "", "", "", ""]
]
array1_2 = [
    ["大祭司的神启礼服", "大祭司的星祈披肩", "大祭司的星祈长裙", "大祭司的星祈腰带", "大祭司的星祈凉鞋", "", "", "", "", "", ""],
    ["大魔法师[???]的长袍", "魔法师[???]的披风", "魔法师[???]的护腿", "魔法师[???]的腰带", "魔法师[???]的长靴", "", "", "", "", "", ""],
    ["浪漫旋律华尔兹", "性感洒脱探戈", "魅惑律动伦巴", "热情舞动桑巴", "激烈欢动踢踏", "", "", "", "", "", ""],
    ["掌管生死之影夹克", "死亡阴影护肩", "死亡阴影短裤", "死亡阴影腰带", "死亡阴影长靴", "", "", "", "", "", ""],
    ["皇家裁决者审判外套", "首席执行官裁决肩甲", "首席执行官裁决短裤", "首席执行官裁决腰带", "首席执行官裁决长靴", "", "", "", "", "", ""],
    ["战无不胜上衣", "枪林弹雨护肩", "破釜沉舟护腿", "浴血奋战腰带", "赤地千里战靴", "", "", "", "", "", ""],
    ["爆裂大地之勇猛", "艰难求生之斗志", "肆虐狂风之意志", "守护战士之苦难", "寂静寒夜之忍耐", "", "", "", "", "", ""],
    ["炙炎：霸王树", "炙炎：榴莲", "炙炎：荔枝", "炙炎：山竹", "炙炎：木瓜", "", "", "", "", "", ""],
    ["摧枯拉朽胸甲", "排山倒海护肩", "雷霆万钧护腿", "风起云涌腰带", "遮天蔽日长靴", "", "", "", "", "", ""],
    ["撒旦：愤怒之王", "贝利亚尔：毁灭之种", "亚蒙：谎言之力", "亚巴顿：绝望地狱", "巴尔：堕落之魂", "", "", "", "", "", ""],
    ["天堂之翼", "魔龙之心", "邪恶之角", "碎钢之牙", "自然之核", "", "", "", "", "", ""],
    ["千链万化战甲", "千链锁灵肩甲", "千链锁灵护腿", "千链锁灵腰带", "千链锁灵战靴", "", "", "", "", "", ""],
    ["英明循环之生命", "奔流不息之山川", "奔流不息之伽蓝", "奔流不息之狂风", "奔流不息之银河", "", "", "", "", "", ""],
    ["神赐的抉择", "矛盾的抉择", "命运的抉择", "正义的抉择", "守护的抉择", "", "", "", "", "", ""],
    ["生命脉动之地", "猛烈燃烧之炎", "蚕食新绿之息", "宁静苍翠之水", "交织烈日之风", "", "", "", "", "", ""]
]
array1_3 = [
    ["古代祭祀的神圣仪式[2]", "古代祭祀的神圣仪式[3]", "古代祭祀的神圣仪式[5]"],
    ["遗忘魔法师的馈赠[2]", "遗忘魔法师的馈赠[3]", "遗忘魔法师的馈赠[5]"],
    ["天堂舞姬[2]", "天堂舞姬[3]", "天堂舞姬[5]"],
    ["死亡阴影[2]", "死亡阴影[3]", "死亡阴影[5]"],
    ["皇家裁决者宣言[2]", "皇家裁决者宣言[3]", "皇家裁决者宣言[5]"],
    ["龙血玄黄[2]", "龙血玄黄[3]", "龙血玄黄[5]"],
    ["贫瘠沙漠的遗产[2]", "贫瘠沙漠的遗产[3]", "贫瘠沙漠的遗产[5]"],
    ["炙炎之盛宴[2]", "炙炎之盛宴[3]", "炙炎之盛宴[5]"],
    ["擎天战甲[2]", "擎天战甲[3]", "擎天战甲[5]"],
    ["噩梦：地狱之路[2]", "噩梦：地狱之路[3]", "噩梦：地狱之路[5]"],
    ["传奇铁匠-封神[2]", "传奇铁匠-封神[3]", "传奇铁匠-封神[5]"],
    ["荆棘漫天[2]", "荆棘漫天[3]", "荆棘漫天[5]"],
    ["永恒不息之路[2]", "永恒不息之路[3]", "永恒不息之路[5]"],
    ["命运歧路[2]", "命运歧路[3]", "命运歧路[5]"],
    ["大自然的呼吸[2]", "大自然的呼吸[3]", "大自然的呼吸[5]"],
]
array2_1 = [
    ["", "", "", "", "", "莱多：变幻的规律", "肯那兹：精神燎原之火", "盖柏：完美的均衡", "", "", ""],
    ["", "", "", "", "", "拥抱晨曦之温暖", "驱散月光之黎明", "寂静无言之露珠", "", "", ""],
    ["", "", "", "", "", "白象之庇护", "四叶草之初心", "红兔之祝福", "", "", ""],
    ["", "", "", "", "", "火魔之焰-沙罗曼达", "冷焰之冰-温蒂妮", "祝福之风-西尔芙", "", "", ""]
]
array2_2 = [
    ["", "", "", "", "", "莱多：秩序创造者", "肯那兹：精神燎原之火", "盖柏：完美的均衡", "", "", ""],
    ["", "", "", "", "", "融化黑暗之温暖", "驱散月光之黎明", "寂静无言之露珠", "", "", ""],
    ["", "", "", "", "", "伽内什的永恒庇护", "四叶草之初心", "红兔之祝福", "", "", ""],
    ["", "", "", "", "", "至高之炎-伊弗利特", "冷焰之冰-温蒂妮", "祝福之风-西尔芙", "", "", ""]
]
array2_3 = [
    ["上古尘封术士[2]", "上古尘封术士[3]"],
    ["破晓曦光[2]", "破晓曦光[3]"],
    ["幸运三角[2]", "幸运三角[3]"],
    ["精灵使的权能[2]", "精灵使的权能[3]"]
]
array3_1 = [
    ["", "", "", "", "", "", "", "", "军神的古怪耳环", "军神的遗书", "军神的庇护宝石"],
    ["", "", "", "", "", "", "", "", "宽容之海", "高贵之天", "智慧之地"],
    ["", "", "", "", "", "", "", "", "时之矛盾", "末日之刻", "时之漩涡"],
    ["", "", "", "", "", "", "", "", "电磁能量传送者", "能量回流控制者", "电光能量支配者"]
]
array3_2 = [
    ["", "", "", "", "", "", "", "", "军神的心之所念", "军神的遗书", "军神的庇护宝石"],
    ["", "", "", "", "", "", "", "", "永恒之海", "高贵之天", "智慧之地"],
    ["", "", "", "", "", "", "", "", "时之魅影", "末日之刻", "时之漩涡"],
    ["", "", "", "", "", "", "", "", "等离子操控者", "能量回流控制者", "电光能量支配者"]
]
array3_3 = [
    ["军神的隐秘遗产[2]", "军神的隐秘遗产[3]"],
    ["灵宝：世间真理[2]", "灵宝：世间真理[3]"],
    ["时间战争的残骸[2]", "时间战争的残骸[3]"],
    ["能量主宰[2]", "能量主宰[3]"]
]
array4_1 = [
    ["堕落深渊黑魔法衬衫", "", "", "", "", "", "堕落世界树之生命", "", "", "暗黑术士亲笔古书", ""],
    ["引路者的黄昏披风", "", "", "", "", "", "引路者的四季项链", "", "", "引路者的旅行书", ""],
    ["地狱边缘", "", "", "", "", "", "悲痛者项链", "", "", "悲情者遗物", ""],
    ["泣血之恨", "", "", "", "", "", "激狂之怒", "", "", "失控之怒", ""]
]
array4_2 = [
    ["深渊囚禁者长袍", "", "", "", "", "", "堕落世界树之生命", "", "", "暗黑术士亲笔古书", ""],
    ["圣者的黄昏披风", "", "", "", "", "", "引路者的四季项链", "", "", "引路者的旅行书", ""],
    ["逆转结局", "", "", "", "", "", "悲痛者项链", "", "", "悲情者遗物", ""],
    ["灭世之怒", "", "", "", "", "", "激狂之怒", "", "", "失控之怒", ""]
]
array4_3 = [
    ["深渊窥视者[2]", "深渊窥视者[3]"],
    ["圣者的黄昏[2]", "圣者的黄昏[3]"],
    ["坎坷命运[2]", "坎坷命运[3]"],
    ["吞噬愤怒[2]", "吞噬愤怒[3]"],
]
array5_1 = [
    ["", "", "驱散黑暗短裤", "", "", "执着的探求", "", "", "", "", "暗黑术士的精髓"],
    ["", "", "时空漩涡护腿", "", "", "时间指引之针", "", "", "", "", "被困的时之沙"],
    ["", "", "灵魂的呐喊", "", "", "支配战场的呐喊", "", "", "", "", "寂寞的呼喊"],
    ["", "", "疯狂之如影随形", "", "", "狂乱之坚如磐石", "", "", "", "", "狂乱之天灾降临"]
]
array5_2 = [
    ["", "", "驱散黑暗短裤", "", "", "无尽的探求", "", "", "", "", "暗黑术士的精髓"],
    ["", "", "时空漩涡护腿", "", "", "时间回溯之针", "", "", "", "", "被困的时之沙"],
    ["", "", "灵魂的呐喊", "", "", "响彻天地的咆哮", "", "", "", "", "寂寞的呼喊"],
    ["", "", "疯狂之如影随形", "", "", "狂乱之逆转宿命", "", "", "", "", "狂乱之天灾降临"]
]
array5_3 = [
    ["黑魔法探求者[2]", "黑魔法探求者[3]"],
    ["时空旅行者[2]", "时空旅行者[3]"],
    ["穿透命运的呐喊[2]", "穿透命运的呐喊[3]"],
    ["狂乱追随者[2]", "狂乱追随者[3]"],
]
array6_1 = [
    ["", "", "", "", "堕入地狱之脚", "", "", "支配黑暗之环", "无尽地狱黑暗之印", "", ""],
    ["", "", "", "", "次元漫步者长靴", "", "", "次元穿越者之印", "次元流星坠", "", ""],
    ["", "", "", "", "悲喜交加", "", "", "命运的捉弄", "命运挑战者", "", ""],
    ["", "", "", "", "崩溃世界的忧伤", "", "", "蓬勃生命的落幕", "悲剧人生的归寂", "", ""]
]
array6_2 = [
    ["", "", "", "", "堕入地狱之脚", "", "", "支配黑暗之环", "永恒地狱黑暗之印", "", ""],
    ["", "", "", "", "次元漫步者长靴", "", "", "次元穿越者之印", "次元穿越者之星", "", ""],
    ["", "", "", "", "悲喜交加", "", "", "命运的捉弄", "命运反抗者", "", ""],
    ["", "", "", "", "崩溃世界的忧伤", "", "", "蓬勃生命的落幕", "心痛如绞的诀别", "", ""]
]
array6_3 = [
    ["地狱求道者[2]", "地狱求道者[3]"],
    ["次元旅行者[2]", "次元旅行者[3]"],
    ["天命无常[2]", "天命无常[3]"],
    ["悲剧的残骸[2]", "悲剧的残骸[3]"]
]

damage_basic = {
    "极诣_剑魂": 8460,
    "极诣_鬼泣": 7267,
    "极诣_狂战士": 8590,
    "极诣_阿修罗": 8475,
    "极诣_剑影": 7517,
    "极诣_驭剑士": 7836,
    "极诣_暗殿骑士": 7301,
    "极诣_契魔者": 8035,
    "极诣_流浪武士": 8004,
    "归元_气功师_男": 9100,
    "归元_散打_男": 7377,
    "归元_街霸_男": 7924,
    "归元_柔道家_男": 7616,
    "归元_气功师_女": 8093,
    "归元_散打_女": 8964,
    "归元_街霸_女": 7584,
    "归元_柔道家_女": 7079,
    "重霄_漫游枪手_男": 7837,
    "重霄_枪炮师_男": 7776,
    "重霄_机械师_男": 7563,
    "重霄_弹药专家_男": 8268,
    "重霄_漫游枪手_女": 8442,
    "重霄_枪炮师_女": 8086,
    "重霄_机械师_女": 7606,
    "重霄_弹药专家_女": 8444,
    "知源_元素爆破师": 8685,
    "知源_冰结师": 8224,
    "知源_血法师": 7867,
    "知源_逐风者": 7119,
    "知源_次元行者": 9110,
    "知源_元素师": 9546,
    "知源_召唤师": 9276,
    "知源_战斗法师": 9362,
    "知源_魔道学者": 8367,
    "神启_圣骑士_男_战斗": 7874,
    "神启_蓝拳圣使": 8166,
    "神启_驱魔师": 8259,
    "神启_复仇者": 8387,
    "神启_异端审判者": 7990,
    "神启_巫女": 7575,
    "神启_诱魔者": 7634,
    "隐夜_刺客": 9279,
    "隐夜_死灵术士": 8195,
    "隐夜_忍者": 8323,
    "隐夜_影舞者": 8349,
    "大地女神": 8552,
    "黑曜神": 8685,
    "破晓女神": 6905,
    "龙神": 8580,
    "不灭战神": 7095,
    "圣武枪魂": 6585,
    "屠戮之魂": 6483,
    "幽影夜神": 5348,
    "铁血统帅": 5816,
    "弑心镇魂者": 7764,
    "巅峰狂徒": 5815,
    "未来开拓者": 5414,
    "缔造者": 7496,
    "黑暗武士": 6579,
}

char_list = [i for i in damage_basic]
# char_list = ["极诣_剑魂"]

test_list = [
    ["*** 防具五件套 ***", 15, "array1_1", "array1_2", "array1_3"],
    ["*** 首饰三件套 ***", 4, "array2_1", "array2_2", "array2_3"],
    ["*** 特殊三件套 ***", 4, "array3_1", "array3_2", "array3_3"],
    ["*** 上链左三件套 ***", 4, "array4_1", "array4_2", "array4_3"],
    ["*** 镯下右三件套 ***", 4, "array5_1", "array5_2", "array5_3"],
    ["*** 环指鞋三件套 ***", 4, "array6_1", "array6_2", "array6_3"],
]


def calc_more_attr(temp_char):
    array = [
        str(temp_char.站街力量()),
        str(temp_char.站街智力()),
        str(int(temp_char.站街物理攻击力())),
        str(int(temp_char.站街魔法攻击力())),
        str(int(temp_char.站街独立攻击力())),
        str(temp_char.attr["火属性强化"]),
        str(temp_char.attr["冰属性强化"]),
        str(temp_char.attr["光属性强化"]),
        str(temp_char.attr["暗属性强化"]),
        str(int(temp_char.attr["伤害增加"] * 100)) + "%",
        str(int(temp_char.attr["暴击伤害"] * 100)) + "%",
        str(int(temp_char.attr["最终伤害"] * 100)) + "%",
        str(int(temp_char.attr["百分比力智"] * 100)) + "%",
        str(int(temp_char.attr["百分比三攻"] * 100)) + "%",
        str(int(temp_char.attr["附加伤害"] * 100)) + "%",
        str(int(temp_char.attr["属性附加"] * 100)) + "%",
        str(int(temp_char.attr["持续伤害"] * 100)) + "%",
        str(int(temp_char.attr["加算冷却缩减"] * 100)) + "%",
        str(int(temp_char.attr["技能攻击力"] * 100 - 100)) + "%"
    ]
    return "\n".join(array)


# 装备对角色适配性测试
for char_name in char_list:
    print("\n开始测试 - " + char_name)
    char_name_en = py.base_char.map_EN_ZH[char_name]
    with open("../user_data_default/{0}.json".format(char_name_en), "r", encoding="utf-8") as f:
        user_data = json.load(f)

    importlib.import_module("py.Part." + char_name_en)
    character = eval("py.Part.{0}.character()".format(char_name_en))
    character.初始化()

    temp = copy.deepcopy(character)
    temp.用户数据覆盖(user_data)
    temp.角色基础数据生成()
    sum_damage = int(temp.计算伤害() / 100000000)

    result = calc_more_attr(temp)
    # print(result)
    print(sum_damage, damage_basic[char_name])
    if sum_damage == damage_basic[char_name]:
        print("伤害基准测试通过")
    else:
        print("伤害基准测试不通过")
        sys.exit()

    for each in test_list:
        # print(each[0])
        for i in range(each[1]):
            temp = copy.deepcopy(character)
            exec('user_data["attr"]["装备栏"] = {0}[i] + ["哈蒂-赎月者"]'.format(each[2]))
            exec('user_data["attr"]["套装栏"] = {0}[i]'.format(each[4]))
            temp.用户数据覆盖(user_data)
            temp.角色基础数据生成()
            sum_damage1 = int(temp.计算伤害() / 100000000)
            calc_more_attr(temp)

            temp = copy.deepcopy(character)
            exec('user_data["attr"]["装备栏"] = {0}[i] + ["哈蒂-赎月者"]'.format(each[3]))
            exec('user_data["attr"]["套装栏"] = {0}[i]'.format(each[4]))
            temp.用户数据覆盖(user_data)
            temp.角色基础数据生成()
            sum_damage2 = int(temp.计算伤害() / 100000000)
            calc_more_attr(temp)

            if sum_damage1 > 2000 or sum_damage2 > 2000:
                print("伤害异常")
                sys.exit()
            else:
                # print("第{0}套测试通过，伤害分别为{1}、{2}".format(i, sum_damage1, sum_damage2))
                pass
