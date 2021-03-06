# nms
前后端分离式网络广播管理系统设计

毕业设计 华中科技大学

最终得分: 94

作者: Landers

------



## 项目介绍

基于web设计的智能ip广播系统

## 设计要求

设计一个IP广播系统应采用集中式管理模式，在校园设立广播系统集成服务器，充分利用校园网络将各个区域的广播音频终端连接起来，组成一套数字化的网络广播系统。在系统服务器统一控制IP广播的播放内容，播放时间，定时上电及下电 。

## 需求环境

- Flask构造的web后端服务，实现底层的api需求
- 使用vue进行前端界面设计
- 使用PCBA提供的javascript SDK进行功能设计，完成整个管理系统的设计
- 对前后端合并完成总体设计
- Jquery，bootstrap等前端技术

## 目标

（1）研究提供的IP广播PCBA控制板及其配套的SDK包解读，实现HTML/JavaScript对SDK包的API函数调用。

（2）研究Python、Node.js、HTML5/JavaScript/CSS、vue.js及MySql数据库等，实现一个基于智慧教室的IP广播管理系统。

（3）设计本课题的教室IP广播网络管理系统中，管理员通过自己的学号或者工号登录系统，并实现权限的分离和管理。

（4）IP广播网络管理系统，支持系统定时播放，临时插播、实时监控音频终端的系统情况。

（5）建立实时数据同步的监控机制，及时发现数据传输中存在的问题，并通过技术手段将告警知会管理人员。

（6）设计为web网站形式，实现前后端分离，前端用vue.js框架，后端实现对数据库的操作并暴露相关的API。

（7）广播网络管理系统具有日志功能，可以记录数据推送的时间等信息。

## 设计思路

1. 使用Flask完成整个后端的设计，设计需求的api与SDK进行对接。使用Flask-Script进行项目控制，使用Flask-migrate进行数据库迁移工作，使用Flask-Restful完成api的设计，对于vue前端的调用使用flask-cors完成跨域需求
2. ~~对于登录需求使用Flask-Login进行用户登录的控制~~
3. 使用Postgresql数据库完成数据的保存
4. 建立全局的Debug函数，对出现的错误进行统计，并且按照时间保存为本地的.log文件以供分析
5. 前端使用vue2.0开发，使用bootstrap和elementUI完成css样式的美化
6. 使用token方式完成用户的登录认证

## 参考资料

- Flask-Restful[文档](http://www.pythondoc.com/Flask-RESTful/quickstart.html)
- Flask-Cors [文档](https://flask-cors.readthedocs.io/en/latest/)
- VUE [文档](https://cn.vuejs.org/)
- vue-cli [文档](https://cli.vuejs.org/zh/guide/cli-service.html)
- bootstrap [文档](https://www.bootcss.com/)

## 项目设计

### 项目名称

NMS(network management sys)网络广播管理系统

### 项目依赖

Python3.7,Flask,Vue@4.1.1

**使用库**

| 库               | 功能实现        |
| ---------------- | --------------- |
| flask-cors       | 跨域请求        |
| flask-restful    | 设计restful api |
| flask-script     | 管理falsk项目   |
| flask-httpauth   | token认证       |
| flask-migrate    | 数据库迁移      |
| flask-sqlalchemy | 数据库映射      |
| psycopg2         | 连接pgsql数据库 |
| psutil           | 获取系统信息    |
| functools        | 自定义log装饰器 |



### 项目api文档

[API for NMS](./api/nmsAPI.md)

###  项目wiki

[Wiki for NMS](https://github.com/Landers1037/ipbroadcast/wiki)



## 源码

该项目已全部完成

参见**frontend**前端代码 **backend**后端代码

最终效果示代码最终版本,本文档均为测试时的数据

## 依赖

1. Vue CLI@4.1.1

2. Python Flask

3. flask-httpauth,falsk-restful,falsk-sqlalchemy,functoools,psutil,psycopg2,flask-migrate,flask-scripts,flask-cors

4. > 注意:本项目需要对应的硬件广播设备和服务器支持,所有的硬件操作由后端Flask和硬件服务器通信完成
    >
    > 硬件服务器为试用版本,测试数据可能与正式使用效果有差别

## 版本

- v1.08
- v1.13
- v1.16
- v1.29
- v3.28
- v4.19
- v4.22
- v5.5
- v5.16

## 迭代信息

- ### v1.08

使用flask-restful构建基础api后端服务框架，使用requests库来请求硬件服务器的web服务，完成服务器后端和硬件后端的分离

- ### v1.13

使用vue-cli完成项目的构建，添加基本的登录页面，关于页面，控制台页面

~~使用flask-login进行用户的身份验证~~

在后期的测试中发现，flask-restful是无状态的api，不能保持请求时的用户状态所以不能使用flask-login

- ### v1.16

| 前端             | 后端          |
| ---------------- | ------------- |
| 添加登录页面验证 | cors跨域      |
| 添加控制台信息   | 设计token验证 |
| 添加API文档指引  | 重写restful   |
| 使用element美化  |               |

#### 登录认证

全局使用token请求头信息的方式完成验证，在前端使用axios发送登录请求数据，接收返回的json数据提取内部的token信息并保存在vuex内存中，每一次的请求发送时都会在请求头中添加token信息发送至后台验证。

修改axios拦截器在请求头上添加内存里存储的token信息。设置response里的401未授权响应直接跳转至登录页面。

后端：使用flask-httpauth的token验证装饰器，每次登录时生成token并设置token的过期时间。在收到api的请求时先验证身份再返回数据。

#### 控制台信息

前端：设计一个控制台用于查看后台的信息，主要查看后端的api地址，当前的登录用户状态，后端的硬件服务器状态，当前运行服务的内存cpu占用信息

后端：使用psutil获取系统的占用信息，从数据库获取当前的登录用户信息并返回

#### API文档

添加后端api的文档在线阅读页面，使用marked .js进行前端渲染

#### 美化

使用element UI的组件库进行页面的美化，实现页面的简单美观。同时使用部分自带的动画库进行过渡动画的渲染

- ### v1.29

重新设计了dashboard操作面板界面，布局更合理，菜单显示更清晰

添加了echarts绘制的后端服务监控信息和api请求次数统计

设计了生命周期更长的路由，用于返回时保存信息

添加了切换用户页面，可以再操作面板方便地切换用户

全局统一了配色样式

| 组件         | 配色     |
| ------------ | -------- |
| 主体色       | #f5f5f5  |
| 主题强调色   | #409eff  |
| 下拉菜单配色 | #426ab3  |
| 警告按钮     | #f56c6c  |
| 普通按钮     | \#909399 |

- ### v3.28

    对Flask后台重新设计，模块解耦。

    重新设计了用户的token认证模块

    添加wsgi server支持后期使用asgi server部署

- ### v4.19

    使用`mockjs`对前端的部分api进行模拟测试

    重新设计了用户操作组件和用户列表组件

    1. 针对当前登录的用户，添加了用户的权限判定，`utm`代表用户模块，任务模块，终端模块的访问权限

    2. 针对当前用户，添加了任务级别 低中高 分别对应123

    3. 优化了用户添加和更新面板的显示 使用flex布局

    4. 优化了用户添加和更新逻辑，添加用户时后端会进行验证，当遇到**重名**或者`root`时会返回`repeat`信息，提示不能添加重复的用户。用户更新的时候如果需要修改用户的名称，会根据ID和用户名称进行验证，确保更新的用户名称和数据库里存在的用户不冲突

    5. 优化了用户列表的显示逻辑，支持双击打开详情，支持删除，更新

    6. 优化了删除操作，删除时后台进行判断，首先root用户不能删除为系统保留。其次判断用户的ID是否存在

    7. > 暂定：当数据库操作后会对IP广播进行操作，如果出错则进行数据库回滚，这样保证数据的统一性

- ### v4.22

    1. 完善了数据库用户表和播放终端表的字段设计
    2. 针对用户模块，root用户被设计为系统内置的用户，不能删除不能修改其他信息，只能修改密码。当首次进入系统时会自动创建root用户
    3. 针对终端模块，独立设计终端的列表数据，所有对终端的列表请求全部交由数据库处理，对于广播内部维护的终端列表在每次用户按下**更新终端**按钮时会和数据库进行同步
    4. 部分模块如添加用户，删除用户，更新用户，更新终端操作加入了数据库回滚，在和广播的通信出现错误时自动回滚数据库
    
    ### v5.16
    
    最终版本预览
    
    1. 完善了用户登出逻辑
    2. 优化了用户权限认证和后端的IP广播交互的逻辑分离
    3. 完善任务管理模块，支持任务添加，更新，删除
    4. 优化数据库回滚逻辑
    5. 增加gevent原生并发支持
    

# 最终版本预览

## IP广播管理系统

### 系统架构图

![1](/store/nms/架构.png)

### 演示视频

请前往Github

### 界面预览

![d1](/store/nms/1.png)

![d2](/store/nms/2.png)

![d3](/store/nms/3.png)

![d4](/store/nms/4.png)

![d5](/store/nms/5.png)

![d6](/store/nms/6.png)

<img src="/store/nms/7.jpg" alt="d7" style="zoom:80%;" />

![d8](/store/nms/8.png)

![d9](/store/nms/9.png)

![d10](/store/nms/10.png)