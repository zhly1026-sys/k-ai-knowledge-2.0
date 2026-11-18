from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_community.llms.tongyi import Tongyi


chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system","假设你现在是一个{expert}专家"),
    MessagesPlaceholder("history"),
    ("human","请你解释一下{content}是什么")

])
chat_history=[
    ("human","什么是langgraph"),
    ("ai","LangGraph是一种结合了自然语言处理（NLP）与图数据结构的技术框架或方法论，它利用图数据库来存储和查询信息，并通过自然语言处理技术使得用户能够以更加自然的方式与这些数据进行交互")
]
prompt = chat_prompt_template.format(expert="AI",content="Langgraph",history=chat_history)
print(type(prompt))
print(prompt)
#prompt = chat_prompt_template.invoke(input={"expert":"AI","content":"Langgraph"})
#print(type(prompt))
# print(prompt)
