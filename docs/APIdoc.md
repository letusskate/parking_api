
# 接口文档
----------------------------------------------------------------------------------

> 环境：开发与测试
>> HOST: http://127.0.0.1:8000

> 环境：应用
>> Host暂未确定

::: note

> 请求头规定（开发测试阶段）

```http
AuthToken: 12345abc
```
> 请求头规定（应用阶段）应该从login接口的返回值中获取authtoken
```http
AuthToken: eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6Inh4eDdAeHh4LmNvbSIsImV4cCI6MTY5MTU5MjM0MH0.RHzjMwTZWrZa8AZS46MNVjdM7SqrCjnJzw-b4rG5IFQ
```
# 用户
## 创建用户   [/api/users/register]
创建用户会创建用户的唯一标识，唯一标识会作为其他表（如订单）的外键，方便后期通过这个唯一标识索引与该用户有关的信息（如找到该用户所有订单）

### 创建用户 [POST]

```
URI:/api/users/register
URL: http://127.0.0.1:8000/api/users/register
```

+ 参数说明
    + first_name: 字符串，用户的名，比如杨
    + last_name: 字符串，用户的姓，比如罗
    + user_name: 字符串，用户名，必须能唯一标识一个用户
    + gender: 枚举int，性别，0为女，1为男，2为其他
    + password: 字符串，密码，可为任意字符串

+ 请求 (application/json)
    
    + Body

            {
                "first_name": "ayden4",
                "last_name": "luo4",
                "username": "xxx7@xxx.com",
                "gender": 1,
                "password":"123654"
            }                     


+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "userId": 4
                }
            }

## 用户登录   [/api/users/login]
用户登录会校验用户名对应的密码是否正确。如果正确，会返回一个token，token需要加在其他接口的header中。（注册和登录不需要）

### 用户登录 [POST]

```
URI:/api/users/login
URL: http://127.0.0.1:8000/api/users/login
```

+ 参数说明
    + user_name: 字符串，用户名，必须能唯一标识一个用户
    + password: 字符串，密码，无最短长度限制
    + token: 字符串，需要加在其他接口的header中，变量名为AuthToken

+ 请求 (application/json)
    
    
    + Body

            {
                "username":"xxx7@xxx.com",
                "password":"123654"
            }

+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Inh4eDdAeHh4LmNvbSIsImV4cCI6MTY5MTcwMTU0M30.aDKMDpYbtVdez3eFK_SFjf_s7KanKmyOROLpbDFEGjo"
                }
            }

## 修改密码   [/api/users/change-password]
修改密码要求输入用户名和原密码，之后输入新密码。

### 修改密码 [POST]

```
URI:/api/users/change-password
URL: http://127.0.0.1:8000/api/users/change-password
```

+ 参数说明
    + user_name: 字符串，用户名，必须能唯一标识一个用户
    + password: 字符串，密码
    + new-password: 字符串，新密码
    + AuthToken: 加在header中的身份验证
+ 请求 (application/json)
    
    + Headers

                AuthToken: 12345abc
    
    + Body

            {
                "username":"xxx7@xxx.com",
                "password":"123654",
                "new-password":"123654"
            }

+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "new-password": "123456"
            }

# 充值与查询

## 查询余额 [/api/users/get-money]
查询用户名的钱包余额

### 查询余额 [GET]

```
URI: api/users/get-money
URL: http://127.0.0.1:8000/api/users/get-money
```

+ 参数说明
    + username: 字符串，注册接口中提到的username，可以唯一标识用户

+ 请求 (application/json)
    
    + Headers

                AuthToken: 12345abc
    
    + Body

			{
			    "username": "luoyang"
            }                      


+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "money": 234.44
            }

+ 响应 404 (application/json)

    + Body

            {
                "code": 404,
                "message": "user not exists"
            }


## 充值   [/api/users/add-money]
为账户充值

### 充值 [POST]

```
URI: /api/users/add-money
URL: http://127.0.0.1:8000/api/users/add-money
```


+ 参数说明
    + username: 注册接口中提到的username，可以唯一标识用户，字符串
    + money: 添加的钱
    + addmoney: 添加的钱
    + totalmoney: 添加后的账户余额

+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "username":"xxx7@xxx.com",
                "money":234.44
            }
+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "addmoney": 234.44,
                    "totalmoney": 234.44
                }
            }
# 停车场

## 查看某个停车场详细信息   [api/parkinglot/get-parkinglot]
输入停车场id，显示停车场名称、简介、价格、位置；所有车位编号、是否空闲

### 查看某个停车场详细信息 [GET]

```
URI: api/parkinglot/get-parkinglot
URL: http://127.0.0.1:8000/api/parkinglot/get-parkinglot
```


+ 参数说明
    + paringlot_id: int，可以通过位置获取到所有停车场id
    + parkinglot_data: object，停车场的基本信息
    + parkingplace_data: list，所有车位的信息
    + latitude: float，纬度
    + longitude: float，经度
    + hourPrice: float，每小时价格

+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "parkinglot_id":1
            }

+ 响应 200 (application/json)

    + Body
    + 
            {
                "code": 200,
                "message": "success",
                "data": {
                    "paringlot_data": {
                        "id": 1,
                        "name": "luoyang",
                        "description": "luoyang parking lot",
                        "hourPrice": 1.0,
                        "monthPrice": 100.0,
                        "latitude": 0.0,
                        "longitude": 0.0
                    },
                    "parkingplace_data": [
                        {
                            "id": 1,
                            "identifier": "xx",
                            "spare": true,
                            "password": "123456",
                            "parkingLot": 1
                        },
                        {
                            "id": 2,
                            "identifier": "yy",
                            "spare": true,
                            "password": "123456",
                            "parkingLot": 1
                        },
                        {
                            "id": 3,
                            "identifier": "zz",
                            "spare": true,
                            "password": "123456",
                            "parkingLot": 1
                        }
                    ]
                }
            }

## 查看坐标区域内的所有停车场   [/api/parkinglot/area-parkinglot]
输入坐标区域，显示区域内所有停车场的id，名称等基本信息

### 查看坐标区域内的所有停车场 [GET]

```
URI: /api/parkinglot/area-parkinglot
URL: http://127.0.0.1:8000/api/parkinglot/area-parkinglot
```

+ 参数说明
    + left-top-latitude: 坐标区域西北角的纬度
    + left-top-longitude: 坐标区域西北角的经度
    + right-bottom-latitude: 坐标区域东南角的纬度
    + right-bottom-longitude: 坐标区域东南角的经度

+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "left-top-latitude":90,
                "left-top-longitude":0,
                "right-bottom-latitude":0,
                "right-bottom-longitude":180
            }
+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "parkinglot_data": [
                        {
                            "id": 1,
                            "name": "luoyang",
                            "description": "luoyang parking lot",
                            "hourPrice": 1.0,
                            "monthPrice": 100.0,
                            "latitude": 0.0,
                            "longitude": 0.0
                        },
                        {
                            "id": 2,
                            "name": "luoyang2",
                            "description": "this is the second parkinglot",
                            "hourPrice": 1.0,
                            "monthPrice": 100.0,
                            "latitude": 30.0,
                            "longitude": 100.0
                        }
                    ]
                }
            }

## 新增停车场   [/api/parkinglot/add-parkinglot]
输入停车场名称，随机创建出停车场和车位，返回空闲车位数量、车位总数、停车场价格。

### 查看坐标区域内的所有停车场 [POST]

```
URI: /api/parkinglot/add-parkinglot
URL: http://127.0.0.1:8000/api/parkinglot/add-parkinglot
```

+ 参数说明
    + parkinglot_id: 停车场的id
    + parkinglot_spare_place_num: 停车场剩余车位数量
    + parkinglot_place_num: 停车场车位总数
    + parkinglot_hour_price: 停车场每小时价格
    + parkinglot_month_price: 停车场每月价格

+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "name":"my test parkinglot"
            }
+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "parkinglot_id": 3,
                    "parkinglot_spare_place_num": 11,
                    "parkinglot_place_num": 26,
                    "parkinglot_hour_price": 5,
                    "parkinglot_month_price": 415
                }
            }

# 订单

## 创建预约订单   [/api/orders/reservation]
创建车位预约订单，输入用户名、停车场id；返回订单id，停车场id，车位id，车位标识符。

### 创建预约订单 [POST]

```
URI: /api/orders/reservation
URL: http://127.0.0.1:8000/api/orders/reservation
```

+ 参数说明
    + parkinglot: int，停车场的id
    + parkingplace_id: int，停车位的id，可以唯一标识一个停车位
    + parkingplace_identifier: string，停车位的编号，由各个停车场自行设置，方便用户找到车位的位置（如"c37"）
    + order_id: int，订单的id，可以唯一标识一个订单，后续更新订单会用到

+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "parkinglot":1,
                "username":"xxx10@xxx.com"
            }
+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "order_id": 7,
                    "parkinglot_id": 1,
                    "parkingplace_id": 1,
                    "parkingplace_identifier": "xx"
                }
            }


## 删除预约订单   [/api/orders/delete-reservation]
输入预约订单id，返回删除成功/失败

### 删除预约订单 [POST]

```
URI: /api/orders/delete-reservation
URL: http://127.0.0.1:8000/api/orders/delete-reservation
```


+ 参数说明
    + order_id: int，创建订单时得到的订单id


+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "order_id":7
            }
+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success"
            }

## 查询某个订单的详细信息   [/api/orders/get-order]
输入订单id，返回当前停车场id、车位id、停车时间、费用、状态包括预约中、停车中、订单完成、停车结束未付款

### 查询某个订单的详细信息 [GET]

```
URI: /api/orders/get-order
URL: http://127.0.0.1:8000/api/orders/get-order
```

+ 参数说明
    + order_id: int，创建订单时得到的订单id
    + created_at: 世界时订单创建时间
    + updated_at: 世界时订单最后一次更新时间
    + status: 0表示预约，1表示停车中，2表示停车结束未付款，3表示停车结束已付款
    + parkingBeginTime: 停车开始时间，用户查询车位密码后，后台会更新这个时间，如果为0则表示停车还未开始
    + parkingPlace: 车位的id，可以唯一标识一个车位
    + user: 用户的id，可以唯一标识一个用户

+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "order_id":1
            }

+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "id": 1,
                    "created_at": 1673707907,
                    "updated_at": 1673760246,
                    "format_created_at": "2023-01-15T05:24:06.499133Z",
                    "format_updated_at": "2023-01-14T14:51:47.893600Z",
                    "status": 0,
                    "parkingBeginTime": 0.0,
                    "parkingEndTime": 0.0,
                    "parkingPlace": 1,
                    "user": 1
                }
            }

## 查询某个用户的所有订单   [/api/orders/get-user-orders]
输入username，返回这个用户的所有订单。

### 查询某个用户的所有订单  [GET]

```
URI: /api/orders/get-user-orders
URL: http://127.0.0.1:8000/api/orders/get-user-orders
```


+ 参数说明
    + id: int，创建订单时得到的订单id
    + username: 注册接口中提到的username，可以唯一标识用户，字符串
    + created_at: 世界时订单创建时间
    + updated_at: 世界时订单最后一次更新时间
    + status: 0表示预约，1表示停车中，2表示停车结束未付款，3表示停车结束已付款
    + parkingBeginTime: 停车开始时间，用户查询车位密码后，后台会更新这个时间，如果为0则表示停车还未开始
    + parkingPlace: 车位的id，可以唯一标识一个车位
    + user: 用户的id，可以唯一标识一个用户

+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "username":"xxx10@xxx.com"
            }
+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "list": [
                        {
                            "id": 1,
                            "created_at": 1673707907,
                            "updated_at": 1673760246,
                            "format_created_at": "2023-01-15T05:24:06.499133Z",
                            "format_updated_at": "2023-01-14T14:51:47.893600Z",
                            "status": 0,
                            "parkingBeginTime": 0.0,
                            "parkingEndTime": 0.0,
                            "parkingPlace": 1,
                            "user": 1
                        },
                        {
                            "id": 3,
                            "created_at": 1673709771,
                            "updated_at": 1673760243,
                            "format_created_at": "2023-01-15T05:24:03.296674Z",
                            "format_updated_at": "2023-01-14T15:22:51.912090Z",
                            "status": 0,
                            "parkingBeginTime": 0.0,
                            "parkingEndTime": 0.0,
                            "parkingPlace": 1,
                            "user": 1
                        },
                        {
                            "id": 6,
                            "created_at": 1673759952,
                            "updated_at": 1673760477,
                            "format_created_at": "2023-01-15T05:27:57.669036Z",
                            "format_updated_at": "2023-01-15T05:19:12.811703Z",
                            "status": 3,
                            "parkingBeginTime": 1673760250.8984494,
                            "parkingEndTime": 1673760482.4836605,
                            "parkingPlace": 1,
                            "user": 1
                        }
                    ]
                }
            }

## 查询车位密码，并把预约订单兑现为停车订单开始计费   [api/orders/check-parking-password]
输入订单id、返回车位密码

### 查询车位密码，并把预约订单兑现为停车订单开始计费  [POST]

```
URI: api/orders/check-parking-password
URL: http://127.0.0.1:8000/api/orders/check-parking-password
```


+ 参数说明
    + order_id: int，创建订单时得到的订单id
    + parkingplace_password: 预约订单的车位的密码

+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "order_id":6
            }
+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "parkingplace_password": "123456"
                }
            }

## 将停车订单标记结束   [/api/orders/end-order]
输入停车订单id，返回停车时间、费用、订单当前状态、客户原先的余额、客户现在的余额。需要停车场有摄像头，停车场一旦发现有车走了，就会调用这个接口把这辆车的订单标记结束。或者客户申诉，也可以把订单标记结束

### 将停车订单标记结束  [POST]

```
URI: /api/orders/end-order
URL: http://127.0.0.1:8000/api/orders/end-order
```


+ 参数说明
    + order_id: order的id
    + parking_time: 停车时间，单位是秒
    + parking_money: 停车的金额，停车时间/3600后向上取整再乘以小时价格
    + status: 0表示预约，1表示停车中，2表示停车结束未付款，3表示停车结束已付款，如果这个接口返回显示2，表示支付失败，用户余额不足
    + user_money_origin: 调用接口前用户余额
    + user_money_now: 调用接口后用户余额，如果和uesr_money_origin相等，那么表示支付失败，用户余额不足
+ 请求 (application/json)
    
    + Headers
				
            AuthToken: 12345abc
    
    + Body

            {
                "order_id":1
            }
+ 响应 200 (application/json)

    + Body

            {
                "code": 200,
                "message": "success",
                "data": {
                    "parking_time": 242.31226515769958,
                    "parking_money": 1.0,
                    "order_status": 3,
                    "user_money_origin": 233.44,
                    "user_money_now": 232.44
                }
            }