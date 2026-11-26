# class WeatherApi:
#     def query(self, city, future_num=1):
#         """只负责拿响应，不做任何断言"""
#         return {
#             "resultcode": "200",
#             "result": {
#                 "city": city,
#                 "future": [
#                     {"date": f"2026-11-2{i}", "weather": "晴", "temperature": "18℃~26℃"}
#                     for i in range(1, future_num + 1)
#                 ],
#             },
#         }


import os
import configparser
import requests


class WeatherApi:
    def __init__(self):
        # 修正路径：weather_autotest/api -> 退3次到根目录 pyone/
        current_file = os.path.abspath(__file__)
        api_dir = os.path.dirname(current_file)
        autotest_dir = os.path.dirname(api_dir)
        root_dir = os.path.dirname(autotest_dir)

        ini_path = os.path.join(root_dir, "pytest.ini")

        # 调试打印（跑通后可删掉）
        print(f"[DEBUG] 读取配置: {ini_path}, 文件存在: {os.path.exists(ini_path)}")

        parser = configparser.ConfigParser()
        parser.read(ini_path, encoding="utf-8")

        # 读取 [api_test]
        self.base_url = parser.get("api_test", "base_url")
        self.api_key = parser.get("api_test", "api_key")
        self.timeout = parser.getint("api_test", "timeout")

    def query(self, city, future_num=1):
        params = {"city": city, "key": self.api_key}
        resp = requests.get(self.base_url, params=params, timeout=self.timeout)
        data = resp.json()
        return data

