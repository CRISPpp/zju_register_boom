import requests

# 请求的URL
url = "http://regi.zju.edu.cn/grs-pro/stu/classinfo/addStudyLog"

# URL参数
params = {
    "t": 1722586488197,
    "studyTime": 500,
    "classId": "xxx",
    "token": "xxx"
}

# 请求的Payload
payload = "t=1722586488197&studyTime=500&classId=xxx&token=xxx"

# 请求头
headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": "0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "Origin": "http://regi.zju.edu.cn",
    "token": "xxx"
}

# Cookies
cookies = {
    "JSESSIONID": "A14C1B36A39AFEF902DA31B425B6C775",
    "_csrf": "S8mwplVi9KWoF2WQ0TlCeEclaeHHBkkn5p79NuWa604%3D",
    "_pv0": "P62J7JSldbcAMl%2F8SYol8I9lNKn5HQ815dRKxbhVNsYieeWeSrZHNeioHtJLuUXldlBD0j%2FIjZ5loliFa91s0QyeKGRXsRo4nr9UWQnU8%2BzTltvTaesoa3uBP0dTOJMYPQ8Qc%2FH%2BgxaxjAgiGir9G%2BoZsLhOGrwxzM%2FsXXovNLJTFEjC7h%2Fu9zzG6N5zqfvV%2BuRBtTgIOoDPcZFhtMmtRc2D8gjSr5GQt0SoIba6vo8Go2qTi%2BVaeHbQOJE7ph6GniCbEOp%2BtFqNouYpNYfPi0xxy7f1XjjY4Yu9hJJOV7SpOQFyV67Y5SkPTpyD2Nct0b%2BhIOqkvYABTAJ4toBQxZUvwSragij%2FUjAxoVGHOA%2FS9kZvc0XDJ25zAcym1LlzUuF2uRFTgoKHAAgNXVeG%2B7xVa5%2B%2BpG5%2F2wiN0A%2Bi%2FeM%3D",
    "_pf0": "EPirbyaIrZgfFQ2kiYwT%2F5zxX9Xf%2FuCeqOpQf7kEUpM%3D",
    "_pc0": "o998dpt3r09gP1IqH%2Fmag1SEZIrxkyUxZGeQa4v4%2FuQ%3D",
    "iPlanetDirectoryPro": "5EWaqpq7PoMF6PRqqupKgbxerKkygzH%2FgDibZxwCdhAAGsIz34zlKcDKLEApH9QJ%2BEDQy%2FrpmUnSe0ztZh1s5BjZ2N6skjpxIoy9E0xjDghTkGpvOWhbpKmuawD%2F9NdzrcHIVZgng4gx9NELGDle3PYXTVBVCUmH%2F6PCcDoQ89VPTq61j4U0ZmQF7izWaxn%2F7bLfCjTQDc1M4NtqquGcEd%2BEZZYfBMb7UHqJJqNLBPC2AA35GD1M7RDI%2BLpeo6V5Ht0rmzeprHbwrAyLnH6vymvlHk7lo%2BQNvTPH8WMEqxMJI3mOuP%2BhD8OAKkHSm%2FYSuAm9RIgDZ4RZ%2FoD4A5l6oFQ6s4%2BZLmY1v%2BDxQJqt3EM%3D",
    "stu-token": "xxx"
}

# 发送POST请求
response = requests.post(url, params=params, data=payload, headers=headers, cookies=cookies)

# 输出响应内容
print("状态码:", response.status_code)
print("响应内容:", response.text)
