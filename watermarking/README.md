# MusicWebsite
Learn to build a website

## Branch: Watermarking
Learn to add watermarking to image.
bonus:a simple web based service
use PIL

## file structure:
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

## CMD:`python runserver.py`

