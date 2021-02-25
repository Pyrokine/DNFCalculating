from py.base_char import *
import py.lite


class skill0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    数据 = [0, 1000, 1058, 1115, 1173, 1230, 1288, 1345, 1403, 1461, 1518, 1576, 1633, 1691, 1748, 1806, 1895, 1984, 2073, 2162, 2251, 2339, 2428, 2517, 2606, 2695, 2784, 2873, 2962, 3051, 3140, 3228,
          3317, 3406, 3495, 3584, 3673, 3762, 3851, 3940, 4029, 4118, 4206, 4295, 4384, 4473, 4562, 4651, 4740, 4829, 4918, 5007, 5095, 5184, 5273, 5362, 5451, 5540, 5629, 5718, 5807, 5896, 5985,
          6073, 6162, 6251, 6340, 6429, 6518, 6607, 6696, 6785, 6874, 6963, 7051, 7140, 7229, 7318, 7407, 7496, 7585, 7674, 7763, 7852, 7940, 8029, 8118, 8207, 8296, 8385, 8474, 8563, 8652, 8741,
          8830, 8918, 9007, 9096, 9185, 9274, 9363, 9452, 9541, 9630, 9719, 9808, 9897, 9986, 10075, 10164, 10253, 10342, 10431, 10520, 10609, 10698, 10787, 10876, 10965, 11054, 11143, 11232, 11321,
          11410, 11499, 11588, 11677, 11766, 11855, 11944, 12033, 12122, 12211, 12300, 12389, 12478, 12567, 12656, 12745, 12834, 12923, 13012, 13101, 13190, 13279, 13368, 13457, 13546, 13635, 13724,
          13813, 13902, 13991, 14080, 14169, 14258, 14347, 14436, 14525, 14614, 14703, 14792, 14881, 14970, 15059, 15148, 15237, 15326, 15415, 15504, 15593, 15682, 15771, 15860, 15949, 16038, 16127,
          16216, 16305, 16394, 16483, 16572, 16661, 16750, 16839, 16928, 17017, 17106, 17195, 17284, 17373, 17462, 17551, 17640, 17729, 17818, 17907, 17996, 18085, 18174, 18263]
    关联技能 = ['神罚之锤', '空斩打']

    def 加成倍率(self, 武器类型):
        return self.数据[self.等级] / 1000


class skill1(主动技能):
    名称 = '空斩打'
    所在等级 = 1
    等级上限 = 20
    基础等级 = 10
    基础 = 84
    成长 = 10.5
    CD = 2.0
    TP成长 = 0.08
    TP上限 = 5


class skill2(主动技能):
    名称 = '落凤锤'
    所在等级 = 15
    等级上限 = 1
    基础等级 = 1
    数据1 = [0, 2533, 2790, 3046, 3304, 3560, 3817, 4075, 4331, 4588, 4845, 5102, 5359, 5616, 5873, 6130, 6386, 6644, 6901,
           7158, 7415, 7672, 7928, 8185, 8443, 8699, 8956, 9214, 9470, 9727, 9985, 10241, 10498, 10755, 11012, 11269, 11525,
           11783, 12040, 12296, 12554]
    攻击次数1 = 2
    倍率 = 1.05  # 三觉
    CD = 6.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * self.倍率


class skill3(被动技能):
    名称 = '勇气恩赐'
    所在等级 = 15
    等级上限 = 25
    基础等级 = 15

    def 加成倍率(self, 武器类型):
        return (1.15 + (self.等级 - 15) * 0.02) if self.等级 >= 15 else (1 + self.等级 * 0.01)


class skill4(主动技能):
    名称 = '光之复仇'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 182, 200, 218, 237, 255, 274, 293, 311, 329, 348, 366, 385, 404, 422, 440, 459, 477, 495, 515, 533, 551, 570,
           588, 606, 625, 644, 662, 681, 699, 717, 735, 755, 773, 791, 810, 828, 846, 865, 884, 902, 921, 939, 957, 976, 995,
           1013, 1032, 1050, 1068, 1087, 1105, 1124, 1143, 1161, 1179, 1198, 1216, 1235, 1253, 1272]
    攻击次数1 = 1
    倍率 = 1.05  # 三觉
    CD = 0.2
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill5(主动技能):
    名称 = '纯白之刃'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 46
    数据1 = [0, 914, 1006, 1099, 1192, 1285, 1377, 1470, 1563, 1655, 1748, 1841, 1934, 2026, 2119, 2213, 2305, 2398, 2491, 2584,
           2676, 2769, 2862, 2955, 3047, 3140, 3233, 3325, 3418, 3511, 3604, 3696, 3789, 3882, 3975, 4067, 4160, 4253, 4345,
           4438, 4531, 4624, 4716, 4809, 4902, 4995, 5087, 5180, 5273, 5365, 5458, 5551, 5644, 5736, 5829, 5922, 6015, 6108,
           6201, 6294, 6386, 6479, 6572, 6665, 6757, 6850, 6943, 7035, 7128, 7221, 7314]
    攻击次数1 = 1
    倍率 = 1.211  # 三觉
    CD = 2.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill6(被动技能):
    名称 = '坚定信念'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 >= 10:
            return (1.10 + (self.等级 - 10) * 0.015)
        else:
            return (1 + self.等级 * 0.01)


class skill7(主动技能):
    名称 = '胜利之矛'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 43
    数据1 = [0, 978, 1077, 1176, 1276, 1375, 1475, 1574, 1673, 1773, 1872, 1971, 2070, 2170, 2269, 2368, 2467, 2566, 2666, 2765,
           2865, 2964, 3063, 3163, 3262, 3361, 3460, 3560, 3659, 3758, 3857, 3956, 4056, 4155, 4255, 4354, 4453, 4553, 4652,
           4751, 4850, 4949, 5049, 5148, 5247, 5346, 5446, 5545, 5645, 5744, 5843, 5943, 6042, 6141, 6240, 6339, 6439, 6538,
           6637, 6736, 6835, 6935, 7035, 7134, 7233, 7333, 7432, 7531, 7630, 7729, 7829]
    攻击次数1 = 1
    数据2 = [0, 1525, 1681, 1835, 1990, 2145, 2300, 2455, 2610, 2765, 2919, 3075, 3229, 3384, 3539, 3694, 3848, 4004, 4158,
           4313, 4468, 4623, 4777, 4933, 5087, 5242, 5397, 5552, 5706, 5862, 6016, 6171, 6326, 6481, 6635, 6791, 6945, 7100,
           7255, 7410, 7565, 7720, 7875, 8029, 8185, 8339, 8494, 8649, 8804, 8958, 9114, 9268, 9423, 9578, 9733, 9887, 10043,
           10197, 10352, 10507, 10662, 10816, 10972, 11126, 11281, 11436, 11591, 11745, 11901, 12055, 12210]
    攻击次数2 = 1
    CD = 6.6
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill8(主动技能):
    名称 = '圣光十字'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [0, 1337, 1473, 1609, 1745, 1880, 2016, 2152, 2287, 2423, 2559, 2695, 2830, 2966, 3102, 3237, 3374, 3509, 3645,
           3780, 3916, 4052, 4187, 4324, 4459, 4595, 4730, 4866, 5002, 5137, 5274, 5409, 5545, 5681, 5816, 5952, 6087, 6224,
           6359, 6495, 6631, 6766, 6902, 7038, 7174, 7309, 7445, 7581, 7716, 7852, 7988, 8124, 8259, 8395, 8531, 8666, 8802,
           8938, 9074, 9209, 9345, 9481, 9616, 9752, 9888, 10024, 10159, 10295, 10431, 10566, 10702]
    攻击次数1 = 1
    倍率1 = 1.158  # 三觉
    数据2 = [0, 2041, 2247, 2455, 2662, 2869, 3076, 3283, 3490, 3697, 3905, 4111, 4318, 4525, 4733, 4940, 5146, 5354, 5561,
           5768, 5975, 6182, 6389, 6596, 6803, 7010, 7217, 7425, 7632, 7838, 8045, 8253, 8460, 8666, 8874, 9081, 9288, 9495,
           9702, 9909, 10116, 10324, 10530, 10737, 10945, 11152, 11359, 11565, 11773, 11980, 12187, 12394, 12601, 12808,
           13015, 13222, 13429, 13636, 13844, 14051, 14257, 14465, 14672, 14879, 15085, 15293, 15500, 15707, 15915, 16121,
           16328]
    攻击次数2 = 1
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5
    关联技能 = ['所有']

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.倍率1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.2


class skill9(主动技能):
    名称 = '圣光沁盾'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [0, 3561, 3923, 4284, 4645, 5006, 5368, 5729, 6090, 6452, 6813, 7175, 7535, 7897, 8258, 8620, 8981, 9342, 9704, 10065, 10426, 10787, 11149, 11510, 11872, 12233, 12595, 12955, 13316, 13678,
           14039, 14401, 14762, 15124, 15485, 15846, 16207, 16569, 16930, 17291, 17653, 18014, 18375, 18736, 19098, 19459, 19821, 20182, 20544, 20905, 21265, 21627, 21988, 22350, 22711, 23073, 23434,
           23795, 24156, 24517, 24879]
    攻击次数1 = 1
    倍率 = 1.09  # 三觉
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill10(主动技能):
    名称 = '圣光琉璃碎'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 789, 869, 949, 1029, 1109, 1189, 1269, 1350, 1430, 1510, 1590, 1670, 1750, 1830, 1910, 1990, 2070, 2150, 2231,
           2311, 2391, 2471, 2551, 2631, 2711, 2791, 2871, 2951, 3031, 3112, 3192, 3272, 3352, 3432, 3512, 3592, 3672, 3752,
           3832, 3912, 3993, 4073, 4153, 4233, 4313, 4393, 4473, 4553, 4633, 4713, 4794, 4874, 4954, 5034, 5114, 5194, 5274,
           5354, 5434, 5514, 5594, 5675, 5755, 5835, 5915, 5995, 6075, 6155, 6235, 6315]
    攻击次数1 = 1
    倍率1 = 0.1
    数据2 = [0, 1790, 1972, 2154, 2335, 2517, 2699, 2881, 3062, 3244, 3425, 3607, 3789, 3971, 4153, 4334, 4515, 4697, 4879,
           5061, 5243, 5425, 5605, 5787, 5969, 6151, 6333, 6515, 6696, 6877, 7059, 7241, 7423, 7605, 7786, 7968, 8149, 8331,
           8513, 8695, 8876, 9058, 9239, 9421, 9603, 9785, 9966, 10148, 10330, 10511, 10693, 10875, 11056, 11238, 11420,
           11602, 11783, 11965, 12146, 12328, 12510, 12692, 12874, 13055, 13236, 13418, 13600, 13782, 13964, 14145, 14326]
    攻击次数2 = 1
    倍率2 = 5.5
    倍率 = 1
    CD = 14.4
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.倍率1 + self.数据2[self.等级] * self.攻击次数2 * self.倍率2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25
        elif x == 1:
            self.倍率 *= 1.34


class skill11(主动技能):
    名称 = '圣光聚合'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [0, 378, 416, 455, 494, 532, 570, 609, 647, 685, 724, 763, 801, 839, 877, 916, 955, 993, 1031, 1070, 1108, 1146, 1185, 1224, 1262, 1300, 1339, 1377, 1415, 1454, 1493, 1531, 1569, 1607, 1646,
           1685, 1723, 1761, 1800, 1838, 1876, 1915, 1954, 1992, 2030, 2069, 2107, 2145, 2184, 2223, 2261, 2299, 2337, 2376, 2415, 2453, 2491, 2530, 2568, 2606, 2645]
    攻击次数1 = 1
    数据2 = [0, 757, 834, 911, 987, 1065, 1141, 1218, 1295, 1372, 1448, 1525, 1602, 1679, 1755, 1833, 1909, 1986, 2063, 2140, 2217, 2294, 2371, 2447, 2525, 2601, 2678, 2755, 2832, 2908, 2985, 3062,
           3139, 3215, 3293, 3369, 3446, 3523, 3600, 3676, 3754, 3830, 3907, 3985, 4061, 4138, 4215, 4292, 4368, 4445, 4522, 4599, 4675, 4753, 4829, 4906, 4983, 5060, 5136, 5214, 5290]
    攻击次数2 = 1
    数据3 = [0, 2978, 3281, 3583, 3885, 4187, 4489, 4792, 5094, 5396, 5698, 6000, 6303, 6605, 6907, 7209, 7511, 7814, 8115, 8418, 8720, 9023, 9325, 9626, 9929, 10231, 10534, 10835, 11138, 11440, 11742,
           12045, 12346, 12649, 12951, 13253, 13555, 13857, 14160, 14462, 14765, 15066, 15368, 15671, 15973, 16275, 16577, 16879, 17182, 17484, 17786, 18088, 18391, 18693, 18995, 19297, 19599, 19902,
           20204, 20506, 20808]
    攻击次数3 = 1
    倍率 = 1.09  # 三觉
    CD = 10.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill12(主动技能):
    名称 = '忏悔之锤'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [0, 4652, 5124, 5595, 6067, 6540, 7012, 7484, 7955, 8427, 8899, 9372, 9844, 10315, 10787, 11259, 11731, 12204, 12675, 13147, 13619, 14091, 14563, 15035, 15507, 15979, 16451, 16923, 17395,
           17867, 18339, 18811, 19283, 19755, 20226, 20699, 21171, 21643, 22115, 22586, 23058, 23530, 24003, 24475, 24946, 25418, 25890, 26362, 26835, 27306, 27778, 28250, 28722, 29194, 29666, 30138,
           30610, 31082, 31554, 32025, 32498, 32970, 33442, 33914, 34385, 34857, 35330, 35802, 36274, 36745, 37217]
    攻击次数1 = 1
    数据2 = [0, 1936, 2133, 2329, 2525, 2722, 2918, 3115, 3311, 3507, 3705, 3901, 4097, 4294, 4490, 4686, 4883, 5079, 5275, 5473, 5669, 5865, 6062, 6258, 6455, 6651, 6847, 7044, 7240, 7437, 7634, 7830,
           8026, 8223, 8419, 8615, 8812, 9008, 9205, 9402, 9598, 9795, 9991, 10187, 10384, 10580, 10776, 10973, 11170, 11366, 11563, 11759, 11955, 12152, 12348, 12545, 12741, 12937, 13135, 13331,
           13527, 13724, 13920, 14116, 14313, 14509, 14705, 14903, 15099, 15295, 15492]
    攻击次数2 = 1
    倍率 = 1.05  # 三觉
    CD = 14.4
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.34
            self.CD *= 0.9


class skill13(主动技能):
    名称 = '正义审判'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [0, 547, 603, 658, 714, 769, 825, 880, 936, 992, 1047, 1103, 1158, 1214, 1269, 1325, 1380, 1435, 1492, 1547, 1603, 1658, 1714, 1769, 1825, 1880, 1935, 1992, 2047, 2103, 2158, 2214, 2269,
           2325, 2380, 2435, 2491, 2547, 2603, 2658, 2714, 2769, 2825, 2880, 2935, 2991, 3046, 3103, 3158, 3214, 3269, 3325, 3380, 3435, 3491, 3546, 3603, 3658, 3714, 3769, 3825, 3880, 3935, 3991,
           4046, 4102, 4158, 4214, 4269, 4325, 4380]
    攻击次数1 = 16
    倍率1 = 1
    数据2 = [0, 8760, 9649, 10538, 11426, 12315, 13205, 14093, 14982, 15871, 16759, 17648, 18537, 19425, 20315, 21204, 22092, 22981, 23870, 24758, 25647, 26536, 27425, 28314, 29203, 30091, 30980, 31869,
           32757, 33646, 34535, 35424, 36313, 37201, 38090, 38979, 39867, 40756, 41645, 42534, 43423, 44312, 45200, 46089, 46978, 47866, 48755, 49645, 50533, 51422, 52311, 53199, 54088, 54977, 55865,
           56755, 57644, 58532, 59421, 60310, 61198, 62087, 62976, 63865, 64754, 65643, 66531, 67420, 68309, 69197, 70086]
    攻击次数2 = 1
    倍率2 = 1
    倍率 = 1.05  # 三觉
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.倍率1 + self.数据2[self.等级] * self.攻击次数2 * self.倍率2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 8
            self.倍率2 = 2
        elif x == 1:
            self.攻击次数1 = 8
            self.倍率2 = 2.16


class skill14(被动技能):
    名称 = '信念光环'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.015 + 0.02 * self.等级, 5)


class skill15(主动技能):
    名称 = '天启之珠'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 489, 603, 716, 830, 943, 1056, 1170, 1284, 1397, 1511, 1625, 1738, 1851, 1965, 2078, 2192, 2305, 2419, 2533, 2646, 2759, 2873, 2986, 3100, 3214, 3327, 3441, 3554, 3667, 3781, 3895, 4008,
           4122, 4235, 4349, 4462, 4575, 4689, 4803, 4916]
    攻击次数1 = 29
    数据2 = [0, 16889, 20805, 24722, 28638, 32554, 36470, 40386, 44303, 48219, 52135, 56052, 59968, 63885, 67801, 71717, 75634, 79550, 83466, 87383, 91299, 95215, 99132, 103048, 106965, 110881, 114797,
           118714, 122630, 126546, 130463, 134379, 138295, 142212, 146128, 150045, 153961, 157877, 161793, 165709, 169625]
    攻击次数2 = 1
    倍率 = 1.3 * 1.177  # 圣灵之槌 三觉
    CD = 145

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * self.倍率


class skill16(主动技能):
    名称 = '圣光突袭'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [0, 1386, 1527, 1668, 1809, 1950, 2090, 2231, 2372, 2513, 2654, 2794, 2935, 3075, 3216, 3357, 3497, 3638, 3779, 3920, 4061, 4201, 4342, 4483, 4624, 4765, 4905, 5045, 5186, 5327, 5468, 5608,
           5749, 5890, 6031, 6172, 6312, 6453, 6594, 6735, 6875, 7015, 7156, 7297, 7438, 7579, 7719, 7860, 8001, 8142, 8283, 8423, 8564, 8705, 8845, 8986, 9126, 9267, 9408, 9549, 9690, 9830, 9971,
           10112, 10253, 10394, 10534, 10675, 10815, 10956, 11097]
    攻击次数1 = 3
    倍率1 = 1
    数据2 = [0, 9234, 10171, 11107, 12045, 12981, 13918, 14855, 15792, 16729, 17665, 18603, 19539, 20476, 21413, 22350, 23286, 24224, 25160, 26097, 27034, 27971, 28907, 29845, 30781, 31718, 32655,
           33592, 34528, 35465, 36402, 37339, 38275, 39213, 40149, 41086, 42023, 42960, 43896, 44834, 45770, 46707, 47645, 48581, 49518, 50455, 51392, 52328, 53265, 54202, 55139, 56075, 57013, 57949,
           58886, 59823, 60760, 61696, 62634, 63570, 64507, 65444, 66381, 67317, 68255, 69191, 70128, 71065, 72002, 72938, 73875]
    攻击次数2 = 1
    倍率2 = 1
    倍率 = 1.19  # 三觉
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.倍率1 + self.数据2[self.等级] * self.攻击次数2 * self.倍率2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率2 *= 1.36
            self.CD *= 0.9
        elif x == 1:
            self.倍率2 *= 1.49
            self.CD *= 0.9


class skill17(主动技能):
    名称 = '神圣之矛'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [0, 340, 373, 408, 444, 479, 512, 550, 583, 620, 654, 689, 724, 760, 793, 830, 864, 900, 934, 970, 1004, 1040, 1074, 1110, 1144, 1181, 1214, 1250, 1285, 1320, 1354, 1390, 1424, 1458, 1495,
           1529, 1566, 1600, 1634, 1670, 1705, 1739, 1776, 1810, 1847, 1880, 1915]
    攻击次数1 = 1
    数据2 = [0, 1547, 1705, 1862, 2018, 2175, 2333, 2490, 2646, 2804, 2961, 3118, 3275, 3432, 3589, 3746, 3903, 4060, 4217, 4375, 4531, 4688, 4845, 5002, 5159, 5316, 5474, 5630, 5787, 5945, 6102, 6258,
           6415, 6573, 6730, 6886, 7044, 7201, 7358, 7515, 7672, 7829, 7986, 8143, 8300, 8457, 8614]
    攻击次数2 = 1
    数据3 = [0, 4644, 5115, 5585, 6056, 6528, 6999, 7470, 7941, 8412, 8884, 9355, 9825, 10296, 10767, 11239, 11710, 12181, 12652, 13124, 13595, 14065, 14536, 15007, 15479, 15950, 16421, 16892, 17363,
           17835, 18305, 18776, 19247, 19719, 20190, 20661, 21132, 21603, 22075, 22545, 23016, 23487, 23959, 24430, 24901, 25372, 25843]
    攻击次数3 = 3
    倍率 = 1.206
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31


class skill18(主动技能):
    名称 = '神圣之光'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 21714, 23916, 26119, 28322, 30525, 32727, 34930, 37134, 39336, 41539, 43742, 45945, 48147, 50350, 52554, 54756, 56959, 59162, 61365, 63567, 65770, 67973, 70176, 72379, 74582, 76785,
           78987, 81190, 83393, 85596, 87799, 90002, 92205, 94407, 96610, 98813, 101016, 103219, 105422, 107625]
    倍率 = 1.185  # 三觉
    CD = 20.0

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.35


class skill19(主动技能):
    名称 = '圣佑结界'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [0, 3993, 4398, 4804, 5208, 5614, 6019, 6424, 6829, 7234, 7639, 8045, 8449, 8855, 9260, 9665, 10070, 10475, 10880, 11285, 11691, 12095, 12501, 12906, 13311, 13716, 14122, 14526, 14932,
           15336, 15742, 16147, 16552, 16957, 17363, 17767, 18173, 18578, 18983, 19388, 19794]
    攻击次数1 = 2
    数据2 = [0, 19967, 21993, 24018, 26044, 28070, 30095, 32121, 34146, 36172, 38198, 40224, 42249, 44275, 46301, 48326, 50352, 52377, 54404, 56429, 58455, 60480, 62506, 64532, 66557, 68583, 70609,
           72635, 74660, 76685, 78712, 80737, 82763, 84788, 86814, 88840, 90865, 92891, 94916, 96943, 98968]
    攻击次数2 = 1
    倍率 = 1.43 * 1.083  # 圣灵之槌 三觉
    CD = 40.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.攻击次数1 = 0
        self.倍率 *= 1.78


class skill20(主动技能):
    名称 = '神罚之锤'
    备注 = '(一轮普通攻击，TP为基础精通)'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 977.0 * 1.05
    成长 = 0.0
    CD = 2.0
    TP成长 = 0.10
    TP上限 = 3
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.24 + 0.02 * self.等级, 5)


class skill21(主动技能):
    名称 = '神圣洗礼：信仰之翼'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    CD = 180.0
    数据1 = [0, 1765, 2175, 2585, 2995, 3404, 3814, 4223, 4633, 5042, 5452, 5862, 6271, 6681, 7090, 7500, 7909, 8319, 8728, 9138, 9547, 9957, 10366, 10776, 11185, 11595, 12005, 12415, 12824, 13234,
           13643, 14053, 14462, 14872, 15281, 15691, 16100, 16510, 16919, 17329, 17738]
    攻击次数1 = 15
    数据2 = [0, 79480, 97910, 116340, 134770, 153201, 171631, 190061, 208491, 226922, 245352, 263782, 282212, 300642, 319073, 337503, 355933, 374363, 392794, 411224, 429654, 448084, 466515, 484945,
           503375, 521805, 540235, 558665, 577095, 595525, 613955, 632386, 650816, 669246, 687676, 706106, 724537, 742967, 761397, 779827, 798258]
    攻击次数2 = 1
    倍率 = 1.17  # 三觉
    CD = 180

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class skill22(被动技能):
    名称 = '神之代行者'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class skill23(主动技能):
    名称 = '神圣愤怒：阿斯忒洛珀'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 91395.8
    成长 = 10319.2
    CD = 60.0


class skill24(主动技能):
    名称 = '最后的审判'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 254312
    成长 = 76775
    CD = 290
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

skill_sn_awaking1 = 0
skill_sn_awaking2 = 0
skill_sn_awaking3 = 0
for i in skill_list:
    if i.所在等级 == 50:
        skill_sn_awaking1 = skill_sn[i.名称]
    if i.所在等级 == 85:
        skill_sn_awaking2 = skill_sn[i.名称]
    if i.所在等级 == 100:
        skill_sn_awaking3 = skill_sn[i.名称]

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
        self.attr["实际名称"] = '神启_圣骑士_男_战斗'
        self.attr["角色"] = '圣职者(男)'
        self.attr["职业"] = '圣骑士'

        self.attr["武器选项"] = ['镰刀', '念珠', '战斧', '十字架']

        self.attr["类型"] = '魔法固伤'
        self.attr["防具类型"] = '板甲'
        self.attr["防具精通属性"] = ['智力']

        self.attr["主BUFF"] = 1.97

        self.attr["远古记忆"] = 10
        self.attr["反身空斩打"] = 0

    def 角色数据输入(self):
        self.attr["技能SP等级"] = [100, 10, 1, 15, 43, 0, 10, 0, 41, 0, 36, 36, 33, 31, 20, 12, 0, 18, 16, 16, 13, 5, 4, 6, 2]
        self.attr["技能TP等级"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 0, 0, 0, 5, 0, 0, 3, 0, 0, 0, 0]
        self.attr["技能释放次数"] = ['', '1', '0', '', '50', '/CD', '', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '/CD', '', '/CD', '/CD', '/CD', '/CD', '/CD', '1', '/CD', '', '/CD', '/CD']
        self.attr["技能宠物次数"] = [0, 0, 0, 0, 20, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1]

        self.attr["装备栏"] = ['撒旦：沸腾之怒', '贝利亚尔：毁灭之种', '亚蒙：谎言之力', '亚巴顿：绝望地狱', '巴尔：堕落之魂', '白象之庇护', '四叶草之初心', '红兔之祝福', '军神的古怪耳环', '军神的遗书', '军神的庇护宝石', '泯灭之灵']
        self.attr["套装栏"] = ['噩梦：地狱之路[2]', '噩梦：地狱之路[3]', '噩梦：地狱之路[5]', '幸运三角[2]', '幸运三角[3]', '军神的隐秘遗产[2]', '军神的隐秘遗产[3]']
        self.attr["武器类型"] = "镰刀"

        self.attr["强化等级"] = [10, 10, 10, 10, 10, 10, 10, 10, 12, 10, 10, 10]
        self.attr["是否增幅"] = [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]
        self.attr["武器锻造等级"] = 8

        self.attr["左槽白金技能"] = "勇气恩赐"
        self.attr["右槽白金技能"] = "勇气恩赐"
        self.attr["时装上衣技能"] = "勇气恩赐"

        self.attr["三觉技能选择"] = "二觉序号"

        self.attr["护石栏"] = ["圣光琉璃碎", "正义审判", "无"]
        self.attr["护石类型"] = ["魔界", "魔界", "魔界"]
        self.attr["符文栏"] = ["圣光琉璃碎", "圣光琉璃碎", "圣光琉璃碎", "圣光琉璃碎", "圣光琉璃碎", "圣光琉璃碎", "无", "无", "无"]
        self.attr["符文效果"] = ["攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%", "攻击+3%", "CD-4%", "攻击+5%,CD+3%"]

    def 三觉技能选择(self):
        self.attr["技能栏"][self.attr[self.attr["三觉技能选择"]]].被动倍率 = 0

    def 被动倍率计算(self):
        super().被动倍率计算()
        技能栏 = self.attr["技能栏"]
        武器类型 = self.attr["武器类型"]

        技能栏[skill_sn['落凤锤']].等级 = 技能栏[skill_sn['神罚之锤']].等级
        技能栏[skill_sn['空斩打']].倍率 *= (1 + 0.1 * 技能栏[skill_sn['神罚之锤']].TP等级) / 技能栏[skill_sn['神之代行者']].加成倍率(武器类型)
        if self.attr["反身空斩打"] == 0:
            技能栏[skill_sn['空斩打']].基础 += 1.05 * 267 * 技能栏[skill_sn['神之代行者']].加成倍率(武器类型) / (1 + 0.08 * 技能栏[skill_sn['空斩打']].TP等级)
        else:
            技能栏[skill_sn['空斩打']].基础 += 1.05 * (267 + 187) * 技能栏[skill_sn['神之代行者']].加成倍率(武器类型) / (1 + 0.08 * 技能栏[skill_sn['空斩打']].TP等级)
