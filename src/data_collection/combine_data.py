import csv
import json

# base data
with open("./data/base_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

    base_data = list([list(d) for d in reader])

# faq
with open("./data/faq.json", "r") as f:
    faq_data = f.read()

faq_data = json.loads(faq_data)
faq_data = [list(d.values()) for d in faq_data]

# add data
with open("./data/add_data.json", "r") as f:
    add_data = f.read()

add_data = json.loads(add_data)
add_data = [list(d.values()) for d in add_data]

final_data = base_data + faq_data + add_data
final_data = [[q.strip().replace("\u2019", "'"), a.strip().replace("\u2019", "'")] for q, a in final_data]

with open("./data/final_data.json", "w+", encoding="utf-8") as f:
    f.write(json.dumps(final_data, indent=4))

with open("./data/final_data.jsonl", "w+", encoding="utf-8") as f:
    for row in final_data:
        f.write(json.dumps(row))
        f.write("\n")

with open("./data/final_data.csv", "w+", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["text_input", "output"])
    writer.writerows(final_data)