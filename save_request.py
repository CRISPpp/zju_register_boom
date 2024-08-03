import requests


def get_all_class_id():
    class_ids = [
        "9be29932adca13a8761a810ad9ff1201",
        "84826a077a3ee7133da28370999c4c4c",
        "9ec7cb7aa59a07f22728a89ffbbcef36",
        "c484e08190c7f908a961d774f1a2b5d3",
        "0de584669b679c2206acfca06522c8c2",
        "79a39e3ce9b4509a7fc1ca3f29c0b869",
        "04b4067f100dce9281bcf7ada15fe658",
        "478ff9d64a0628e3dc5622c26111bc7d",
        "345ee2eee7189a6e3507c755b34e1316",
        "35e292a1fb2f0e388c29fc1ac10f4c99",
        "4ba2e4620b5b6f3f38c46f15ba0312f7",
        "37735aaafc0be61faf07b892a22685bd",
        "5eaddb36193b306c4b8d02dd1e802583",
        "d3d144557cea570a37fcb283d5f688eb",
        "35e292a1fb2f0e388c29fc1ac10f4c99",
        "7dafbc08703db2aba98f6fa5991d6136",
        "21a99f1d4ddfa2661f93d0c5e54c2abb",
        "5b1416709697175da4a2015a31b1fc9c",
        "f07e6ee8c6ef732a212f6d55974a3daf",
    ]
    return class_ids


# TODO: 请将下面的Cookie信息替换为你自己的Cookie信息
cookies = {
    "JSESSIONID": "input_your_JSESSIONID_here",
    "_csrf": "input_your__csrf_here",
    "_pv0": "input_your__pv0_here",
    "_pf0": "input_your__pf0_here",
    "_pc0": "input_your__pc0_here",
    "iPlanetDirectoryPro": "input_your_iPlanetDirectoryPro_here",
    "stu-token": "input_your_stu-token_here",
}

if __name__ == "__main__":
    if cookies["stu-token"] == "input_your_stu-token_here":
        raise Exception("请先将Cookie信息替换为你自己的Cookie信息")
    url = "http://regi.zju.edu.cn/grs-pro/stu/classinfo/addStudyLog"
    params = {
        "t": 1722586488197,
        "studyTime": 500,
        "token": cookies["stu-token"]
    }
    payload = "t=1722586488197&studyTime=500&token="+cookies["stu-token"]
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
        "Origin": "http://regi.zju.edu.cn",
        "token": cookies["stu-token"],
    }

    for class_id in get_all_class_id():
        cur_payload = payload + "&classId=" + class_id
        params["classId"] = class_id
        response = requests.post(url, params=params, data=payload, headers=headers, cookies=cookies)
        print("class_id:", class_id)
        # 输出响应内容
        print("状态码:", response.status_code)
        print("响应内容:", response.text)
        print("=====================================")
