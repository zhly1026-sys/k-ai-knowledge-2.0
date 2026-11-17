from langchain_community.llms.tongyi import Tongyi

# 1.创建模型客户端
llm = Tongyi(model="qwen-max")

# 2.调用模型
result = llm.stream(input="你是谁")

# 3.处理输出
for chunk in result:
    print(chunk,end="")
