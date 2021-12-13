# tools
tools for personal use

个人工具集

## 功能

- 由hexo博客的`xml`文件索引转为`json`
- 通过索引json建立博客数据库sqlite3
- 根据索引内容读取本地`post`路径下的`markdown`文件，添加正文内容
- 博客增量更新，更新索引，更新文章内容，更新标签内容
- 图片转webp格式
- 图片质量压缩，不改变分辨率的情况下尽量减小图片体积
- 图片转换为base64
- 推送文件到远程服务器，支持`POST`请求的http文件服务器
- mp4视频切片ts

## 使用

拉取打包程序

```bash
https://github.com/Landers1037/tools/releases
chmod +x tools
```

### 帮助信息

```bash
$ tools --help
Usage: tools [OPTIONS] COMMAND [ARGS]...

  整合工具

Options:
  --help  Show this message and exit.

Commands:
  blog    生成/删除数据库文件
  img64   图片转base64
  imgzip  图片压缩质量，删除原图
  send    发送云端文件 file+url
  system  平台测试
  test    路径测试
  update  更新数据库文件
  webp    webp转换
```

### 博客相关帮助信息

```bash
$ tools blog --help
It's Mgek Tools
type --help for more info
Usage: tools blog [OPTIONS]

  生成/删除数据库文件

Options:
  -r, --remove     删除数据库
  -n, --new        新建数据库
  -j, --json TEXT  json文件
  -t, --test TEXT  文章测试
  --help           Show this message and exit.
```

#### Hexo索引转换为Json

```bash
$tools blog -j "/path/search.xml"
```

默认会`blog.json`保存到当前目录下

#### 博客数据库初始化

> 数据库初始化的信息依赖于当前路径下的`blog.json`文件

```bash
$tools blog -n
```

#### 博客旧数据库删除

```bash
$tools blog -r
#默认在新生成时会删除旧的数据库
```

#### 博客数据库测试

```bash
$tools blog -t
#输出当前写入数据库的索引列表
```

### 博客更新帮助信息

```bash
Usage: tools update [OPTIONS]

  更新数据库文件

Options:
  -p, --post TEXT  更新指定文章
  -ps, --posts     更新文章列表
  -u, --uv TEXT    是否更新uv
  -t, --tag        更新标签
  --help           Show this message and exit.
```

#### 更新文章列表

```bash
$tools update -ps
#文章列表会从默认的blog.json文件读取生成，请在之前就重新生成json文件
```

#### 更新指定文章

```bash
$tools update -p post-name
#附带args信息为文章对应的md文件名称，不需要加后缀名
#会更新此文件对应的文章
```

> 注意：这里的文件名默认与文章在数据库里的URL名称相同，这是hexo默认生成时指定的
>
> 如果文件名为`test.md`那么它在数据库的URL字段为`test`

#### 更新UV

```bash
$tools update -u 100
```

这是一个统计访问量的字段，表名为uv

#### 更新标签

```bash
$tools update -t
```

更新标签依赖`blog.json`告知文件总数，tools会自动从文件内读取标签，保存的格式为`TEXT`由`,`分隔

### webp图片转换

```bash
Usage: tools webp [OPTIONS]

  webp转换

Options:
  -k, --keep   保存原图
  -w, --water  开启水印
  --help       Show this message and exit.
```

#### 默认转换

```bash
$tools webp
```

默认转换会将当前路径下的全部图片文件转换为`webp`，不保留原图，没有水印，水印是我自己的

#### 保留原图

```bash
$tools webp -k
```

#### 开启水印和保留原图

```bash
$tools webp -k -w
```

### 图片压缩

```bash
Usage: tools imgzip [OPTIONS]

  图片压缩质量，删除原图

Options:
  -q, --quality INTEGER  默认分辨率调整
  --help                 Show this message and exit.
```

#### 指定质量压缩

```bash
$tools imgzip [-q]
```

不使用`-q`传入变量时默认的压缩质量为80%

使用`-q`传入压缩质量`1-100`

```bash
$tools imgzip 60
```

### 图片转base64

```bash
Usage: tools img64 [OPTIONS]

  图片转base64

Options:
  -f, --file TEXT  图片转base64
  --help           Show this message and exit.
```

使用`-f`指定需要转换的文件路径，建议使用绝对路径

```bash
$tools img64 -f "/path/test.jpg"
```

### 上传文件到服务器

```bash
Usage: tools send [OPTIONS] FILE URL

  发送云端文件 file+url

Options:
  --help  Show this message and exit.
```

按顺序传入参数`file`和`url`，`file`为文件的本地路径，`url`为远程服务器的地址。

支持使用`POST`请求的http服务器

```bash
$tools send "/path/test.zip" http://127.0.0.1:1234/upload
```

### 视频切片

```bash
$tools ts
$tools ts -n opt-name
```

将当前路径下的全部视频文件转为ts流，生成m3u8文件

添加参数`-n`自定义输出的文件名称，默认为传入的文件名

### 注意事项

如果有`-f`参数则允许传入路径参数

否则所有的执行都是在当前路径下