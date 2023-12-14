import json
import requests

def get_geo(University):
    key = 'a8e88ea836bb084ebc67f9758357eb6e'
    url = f"https://restapi.amap.com/v3/geocode/geo?address={University}&output=json&key={key}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['geocodes'][0]['location']

with open('985University.txt', 'r', encoding='utf-8') as file:
    for line in file:
        university = line.strip() # 去除可能的空格和换行符
        location = get_geo(university)
        with open('985location.txt', 'a') as fs:
            fs.write("{1}{0}{2}\n".format("|", university, location))