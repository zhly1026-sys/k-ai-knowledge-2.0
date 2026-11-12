from openai import OpenAI
# 1. 创建客户端对象
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"

)
# 2. 第一次调用 :告诉模型用户身份
completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {"role":"user","content":"你好,我是浩亮,我是一位研究生"}
    ]
)
print(completion.choices[0].message.content)
# 2. 第一次调用 :告诉模型我是谁
completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {"role":"user","content":"我是谁?"}
    ]
)
print("第2次调用")
print(completion.choices[0].message.content)