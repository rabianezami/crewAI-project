# CrewAI Beginner AI Topics Pipeline

This is a small **CrewAI learning project** that shows how multiple AI agents can work together through clear roles and tasks.

The goal is simple: simulate a realistic content workflow where agents research, write, and edit beginner‑friendly AI topics.

---

## What This Project Does

The pipeline includes three agents:

* **Beginner AI Research Analyst** : finds exactly three recent and practical AI topics suitable for beginners.
* **Technical Content Writer** : explains those topics in a clear, beginner‑friendly way.
* **Content Editor** : improves clarity and tone without changing the meaning.

Agents can delegate work to each other, similar to a real team.

---

## Project Structure

```
crewAI/
├── agents/
├── tasks/
├── tools/
├── config/
├── output/
├── main.py
├── requirements.txt
└── README.md
```

---

## How to Run

````bash
python -m venv venv
venv\Scripts\activate  # Windows

source venv/bin/activate  # Linux / Mac

pip install -r requirements.txt
python main.py
```bash
pip install -r requirements.txt
python main.py
````

---

## Debug Mode

During development, debug mode was used to inspect task outputs and agent behavior.

Debug files and logs are **not included** in this repository to keep it clean and focused on the core logic.

---

## Author

**Rabia Zia Nezami**


