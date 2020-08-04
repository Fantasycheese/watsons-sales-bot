import pandas
import json

df = pandas.read_csv('watsons.csv')
i = [{'index': {'_id': i}} for i in df.index]
j = [{
    'name': x['name'],
    'imageUrl': x['imgUrl'],
    'price': x['price'],
    'url': x['detailUrl'],
    'discount': x['discountText']
} for x in df.iloc]
ij = [json.dumps(i) + '\n' + json.dumps(j, ensure_ascii=False) for i, j in zip(i, j)]
with open('result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(ij))
