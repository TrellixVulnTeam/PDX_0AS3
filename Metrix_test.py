#!user/bin/env python3
# -*- coding: gbk -*-
import csv
import pandas as pd
import numpy as np
mat = np.zeros((64, 64),dtype=np.int)
df = pd.DataFrame(mat,columns=["东方明珠塔","上海野生动物园","上海科技馆","上海自然博物馆","上海金茂大厦88层观光厅","上海环球金融中心观光厅","上海城市规划展示馆","上海锦江乐园","上海海洋水族馆","东平国家森林公园","上海枫泾古镇","辰山植物园","上海世纪公园","东方绿舟","上海朱家角古镇","上海欢乐谷","海海湾国家森林公园","上海动物园","上海长风海洋世界","杜莎夫人蜡像馆","上海共青森林公园","上海影视乐园","上海鲜花港","上海方塔园","中国航海博物馆","上海月湖雕塑公园","上海宋庆龄故居纪念馆","上海植物园","上海中心上海之巅观光厅","上海古猗园","孙桥现代农业开发区","上海大观园","上海鲁迅故居","崇明前卫生态村","上海滨江森林公园","上海孙中山故居纪念馆","上海大自然野生昆虫馆","上海马陆葡萄公园","上海东方地质科普馆","华亭人家","上海东方假日田园","江南三民文化村","上海都市菜园","上海高家庄园","上海南翔景区","上海电影博物馆","上海吴淞炮台湾湿地公园","上海碧海金沙景区","上海宝山顾村公园","周浦花海","上海游龙石文化科普馆","上海醉白池公园","宝山国际民间艺术博览馆","上海崇明岛荷花博览园","探险者世界","世嘉都市乐园","家家乐梦幻乐园","泰迪之家博物馆","上海新场古镇","韩湘水博园","上海金山嘴渔村","廊下生态园","上海汽车博物馆","震旦博物馆"],index=["东方明珠塔","上海野生动物园","上海科技馆","上海自然博物馆","上海金茂大厦88层观光厅","上海环球金融中心观光厅","上海城市规划展示馆","上海锦江乐园","上海海洋水族馆","东平国家森林公园","上海枫泾古镇","辰山植物园","上海世纪公园","东方绿舟","上海朱家角古镇","上海欢乐谷","海海湾国家森林公园","上海动物园","上海长风海洋世界","杜莎夫人蜡像馆","上海共青森林公园","上海影视乐园","上海鲜花港","上海方塔园","中国航海博物馆","上海月湖雕塑公园","上海宋庆龄故居纪念馆","上海植物园","上海中心上海之巅观光厅","上海古猗园","孙桥现代农业开发区","上海大观园","上海鲁迅故居","崇明前卫生态村","上海滨江森林公园","上海孙中山故居纪念馆","上海大自然野生昆虫馆","上海马陆葡萄公园","上海东方地质科普馆","华亭人家","上海东方假日田园","江南三民文化村","上海都市菜园","上海高家庄园","上海南翔景区","上海电影博物馆","上海吴淞炮台湾湿地公园","上海碧海金沙景区","上海宝山顾村公园","周浦花海","上海游龙石文化科普馆","上海醉白池公园","宝山国际民间艺术博览馆","上海崇明岛荷花博览园","探险者世界","世嘉都市乐园","家家乐梦幻乐园","泰迪之家博物馆","上海新场古镇","韩湘水博园","上海金山嘴渔村","廊下生态园","上海汽车博物馆","震旦博物馆"])


with open("data_total2.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

lists = ["东方明珠塔","上海野生动物园","上海科技馆","上海自然博物馆","上海金茂大厦88层观光厅","上海环球金融中心观光厅","上海城市规划展示馆","上海锦江乐园","上海海洋水族馆","东平国家森林公园","上海枫泾古镇","辰山植物园","上海世纪公园","东方绿舟","上海朱家角古镇","上海欢乐谷","海海湾国家森林公园","上海动物园","上海长风海洋世界","杜莎夫人蜡像馆","上海共青森林公园","上海影视乐园","上海鲜花港","上海方塔园","中国航海博物馆","上海月湖雕塑公园","上海宋庆龄故居纪念馆","上海植物园","上海中心上海之巅观光厅","上海古猗园","孙桥现代农业开发区","上海大观园","上海鲁迅故居","崇明前卫生态村","上海滨江森林公园","上海孙中山故居纪念馆","上海大自然野生昆虫馆","上海马陆葡萄公园","上海东方地质科普馆","华亭人家","上海东方假日田园","江南三民文化村","上海都市菜园","上海高家庄园","上海南翔景区","上海电影博物馆","上海吴淞炮台湾湿地公园","上海碧海金沙景区","上海宝山顾村公园","周浦花海","上海游龙石文化科普馆","上海醉白池公园","宝山国际民间艺术博览馆","上海崇明岛荷花博览园","探险者世界","世嘉都市乐园","家家乐梦幻乐园","泰迪之家博物馆","上海新场古镇","韩湘水博园","上海金山嘴渔村","廊下生态园","上海汽车博物馆","震旦博物馆"]


for i in rows:
    if reader.line_num == 1:  # 由于第一行为变量名称，故忽略掉
        continue
    for l,j in enumerate(i[4:]):
        if j in lists:
            if i[l+5 ] in lists:
                mat[lists.index(j)][lists.index(i[l+5])] = mat[lists.index(j)][lists.index(i[l+5])] + 1
            elif l+1 < len(i):
                l=l+1
        else:
            break

print(df)