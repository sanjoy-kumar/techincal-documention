# 📚 Personal Prompt Library (Sanjoy Kumar)

A reusable, real‑world prompt collection tailored for **Backend, SQL, React, Python, and GenAI development**. Copy, adapt, and iterate.

---

## 🧠 MASTER PROMPT FORMULA
```
Role + Context + Task + Constraints + Output Format
```

---

## 🗄️ SQL PROMPTS (MySQL 5.7)

### 1️⃣ Write Query
```
Act as a MySQL 5.7 expert.
Task: Write a SQL query to <goal>.
Constraints:
- Use indexes
- Avoid subqueries if possible
Output format:
- SQL query
- Short explanation
```

### 2️⃣ Debug Query Error
```
Act as a database administrator.
Task: Debug and fix this SQL query:
<PASTE QUERY>
Output format:
- Error cause
- Corrected query
```

### 3️⃣ Optimize Slow Query
```
Act as a database performance engineer.
Context: Table has millions of rows.
Task: Optimize this query:
<QUERY>
Output format:
- Optimized SQL
- Index suggestions
```

---

## ⚛️ REACT PROMPTS (React 18 + MUI v5)

### 4️⃣ Create Component
```
Act as a senior React developer.
Task: Create a reusable <component name>.
Constraints:
- Functional component
- Hooks only
- MUI v5
Output format:
- Full component code
- Usage example
```

### 5️⃣ Fix React Bug
```
Act as a React debugging expert.
Error:
<ERROR MESSAGE>
Code:
<CODE>
Output format:
- Root cause
- Fixed code snippet
```

### 6️⃣ Improve Performance
```
Act as a React performance engineer.
Task: Optimize this component to avoid re-renders:
<CODE>
Output format:
- Explanation
- Optimized code
```

---

## 🐍 PYTHON PROMPTS (Python 3.11)

### 7️⃣ Write Script
```
Act as a Python 3.11 expert.
Task: Write a script to <goal>.
Constraints:
- Clean code
- Exception handling
Output format:
- Complete script
- Example usage
```

### 8️⃣ Debug Python Error
```
Act as a Python debugging expert.
Traceback:
<TRACEBACK>
Code:
<CODE>
Output format:
- Error explanation
- Fixed code
```

### 9️⃣ Optimize Python Code
```
Act as a Python performance engineer.
Task: Optimize this code:
<CODE>
Constraints:
- No external libraries
Output format:
- Optimized code
- Reasoning
```

---

## 🌐 BACKEND / API PROMPTS (FastAPI / Flask)

### 🔟 Design API Endpoint
```
Act as a backend architect.
Task: Design a REST API endpoint for <feature>.
Constraints:
- REST standards
- Secure
Output format:
- Endpoint
- Request/Response JSON
- Status codes
```

### 1️⃣1️⃣ Debug API Issue
```
Act as a backend debugging expert.
Issue:
<ERROR / BEHAVIOR>
Code:
<CODE>
Output format:
- Root cause
- Fix
```

---

## 🤖 GENAI / LLM PROMPTS

### 1️⃣2️⃣ System Prompt (Chatbot)
```
You are a helpful technical assistant.
Rules:
- Be concise and accurate
- Do not hallucinate
- Say "I don't know" if unsure
```

### 1️⃣3️⃣ RAG Prompt
```
You are a document-based assistant.
Context:
{retrieved_docs}
Task:
Answer the user's question using ONLY the context.
If not found, say "Not available in documents".
```

### 1️⃣4️⃣ Tool-Using Agent Prompt
```
You are an AI agent.
Available tools:
- search()
- database()
- send_email()
Rules:
- Explain before using a tool
- Choose the correct tool
```

---

## 🧪 TESTING & QUALITY PROMPTS

### 1️⃣5️⃣ Write Test Cases
```
Act as a QA engineer.
Task: Write unit test cases for this function:
<CODE>
Output format:
- Test cases
- Edge cases
```

---

## 🔁 PROMPT REFINEMENT SHORTCUTS
Use anytime:
```
Make it production-ready
Add edge cases
Explain for beginners
Rewrite for interview
Simplify
```

---

## ⭐ HOW TO USE THIS LIBRARY
1. Pick the closest template
2. Replace placeholders
3. Run
4. Refine with follow-ups

---

🚀 This library is designed for daily professional development work.

