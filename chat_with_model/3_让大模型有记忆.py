from openai import  OpenAI
client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"

)
chat_history = []
user_message_1="你好,我是啊怨,是一名研究生"
chat_history.append({"role":"user","content":user_message_1})
completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages = chat_history
)

chat_history.append({"role": "assistant","content":completion.choices[0].message.content})

# 4 第二次调用:询问模型 我是谁
user_message_2 = "我是谁?"
chat_history =chat_history + [{"role":"user","content":user_message_2}]


completion = client.chat.completions.create(
    model="qwen3.8-max",
    messages = chat_history
)
print(completion.choices[0].message.content)