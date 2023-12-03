from openai import OpenAI

api_key=input("Kindly insert your API key: \n")

client = OpenAI(api_key=api_key)

SysPersonalization=input("Kindly define how would you like your assistant to be ?\n")

Conversation=[
    {"role":"system",
     "content":SysPersonalization},
    ]

print("Start your conversation and if you want to end it type 0 \n")
while True:
    print("User: ")
    userMessage=input()
    if userMessage=="0":
        break
    user_dict ={"role":"user","content":userMessage}
    Conversation.append(user_dict)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=Conversation
    )
    assistantResponse_dict=response.dict()["choices"][0]["message"]
    assistant_dict = {"role":assistantResponse_dict["role"],'content':assistantResponse_dict["content"]}
    Conversation.append(assistant_dict)
    print("\nAssistant: \n", assistant_dict["content"],"\n")

