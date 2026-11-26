# 先只放一个真正常用的 JSON 结构校验工具。
# 不要为了“目录完整”硬塞一堆没用的工具。

from __future__ import annotations
import jsonschema

def assert_json_schema(data, schema, ignore_missing: list = None):
    ignore = set(ignore_missing or [])
    # 简单实现：校验前从 schema 的 required 中剔除忽略项（针对顶层/已知路径）
    if "required" in schema:
        schema["required"] = [f for f in schema["required"] if f not in ignore]
    jsonschema.validate(instance=data, schema=schema)