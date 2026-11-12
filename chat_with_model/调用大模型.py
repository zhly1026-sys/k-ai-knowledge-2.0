import os

from openai import OpenAI

# API Key 只从环境变量读，不写进代码（避免被 git 提交泄露）
API_KEY = os.getenv("DASHSCOPE_API_KEY")
if not API_KEY:
    raise SystemExit('未找到 DASHSCOPE_API_KEY，请先执行：setx DASHSCOPE_API_KEY "sk-你的key"')
# 1. 创建客户端对象
client = OpenAI(
    api_key=API_KEY,
    # 百炼（DashScope）OpenAI 兼容模式地址
    # 若用的是 MaaS 专属空间，则改成：https://<你的WorkspaceId>.cn-beijing.maas.aliyuncs.com/compatible-mode/v1
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 2. 调用模型
completion = client.chat.completions.create(
    # 可用模型：qwen-plus / qwen-turbo / qwen-max / qwen3-max
    model="qwen-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁？"},
    ],
)
# 3.打印输出
print(completion.model_dump_json())
print(completion.choices[0].message.content)