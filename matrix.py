#!user/bin/env python3
# -*- coding: gbk -*-
import csv
import pandas as pd
import numpy as np
mat = np.zeros((55, 55),dtype=np.int)
df = pd.DataFrame(mat,columns=['东方明珠塔', '上海杜莎夫人蜡像馆', '上海环球金融中心观光厅', '上海科技馆', '上海朱家角古镇', '上海金茂大厦88层观光厅', '上海海洋水族馆', '上海南翔景区', '上海世纪公园', '上海影视乐园', '上海宋庆龄故居纪念馆', '上海欢乐谷', '辰山植物园', '上海古猗园', '上海植物园', '上海自然博物馆', '上海中心上海之巅观光厅', '上海宝山顾村公园', '上海野生动物园', '上海新场古镇', '上海电影博物馆', '上海金山嘴渔村', '东平国家森林公园', '上海动物园', '泰迪之家博物馆', '上海孙中山故居纪念馆', '上海鲁迅故居', '上海城市规划展示馆', '上海枫泾古镇', '上海汽车博物馆', '上海大观园', '上海月湖雕塑公园', '上海长风海洋世界', '上海锦江乐园', '上海鲜花港', '上海滨江森林公园', '上海碧海金沙景区', '上海海湾国家森林公园', '上海吴淞炮台湾湿地公园', '韩湘水博园', '上海共青森林公园', '周浦花海', '上海醉白池公园', '外滩', '南京路步行街', '上海迪士尼', '田子坊', '豫园', '1933老场坊', '新天地', '陆家嘴', '上海世博园', '思南公馆', '七宝老街', '中共一大会址纪念馆'],index=['东方明珠塔', '上海杜莎夫人蜡像馆', '上海环球金融中心观光厅', '上海科技馆', '上海朱家角古镇', '上海金茂大厦88层观光厅', '上海海洋水族馆', '上海南翔景区', '上海世纪公园', '上海影视乐园', '上海宋庆龄故居纪念馆', '上海欢乐谷', '辰山植物园', '上海古猗园', '上海植物园', '上海自然博物馆', '上海中心上海之巅观光厅', '上海宝山顾村公园', '上海野生动物园', '上海新场古镇', '上海电影博物馆', '上海金山嘴渔村', '东平国家森林公园', '上海动物园', '泰迪之家博物馆', '上海孙中山故居纪念馆', '上海鲁迅故居', '上海城市规划展示馆', '上海枫泾古镇', '上海汽车博物馆', '上海大观园', '上海月湖雕塑公园', '上海长风海洋世界', '上海锦江乐园', '上海鲜花港', '上海滨江森林公园', '上海碧海金沙景区', '上海海湾国家森林公园', '上海吴淞炮台湾湿地公园', '韩湘水博园', '上海共青森林公园', '周浦花海', '上海醉白池公园', '外滩', '南京路步行街', '上海迪士尼', '田子坊', '豫园', '1933老场坊', '新天地', '陆家嘴', '上海世博园', '思南公馆', '七宝老街', '中共一大会址纪念馆'])


with open("TF1.csv", "r", encoding = "utf-8") as f:
    reader = csv.reader(f)
    rows = [row for row in reader]

lists = ['东方明珠塔', '上海杜莎夫人蜡像馆', '上海环球金融中心观光厅', '上海科技馆', '上海朱家角古镇', '上海金茂大厦88层观光厅', '上海海洋水族馆', '上海南翔景区', '上海世纪公园', '上海影视乐园', '上海宋庆龄故居纪念馆', '上海欢乐谷', '辰山植物园', '上海古猗园', '上海植物园', '上海自然博物馆', '上海中心上海之巅观光厅', '上海宝山顾村公园', '上海野生动物园', '上海新场古镇', '上海电影博物馆', '上海金山嘴渔村', '东平国家森林公园', '上海动物园', '泰迪之家博物馆', '上海孙中山故居纪念馆', '上海鲁迅故居', '上海城市规划展示馆', '上海枫泾古镇', '上海汽车博物馆', '上海大观园', '上海月湖雕塑公园', '上海长风海洋世界', '上海锦江乐园', '上海鲜花港', '上海滨江森林公园', '上海碧海金沙景区', '上海海湾国家森林公园', '上海吴淞炮台湾湿地公园', '韩湘水博园', '上海共青森林公园', '周浦花海', '上海醉白池公园', '外滩', '南京路步行街', '上海迪士尼', '田子坊', '豫园', '1933老场坊', '新天地', '陆家嘴', '上海世博园', '思南公馆', '七宝老街', '中共一大会址纪念馆']


for i in rows:
    if reader.line_num == 1:  # 由于第一行为变量名称，故忽略掉
        continue
    for l,j in enumerate(i):
        if j in lists:
            k = 1
            if i[l+1] in lists:
                mat[lists.index(j)][lists.index(i[l+1])] = mat[lists.index(j)][lists.index(i[l+1])] + 1
            else:
                while(l+k+1<len(i)):
                   if i[l+k+1] in lists:
                       mat[lists.index(j)][lists.index(i[l + +k + 1])] = mat[lists.index(j)][lists.index(i[l + +k + 1])] + 1
                       break
                   else:
                       k=k+1
                       pass
        else:
            continue

print(df)

for a in mat:
    with open('TF_matrix.csv', 'a+', newline='', encoding='UTF-8') as csv_file:
        writer = csv.writer(csv_file, dialect='excel')
        writer.writerow(a)