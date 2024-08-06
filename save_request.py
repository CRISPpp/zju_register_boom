import requests
import time
from time import sleep
import json
import os
import sys
import sys
import time
#看自己浏览器里面的cookies，如果有没有的字段，需要手动加上,每个字段都要写，某些某些视频无法刷
cookies = {
    "JSESSIONID": "",
    "_csrf": "",
    "_pv0": "",
    "_pf0": "",
    "_pc0": "",
    "_pm0":"",
    "iPlanetDirectoryPro": "",
    "stu-token": "",
}
cookies = {
    "JSESSIONID": "CFF4A67BA67FF90664E358CA0510EEF7",
    "_csrf": "S8mwplVi9KWoF2WQ0TlCeNKhcpPcCrki%2F2cCMHtF%2B7c%3D",
    "_pv0": "635kHYG9rOi%2BBHMDMh5a3ge0wLF7O1ynje4tWtPxln9061MQ4XWy9WqY47oLL%2FLoGkyt%2F4mpqlZNZdFc4a60QsHAmpJRogA%2By1CQc22GucyebomEkxfp2klEEdYjQ1%2BFZnJFiicV%2F3rbz09w%2FKBZ3krzUo2G4XCXWBRWXGQaznmhQbwHGBDlVFK8wzteCXMkhyFlJN201HGHVcBf3bPuExNZoewcLqZDZUmkA0%2FQak18TDU6cjAk%2BDTvUn%2BHfXIuV91yGmJ%2BUXNT4lWxNxB60DwmpQWo7ko1g8t4rO0AX4PAejS63LbtqdRTv0NV9U074lgEqx6TtHSD0rvUK9gVhcGWlFaEYKgFktl8kUWsZT%2BFsEsyBGC3C6YX2zm1SgBkWGJbPOGUCMcbPsF7Ro%2BMPPvLdTWtbfjqorf8a6K%2FQEM%3D",
    "_pf0": "KKL%2BQ7DiP3SCcpQrwmFzEgXLgaPaBx4zJDL0WMTo4rY%3D",
    "_pc0": "ZF1AKfG8yOMoTRJS6fMbxorNsAaiDlQpwiWPi6bR30w%3D",
    "_pm0":"5TfJ%2BQU%2FgbLUVgsjZmtXW2TnY6FG1Do7oz04YKnXkd4%3D",
    "iPlanetDirectoryPro": "Z0aunJC8FRTz08zLcU3z9X4MZW%2Bgftdhhplq%2Bx5m3nY%2BbJrt9wlb2X%2FRWZO4T92rbPb1KSvVz7Jy%2BiwC32VEhRuRg1evNpK%2BSPYfMnmYeOz0x2pOmJyQxDBYf4x8Av8g1%2BmL5mkLsznOQ8tbHLhziG7rc23fPUEslhd%2BMd27hMPTEmaytMMQ9U5Orq0gPi5MJPRyCiTqmjPJ%2FsK2BXpVZh6ASpaZh6Bx4m7zD3SJlcSDMK%2FGM3jN5yPioDwU1TiJvdvoOgnLOP51DREAUf4o9TOnLDAWfAQRaOf9j9lQ5M%2FAzhA5UXaF71dle6T5hzZfdGF81IBEOl4%2FmvfVU4iu5J7dsxmPwqBK%2BPjGws3BDmk%3D",
    "stu-token": '81d68095d86f92bd1cb7df5aaf015cd8'
}
for key,val in cookies.items():
    if val=="":
        raise Exception("请先将Cookie信息替换为你自己的Cookie信息")
token=cookies['stu-token']
option=input("秒刷输入1，慢刷(安全些)输入2\n")

def progress_bar(duration, length=50):
    """显示一个在指定时间内完成的进度条。

    Args:
    duration (int): 进度条完成所需的总时间（秒）。
    length (int): 进度条的长度（单位：字符）。
    """
    for i in range(duration + 1):
        percent = (i / duration) * 100  # 计算百分比
        bar_length = int((i / duration) * length)  # 计算当前应有的进度条长度
        bar = '█' * bar_length + '-' * (length - bar_length)  # 创建进度条图形
        sys.stdout.write(f'\rProgress: |{bar}| {i}s/{duration}s Complete')
        sys.stdout.flush()
        time.sleep(1)  # 等待一秒

    print('\nProgress complete!')

def get_current_timestamp():
    # 获取当前时间的时间戳，单位为毫秒
    return int(time.time() * 1000)

def getStuDetail(token):
    timestamp = get_current_timestamp()
    payload = f"t={timestamp}&token={token}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Origin": "http://regi.zju.edu.cn",
        "token": token
    }

    # 发送POST请求
    response = requests.get('http://regi.zju.edu.cn/grs-pro/stu/vstudydetail/getStuDetail', data=payload, headers=headers,cookies=cookies)
    # print(f" Status Code: {response.status_code}, Response: {response.text}")

    stuDetail = json.loads(response.text)

    return stuDetail
def get_courses(base_url):
    # 生成时间戳
    timestamp = get_current_timestamp()
    url = f"{base_url}?t={timestamp}&title=&isRequired="
    # 发送GET请求获取课程信息
    response = requests.get(url)
    return response.json()
    course_data = response.json()
    course_ids = [course['id'] for course in course_data['list']]
    timeLimits= [course['timeLimit'] for course in course_data['list']]

    return course_ids,timeLimits


def post_study_log(base_url, token, course_ids,timeLimits):
    cnt=0
    for course_id,timeLimit in zip(course_ids,timeLimits):
        # 生成时间戳
        timestamp = get_current_timestamp()
        # 设置参数和payload
        params = {
            "t": timestamp,
            "studyTime": timeLimit,
            "classId": course_id,
            "token": token
        }
        payload = f"t={timestamp}&studyTime=500&classId={course_id}&token={token}"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive",
            "Content-Length": "0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
            "Origin": "http://regi.zju.edu.cn",
            "token": token
        }

        # 发送POST请求
        response = requests.post(base_url, params=params, data=payload, headers=headers,cookies=cookies)
        print(f"Course ID: {course_id}, Status Code: {response.status_code}, Response: {response.text}")
        cnt+=1
        # if cnt==5:
        #     break
        # sleep(int(timeLimit))

flag=1
while flag==1:
    flag=0
    # 获取课程ID
    courses=get_courses("http://regi.zju.edu.cn/grs-pro/config/vclassesdetail/queryList")
    print(courses['list'])
    StuDetails=getStuDetail(token)
    print(StuDetails['list'])

    course_ids = [course['classId'] for course in StuDetails['list']]
    StuDetails['list']+=[course for course in courses['list'] if course['id'] not in course_ids]
    print(StuDetails['list'])
    print(len(StuDetails['list']))
    # exit()
    os.system('cls' if os.name == 'nt' else 'clear')
    print("----------------------------------------------------------")
    tot=1
    for course in StuDetails['list']:

        if 'studyTime' not in course:
            course['studyTime']=0
        if 'classId' not in course:
            course['classId']=course['id']
        course['studyTime']=int(course['studyTime'])
        course['timeLimit']=int(course['timeLimit'])

        if course['studyTime']>=course['timeLimit']:
            print(""+f"{course['title']}({course['studyTime']}/{course['timeLimit']})"+"\033[32m已完成\033[0m")
            tot+=1
        else:
            print(f"已完成课程数量\033[32m{tot}/{len(StuDetails['list'])}\033[0m")
            flag=1
            print(""+f"{course['title']}({course['studyTime']}/{course['timeLimit']})"+"\033[31m未完成\033[0m")
            need=course['timeLimit']-course['studyTime']
            print(f"需要{need}s")

            post_study_log("http://regi.zju.edu.cn/grs-pro/stu/classinfo/addStudyLog",token, [course['classId']],[need])
            if option=="2":
                progress_bar(need)
            progress_bar(3)
            break


print("----------------------------------------------------------")

# 对每个ID发送POST请求记录学习日志
# post_study_log("http://regi.zju.edu.cn/grs-pro/stu/classinfo/addStudyLog",token, course_ids,timeLimits)
