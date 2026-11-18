from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplate
# 1. 准备提示词模版
prompt_template =PromptTemplate.from_template(
    "假设你是一个{expert}专家,请你解释一下{content}是什么"
)
# 2.创建客户端
llm = Tongyi(model ="qwen-max")

# 3.组装chain(lcel表达式)
chain = prompt_template | llm  # 前一个组件的输出 是后一个组件的输入
# 4.调用模型
result = chain.stream(input= {"expert":"ai","content":"Langgraph"})
# 5.处理输出
for chunk in result:
    print(chunk,end='',flush=True)