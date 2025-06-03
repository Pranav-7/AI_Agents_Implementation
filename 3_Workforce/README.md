# CAMEL-Powered Adaptive Learning Assistant — Hackathon Evaluation

## Overview

This repository contains the code for evaluating a hackathon project using the **CAMEL** multi-agent framework. The evaluation involves multiple AI judges with different personas assessing the project on various criteria.

The project being evaluated is the **CAMEL-Powered Adaptive Learning Assistant**, which aims to provide personalized education through adaptive AI.

---

## Repository Contents

* `main.py` — Main Python script implementing the workforce agents and running the evaluation task.
* `.env` — Environment variables file (should contain your API keys; **do NOT commit this file to GitHub**).
* `requirements.txt` — List of Python dependencies.
* `README.md` — This documentation.

---

## Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/Pranav-7/AI_Agents_Implementation.git
   cd 3_Workforce
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root folder and add your API keys:

   ```ini
   OPENAI_API_KEY=your_openai_api_key
   GOOGLE_API_KEY=your_google_api_key
   SEARCH_ENGINE_ID=your_search_engine_id
   ```

---

## Usage

Run the evaluation script:

```bash
python main.py
```

The script will run the multi-agent evaluation process, outputting the scores and feedback from different judge personas, along with a final summary.

---

## Notes

* This code uses async features that may cause issues in notebook environments like Google Colab or Jupyter due to event loop conflicts.
* It is recommended to run this script in a standard Python environment (local machine, remote server, or IDE terminal).
* Make sure you have valid API keys and that your environment variables are correctly set.

---

## About CAMEL

CAMEL is an open-source multi-agent framework designed to enable complex AI agent collaboration and workflows.

---
## 🛠️ Contributing

Pull requests are welcome. Please open an issue first to discuss any major changes.

---

## ⚖️ License

MIT License

---
