import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from io import StringIO

def generate_text_summary(results_df):
    """Generate text summary for crossover analysis"""
    buffer = StringIO()
    buffer.write("=== Crossover Performance Analysis ===\n")
    for _, row in results_df.iterrows():
        direction = "↑ UP" if row['Percentage Change'] > 0 else "↓ DOWN"
        buffer.write(f"\n{row['Start Type']} on {row['Start Date'].date()}\n")
        buffer.write(f"  → {row['End Type']} on {row['End Date'].date()} ({row['Days Between']} days later)\n")
        buffer.write(f"  Price moved from ₹{row['Start Price']:.2f} to ₹{row['End Price']:.2f}\n")
        buffer.write(f"  {direction} {abs(row['Percentage Change']):.2f}%\n")
    return buffer.getvalue()

from matplotlib.backends.backend_pdf import PdfPages

def create_pdf_report(text_summary, image_path, output_pdf):
    with PdfPages(output_pdf) as pdf:
        # Page 1: Text Summary
        plt.figure(figsize=(8.5, 11))
        plt.axis('off')
        plt.text(0.01, 0.99, text_summary, va='top', ha='left', fontsize=10, family='monospace')
        pdf.savefig()
        plt.close()
        
        # Page 2: Chart Image
        img = plt.imread(image_path)
        plt.figure(figsize=(11, 7))
        plt.imshow(img)
        plt.axis('off')
        pdf.savefig()
        plt.close()
