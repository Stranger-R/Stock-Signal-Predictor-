from data_fetcher import get_indian_stock_data
from indicators import calculate_moving_averages
from analyzer import analyze_crossovers
from visualizer import plot_and_save_chart
from report_generator import generate_text_summary, create_pdf_report

if __name__ == "__main__":
    ticker = 'TVSMOTOR.NS'

    stock_data = get_indian_stock_data(ticker)
    if stock_data is not None:
        stock_data = calculate_moving_averages(stock_data)
        crossover_results = analyze_crossovers(stock_data)

        # Generate chart image
        chart_path = 'chart.png'
        plot_and_save_chart(stock_data, ticker, chart_path)

        # Generate text summary
        summary = generate_text_summary(crossover_results)

        # Create PDF
        create_pdf_report(summary, chart_path, 'Stock_Analysis_Report.pdf')

        print("✅ Report generated: Stock_Analysis_Report.pdf")
