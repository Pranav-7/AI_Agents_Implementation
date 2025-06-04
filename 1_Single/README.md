````markdown
# 🧠 AI Code Reviewer (Single-Agent)

This project implements a single AI agent that reviews Python code and provides detailed feedback using the CAMEL-AI framework.

## 🚀 Features

- Detects bugs, security issues, and performance problems
- Checks for coding standards and best practices
- Suggests improvements for readability and maintainability
- Rates code quality (1–10) with reasoning

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Pranav-7/AI_Agents_Implementation.git
cd 1_Single
````

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a `.env` file in the project root with the following line:

```env
OPENAI_API_KEY=your-openai-api-key-here
```

Replace `your-openai-api-key-here` with your actual OpenAI API key.

---

## ▶️ How to Run

```bash
python main.py
```

You’ll see a review of the sample code printed in your terminal.

---

## 📁 Project Structure

```
reviewer_agent.py    # Agent definition and system message
main.py              # Entry point for running the review
requirements.txt     # Project dependencies
.env                 # Environment file (not committed)
```

---

## ❗ Notes

* The `.env` file is required to authenticate with OpenAI's API.
* Make sure you are using a model compatible with the `CAMEL-AI` framework, such as GPT-4 or GPT-4o.

---


