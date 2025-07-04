# Stock-Signal-Predictor-
This project is a Python-based stock analysis tool that predicts buy and sell signals based on the Exponential Moving Average (EMA) crossover strategy. It primarily uses the 50-day and 200-day EMAs to detect bullish (Golden Cross) and bearish (Death Cross) signals in historical stock data

# 📈 Stock Buy/Sell Signal Predictor (PDF Report Generator)

This is a complete Python project that automates the process of analyzing stock market data to detect potential buy and sell signals using technical indicators. The tool fetches historical stock data, processes it, highlights crossover events, visualizes them, and finally exports a clean and professional PDF report with analysis and charts — all in one run.

---

## 📌 What This Project Does

- ✅ Automatically fetches historical stock data from Yahoo Finance (via `yfinance`)
- ✅ Calculates and stores technical indicator data (moving averages)
- ✅ Detects signal points in the trend and calculates performance between them
- ✅ Plots the closing price along with signal overlays and saves as an image
- ✅ Combines both text-based analysis and visual chart into a **single PDF**
- ✅ Designed to work with Indian stock tickers (like `RELIANCE.NS`, `TVSMOTOR.NS`, etc.)

---

## 📁 Output Example

When the program is executed:
- A chart is saved with:
  - Stock closing price line
  - 50-day and 200-day moving average lines
  - Buy/sell crossover markers
- A formatted PDF report is generated containing:
  - Crossover events with dates
  - Days between signals
  - Price before and after each signal
  - % change from entry to exit
  - Chart image (on the second page)

📄 Sample File:  
`TVSMOTOR.NS_Analysis_2025-07-04.pdf`

---

## 🛠️ Tech Stack

This project is built with:

- **Python 3.9+**
- **Pandas** – for data manipulation
- **NumPy** – for numerical computation
- **Matplotlib** – for plotting charts
- **yFinance** – to get historical stock data
- **PdfPages (matplotlib backend)** – to generate multipage PDF reports

---

## 🧰 How to Use

1. **Clone the repository**  
```bash
git clone https://github.com/your-username/stock-predictor-report.git
cd stock-predictor-report
