import datetime
import base64


# 定义一个函数，根据传入的密钥生成密码
def generate_password(secret_key):
    # 获取当前日期，并格式化
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    # 将密钥和当前日期拼接
    password = secret_key + current_date
    # 将拼接后的字符串进行base64编码
    encoded_message = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    # 返回编码后的字符串
    return encoded_message


# 定义一个函数，获取密钥
def get_key():
    # 定义一个密钥列表
    secret_key = ["bsbflsgxh..", "Jin13389791067"]
    # 获取当前日期
    today = datetime.datetime.now().date()
    # 获取当前日期的天数
    day = today.day
    # 如果天数是偶数，则取密钥列表中的第一个元素
    if day % 2 == 0:
        key = secret_key[0]
    # 否则取密钥列表中的第二个元素
    else:
        key = secret_key[1]
    # 根据密钥生成密码
    current_password = generate_password(key)
    # 返回密码
    return current_password
