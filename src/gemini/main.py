import csv

import os
import google.generativeai as genai

genai.configure(api_key=os.environ["API_KEY"])

model = genai.GenerativeModel("gemini-1.5-pro")

base_model = [m for m in genai.list_models() if "createTunedModel" in m.supported_generation_methods][0]

with open("./data/base_data.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)

training_data = [{"text_input": a, "output": b} for a, b in reader]

name = "generate-num-1"
operation = genai.create_tuned_model(
    source_model=base_model.name,
    training_data=training_data,
    id = name,
    epoch_count = 100,
    batch_size = 4,
    learning_rate = 0.001,
)

