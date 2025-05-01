import json
import ast

# 输入文件路径（必须存在）
input_path = r'D:\movies.csv'  # 使用原始字符串避免转义问题

# 输出文件路径（自动生成）
output_path = r'D:\movies_fxed.json'

with open(input_path, 'r', encoding='utf-8') as f:
    data = [ast.literal_eval(line) for line in f]

with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)