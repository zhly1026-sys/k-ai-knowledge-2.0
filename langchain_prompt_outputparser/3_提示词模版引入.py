from langchain_community.llms.tongyi import Tongyi
from langchain_core.prompts import PromptTemplatep

llms = Tongyi(model="qwen-max")

prompt_template = PromptTemplatep.from_template(
    "假设你是一个{expert}专家,请你解释一下{content}是什么"
)
prompt = prompt_template.format(expert="AI",content ="langgrah")

result = llms.stream(input = prompt)

for chunk in result:
    print(chunk,end='',flush=True)