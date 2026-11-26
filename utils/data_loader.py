import os
import yaml


def load_yaml_data(filename):
    """基于项目根目录，统一加载 data 目录下的 yaml 文件"""
    # 自动向上定位到项目根（weather_autotest），再进 data
    _BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    yaml_path = os.path.join(_BASE_DIR, "data", filename)
    yaml_path = os.path.normpath(yaml_path)

    with open(yaml_path, encoding="utf-8") as f:
        return yaml.safe_load(f)


