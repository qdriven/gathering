# github3.py 代码分析

github3是github的一个python sdk,使用起来比较方便,通过他的代码来分析一下一个sdk如何
写，同时又比较好用。

## 分析

- 第三方依赖

```shell
  PyJWT[crypto]>=2.3.0
    python-dateutil>=2.6.0
    requests>=2.18
    uritemplate>=3.0.0
```

- 源码入口
__init__.py文件

- 结构
  * models
  * exceptions
  * api
  * other domains

- BaseObejct GitHubCore
