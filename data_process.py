import pandas as pd


def read_csv_with_encoding(filename):
    encodings = [
        "utf-8",
        "gbk",
        "ascii",
        "latin1",
        "cp1252",
        "ISO-8859-1",
    ]

    for encoding in encodings:
        try:
            return pd.read_csv(filename, encoding=encoding)
        except UnicodeDecodeError:
            print(f"尝试使用 {encoding} 编码读取失败，尝试下一种编码。")

    raise ValueError("无法确定文件的编码，所有尝试的编码都失败了。")


def data_process(df, col_do):
    ans = df[col_do].copy()
    ans = ans.to_frame(name="data")
    return ans
