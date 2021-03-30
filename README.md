# DNFCalculating 

本计算器为使用python3.8(anaconda3)编写的轻量版计算核心（无GUI）</br>
主框架由纸飞机实现，西瓜提供数据公式并协助修改，SCUDRT对算法进行优化修改，风之凌殇添加多进程优化</br>
本程序由Pyrokine根据原项目基于GPL协议修改并开源，相关教程和说明请参阅原项目<br></br>

## 程序目录结构说明
|--　DNFCalculating</br>
　　　　|--　CHANGELOG.md：程序更新记录</br>
　　　　|--　LICENSE：开源许可</br>
　　　　|--　README.md：程序说明</br>
　　　　|--　py：计算核心模块，可以调用函数来计算伤害</br>
　　　　　　　　|--  Equip：职业实现目录</br>
　　　　　　　　|　　　|--  equ_list.py：用来生成全身装备和套装的列表已经映射</br>
　　　　　　　　|　　　|--  equip_accessory.py：首饰</br>
　　　　　　　　|　　　|--  equip_armour.py：防具</br>
　　　　　　　　|　　　|--  equip_set.py：套装</br>
　　　　　　　　|　　　|--  equip_special.py：特殊装备</br>
　　　　　　　　|　　　|--  equip_weapon.py：武器</br>
　　　　　　　　|--  Part：每个角色的实现，中英文名字对应可以在glossary.py中查看</br>
　　　　　　　　|--  Test：单元测试</br>
　　　　　　　　|　　　|--  extract.py：抽取数据生成默认配置用的程序</br>
　　　　　　　　|　　　|--  json_formatter.py：简单的json格式化函数</br>
　　　　　　　　|　　　|--  test.py：测试主函数，主要测试默认配置下伤害是否和原计算器相等以及是否出现计算出错和伤害异常的现象</br>
　　　　　　　　|--  user_data_default：每个角色的默认配置，即网页版新建存档时得到的文件</br>
　　　　　　　　|--  base_char.py：和角色相关的基础数据</br>
　　　　　　　　|--  base_equip.py：和装备相关的基础数据</br>
　　　　　　　　|--  glossary.py：中英文字典</br>
　　　　　　　　|--  lite.py：轻量版计算器主程序</br>
