from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("请解释一下{concept}的概念")
llm = ChatTongyi(model ="qwen-max",streaming =True)

parser = StrOutputParser()
chain = prompt|llm|parser
res = chain.invoke(input={"concept":"机器学习"})
print(type(res))
print(res)