# OSS Command
[![build status](http://gitlab.imhuwq.com/imhuwq/oss_command/badges/master/build.svg)](http://gitlab.imhuwq.com/imhuwq/oss_command/commits/master)
[![coverage report](http://gitlab.imhuwq.com/imhuwq/oss_command/badges/master/coverage.svg)](http://gitlab.imhuwq.com/imhuwq/oss_command/commits/master)

在命令行执行 oss 的操作.  
安装后必须执行 `oss_command config` 来配置秘钥.  
目前支持的操作有: 上传, 检查存在, 下载和复制.  

## 所有命令
```bash
oss_command help
```

## 配置
```bash
oss_command config
```

## 上传
```bash
oss_command upload /local/path/file.ext bucket-name.oss-endpoint.aliyuncs.com remote/path/file.ext
```

## 检查存在
```bash
oss_command exist bucket-name.oss-endpoint.aliyuncs.com remote/path/file.ext
```

## 下载
```bash
oss_command download /local/path/file.ext bucket-name.oss-endpoint.aliyuncs.com remote/path/file.ext
```

## 复制
```bash
oss_command copy bucket-name.oss-endpoint.aliyuncs.com remote/src.ext remote/dst.ext
```
