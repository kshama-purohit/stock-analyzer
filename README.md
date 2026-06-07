# 📈 Stock Analyzer

A Django web application for displaying and analyzing historical stock data across multiple companies, featuring interactive charts and technical indicators.

---

## Features

- 📊 **Line Chart** — closing prices over time for all stocks
- 🕯️ **Candlestick Chart** — OHLC data with filtering by stock and date
- 📉 **Bollinger Bands** — technical analysis with rolling averages
- 💬 **Feedback System** — users can submit feedback
- 🔒 **Django Admin** — manage stock data and feedback
- 🐳 **Dockerized** — easy deployment with Docker

Covers 10 stocks: `AAPL`, `AMZN`, `GOOGL`, `BA`, `CMG`, `GE`, `JNJ`, `KO`, `SNPS`, `ZTS` over a 5-year range (2013–2018).

---

## Tech Stack

- **Backend:** Python 3.10, Django
- **Charts:** Plotly, Plotly Express
- **Data:** Pandas, historical stock data via Django fixtures
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Containerization:** Docker

---

## Getting Started

### Option 1: Docker (Recommended)

1. **Clone the repository**
   ```bash
   git clone https://github.com/kshama-purohit/stock-analyzer.git
   cd stock-analyzer
   ```

2. **Set up environment variables**

   Create a `.env` file in the project root:
   ```env
   DATABASE_ENGINE=django.db.backends.sqlite3
   DATABASE_NAME=db.sqlite3
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

3. **Build and run with Docker**
   ```bash
   docker-compose up --build
   ```

4. **Load stock data** (in a separate terminal)
   ```bash
   docker-compose exec web python manage.py loaddata stockdata.json
   ```

   Visit `http://localhost:8000` in your browser.

---

### Option 2: Local Setup

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

## Project Structure

```
stock-analyzer/
├── webapp/                  # Main Django app
│   ├── templates/webapp/    # HTML templates
│   │   ├── index.html
│   │   ├── stockdata.html
│   │   ├── candlestick_chart.html
│   │   ├── bollinger_bands.html
│   │   ├── feedback.html
│   │   └── header.html
│   ├── models.py            # Stock & Feedback models
│   ├── views.py             # Chart rendering logic
│   ├── filters.py           # Stock filtering (django-filter)
│   ├── utils.py             # Bollinger Bands calculations
│   └── urls.py
├── stocks/                  # Django project settings
├── static/
├── all_stocks_5yr.csv       # Raw data source
├── manage.py
├── .env                     # Not committed
├── .gitignore
└── .dockerignore
```

---

## License

This project is for educational/internship purposes.

---

## Screenshots
Landing Page:
<img width="1896" height="912" alt="image" src="https://github.com/user-attachments/assets/a7e540f3-0c33-42af-aa0a-86f68d52a28a" />

Candlestick Chart (AAPL):
<img width="1896" height="907" alt="image" src="https://github.com/user-attachments/assets/f5c1f9c8-3ae2-43f5-be2b-f73368e9b8f8" />

Bollinger Bands (AAPL):
<img width="1901" height="907" alt="image" src="https://github.com/user-attachments/assets/e3153e01-76c8-4270-ae47-72b92821a703" />

Historical Stock Growth:
<img width="1917" height="905" alt="image" src="https://github.com/user-attachments/assets/b7dc8c0c-e3fa-4158-b1bf-1e0a086e4252" />

Feedback Page:
<img width="1891" height="907" alt="image" src="https://github.com/user-attachments/assets/225d1dab-1148-4823-bc68-d308fef38f6d" />


---
