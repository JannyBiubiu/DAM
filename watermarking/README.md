# MusicWebsite
Learn to build a website

## 【非作业相关】练习svg
- embed.html
- example.svg
- icon.svg

## Hw02
- 音乐资源展示

## Hw02a
1. 增加spyder.py,可以爬取网易云指定歌单的歌曲。
2. 添加资源索引和分区索引，动态生成网页，使分区数可修改
3. 将播放和展示分离开，避免同时播放多首歌曲的问题产生
4. 增加读取.lrc标准文件功能
5. 固定展示框高度，并自动为内容溢出部分添加scroll

> 爬虫使用说明：
- （可选）建立文件夹，并且在/myapp/static/meta.json中输入新文件夹信息
- 在config.py中输出歌单id、下载到的文件夹名、分类名
- 运行spyder.py文件，下载资源，（如果建立了新文件夹，则网页中的分区数量会增加）

## HW03 Watermarking
Learn to add watermarking to image.
bonus:a simple web based service
use PIL

### file structure:
- README.md<br>//help
- requirement.txt<br>//应用
- test.py<br>//生成图片，使用PIL，最终没有应用到网页服务中，是否存在不影响
- extract.py<br>//提取水印，使用PIL，最终没有应用到网页服务中，是否存在不影响
- runserver.py<br>//运行此文件，启动后端服务
- myapp<br>//应用
	- __init__.py<br>//初始化
	- view.py<br>//路由
	- __pycache__<br>//编译缓存，是否存在不影响
	- static<br>//静态资源，样式、字体、图片
	- templates<br>//页面
		- index.html<br>//首页&生成图片的页面
		- layout.html<br>//布局
		- test.html<br>//提取水印的页面

### CMD:`python runserver.py`


