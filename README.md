# ecsa

**AI-powered tool to analyze stakeholder comments from MCA e-Consultation**  
Performs sentiment analysis, generates word clouds, and summarizes feedback to help policymakers efficiently review public opinion on draft legislation.

---

## Table of Contents

- [About](#about)  
- [Features](#features)  
- [Tech Stack](#tech-stack)  
- [Usage](#usage)  
- [Data](#data)  
- [Installation](#installation)  
- [How It Works](#how-it-works)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

## About

When draft legislations are open for public e-Consultation by the Ministry of Corporate Affairs (MCA), stakeholders submit comments. Reviewing large volumes of feedback manually is inefficient and time consuming. **ecsa** helps by using AI to:

- Classify sentiment (positive / negative / neutral) of comments  
- Generate visual summaries such as word clouds  
- Derive textual summaries of feedback  

Thus enabling faster, more informed decision-making for policymakers.

---

## Features

- **Sentiment Analysis**: Understand whether a comment is positive, negative, or neutral.  
- **Word Cloud Generation**: Visualize frequently occurring themes and words.  
- **Summarization**: Automatically summarize stakeholder feedback.  
- **Export Results**: Save analyzed data to CSV files for reporting and further review.  
- **Streamlit UI**: Simple web interface to interact with data and models.  

---

## Tech Stack

- **Programming Language:** Python 3.x  
- **Frontend/UI:** Streamlit  
- **Machine Learning Models:** Hugging Face Transformers  
- **Visualization:** Matplotlib, WordCloud, Pandas  
- **Other Dependencies:** See [`requirements.txt`](requirements.txt)  

---

## Usage

### 1. Clone the repository

```bash
git clone https://github.com/narasingapranav/ecsa.git
cd ecsa
