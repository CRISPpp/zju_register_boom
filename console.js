// 无需 python，只需浏览器，更为快捷
// 丢到 console 里即可，然后执行 main()

function getCookie(name) {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
}

async function getList() {
  const token = getCookie("stu-token");

  const url = `http://regi.zju.edu.cn/grs-pro/config/vclassesdetail/queryList`;
  // 设置请求参数
  const params = {
    t: Date.now(),
    token: token
  };

  const payload = new URLSearchParams(params).toString();

  const options = {
    method: "GET",
    headers: {
      "token": token
    },
  };
  
  // 发送 GET 请求
  return fetch(url + "?" + payload, options)
    .then(response => response.json())
    .then(data => {
      console.log(data);
      const list = [];
      for (const item of data.list) {
        list.push({
          classId: item.id,
          className: item.title,
        });
      }
      return list;
    })
    .catch(error => {
      console.error("Error:", error);
    });
}

async function finish(classId) {
  const studyTime = 500;
  const token = getCookie("stu-token");

  const url = `http://regi.zju.edu.cn/grs-pro/stu/classinfo/addStudyLog`;
  // 设置请求参数
  const params = {
    t: Date.now(),
    studyTime: studyTime,
    classId: classId,
    token: token
  };

  const payload = new URLSearchParams(params).toString();

  const options = {
    method: "POST",
    headers: {
      "token": token
    },
  };
  
  // 发送 POST 请求
  await fetch(url + "?" + payload, options)
    .then(response => response.json())
    .then(data => {
      console.log(data);
    })
    .catch(error => {
      console.error("Error:", error);
    });
}

function main() {
  getList().then(async (list) => {
    console.log(list);
    for (const item of list) {
      console.log("begin", item);
      await finish(item.classId);
      console.log("end", item);
    }
  });
}
