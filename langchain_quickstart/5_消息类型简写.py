from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage

# 1.创建客户端
llm = ChatTongyi(model="qwen-max",streaming=True)

# 2.准备上下文
chat_history = [
    ("system","背景设定:你现在是一个ai老师,负责上ai课程"),
    ("human","你是谁?")

]
result = llm.stream(input=chat_history)

print(type(result))
for message in result:
    print(message.content,end="")
