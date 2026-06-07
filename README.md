# stock-analyzer

A Django web application for displaying and analyzing historical stock data across multiple companies.

---

## Features

- View historical stock data (open, high, low, close, volume) for multiple tickers
- Analyze price trends over a date range (2013–2018)
- Covers 10 stocks: AAPL, AMZN, GOOGL, BA, CMG, GE, JNJ, KO, SNPS, ZTS
- User feedback system
- Django admin panel for data management

---

## Tech Stack

- **Backend:** Python, Django
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Data:** Historical stock data loaded via Django fixtures

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kshama-purohit/stock-analyzer.git
   cd stock-analyzer
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate      # Windows
   source venv/bin/activate   # macOS/Linux
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   DATABASE_ENGINE=django.db.backends.sqlite3
   DATABASE_NAME=db.sqlite3
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Load stock data**
   ```bash
   python manage.py loaddata stockdata.json
   ```

7. **Start the development server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000` in your browser.

---

## Screenshots

<img width="1896" height="912" alt="image" src="https://github.com/user-attachments/assets/a7e540f3-0c33-42af-aa0a-86f68d52a28a" />


---

## Project Structure

```
stock-analyzer/
├── webapp/              # Main Django app
│   ├── models.py        # Stock & Feedback models
│   ├── views.py
│   └── templates/
├── manage.py
├── requirements.txt
├── .env                 # Not committed
└── .gitignore
```

---

## License

This project is for educational/internship purposes.
