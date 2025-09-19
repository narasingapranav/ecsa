# ecsa

**AI-powered tool to analyze stakeholder comments from MCA e-Consultation**

`ecsa` helps automate the review of large volumes of stakeholder comments collected during public e-Consultation processes by the Ministry of Corporate Affairs (MCA).  
It performs **sentiment analysis**, **summarization**, and **word cloud generation** to assist policymakers in efficiently understanding public feedback on draft legislations.

---

## Table of Contents
- [About](#about)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Data](#data)
- [How It Works](#how-it-works)
- [Example Output](#example-output)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Future Enhancements](#future-enhancements)
- [Acknowledgements](#acknowledgements)

---

## About

When the MCA releases draft legislations for public consultation, stakeholders like companies, professionals, and citizens submit comments.  
Manually reviewing these thousands of comments is **time-consuming** and **inefficient**.

The **ecsa** project solves this by:
- Classifying each comment into **Positive**, **Negative**, or **Neutral** sentiment.
- Summarizing all feedback into concise insights.
- Generating **word clouds** to highlight frequent terms and themes.
- Exporting results for reporting and further analysis.

This helps decision-makers **quickly understand the overall sentiment** and focus on the most critical feedback.

---

## Features

- **Sentiment Analysis**  
  Detect the tone of each comment (Positive, Negative, Neutral).

- **Word Cloud Visualization**  
  Quickly see the most commonly discussed words and topics.

- **Automatic Summarization**  
  Generate text summaries of the feedback dataset.

- **CSV Export**  
  Save analyzed results with sentiment tags for further processing.

- **Streamlit UI**  
  User-friendly web interface to interact with the tool.

---

## Tech Stack

| Category        | Tools Used            |
|-----------------|-----------------------|
| **Language**    | Python 3.x           |
| **Web UI**      | Streamlit            |
| **NLP Models**  | Hugging Face Transformers |
| **Visualization** | WordCloud, Matplotlib, Pandas |
| **Data Handling** | Pandas, NumPy |
| **Deployment**  | Local via Streamlit |

> All dependencies are listed in [`requirements.txt`](requirements.txt).

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/narasingapranav/ecsa.git
cd ecsa
