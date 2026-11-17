from langchain_community.chat_models import ChatTongyi

import dashscope

class MultiTurnChat:
    def __init__(self,model:str,system_prompt:str=None) -> None:
        self.llm = ChatTongyi(
            model=model,
            streaming =True
        )

        self.history = []
        if system_prompt:
            self.history.append(("system",system_prompt))
    def add_user_message(self,content:str) -> None:
        self.history.append(("human",content))
    def add_ai_message(self,content:str) -> None:
        self.history.append(("ai",content))
    def send(self,message:str) :
        # 1.添加用户消息到历史
        self.add_user_message(message)
        # 2.直接使用history 调用模型进行流式输出
        stream = self.llm.stream(input=self.history)
        # 3.收集完整回复并逐块返回
        full_reply = ""
        for chunk in stream:
            if chunk.content:
                full_reply += chunk.content
                yield chunk.content
        # 4.添加模型的完整回复到历史
        self.add_ai_message(full_reply)
if __name__ == '__main__':
    #1.配置参数
    MODEL = "qwen-max"
    SYSTEM_MESSAGE = " 背景设定: 你现在是一个ai老师,负责上AI课程"
    #2.创建多轮对话对象
    chat = MultiTurnChat(MODEL,SYSTEM_MESSAGE)
    print("多轮对话已启动,输入内容按回车发送,输入'exit'或'quit'退出程序")
    #3.循环接受用户输入并且回答
    while True:
        # 获取用户输入
        user_input = input('human:')
        # 退出条件判断
        if user_input.strip() in ['exit','quit']:
            print("对话结束,拜拜")
            break
        if not user_input.strip():
            print("请勿输入空白字符")
            continue
        print("ai老师:",end='',flush=True)
        for chunk in chat.send(user_input):
            print(chunk,end='',flush=True)
        print()