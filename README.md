# scrapy_demo
练习scrapy框架时python编写的程序

1，微信小程序社区教程爬取
  
  
  http://www.wxapp-union.com/
  
  使用方法：
    
  在scrapy_demo-master\wxapp文件夹下开启命令行
  
  输入 scrapy crawl index，即可开始爬取，并且每爬取一个教程的详细信息，就会输出一个标题

2，edusrc登录爬虫
  
  使用时需要在index中输入username和password
  
  手动识别验证码
  
  介绍博客：https://www.cnblogs.com/Cl0ud/p/12355851.html

3，buxiuse 不羞涩网站小姐姐图片爬取下载

https://www.buxiuse.com/

4，useragent，自定义中间件Middleware，同时使用fake-agent随机更改伪造请求头

一定程度上防止网站反爬

  
