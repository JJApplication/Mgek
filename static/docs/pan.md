# pan

personal web storage

> 此文档未更新，部分接口配置已失效

简单的个人云端网盘存储服务

特性：支持自定义文件的上传大小，文件的保存地址，文件的外部URL地址

基于**jwt-extend**验证身份，默认通过**args**中的`token`参数传递`token`。你可以在配置中修改对应的配置改为使用authority请求头或者JSON格式body的方式。

## 使用

### 初始化数据库

| 接口         | 方式 | 参数 |
| ------------ | ---- | ---- |
| /api/db_init | post | -    |

### 创建用户

| 接口         | 方式 | 参数                             |
| ------------ | ---- | -------------------------------- |
| /api/sign_up | post | JSON `{"name": -,"password": -}` |

用户会存储在数据库内

### 登录

| 接口       | 方式 | 参数                             |
| ---------- | ---- | -------------------------------- |
| /api/login | post | JSON `{"name": -,"password": -}` |

输入用户名称和密码后登录，后端会返回token数据，形如`{"token": -}`

默认的token有效期为3600s，你可以在config中修改此项

### 上传

| 接口        | 方式 | 参数                         |
| ----------- | ---- | ---------------------------- |
| /api/upload | post | FORM `{"file": binary file}` |

通过表单形式传递文件，文件标识符默认为`file`

### 返回文件信息

| 接口           | 方式 | 参数           |
| -------------- | ---- | -------------- |
| /api/file_info | get  | ARGS `?name=-` |

通过文件名称获取该文件的信息，默认会返回文件名，文件在服务器上的URL

### 更多接口

| 接口            | 方式 | 参数               |
| --------------- | ---- | ------------------ |
| /api/file_list  | get  | ARGS `?name=-`     |
| /api/fie_delete | post | JSON `{"name": -}` |
| /api/db_del     | post | -                  |



## 二次开发

### 标准化输出

修改**response**包下的`http_response`函数，已标准化响应数据

默认的响应为：

```python
return jsonify({
	"code": code,
	"msg": msg,
	"data": data
})
```



### 限制文件类型

修改**config**包下的`normal_config`

默认的文件格式

```python
    MAX_CONTENT_LENGTH = 100 * 1024 * 1024 * 1024
    UPLOADED_FILE_DEST = os.path.join(os.getcwd(),'upload_file')
    UPLOADED_FILE_URL = 'http://localhost:5000/file/'
    UPLOADED_FILE_ALLOW = '*'
    UPLOADED_FILE_DENY = ('bat', 'sh','db','sqlite','sql','bash','o')
    UPLOADS_DEFAULT_DEST = os.path.join(os.getcwd(),'upload_file')
    UPLOADS_DEFAULT_URL = 'http://localhost:5000/file/'
```

修改`UPLOADED_FILE_ALLOW`为允许的文件类型，元组形式

修改`UPLOADED_FILE_DENY`为禁止上传的文件类型。元组形式

### 使用关系型数据库

默认使用sqlite作为存储数据库，你可以在**config**包下修改数据库地址

默认地址`SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.getcwd()+"/pan.db"`

如果修改为MySQL，需要安装pymysql库，请使用格式化的语句例如：

`mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USER,PASS,ADDRESS,PORT,DATABASE)`



## 部署

使用gevent库部署应用或者使用gunicorn部署此应用