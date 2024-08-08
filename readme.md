# 刷课脚本

目前刷课脚本有两个版本:

- [Python 版本](#python)：自动读取每个课程的进度，只刷不够的过程，需要查看并填写 Cookies。
- [JavaScript 版本](#javascript)：打开 F12 即可运行，无需查看 Cookies，会刷所有的课。

## Python

Python 脚本需要浏览器的 Cookies，如果有没有的字段，需要手动加上，每个字段都要写，否则某些视频无法刷。所有字段都要加，不单单是token。

![Cookies](./img/image3.png)

能够自动读取每个课程的进度，只刷不够的课程。增加慢刷选择，慢刷安全些。每个课程只刷所需要的时间，绝不多刷

![alt text](./img/img.png)

执行命令python save_request.py

![alt text](./img/image4.png)

## JavaScript

首先前往 [适应性课程](http://regi.zju.edu.cn/classesOpen)，显示课程列表。

按 F12，开启控制台，将 `console.js` 贴入控制台。然后手动输入 `main()` 回车，即可运行。

## 废弃

~~进入具体课程界面，查看课程id~~ 已实现自动读取课程id功能
![alt text](./img/image.png)
