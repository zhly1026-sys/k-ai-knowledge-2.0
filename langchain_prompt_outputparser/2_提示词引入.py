from langchain_community.llms.tongyi import Tongyi

# 1.创建模型客户端
llm = Tongyi(model="qwen-max")
# 2. 调用模型
#user_query1= "请简单介绍机器学习"
#user_query2="请从以下几个方面介绍机器学习"
user_query ="假设你是一个{expert}专家,请你解释一下{content}是什么".format(expert ="AI",content ="Langgraph")
result = llm.stream(input=user_query)

# 处理输出
for chunk in result:
    print(chunk, end='', flush=True)