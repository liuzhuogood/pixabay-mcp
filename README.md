# Pixabay图片搜索MCP

一个用于从Pixabay搜索图片的MCP服务。

## 使用方法

请预先申请自己的API KEY:
https://pixabay.com/api/docs/
### PIP方式
``` 
 # 安装
 pip install pixabay-mcp

 # 获取工具路径
 which pixabay-mcp

 # 运行
 /Users/liuzhuo/miniconda3/bin/pixabay-mcp  --api-key=APIKEY
```

### uv方式
```
uvx pixabay-mcp --api-key=APIKEY
```

<img src="https://i.miji.bid/2025/04/03/d9a02825037eb5b96dd87f671264bca9.jpeg" width="800">
<img src="https://i.miji.bid/2025/04/03/74af7d5580b6346123972f1b150aeeb6.jpeg" width="800">


## 启动服务

运行服务器：

```
# 方法1: 使用.env文件
# 在根目录创建.env文件并添加以下内容:
# PIXABAY_API_KEY=你的API密钥
python server.py

# 方法2: 使用命令行参数
python server.py --api-key=APIKEY
```

MCP服务器将可供AI代理用于图片搜索。

## 日志

日志保存在应用程序目录中，文件名格式为`app_YYYYMMDD.log`。

## 开发

- `.env`文件被排除在git之外以保护API密钥
- 如果您计划贡献代码，请确保安装开发依赖项

## 许可证

[MIT](LICENSE) 