import requests
import execjs
import json

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}
url = 'https://www.endata.com.cn/API/GetData.ashx'
data = {
    'year': '2020',
    'MethodName': 'BoxOffice_GetYearInfoData'
}
response = requests.post(url=url, data=data, headers=headers).text
# print(response)

# 解密
cxt = execjs.compile(open('jiemi.js', 'r', encoding='utf-8').read())
res = cxt.call('webInstace.shell', response)
res = json.loads(res)
with open('yien.json', 'w', encoding='utf-8') as fp:
    json.dump(res, fp=fp, ensure_ascii=False)
