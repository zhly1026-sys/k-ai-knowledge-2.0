from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_community.llms.tongyi import Tongyi
# 1. 准备示例数据
examples =[
    {"input":"高兴","output":"愉悦"},
    {"input":"快速","output":"迅猛"},
    {"input":"美丽","output":"绚丽"}
]

# 2.构建提示词模版
examples_prompt = PromptTemplate.from_template(
    "输入:{input} \n 输出:{output}"
)

# 3.创建Fewshot
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=examples_prompt,
    prefix="请根据以下示例,将输入词语转换为同义词",
    suffix="基于示例回答问题. 用户输入:{word}\n输出:",
    input_variables=["word"]
)

# 4.调用
#prompt_text = few_shot_prompt.format(word="悲伤")
prompt = few_shot_prompt.invoke(input={"word":"悲伤"})
#print(type(prompt_text))
#print(prompt_text)

llm = Tongyi(model="qwen-max")
#result = llm.invoke(input=prompt_text)
# print(result)
chain = few_shot_prompt|llm
print(chain.invoke(input={"word":"悲伤"}))