from tqdm import tqdm

import json

import requests
from bs4 import BeautifulSoup

url = "https://www.admissions.hci.edu.sg/faqs"

qnas_lst = []

def extract_questions(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    questions_and_answers = []
    current_question = None
    current_answer = ""

    for element in soup.find_all(["h4", "p"]):
        if element.name == "h4":
            if current_question:
                questions_and_answers.append({"question": current_question.strip(), "answer": current_answer.strip()})
            
            current_question = element.text.strip().lstrip(". ")
            current_question = current_question.lstrip(str(element.text.strip().split()[0]))
            current_answer = ""

        elif element.name == "p":
            current_answer += element.text.strip() + "\n"

    if current_question:
        questions_and_answers.append({"question": current_question.strip(), "answer": current_answer.strip()})

    return questions_and_answers

for idx in tqdm(range(6)):
    cur_url = url

    if idx != 0:
        cur_url += f"-pg{idx+1}"

    r = requests.get(cur_url)

    qnas = extract_questions(r.text)

    qnas_lst += qnas

with open("data/faq.json", "w+") as f:
    f.write(json.dumps(qnas_lst, indent=4))