import requests
import json

#题库，不同专业可能不同，在【题库学习】-【按题库学习】打开后抓个包找到pool即可绝对正确
pools = (99,96,80,79,78,77,76,75,74,73)
#进考试之后抓包得，形如http://sjgl.swu.edu.cn/exam/my-exam/xxx/paper/xxx/score/xxx
selfurl = "xxx"
#登陆后抓包得到自己的cookie
selfcookie = "xxx"

#抓包？
#按F12点网络，刷新页面，你将得到一个新世界ヾ(≧▽≦*)o

def get(url):
    header = {
        'Cookie': selfcookie
    }
    res = requests.get(url,headers=header)
    return json.loads(res.text)

ab = get(selfurl)

number = 0

for x in ab["content"]["content"]:
    number +=1
    getFromPoolIndex = 0
    
    for i in range(10000):
        url = "http://sjgl.swu.edu.cn/exam/pool/"+ str(pools[getFromPoolIndex]) +"/item/"+ str(x["4"])
        acc = get(url)
        res = ""
        try:
            accca = acc["content"]["answers"]
            for xx in accca:
                res = res + xx
            print(str(number)+"." + res)
            break
        except:
            getFromPoolIndex+=1
            continue
            
