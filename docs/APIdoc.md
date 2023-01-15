
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

## 查看某个停车场详细信息   [/api/users/add-money]
显示停车场名称、简介、所有车位编号、剩余车位数量

### 查看某个停车场详细信息 [POST]

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

## 查看坐标区域内的所有停车场   [/api/users/add-money]
输入坐标区域，显示区域内所有停车场的id，名称，剩余车位

### 查看坐标区域内的所有停车场 [POST]

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

# 订单

## 创建预约订单   [/api/users/add-money]
创建车位预约订单，输入用户名、停车场id；返回订单id，停车场id，车位id，车位标识符。

### 创建预约订单 [POST]

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


## 删除预约订单   [/api/users/add-money]
输入预约订单id，返回删除成功/失败

### 删除预约订单 [POST]

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

## 查询某个订单的详细信息   [/api/users/add-money]
输入订单id，返回当前停车场id、车位id、停车时间、费用、状态包括预约中、停车中、订单完成、停车结束未付款

### 查询某个订单的详细信息 [POST]

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

## 查询某个用户的所有订单   [/api/users/add-money]
输入username，返回这个用户的所有订单。

### 查询某个用户的所有订单  [POST]

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

## 查询车位密码，并把预约订单兑现为停车订单开始计费   [/api/users/add-money]
输入订单id、返回车位密码

### 查询车位密码，并把预约订单兑现为停车订单开始计费  [POST]

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

## 将停车订单标记结束   [/api/users/add-money]
输入停车订单id，返回停车时间、费用、费用是否充足。这个需要停车场有摄像头，停车场一旦发现有车走了，就会把这辆车的订单标记结束。

### 将停车订单标记结束  [POST]

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