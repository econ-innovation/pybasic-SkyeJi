import json
import datetime
import sys

with open('google100.txt', "r") as f:  # 打开文件 "google100.txt" 用于读取
    for pt in f.readlines():  # 遍历该文件的每一行:
        patent = json.loads(pt)  # 将当前行解析为 JSON 格式，得到一个名为 "patent" 的字典
        filing_date = patent.get("filing_date", "")  # 获取 "filing_date" 的值，如果不存在则返回空字符串 ""
        publication_date = patent.get("publication_date","")
        grant_date = patent.get("grant_date","")
        priority_date = patent.get("priority_date","")
        with open('/Users/liji/PycharmProjects/pythonProject/google.txt', 'a') as fs:  # 打开文件 "assignment3.txt" 用于追加数据
            line = f"{patent['application_number']}|{filing_date}|{publication_date}|{grant_date}|{priority_date}\n"  # 使用 f-string 来格式化字符串
            fs.write(line)  # 将整个字符串写入文件
