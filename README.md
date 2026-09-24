# 🚀 Student Budget Planner AI

[![Built with AWS PartyRock](https://img.shields.io/badge/Built%20with-AWS%20PartyRock-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)]()
[![Prompt Engineering](https://img.shields.io/badge/Skill-Prompt_Engineering-412991?style=for-the-badge)]()

**Student Budget Planner AI** is a lightweight, beginner-friendly financial tool designed specifically for university and college students. Built using AWS PartyRock, the app takes user inputs (in Malaysian Ringgit - RM) and uses generative AI to analyze spending habits, calculate daily/weekly limits, and act as a personalized financial assistant.

### 🔗 [Live Demo: Try the App on PartyRock Here](https://partyrock.aws/u/JimmyNeutron/L1vaUmhJQ/Student-Budget-Planner-for-Malaysian-Students)

---

## 📸 App Preview
<img width="1319" height="816" alt="image" src="https://github.com/user-attachments/assets/3632be3d-34ff-4203-b9f7-ace1b9f5cc36" />
<img width="1208" height="709" alt="image" src="https://github.com/user-attachments/assets/390102f5-0090-4f05-ad6c-4ab7a8bbecba" />
<img width="1205" height="700" alt="image" src="https://github.com/user-attachments/assets/740db941-de60-4cbe-80e6-71172e0facf6" />
<img width="1205" height="696" alt="image" src="https://github.com/user-attachments/assets/be13c72d-bc95-495f-b7ae-a0cf174051cc" />
<img width="1206" height="697" alt="image" src="https://github.com/user-attachments/assets/9e36332d-0ac6-458d-9669-8e33745be168" />




## 🎯 Problem Statement
University students often struggle with managing monthly allowances, overspending on non-essentials, and tracking their finances. Traditional budgeting apps can feel overwhelming. This app solves that by using AI to translate raw numbers into simple, conversational insights, actionable tips, and an interactive chat assistant.

*Disclaimer: This application is for educational and personal budgeting purposes only, not professional financial advice.*

---

## 💡 System Architecture & Prompt Engineering
Since this application was built without traditional code using AWS PartyRock, the core logic relies on **advanced prompt engineering** and **widget chaining**. Here is how the AI pipeline is structured:

### 1. Data Collection (User Input)
The app features a clean interface that collects standard student financial metrics (in RM):
* Monthly Income/Allowance & Savings Goal
* Fixed & Variable Expenses (Accommodation, Food, Transport, Phone/Internet, Education, Entertainment, Shopping, Other)

### 2. Budget Analyzer (Text Generation Widget)
* **Function:** Acts as the core computational engine.
* **Prompt Strategy:** Instructed the AI to ingest the raw numerical variables and output a highly structured **Monthly Budget Summary**. The prompt strictly enforces the AI to:
  * Calculate total expenses vs. income.
  * Establish a safe **Weekly & Daily Spending Limit** that mathematically protects the user's stated savings goal.
  * Classify the user's budget status into strict categories: **Healthy**, **Needs Attention**, or **Over Budget**, along with a brief explanation of the verdict.

### 3. Spending Insights (Text Generation Widget)
* **Function:** Categorizes and critiques spending habits.
* **Prompt Strategy:** The AI is prompted to act as an empathetic but realistic student advisor. It analyzes the variables to separate "Necessary" vs "Optional" expenses, identifies the largest spending category, and suggests exact areas to cut back. It is constrained to output 3-5 highly practical, realistic money-saving tips tailored for a student lifestyle.

### 4. AI Budget Assistant (Chatbot Widget)
* **Function:** An interactive Q&A assistant for real-time financial decisions.
* **Prompt Strategy:** This widget references the outputs of the previous widgets. The AI is given a system prompt to adopt the persona of a helpful, simple-to-understand financial buddy. Because it has context of the user's specific budget, it can answer highly specific queries like:
  * *"Can I afford to spend RM20 on coffee today?"*
  * *"How can I save RM200 this month?"*
  * *"Which expense should I reduce right now?"*

---

## 🛠️ Skills Demonstrated
* **Generative AI System Design:** Structuring an application flow where data passes seamlessly from user input to analytical models and finally to an interactive chatbot.
* **Context-Aware Prompting:** Engineering AI instructions that force the model to respect mathematical constraints (like the user's savings goal) while maintaining a specific, beginner-friendly tone.
* **Rapid Prototyping:** Moving quickly from concept to a fully functional, cloud-hosted AI tool.

## 🚀 Future Improvements
* Add functionality to export the budget summary to a downloadable CSV or PDF.
* Integrate visual charts (via image generation or external integrations) to show expense distribution.
* Expand the chatbot's system prompt to handle "what-if" scenarios (e.g., "What if my rent increases by RM50 next month?").
