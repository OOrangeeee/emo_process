from os import makedirs
import pandas as pd

import data_process as dp
from solve import Solver
import key
import time
import sys
import clear


def main():
    global data
    user_key = input("输入密码：")
    if user_key != key.get_key():
        clear.clear_console()
        print("密码错误，你不是柠檬头！")
        time.sleep(10)
        sys.exit()
    print("密码正确，继续程序！")
    makedirs("data", exist_ok=True)
    file_path = input("输入文件位置:")  # E:\university\宁静\知乎会员.csv
    col_do = int(input("输入分析的列编号，从左到右，从0开始编号:"))  # 7
    title = input("自己起一个文件名称:")  # 知乎
    qps = int(input("输入每秒查询次数:"))# 20
    app_id = input("输入app_id:")
    api_key = input("输入api_key:")
    secret_key = input("输入secret_key:")
    print("开始分析！")

    if file_path.endswith(".csv"):
        data = dp.read_csv_with_encoding(file_path)
    elif file_path.endswith(".xlsx"):
        data = pd.read_excel(file_path, engine="openpyxl")

    col_do = data.columns[col_do]
    df = dp.data_process(data, col_do)
    s = Solver(df, qps, app_id, api_key, secret_key)
    s.process_emo(title)
    print("分析完成！")
    time.sleep(10)

    pass


if __name__ == "__main__":
    main()
