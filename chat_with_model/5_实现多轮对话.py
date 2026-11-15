from openai import OpenAI


class MultiTurnChat:
    def __init__(self, base_url:str,model:str,system_prompt:str=None):
        self.client = OpenAI(base_url=base_url)
        self.model = model
        self.chat_history = []

        # 若提供了系统提示词,则将其添加至对话历史起始位置
        if system_prompt:
            self.chat_history.append({"role":"system","content":system_prompt})
    def add_user_message(self,content:str)->None:
        self.chat_history.append({"role":"user","content":content})
    def send(self,user_message: str)->str:
        """"发送消息"""""
        # 1.添加用户消息到历史
        self.add_user_message(user_message)
        # 2.调用模型
        completion = self.client.chat.completions.create(model=self.model,messages=self.chat_history)
        # 3.提取模型的回复结果
        reply = completion.choices[0].message.content
        # 4.添加模型的回复到历史
        self.add_user_message(reply)
        return reply
if __name__ == '__main__':
    base_url = "https://dashscope.aliyuncs.com/compatible-mode/v1"
    MODEL = "qwen3.8-max"
    SYSTEM_MESSAGE = "背景设定: 你现在是一个AI老师,负责上AI课程"

    #创建多轮对话对象
    chat = MultiTurnChat(base_url= base_url,model=MODEL,system_prompt=SYSTEM_MESSAGE)
    print("多轮对话已启动,输入内容后按回车发送. 输入'exit'或'quit'退出程序 \n")
    while True:
        # 获取用户输入
        user_input = input("用户:")
        # 退出条件判断
        if user_input in ["exit","quit"]:
            print("对话结束!拜拜")
            break
        if not user_input.strip():
            print("请勿输入空白字符")
            continue
        reply = chat.send(user_input)
        print(f"AI老师:{reply}")