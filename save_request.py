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
