
# **ECSA – e-Consultation Sentiment Analyzer**

ECSA (**E-Consultation Sentiment Analyzer**) is a tool designed to process and analyze public feedback collected during e-Consultation processes.  
It helps policymakers and analysts by **classifying sentiments**, **summarizing key feedback**, and **visualizing common themes** from stakeholder comments.

The tool is built using **Python**, **Streamlit**, and **NLP models** from Hugging Face.

---

## **Features**

- 📊 **Sentiment Analysis** – Automatically classifies each comment as **Positive**, **Negative**, or **Neutral**.  
- ☁️ **Word Cloud Generation** – Visualize the most frequent and relevant words in the comments.  
- 📝 **Summarization** – Generate concise summaries of lengthy feedback.  
- 📂 **Export Results** – Save processed data into CSV for further review.  
- 🖥 **Streamlit Web App** – Simple and interactive UI for analysis.

---

## **Dataset Format**

The tool expects an input CSV file with **exactly these columns**:

| Column Name          | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **comment_id**       | A unique identifier for each comment.                                       |
| **stakeholder**      | The stakeholder providing the feedback (e.g., individual, company, NGO).    |
| **provision_reference** | The reference to the specific provision or rule being commented on.        |
| **date**             | Date when the comment was submitted (format: YYYY-MM-DD).                   |
| **comment_text**     | The full text of the stakeholder's comment.                                 |

⚠️ **Note:**  
- These five columns are **mandatory**.  
- Additional columns are **ignored by the app**.  
- The `comment_text` field should contain actual feedback text for accurate analysis.

---

### **Example CSV**

```csv
comment_id,stakeholder,provision_reference,date,comment_text
1,Company A,Rule 5,2025-09-18,"We strongly support this provision as it improves transparency."
2,Individual,Rule 7,2025-09-19,"This rule may create additional compliance burden."
3,NGO,Rule 9,2025-09-20,"The new changes will benefit the environment greatly."

## **Installation**

Follow these steps to set up and run the project locally.

### **1. Clone the repository**

```bash
git clone https://github.com/narasingapranav/ecsa.git
cd ecsa
```

### **2. Create a virtual environment (recommended)**

```bash
python -m venv venv
```

Activate the virtual environment:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Linux/Mac:**

  ```bash
  source venv/bin/activate
  ```

### **3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

## **Usage**

### **Run the Streamlit App**

```bash
streamlit run app.py
```

After running the above command, open your browser and go to:
[http://localhost:8501](http://localhost:8501)

---

## **How It Works**

1. **Upload a CSV file** with the required columns:

   * `comment_id`
   * `stakeholder`
   * `provision_reference`
   * `date`
   * `comment_text`

2. The tool will:

   * **Clean and preprocess** the comment text.
   * **Analyze sentiment** using a Hugging Face transformer model.
   * **Summarize feedback** into concise insights.
   * **Generate a word cloud** of the most common terms.
   * Display results in an interactive **Streamlit dashboard**.

3. **Download Processed Data**

   * The processed results, including sentiment labels, can be **exported as a CSV file**.

---

## **Output Example**

Here’s an example of what the processed output CSV will look like:

| comment\_id | stakeholder | provision\_reference | date       | comment\_text                                 | sentiment |
| ----------- | ----------- | -------------------- | ---------- | --------------------------------------------- | --------- |
| 1           | Company A   | Rule 5               | 2025-09-18 | We strongly support this provision...         | Positive  |
| 2           | Individual  | Rule 7               | 2025-09-19 | This rule may create additional burden.       | Negative  |
| 3           | NGO         | Rule 9               | 2025-09-20 | The new changes will benefit the environment. | Positive  |

---

## **Tech Stack**

* **Python 3.9+**
* **Streamlit** – for building the interactive web interface
* **Pandas / NumPy** – data manipulation and processing
* **Matplotlib / WordCloud** – data visualization
* **Hugging Face Transformers** – sentiment analysis and summarization

---

## **Folder Structure**

```
ecsa/
├── app.py                       # Main Streamlit app
├── requirements.txt             # Python dependencies
├── mca_consultation_comments.csv  # Sample dataset
├── results_with_sentiment.csv     # Example processed output
├── runtime.txt                   # Runtime environment settings
├── LICENSE
└── README.md
```

---

## **Future Enhancements**

* **Fine-tuned NLP Models:**
  Improve accuracy by training on domain-specific consultation data.

* **Topic Modeling:**
  Automatically detect themes from comments using clustering techniques like LDA or BERTopic.

* **Interactive Visualizations:**
  Filter results by sentiment, stakeholder type, or provision reference.

* **Multilingual Support:**
  Handle and analyze comments submitted in multiple languages.

* **Aspect-Based Sentiment Analysis:**
  Identify which specific provisions or aspects are being praised or criticized.

---

## **License**

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.

```
