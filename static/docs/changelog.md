# change log

## Mgek

- **build19.2** 增添Restful API接口页
- **build 19.5** 增添数据库
- **build 19.10** 增加订阅`subscribe`页面
- **build 20.4** 更换订阅相关接口
- **build20.8** 使用模板重构页面, 删除无效接口
- **build20.8.10** doc站点由vuepress静态页面代理至mgek doc站点, 通过Nginx设置资源
- **build20.8.20** 接口合并，关闭Mgek API
- **build20.9.9** webp不适应ios设备，重新适配

## Renj

- **build18.6** WordPress部署
- **build19.2** 转为Hexo部署,数据同步转移, 域名landers1037.top
- **build19.6** 更换域名lrenj.top
- **build19.8** flask部署测试完成
- **build20.1** 更换部分页面样式,页面重构
- **build20.7** 全站架构重写,精简页面,优化数据库.使用模板重构主页及部分页面, 添加数据库字段, 优化静态资源加载, 全部页面使用CDN加速, 部分CDN资源由**bootCDN**调整为**staticfile**. 配置Nginx缓存策略优化数据显示和刷新, 加速静态资源加载.目录结构分层设计,API接口暴露更加直观
- **build20.8.1** 更换域名renj.io
- **build20.8.5** 新增console控制台,利用密钥与后端通信
- **build20.8.10** 调整数据库结构, 增加分析页面统计站点访问情况, 对部分搜索引擎爬虫采取优化爬取,统计的措施. 丰富了`robots.txt`. 增加防爬虫中间件, 禁止部分测试机器爬虫和非法scrapy爬虫
- **build20.8.14** 全站图片资源整合为`webp`，增加安卓设备，apple设备浏览器移动端适配，支持本地APP模式显示
- **build20.8.20** 增加异步通知bot接口
- **build20.9.9** webp不适应ios设备，重新适配。新增sitemap页面
- **build20.9.30** 更换服务器，JJ计划开启，开发JJservice：可视化服务管理平台；JJGo：基于Go的restful接口，旨在汇聚全局服务接口，分app响应数据，逐渐由Flask转为Go框架
- **build20.10.2** 个人主页重归简单设计页面，移动端和PC端统一显示样式。取消博客文章下的分享按钮因为会引起safari上的页面布局问题，改用动态生成二维码方式分享（该功能正在测试中）。 JJService云服务正式上线，访客模式下不能操作可以查看服务器状态。