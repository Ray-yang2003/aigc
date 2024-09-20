import json
import os
import run


# 读取JSON文件
def load_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 加载文本并提取需要分析的字段
def extract_texts_from_json(data):
    texts = []
    for entry in data:
        if 'text' in entry:
            texts.append(entry['text'])
    return texts

# 运行代码的方法：
def run_text_analysis(texts):
    span_length = 10
    pct = 0.1  # 例如，扰动10%的单词
    n_perturbations = 5  # 设置每个文本扰动5次
    n_samples = len(texts)

    # 生成扰动文本
    perturbed_texts = perturb_texts(texts, span_length, pct)

    # 计算原始文本与扰动文本的对数似然
    original_lls = get_lls(texts)
    perturbed_lls = get_lls(perturbed_texts)

    # 返回对数似然结果
    return {
        "original_lls": original_lls,
        "perturbed_lls": perturbed_lls
    }


if __name__ == "__main__":
    file_path = '/mnt/data/“但书”出罪运行机制实证研究_夏伟_改写.json'  # JSON文件路径
    data = load_json_file(file_path)

    # 提取JSON中的文本内容
    texts = extract_texts_from_json(data)
    
    # 执行扰动与对数似然分析
    results = run_text_analysis(texts)

    # 输出分析结果
    print("原始文本的对数似然值:", results["original_lls"])
    print("扰动文本的对数似然值:", results["perturbed_lls"])
