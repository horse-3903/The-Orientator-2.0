<div align="center">

# The Orientator 2.0

A Gemini-powered web chatbot that helps Hwa Chong Institution (HCI) freshmen navigate school life

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev/)
[![License](https://img.shields.io/github/license/horse-3903/The-Orientator-2.0?style=flat-square)](LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/horse-3903/The-Orientator-2.0?style=flat-square)](../../commits)

</div>

---

## Overview

The Orientator 2.0 is a web-based chatbot application built with Flask and powered by a fine-tuned Google Gemini model. It is designed to answer HCI-specific questions, assist freshmen in understanding school culture and traditions, and provide guidance on navigating life at Hwa Chong Institution. This is the successor to [The Orientator PW 2023](https://github.com/horse-3903/The-Orientator-PW-2023), featuring a significantly upgraded AI backend and a full web interface with an interactive campus map.

## Features

- **Fine-tuned Gemini model** — uses a custom-tuned Gemini model trained on HCI-specific Q&A data for accurate, school-relevant responses
- **Web chat interface** — clean browser-based UI for sending messages and receiving responses
- **Interactive campus map** — dedicated map route for exploring the school grounds
- **Multi-model support** — dynamically lists and selects from available fine-tuned models
- **Configurable generation** — supports generation parameters (temperature, top-p, top-k, max tokens, stop sequences)
- **Light/dark mode** — user mode preference stored in session

## Tech Stack

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)

## Getting Started

### Prerequisites

- Python 3.10+
- A Google AI / Gemini API key with access to tuned models
- A fine-tuned Gemini model trained on HCI Q&A data (see `data/` and `src/model/train_model.ipynb`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/horse-3903/The-Orientator-2.0.git
   cd The-Orientator-2.0
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   > All other required files will be automatically installed on first run.

3. Create the environment file at `src/.env`:
   ```env
   PARENT_DIR=<full path to The-Orientator-2.0/ folder>
   GOOGLE_API_KEY=<your Gemini API key>
   ```

### Usage

Run the Flask application:
```bash
python src/app/app.py
```

Then open your browser and navigate to `http://localhost:5000`.

#### Available Routes

| Route | Description |
|-------|-------------|
| `/` | Home / landing page |
| `/app` | Main chatbot interface |
| `/map` | Interactive campus map |

#### Training the Model

To train or retrain the fine-tuned Gemini model:
1. Ensure `src/data/base_data.csv` exists with Q&A pairs
2. Run data augmentation: `python src/data_collection/augment_data.py`
3. Open and execute `src/model/train_model.ipynb`

## Project Structure

```
The-Orientator-2.0/
├── src/
│   ├── app/
│   │   ├── app.py              # Flask application entry point
│   │   ├── static/             # CSS, JS, and assets
│   │   └── templates/          # Jinja2 HTML templates
│   ├── gemini/
│   │   └── load_creds.py       # Gemini API credential loader
│   └── data_collection/        # Data augmentation and scraping scripts
├── data/
│   ├── base_data.csv           # Original HCI Q&A dataset (~81 rows)
│   ├── augmented_data.csv      # Augmented dataset (~6.7M rows)
│   └── processed_data.csv      # Final training dataset (~2000 rows)
└── test/                       # Model testing scripts
```

## License

This project is licensed under the [MIT License](LICENSE).
