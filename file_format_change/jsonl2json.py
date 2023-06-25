import io
import json

path1 = 'your_jsonl_file_path.jsonl'
# 读取 JSONL 文件
jsonl_file = path1
json_data = []
with io.open(jsonl_file, "r", encoding="utf-8") as f:
    for line in f:
        # 解析 JSONL 行并转换为 JSON 对象
        json_data.append(json.loads(line))

# 存储为 JSON 文件
json_file = "your_target_json_file_output_path.json"
with io.open(json_file, "w", encoding="utf-8") as f:
    json.dump(json_data, f, ensure_ascii=False, indent=4)