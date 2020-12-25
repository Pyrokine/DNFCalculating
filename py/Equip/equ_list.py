from py.Equip.equip_set import *
from py.Equip.equip_weapon import *
from py.Equip.equip_special import *
from py.Equip.equip_armour import *
from py.Equip.equip_accessory import *

装备列表 = []
套装列表 = []


def add_equips(start_num, end_num):
    for i in range(start_num, end_num + 1):
        exec('装备列表.append(装备' + str(i) + '())')


def add_sets(start_num, end_num):
    for i in range(start_num, end_num + 1):
        exec('套装列表.append(套装效果' + str(i) + '())')


add_equips(0, 73)  # 100级ss武器
add_equips(74, 179)  # 100级ss防具
add_equips(180, 211)  # 100级ss首饰
add_equips(212, 243)  # 100级ss特殊
add_sets(0, 84)  # 100级ss套装

# print([x.名称 for x in 装备列表])
# print([x.名称 for x in 套装列表])

装备序号 = {}
套装序号 = {}
套装映射 = {}
for i in range(len(装备列表)):
    装备序号[装备列表[i].名称] = i
    套装映射[装备列表[i].所属套装 + '-' + 装备列表[i].品质 + '-' + 装备列表[i].部位] = i


for i in range(len(套装列表)):
    套装序号[套装列表[i].名称 + '[' + str(套装列表[i].件数) + ']'] = i
