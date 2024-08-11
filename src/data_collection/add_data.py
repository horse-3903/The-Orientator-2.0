import json

qnas_lst = []

with open("./data/add_data.txt", "r", encoding="utf-8") as f:
    data = f.read()

data = data.splitlines()

for i in range(0, len(data)-1, 2):
    question = data[i].lstrip("Q: ")
    answer = data[i+1].lstrip("A: ")

    qnas_lst.append({"question": question, "answer": answer})

with open("data/add_data.json", "w+") as f:
    f.write(json.dumps(qnas_lst, indent=4))