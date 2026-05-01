# 💰 Net Salary Calculator – Italy (CCNL Metalmeccanici)

Web application for estimating net salary from gross annual income (RAL) under a simplified Italian tax model.

Built with **Python + Streamlit**, the project focuses on **data processing, tax logic modeling, and clean code structure**, making it suitable as a portfolio project for software engineering roles.

---

## 📌 Overview

This application allows users to estimate their net salary based on:

- Gross annual salary (RAL)
- Number of monthly payments (12–14)
- Region (for regional tax adjustments)

It provides a breakdown of:

- Net salary
- INPS contributions
- Gross IRPEF
- Tax deductions
- Regional additional tax

> ⚠️ Disclaimer: This is a **simplified fiscal model** for demonstration purposes only.

---

## 🧠 Technical Highlights

- Modular architecture:
  - `tax_rules.py` → tax computation logic
  - `csv_utils.py` → data parsing and rule extraction
  - `app.py` → UI layer
- Data-driven approach:
  - Regional tax rules loaded dynamically from CSV
- Progressive tax computation (IRPEF brackets)
- Input validation via Streamlit components
- Clear separation between **business logic and presentation layer**

---

## 🏗️ Project Structure
.
├── app.py                  # Streamlit UI
├── tax_rules.py            # Core tax computation logic
├── csv_utils.py            # CSV parsing & regional tax extraction
├── data/
│   └── addreg2026.csv      # Regional tax rates dataset
└── README.md

---

## ⚙️ Installation

```bash
git clone https://github.com/irene-vanni/stipendio-netto
cd net-salary-calculator
pip install streamlit pandas

---

## ⚙️ Run the application 

```bash
streamlit run app.py

Then open:
http://localhost:8501