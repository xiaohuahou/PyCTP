pip i# Python3 wrapper of CTP

CTP接口的python3封装。使用swig直接转换，接口使用和c++的CTP完全相同。

## 安装

1. 按照ctp的动态链接库

  ```
  cp ./api/thostmduserapi.so /usr/lib/libthostmduserapi_se.so
  cp ./api/thosttraderapi.so /usr/lib/libthosttraderapi_se.so
  ```

2. 使用pip安装PyCTP

  ```
  pip install .
  ```

## swig

如果需要重新生成swig相关文件，执行`run_swig.sh`

