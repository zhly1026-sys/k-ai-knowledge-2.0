from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms.tongyi import Tongyi


chat_prompt_template = ChatPromptTemplate.from_messages([
    ("system","假设你现在是一个{expert}专家"),

    ("human","请你解释一下{content}是什么")

])
#prompt = chat_prompt_template.format(expert="AI",content="Langgraph")
#print(type(prompt))
#print(prompt)
#prompt = chat_prompt_template.invoke(input={"expert":"AI","content":"Langgraph"})
#print(type(prompt))
# print(prompt)
llm = Tongyi(model="qwen-max")
chain = chat_prompt_template |llm
result = chain.stream(input={"expert":"AI","content":"Langgraph"})
for chunk in result:
    print(chunk,end='',flush=True)