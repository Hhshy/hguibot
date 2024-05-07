## /webChat

```text
暂无描述
```

#### 公共Header参数

| 参数名 | 示例值 | 参数描述 |
| --- | --- | ---- |
| 暂无参数 |

#### 公共Query参数

| 参数名 | 示例值 | 参数描述 |
| --- | --- | ---- |
| 暂无参数 |

#### 公共Body参数

| 参数名 | 示例值 | 参数描述 |
| --- | --- | ---- |
| 暂无参数 |

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```

## /webChat/localhost:8085/api/webChat/queryAll

```text
暂无描述
```

#### 接口状态

> 开发中

#### 接口URL

> 39.101.199.180:8085/api/webChat/queryAll

#### 请求方式

> POST

#### Content-Type

> none

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```

## /webChat/localhost:8085/api/webChat/test

```text
暂无描述
```

#### 接口状态

> 开发中

#### 接口URL

> 39.101.199.180:8085/api/webChat/test

#### 请求方式

> POST

#### Content-Type

> none

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```

## /webChat/localhost:8085/api/webChat/receiveMsg

```text
暂无描述
```

#### 接口状态

> 开发中

#### 接口URL

> 39.101.199.180:8085/api/webChat/receiveMsg

#### 请求方式

> POST

#### Content-Type

> json

#### 请求Body参数

```javascript
{
    "outUserId":"outUserId11",
    "isTransferPeople":true,
    "content":"test114",
    "secretKey":"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2KMgReh1YMJcFrBOlizV1lRbTRXDIFJnp"
}
```

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```

## /webChat/localhost:8085/api/webChat/updateById

```text
暂无描述
```

#### 接口状态

> 开发中

#### 接口URL

> 39.101.199.180:8085/api/webChat/updateById

#### 请求方式

> GET

#### Content-Type

> json

#### 请求Body参数

```javascript
{
    "id":"7ae10c1a-e716-4a67-8621-4de27cde6f7a",
    "secretKey":"MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2KMgReh1YMJcFrBOlizV1lRbTRXDIFJnp",
    "replStatus":1
}
```

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```

## /webChat/localhost:8085/api/webChat/payOrder/list

```text
暂无描述
```

#### 接口状态

> 开发中

#### 接口URL

> 39.101.199.180:8085/api/webChat/payOrder/list

#### 请求方式

> GET

#### Content-Type

> none

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```

## /webChat/localhost:8085/api/webChat/payOrder/edit

```text
暂无描述
```

#### 接口状态

> 开发中

#### 接口URL

> 39.101.199.180:8085/api/webChat/payOrder/edit

#### 请求方式

> POST

#### Content-Type

> json

#### 请求Body参数

```javascript
{
    "id":2,
    "userId":"userId11",
    "pushStatus":1,
    "orderNo":"orderNo111222",
    "platformOrderNo":"platformOrderNo1111"

}
```

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```

## /webChat/localhost:8085/api/webChat/payOrder/add

```text
暂无描述
```

#### 接口状态

> 开发中

#### 接口URL

> 39.101.199.180:8085/api/webChat/payOrder/add

#### 请求方式

> POST

#### Content-Type

> json

#### 请求Body参数

```javascript
{
    "userId":"userId11",
    "pushStatus":0,
    "orderNo":"orderNo111",
    "platformOrderNo":"platformOrderNo1111"

}
```

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```

## /webChat/localhost:8085/api/file/upload

```text
暂无描述
```

#### 接口状态

> 开发中

#### 接口URL

> 39.101.199.180:8085/api/file/upload?secretKey=MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2KMgReh1YMJcFrBOlizV1lRbTRXDIFJnp&file=

#### 请求方式

> POST

#### Content-Type

> form-data

#### 请求Query参数

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| secretKey | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2KMgReh1YMJcFrBOlizV1lRbTRXDIFJnp | Text | 是 | - |
| file | - | Text | 是 | - |

#### 请求Body参数

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| secretKey | MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA2KMgReh1YMJcFrBOlizV1lRbTRXDIFJnp | Text | 是 | - |
| file | - | Text | 是 | - |

#### 预执行脚本

```javascript
暂无预执行脚本
```

#### 后执行脚本

```javascript
暂无后执行脚本
```
