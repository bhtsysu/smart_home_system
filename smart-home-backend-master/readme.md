## TODO List
- DONE  根据前端写出数据模型，可以实现通过json创建 Room、Device、Scene 等资源。
  - 具体的请求示例可以看下方
- DONE scene activate/deactive函数 一键设置所有的设备(post提交一个空的东西就可以激活)
![1748877093503](image/readme/1748877093503.png)
- 日志
- 登录模块
- 测试文件
- 
---
## api参考
一、创建 Room（房间）
请求地址
```
POST /api/rooms/
```
请求体

```json
{
  "name": "书房"
}
```
 二、创建 Device（设备）
请求地址

```
POST /api/devices/
```
请求体

```json
{
  "name": "书房台灯",
  "type": "light",
  "room": 1,  // 房间的ID（外键）
  "status": true,
  "extra": {
    "brightness": 80,
    "color": "#FFDD88"
  }
}
```
🔸 注意事项：
* `room` 要传房间的 `id`。
* `extra` 是一个自由格式的字典（JSON对象），可以存 brightness、temperature、volume 等属性。

三、创建 Scene（场景）
请求地址
```
POST /api/scenes/
```
请求体

```json
{
  "name": "工作模式",
  "description": "打开书房台灯，调整亮度",
  "device_configs": [
    {
      "device": 6,  // 设备ID（如书房台灯）
      "status": true,
      "config": {
        "brightness": 100
      }
    },
    {
      "device": 2,  // 设备ID（如卧室空调）
      "status": true,
      "config": {
        "temperature": 25
      }
    }
  ]
}
```
注意事项：
* `device_configs` 是一个列表，每个元素表示一个设备的目标配置；
* 每项需要包括：

  * `device`: 设备 ID；
  * `status`: 是否开启；
  * `config`: 附加参数，如亮度、温度等。

四、修改（PUT 或 PATCH）

可以通过 PUT 或 PATCH 来修改上述资源，比如：
修改设备状态
```
PATCH /api/devices/6/
```

```json
{
  "status": false
}
```
修改场景描述

```
PATCH /api/scenes/1/
```
```json
{
  "description": "新的描述"
}
```


## 字段对照表

| 模型      | 字段名              | 类型             | 说明              |
| ------- | ---------------- | -------------- | --------------- |
| Room    | `name`           | string         | 房间名称            |
| Device  | `name`           | string         | 设备名             |
|         | `type`           | string         | 类型，如 light、ac 等 |
|         | `room`           | integer (外键ID) | 所属房间            |
|         | `status`         | boolean        | 开关状态            |
|         | `extra`          | dict           | 配置，如亮度、温度等      |
| Scene   | `name`           | string         | 场景名称            |
|         | `description`    | string         | 场景说明            |
|         | `device_configs` | list of dicts  | 设备目标状态及配置       |
| Config项 | `device`         | integer (外键ID) | 被控制的设备          |
|         | `status`         | boolean        | 打开/关闭           |
|         | `config`         | dict           | 额外配置，如亮度/温度等    |


