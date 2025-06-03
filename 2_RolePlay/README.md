````md
# 🧠 CAMEL Role-Playing Agents (LangChain + OpenAI)

This project demonstrates how to simulate two AI agents—each playing a defined role—collaborating to solve a task using natural language.

Inspired by the [CAMEL framework](https://arxiv.org/abs/2303.17760), this repo implements a **role-playing architecture** using LangChain and OpenAI models, where:

- 🤖 One agent acts as a **User** (e.g. Game Designer)
- 👨‍💻 The other agent acts as an **Assistant** (e.g. Unity Developer)
- 💬 They take turns exchanging instructions and responses to **complete a shared task**.

---

## 📦 What’s Inside

- `main.py` – Runs the role-playing simulation
- `camel_agent.py` – The core agent class
- `prompts.py` – Role-based inception prompts
- `.env` – Store your OpenAI API key (you must create this)
- `requirements.txt` – List of required Python packages

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Pranav-7/AI_Agents_Implementation.git
cd 2_RolePlay
````

---

### 2. Set Up Python Environment

(Optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:

* `openai` – to access GPT models
* `langchain` and `langchain-community` – to manage agent conversations
* `python-dotenv` – to securely load your API key

---

### 4. Add Your OpenAI API Key

Create a file named `.env` in the root folder with this content:

```env
OPENAI_API_KEY=sk-xxxxx-your-key-here
```

---

### 5. Run the Simulation

```bash
python main.py
```

You’ll see a turn-by-turn conversation between:

* 🧑‍🎨 **Game Designer** – giving instructions
* 🧑‍💻 **Unity Developer** – writing solutions (e.g., Unity C# code)

Example output:

```
Unity Developer:
Solution: Here's a C# script to implement jump physics...
Next request.

Game Designer:
Instruction: Add horizontal movement with arrow keys.
Input: None
```

The session automatically stops when the user sends `<CAMEL_TASK_DONE>`.

---

## 🧠 How It Works

This project is based on the CAMEL (Communicative Agents for Mind Exploration) structure. It uses:

* **System prompts ("inception prompts")** to assign strict roles
* **Turn-based message passing** between two autonomous agents
* **OpenAI’s GPT model** as the LLM backend

Agents follow a strict format:

* 🧑‍💻 Assistant always replies with:

  ```
  Solution: <answer>
  Next request.
  ```

* 🧑‍🎨 User gives one instruction at a time:

  ```
  Instruction: <do something>
  Input: <context>
  ```

---

## 🔍 Customizing It

You can easily change:

* The task
* The agent roles
* The model temperature
* Turn limits or stop criteria

Just update values in `main.py`.

---

## 📚 References

* [CAMEL Paper (arXiv)](https://arxiv.org/abs/2303.17760)
* [LangChain Documentation](https://docs.langchain.com/)
* [OpenAI API Docs](https://platform.openai.com/docs)

---

## 🛠️ Contributing

Pull requests are welcome. Please open an issue first to discuss any major changes.

---

## ⚖️ License

MIT License

---

