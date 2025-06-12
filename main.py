from langchain.llms import OpenAI


llm = OpenAI(
    openai_api_key= api_key
)

result = llm("Who is the best cricket batsman in the world?")
print(result)