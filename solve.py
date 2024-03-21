from re import search
from aip import AipNlp
from time import sleep


class Solver:
    def __init__(self, df, q, a1, a2, a3):
        self.df_clean = df
        self.get_api(q, a1, a2, a3)
        pass

    def analyse_word(self, s):
        """
        分析情感
        :param s:
        :return:
        """
        sleep(self.QPS)
        result = self.client.sentimentClassify(s)  # 调用api
        return result

    def save_emotion(self, title):
        """
        生成情感分析文件
        :return: 无
        """
        emo_df = self.df_clean
        emo_df["emo"] = emo_df["data"].apply(self.analyse_word)
        path = "data/" + title + "情感分析.xlsx"
        emo_df.to_excel(path, index=False)

    def is_items(self, s):
        """
        清洗错误数据
        :param s: 文本
        :return: 是否正确
        """
        return "items" in s

    def get_sentiment(self, s):
        """
        获取倾向
        :param s:结论
        :return: 倾向
        """
        match = search(r"'sentiment': (\d+)", s)
        return int(match.group(1)) if match else None

    def get_api(self, q, a1, a2, a3):
        """
        获取api
        :param q: 每秒请求数
        :param a1: 百度api_key
        :param a2: 百度api_secret
        :param a3: 百度api_id
        :return: 无
        """
        self.client = AipNlp(a3, a1, a2)
        QPS = int(q)
        if QPS >= 20:
            self.QPS = 0
        else:
            self.QPS = 1.0 / QPS
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

    def process_emo(self, title):
        """
        分析情感
        :param title: 分析模式
        :return: 无
        """
        app_id = self.a1
        api_key = self.a2
        secret_key = self.a3
        self.client = AipNlp(app_id, api_key, secret_key)
        self.save_emotion(title)
        # path = "./用户数据/data/" + title + "情感分析.xlsx"
        # emo_df = pd.read_excel(path)
        # emo_df = emo_df[emo_df["emo"].apply(self.is_items)]
        # emo_df["emo_rank"] = emo_df["emo"].apply(self.get_sentiment)
        # emo_rank_counts = (
        #     emo_df.groupby("emo_rank").size().reindex(range(0, 3), fill_value=0)
        # )
        # emo_rank_counts = emo_rank_counts.to_frame()
        # emo_rank_counts = emo_rank_counts.reset_index()
        # emo_rank_counts.columns = ["rank", "counts"]
        # emo_rank_counts.sort_values(by="rank")
