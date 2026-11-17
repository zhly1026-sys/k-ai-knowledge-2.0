from langchain_community.embeddings import DashScopeEmbeddings

# 1. 创建嵌入模型对象
embeddings = DashScopeEmbeddings()
# 2. 文本向量化
text = "我是傻逼"
vector = embeddings.embed_query(text)

# 3. 处理输出
print(vector)
print(len(vector))

# 2.文本向量化
texts = ["你好,啊苑","阿苑你真好","阿苑你太好了"]
vector = embeddings.embed_documents(texts)
print(vector)