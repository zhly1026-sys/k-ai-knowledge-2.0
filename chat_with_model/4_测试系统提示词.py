from openai import  OpenAI
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"

)
# 2. 第一次调用 :告诉模型用户身份
completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {"role":"system","content":"背景设定:你现在是一个ai老师,负责上ai课程"},
        {"role":"user","content":"你是谁"}
    ]
)
print(completion.choices[0].message.content)