from py.base_char import *
import py.lite


# 技能后的倍率是魔化后的倍率
class skill0(主动技能):
    名称 = '恶魔之手'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    数据1 = [0, 426, 469, 512, 555, 599, 642, 685, 728, 772, 815, 858, 901, 945, 988, 1031, 1074, 1117, 1161, 1204, 1247, 1290,
           1334, 1377, 1420, 1463, 1507, 1550, 1593, 1636, 1680, 1723, 1766, 1809, 1852, 1896, 1939, 1982, 2025, 2069, 2112,
           2155, 2198, 2242, 2285, 2328, 2371, 2415, 2458, 2501, 2544, 2587, 2631, 2674, 2717, 2760, 2804, 2847, 2890, 2933,
           2977, 3020, 3063, 3106, 3150, 3193, 3236, 3279, 3322, 3366, 3409]
    数据2 = [0, 852, 938, 1025, 1111, 1198, 1284, 1371, 1457, 1544, 1630, 1717, 1803, 1890, 1976, 2062, 2149, 2235, 2322, 2408,
           2495, 2581, 2668, 2754, 2841, 2927, 3014, 3100, 3187, 3273, 3360, 3446, 3532, 3619, 3705, 3792, 3878, 3965, 4051,
           4138, 4224, 4311, 4397, 4484, 4570, 4657, 4743, 4830, 4916, 5002, 5089, 5175, 5262, 5348, 5435, 5521, 5608, 5694,
           5781, 5867, 5954, 6040, 6127, 6213, 6300, 6386, 6472, 6559, 6645, 6732, 6818]
    倍率 = 2.24  # 魔化
    CD = 6 * 1.6
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill1(主动技能):
    名称 = '死亡切割'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 190, 209, 228, 248, 268, 287, 306, 325, 344, 364, 383, 402, 422, 441, 460, 480, 499, 518, 537, 556, 576, 596,
           615, 634, 653, 672, 691, 712, 731, 750, 769, 788, 807, 827, 846, 865, 885, 904, 923, 943, 962, 981, 1000, 1019,
           1040, 1059, 1078, 1097, 1116, 1135, 1155, 1175, 1194, 1213, 1232, 1251, 1271, 1290, 1309, 1329, 1348, 1367, 1387,
           1406, 1425, 1444, 1463, 1482, 1503, 1522]
    攻击次数1 = 6
    倍率 = 2.25 * 1.163  # 魔化 三觉
    CD = 5 * 1.6
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill2(被动技能):
    名称 = '镰刀精通'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class skill3(主动技能):
    名称 = '裂地锤'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 441, 487, 532, 577, 620, 668, 714, 759, 805, 852, 896, 943, 986, 1034, 1079, 1124, 1170, 1216, 1260, 1307, 1351,
           1397, 1444, 1488, 1534, 1582, 1625, 1670, 1716, 1761, 1809, 1852, 1899, 1942, 1990, 2036, 2081, 2127, 2174, 2218,
           2265, 2308, 2354, 2401, 2444, 2492, 2538, 2582, 2629, 2673, 2719, 2765, 2810, 2855, 2902, 2947, 2992, 3038, 3083,
           3128, 3176, 3221, 3266, 3312, 3357, 3402, 3448, 3494, 3539, 3585]
    攻击次数1 = 8  # 最高8hit 三觉优化
    CD = 5 * 1.55
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill4(被动技能):
    名称 = '恶魔诅咒'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10
    关联技能 = ['不朽战吼', '地狱之门', '厄运之轮', '恶魔之拳', '恶魔之手', '恶魔之握', '复仇之刺', '黑暗权能', '回旋飞镰', '毁灭强击', '裂地锤', '末日浩劫', '死亡切割', '永堕：混沌弑神', '审判', '魔流光杀', '崩坏福音']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.03 * self.等级, 5)


class skill5(主动技能):
    名称 = '回旋飞镰'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [0, 642, 698, 756, 820, 897, 948, 1006, 1077, 1133, 1191, 1249, 1319, 1377, 1435, 1499, 1556, 1613, 1684, 1742,
           1812, 1870, 1934, 1991, 2048, 2106, 2177, 2241, 2299, 2363, 2419, 2477, 2541, 2599, 2670, 2727, 2792, 2848, 2906,
           2970, 3028, 3105, 3162, 3227, 3283, 3341, 3405, 3463, 3521, 3585, 3655, 3712, 3776, 3834, 3898, 3956, 4013, 4078,
           4134, 4205, 4262, 4327, 4384, 4449, 4506, 4569, 4627, 4698, 4755, 4819, 4877]
    攻击次数1 = 1
    数据2 = [0, 377, 417, 457, 495, 531, 572, 612, 649, 689, 729, 769, 806, 846, 886, 924, 964, 1004, 1041, 1081, 1118, 1158,
           1196, 1236, 1276, 1316, 1353, 1391, 1431, 1470, 1509, 1549, 1588, 1627, 1665, 1704, 1743, 1783, 1823, 1861, 1901,
           1937, 1977, 2015, 2055, 2095, 2133, 2173, 2213, 2251, 2288, 2328, 2367, 2407, 2445, 2485, 2525, 2563, 2603, 2640,
           2680, 2718, 2758, 2797, 2836, 2875, 2915, 2952, 2992, 3030, 3070]
    攻击次数2 = 6  # 最高6hit
    倍率 = 1.9 * 1.05  # 魔化 三觉
    CD = 10 * 1.5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill6(主动技能):
    名称 = '复仇之刺'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [0, 2400, 2643, 2886, 3131, 3374, 3617, 3861, 4104, 4347, 4591, 4835, 5079, 5322, 5565, 5809, 6052, 6295, 6540,
           6783, 7027, 7270, 7513, 7757, 8001, 8244, 8488, 8731, 8974, 9218, 9461, 9706, 9949, 10192, 10436, 10679, 10922,
           11166, 11410, 11654, 11897, 12140, 12384, 12627, 12871, 13115, 13358, 13601, 13845, 14088, 14331, 14576, 14819,
           15063, 15306, 15549, 15793, 16036, 16280, 16524, 16767, 17010, 17254, 17497, 17740, 17985, 18228, 18472, 18715,
           18958, 19202]
    数据2 = [0, 3504, 3859, 4214, 4571, 4926, 5281, 5637, 5992, 6347, 6703, 7059, 7415, 7770, 8125, 8481, 8836, 9191, 9548,
           9903, 10259, 10614, 10969, 11325, 11681, 12036, 12392, 12747, 13102, 13458, 13813, 14171, 14526, 14880, 15237,
           15591, 15946, 16302, 16659, 17015, 17370, 17724, 18081, 18435, 18792, 19148, 19503, 19857, 20214, 20568, 20923,
           21281, 21636, 21992, 22347, 22702, 23058, 23413, 23769, 24125, 24480, 24835, 25191, 25546, 25900, 26258, 26613,
           26969, 27324, 27679, 28035]
    倍率 = 1.165  # 三觉
    CD = 10 * 1.6
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill7(主动技能):
    名称 = '厄运之轮'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 591, 652, 712, 772, 831, 892, 952, 1012, 1072, 1131, 1192, 1252, 1312, 1371, 1432, 1492, 1552, 1612, 1673, 1732,
           1792, 1852, 1912, 1973, 2032, 2092, 2152, 2213, 2272, 2332, 2392, 2453, 2513, 2572, 2632, 2692, 2753, 2813, 2872,
           2932, 2993, 3053, 3113, 3172, 3233, 3293, 3353, 3412, 3472, 3533, 3593, 3653, 3712, 3773, 3833, 3893, 3953, 4014,
           4073, 4133, 4193, 4252, 4313, 4373, 4433, 4493, 4554, 4613, 4673, 4733]
    攻击次数1 = 6
    倍率 = 2.34 * 1.165  # 魔化 三觉
    CD = 16 * 1.5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25
        elif x == 1:
            self.倍率 *= 1.34


class skill8(主动技能):
    名称 = '恶魔之拳'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [0, 165, 182, 199, 216, 232, 249, 266, 283, 300, 316, 333, 350, 367, 384, 400, 417, 434, 451, 468, 484, 501, 518,
           535, 552, 568, 585, 602, 619, 636, 652, 669, 686, 703, 720, 736, 753, 770, 787, 804, 820, 837, 854, 871, 888, 904,
           921, 938, 955, 972, 988, 1005, 1022, 1039, 1056, 1072, 1089, 1106, 1123, 1140, 1156, 1173, 1190, 1207, 1224, 1240,
           1257, 1274, 1291, 1308, 1324]
    攻击次数1 = 10
    倍率1 = 1
    数据2 = [0, 6399, 7049, 7698, 8347, 8996, 9646, 10295, 10944, 11593, 12243, 12892, 13541, 14191, 14840, 15489, 16138, 16788,
           17437, 18086, 18735, 19385, 20034, 20683, 21332, 21982, 22631, 23280, 23930, 24579, 25228, 25877, 26527, 27176,
           27825, 28474, 29124, 29773, 30422, 31071, 31721, 32370, 33019, 33668, 34318, 34967, 35616, 36266, 36915, 37564,
           38213, 38863, 39512, 40161, 40810, 41460, 42109, 42758, 43407, 44057, 44706, 45355, 46004, 46654, 47303, 47952,
           48602, 49251, 49900, 50549, 51199]
    倍率2 = 1
    倍率 = 1.128  # 三觉
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.倍率1 + self.数据2[self.等级] * self.倍率2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率1 *= 1.1
            self.倍率2 *= 1.25
            self.CD *= 0.85
        elif x == 1:
            self.倍率1 *= 1.1
            self.倍率2 *= 1.37
            self.CD *= 0.85


class skill9(主动技能):
    名称 = '恶魔之握'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [0, 460, 507, 554, 601, 647, 694, 741, 788, 834, 881, 928, 975, 1022, 1068, 1115, 1162, 1209, 1255, 1302, 1349,
           1396, 1442, 1489, 1536, 1583, 1629, 1676, 1723, 1770, 1816, 1863, 1910, 1957, 2003, 2050, 2097, 2144, 2190, 2237,
           2284, 2331, 2378, 2424, 2471, 2518, 2565, 2611, 2658, 2705, 2752, 2798, 2845, 2892, 2939, 2985, 3032, 3079, 3126,
           3172, 3219, 3266, 3313, 3359, 3406, 3453, 3500, 3546, 3593, 3640, 3687]
    攻击次数1 = 2
    数据2 = [0, 9903, 10907, 11912, 12917, 13921, 14926, 15930, 16935, 17940, 18944, 19949, 20954, 21958, 22963, 23968, 24972,
           25977, 26982, 27986, 28991, 29996, 31000, 32005, 33010, 34014, 35019, 36024, 37028, 38033, 39038, 40042, 41047,
           42052, 43056, 44061, 45066, 46070, 47075, 48080, 49084, 50089, 51094, 52098, 53103, 54107, 55112, 56117, 57121,
           58126, 59131, 60135, 61140, 62145, 63149, 64154, 65159, 66163, 67168, 68173, 69177, 70182, 71187, 72191, 73196,
           74201, 75205, 76210, 77215, 78219, 79224]
    倍率 = 1.099  # 三觉
    CD = 30
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级]) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill10(主动技能):
    名称 = '黑暗权能'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 510, 562, 614, 665, 717, 769, 821, 872, 924, 976, 1028, 1080, 1131, 1183, 1235, 1287, 1339, 1390, 1442, 1494,
           1546, 1597, 1649, 1701, 1753, 1805, 1856, 1908, 1960, 2012, 2063, 2115, 2167, 2219, 2271, 2322, 2374, 2426, 2478,
           2530, 2581, 2633, 2685, 2737, 2788, 2840, 2892, 2944, 2996, 3047, 3099, 3151, 3203, 3255, 3306, 3358, 3410, 3462,
           3513, 3565, 3617, 3669, 3721, 3772, 3824, 3876, 3928, 3980, 4031, 4083]
    攻击次数1 = 1
    数据2 = [0, 303, 333, 364, 395, 426, 456, 487, 518, 549, 579, 610, 641, 672, 702, 733, 764, 795, 825, 856, 887, 918, 948,
           979, 1010, 1041, 1071, 1102, 1133, 1164, 1194, 1225, 1256, 1286, 1317, 1348, 1379, 1409, 1440, 1471, 1502, 1532,
           1563, 1594, 1625, 1655, 1686, 1717, 1748, 1778, 1809, 1840, 1871, 1901, 1932, 1963, 1994, 2024, 2055, 2086, 2117,
           2147, 2178, 2209, 2240, 2270, 2301, 2332, 2363, 2393, 2424]
    攻击次数2 = 32
    数据3 = [0, 4803, 5290, 5778, 6264, 6752, 7239, 7727, 8214, 8700, 9188, 9675, 10163, 10650, 11138, 11624, 12112, 12599,
           13086, 13574, 14060, 14548, 15035, 15523, 16010, 16498, 16984, 17471, 17959, 18446, 18934, 19420, 19908, 20395,
           20883, 21370, 21856, 22344, 22831, 23319, 23806, 24293, 24780, 25268, 25755, 26242, 26729, 27216, 27704, 28191,
           28679, 29165, 29653, 30140, 30627, 31115, 31601, 32089, 32576, 33064, 33551, 34039, 34525, 35013, 35500, 35987,
           36475, 36961, 37449, 37936, 38424]
    攻击次数3 = 1
    倍率 = 1.225  # 三觉
    CD = 40
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 42
            self.CD *= 0.9
        elif x == 1:
            self.攻击次数2 = 42 * 1.09
            self.CD *= 0.9


class skill11(主动技能):
    名称 = '魔化：末日审判者'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 783, 898, 1012, 1127, 1241, 1357, 1472, 1586, 1702, 1815, 1931, 2046, 2160, 2274, 2390, 2503, 2618, 2733, 2847,
           2961, 3076, 3191, 3305, 3420, 3533, 3649, 3763, 3878, 3992, 4107, 4221, 4336, 4450, 4565, 4680, 4794, 4908, 5023,
           5138, 5250]
    攻击次数1 = 2
    数据2 = [0, 936, 1090, 1245, 1399, 1552, 1707, 1861, 2014, 2171, 2324, 2478, 2633, 2787, 2941, 3094, 3248, 3402, 3557, 3711,
           3864, 4018, 4172, 4327, 4480, 4633, 4788, 4941, 5096, 5250, 5403, 5558, 5711, 5866, 6020, 6172, 6328, 6482, 6635,
           6790, 6944]
    攻击次数2 = 2
    数据3 = [0, 1431, 1714, 1997, 2279, 2560, 2844, 3125, 3407, 3691, 3974, 4255, 4538, 4820, 5102, 5385, 5667, 5948, 6231,
           6513, 6795, 7077, 7360, 7642, 7923, 8206, 8488, 8770, 9052, 9334, 9616, 9900, 10180, 10462, 10746, 11027, 11308,
           11591, 11873, 12157, 12437]
    攻击次数3 = 2
    数据4 = [0, 1527, 1834, 2142, 2449, 2753, 3062, 3368, 3675, 3984, 4291, 4596, 4905, 5212, 5519, 5826, 6132, 6438, 6746,
           7052, 7359, 7665, 7973, 8280, 8586, 8893, 9200, 9506, 9814, 10120, 10426, 10734, 11039, 11347, 11655, 11960, 12267,
           12574, 12880, 13188, 13494]
    攻击次数4 = 2
    倍率 = 1.05  # 三觉
    审判数据1 = [0, 8042, 9907, 11772, 13636, 15501, 17366, 19231, 21096, 22961, 24826, 26691, 28555, 30420, 32285, 34150, 36015,
             37880, 39745, 41610, 43474, 45339, 47204, 49069, 50934, 52799, 54664, 56529, 58393, 60258, 62123, 63988, 65853,
             67718, 69583, 71448, 73312, 75177, 77042, 78907, 80772]
    审判数据2 = [0, 22889, 28197, 33504, 38812, 44120, 49428, 54735, 60043, 65351, 70659, 75966, 81274, 86582, 91889, 97197, 102505,
             107813, 113120, 118428, 123736, 129043, 134351, 139659, 144967, 150274, 155582, 160890, 166198, 171505, 176813,
             182121, 187428, 192736, 198044, 203352, 208659, 213967, 219275, 224582, 229890]
    CD = 1
    关联技能 = ['所有']

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.15


class skill12(主动技能):
    名称 = '审判'
    所在等级 = 50
    等级上限 = 1
    基础等级 = 1
    数据1 = 0
    数据2 = 0
    倍率 = 1.1 * 1.095  # 魔化 三觉
    CD = 145

    def 等效百分比(self, 武器类型):
        return (self.数据1 + self.数据2) * self.倍率


class skill13(被动技能):
    名称 = '恶魔唤醒'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    关联技能 = ['不朽战吼', '地狱之门', '厄运之轮', '恶魔之拳', '恶魔之手', '恶魔之握', '复仇之刺', '黑暗权能', '回旋飞镰', '毁灭强击', '裂地锤', '末日浩劫', '死亡切割', '永堕：混沌弑神', '魔流光杀', '崩坏福音']
    关联技能2 = ['魔化：末日审判者']
    关联技能3 = ['审判']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.015 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.01 * self.等级, 5)

    def 加成倍率3(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00 + 0.02 * self.等级, 5)


class skill14(主动技能):
    名称 = '地狱之门'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [0, 1332, 1466, 1601, 1736, 1871, 2007, 2141, 2276, 2412, 2546, 2681, 2817, 2951, 3087, 3221, 3356, 3492, 3626,
           3762, 3897, 4031, 4167, 4302, 4436, 4572, 4707, 4842, 4977, 5113, 5247, 5382, 5518, 5652, 5788, 5923, 6057, 6191,
           6328, 6462, 6597, 6733, 6868, 7002, 7139, 7273, 7407, 7544, 7678, 7812, 7949, 8083, 8217, 8354, 8488, 8623, 8758,
           8894, 9028, 9162, 9299, 9433, 9567, 9704, 9838, 9972, 10109, 10243, 10377, 10514, 10648]
    攻击次数1 = 8
    倍率 = 1.5 * 1.101  # 魔化 三觉
    CD = 30
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 9
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.08
            self.攻击次数1 = 9
            self.CD *= 0.88


class skill15(主动技能):
    名称 = '末日浩劫'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 18725, 20625, 22525, 24424, 26324, 28224, 30123, 32023, 33923, 35822, 37722, 39622, 41522, 43421, 45321, 47221,
           49120, 51020, 52920, 54819, 56719, 58619, 60519, 62418, 64318, 66218, 68117, 70017, 71917, 73816, 75716, 77616,
           79515, 81415, 83315, 85215, 87114, 89014, 90914, 92813, 94713, 96613, 98512, 100412, 102312, 104212, 106111,
           108011, 109911, 111810, 113710, 115610, 117509, 119409, 121309, 123209, 125108, 127008, 128908, 130807, 132707,
           134607, 136506, 138406, 140306, 142206, 144105, 146005, 147905, 149804]
    倍率 = 1.35 * 1.101  # 魔化 三觉
    CD = 50
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.08 * 1.1
        elif x == 1:
            self.倍率 *= 1.08 * 1.18


class skill16(主动技能):
    名称 = '不朽战吼'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 6766, 7453, 8140, 8826, 9513, 10200, 10886, 11573, 12259, 12946, 13633, 14319, 15006, 15692, 16379, 17066,
           17751, 18438, 19124, 19811, 20498, 21184, 21871, 22557, 23244, 23931, 24617, 25304, 25990, 26677, 27363, 28049,
           28736, 29422, 30109, 30795, 31482, 32169, 32855, 33542, 34228, 34915, 35601, 36288, 36975, 37661, 38348, 39033,
           39720, 40407, 41093, 41780, 42466, 43153, 43840, 44526, 45213, 45900, 46586, 47273, 47959, 48646, 49332, 50018,
           50705, 51391, 52078, 52765, 53451, 54138]
    攻击次数1 = 5
    数据2 = [0, 2418, 2665, 2910, 3153, 3399, 3645, 3889, 4136, 4381, 4627, 4873, 5118, 5363, 5607, 5854, 6099, 6344, 6591,
           6835, 7080, 7327, 7571, 7816, 8063, 8307, 8552, 8798, 9043, 9289, 9534, 9780, 10025, 10270, 10516, 10760, 11005,
           11252, 11496, 11741, 11987, 12233, 12478, 12724, 12970, 13214, 13459, 13706, 13951, 14195, 14441, 14687, 14931,
           15178, 15423, 15667, 15914, 16158, 16403, 16649, 16895, 17141, 17385, 17631, 17876, 18120, 18367, 18612, 18857,
           19104, 19348]
    攻击次数2 = 2
    倍率 = 1.138  # 三觉
    CD = 40

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.29
        self.CD *= 0.86


class skill17(被动技能):
    名称 = '原罪之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.17 + 0.02 * self.等级, 5)


class skill18(主动技能):
    名称 = '毁灭强击'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据1 = [0, 4344, 4785, 5226, 5667, 6108, 6548, 6989, 7430, 7871, 8311, 8752, 9193, 9634, 10075, 10515, 10956, 11397, 11838,
           12278, 12719, 13160, 13601, 14042, 14482, 14923, 15364, 15805, 16246, 16686, 17127, 17568, 18009, 18449, 18890,
           19331, 19772, 20213, 20653, 21094, 21535, 21976, 22416, 22857, 23298, 23739, 24180, 24620, 25061, 25502, 25943,
           26384, 26824, 27265, 27706, 28147, 28587, 29028, 29469, 29910, 30351, 30791, 31232, 31673, 32114, 32555, 32995,
           33436, 33877, 34318, 34758]
    攻击次数1 = 1
    数据2 = [0, 20275, 22332, 24389, 26446, 28502, 30560, 32617, 34674, 36731, 38788, 40845, 42902, 44959, 47016, 49073, 51130,
           53187, 55244, 57300, 59358, 61415, 63471, 65529, 67586, 69643, 71700, 73757, 75814, 77871, 79927, 81985, 84042,
           86098, 88156, 90213, 92269, 94327, 96384, 98440, 100498, 102555, 104611, 106669, 108725, 110783, 112840, 114896,
           116954, 119011, 121067, 123125, 125182, 127238, 129296, 131352, 133409, 135467, 137523, 139580, 141638, 143694,
           145751, 147809, 149865, 151923, 153979, 156036, 158094, 160150, 162207]
    攻击次数2 = 1
    数据3 = [0, 868, 957, 1045, 1133, 1221, 1309, 1397, 1486, 1574, 1662, 1750, 1838, 1926, 2015, 2103, 2191, 2279, 2367, 2455,
           2543, 2632, 2720, 2808, 2896, 2984, 3072, 3161, 3249, 3337, 3425, 3513, 3601, 3689, 3778, 3866, 3954, 4042, 4130,
           4218, 4307, 4395, 4483, 4571, 4659, 4747, 4836, 4924, 5012, 5100, 5188, 5276, 5364, 5453, 5541, 5629, 5717, 5805,
           5893, 5982, 6070, 6158, 6246, 6334, 6422, 6511, 6599, 6687, 6775, 6863, 6951]
    攻击次数3 = 10  # 最低5
    倍率 = 1.35 * 1.166  # 魔化 三觉
    CD = 45.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.35


class skill19(主动技能):
    名称 = '永堕：混沌弑神'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [0, 3504, 4317, 5130, 5942, 6755, 7568, 8381, 9193, 10006, 10819, 11632, 12444, 13257, 14070, 14882, 15695, 16508,
           17321, 18133, 18946, 19759, 20571, 21384, 22197, 23010, 23822, 24635, 25448, 26260, 27073, 27886, 28699, 29511,
           30324, 31137, 31949, 32762, 33575, 34388, 35200]
    攻击次数1 = 0
    数据2 = [0, 2511, 3094, 3676, 4259, 4841, 5424, 6006, 6588, 7171, 7753, 8336, 8918, 9501, 10083, 10666, 11248, 11830, 12413,
           12995, 13578, 14160, 14743, 15325, 15908, 16490, 17072, 17655, 18237, 18820, 19402, 19985, 20567, 21150, 21732,
           22315, 22897, 23479, 24062, 24644, 25227]
    攻击次数2 = 12
    数据3 = [0, 6308, 7771, 9234, 10697, 12160, 13623, 15086, 16548, 18011, 19474, 20937, 22400, 23863, 25326, 26789, 28252,
           29714, 31177, 32640, 34103, 35566, 37029, 38492, 39955, 41418, 42880, 44343, 45806, 47269, 48732, 50195, 51658,
           53121, 54584, 56047, 57509, 58972, 60435, 61898, 63361]
    攻击次数3 = 1
    数据4 = [0, 15070, 18565, 22060, 25554, 29049, 32544, 36038, 39533, 43028, 46522, 50017, 53512, 57007, 60501, 63996, 67491,
           70985, 74480, 77975, 81469, 84964, 88459, 91953, 95448, 98943, 102437, 105932, 109427, 112921, 116416, 119911,
           123406, 126900, 130395, 133890, 137384, 140879, 144374, 147868, 151363]
    攻击次数4 = 2
    倍率4 = 1.35  # 按X或Z
    倍率 = 1.35 * 1.145  # 魔化 三觉
    CD = 180.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4 * self.倍率4) * self.倍率


class skill20(被动技能):
    名称 = '不死恶魔'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill21(主动技能):
    名称 = '魔流光杀'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 7562.4 * 1.2 * 1.3
    成长 = 853.6 * 1.2 * 1.3
    攻击次数 = 3
    基础2 = 34029 * 1.2 * 1.3
    成长2 = 3842 * 1.2 * 1.3
    攻击次数2 = 1
    CD = 60.0


class skill22(主动技能):
    名称 = '崩坏福音'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 189029 * 1.4
    成长 = 57067 * 1.4
    CD = 290.0

    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        return 0.0


skill_list = []
i = 0
while i >= 0:
    try:
        exec('skill_list.append(skill' + str(i) + '())')
        i += 1
    except:
        i = -1

skill_sn = dict()
for i in range(len(skill_list)):
    skill_sn[skill_list[i].名称] = i

skill_sn_awaking1 = 12
skill_sn_awaking2 = 19
skill_sn_awaking3 = 22

option_talismans = ['无']
for i in skill_list:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        option_talismans.append(i.名称)

option_rune = ['无']
for i in skill_list:
    if 20 <= i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        option_rune.append(i.名称)


class character(py.lite.CharBase):
    def 角色賦予(self):
        self.attr["实际名称"] = '神启_复仇者'
        self.attr["角色"] = '圣职者(男)'
        self.attr["职业"] = '复仇者'

        self.attr["武器选项"] = ['镰刀']

        self.attr["类型"] = '魔法百分比'
        self.attr["防具类型"] = '重甲'
        self.attr["防具精通属性"] = ['智力']

        self.attr["主BUFF"] = 1.9

        self.attr["技能栏"] = skill_list
        self.attr["技能序号"] = skill_sn
        self.attr["一觉序号"] = skill_sn_awaking1
        self.attr["二觉序号"] = skill_sn_awaking2
        self.attr["三觉序号"] = skill_sn_awaking3
        self.attr["护石选项"] = option_talismans
        self.attr["符文选项"] = option_rune

        self.attr["远古记忆"] = 10

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [1, 1, 10, 43, 10, 1, 1, 36, 33, 33, 31, 12, 1, 20, 23, 18, 16, 11, 13, 5, 4, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 5, 0, 0, 0, 5, 5, 5, 1, 0, 0, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['0', '0', '', '3', '', '0', '0', '2', '2', '1', '1', '7', '0', '', '2', '1', '1', '', '1', '1', '', '1', '1']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '泯灭之灵']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "镰刀"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 12]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "镰刀精通"
        self.attr["右槽白金技能"] = "镰刀精通"
        self.attr["时装上衣技能"] = "镰刀精通"

        self.attr["三觉技能选择"] = "一觉序号"

        self.attr["护石栏"] = ["厄运之轮", "地狱之门", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["恶魔之拳", "恶魔之拳", "恶魔之拳", "恶魔之拳", "恶魔之拳", "恶魔之拳", "无", "无", "无"]
        self.attr["符文效果"] = ["攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%"]
        self.attr["辟邪玉栏"] = [
            ["无", 0],
            ["无", 0],
            ["无", 0],
            ["无", 0]
        ]
        self.attr["希洛克装备栏"] = ["无", "无", "无"]
        self.attr["希洛克武器栏"] = [
            ["无", 6],
            ["无", 3]
        ]

    def 三觉技能选择(self):
        self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].被动倍率 = 0

    def 被动倍率计算(self):
        super().被动倍率计算()
        技能栏 = self.attr["技能栏"]

        一觉 = 技能栏[skill_sn['魔化：末日审判者']]
        技能栏[skill_sn['审判']].数据1 = 一觉.审判数据1[一觉.等级]
        技能栏[skill_sn['审判']].数据2 = 一觉.审判数据2[一觉.等级]