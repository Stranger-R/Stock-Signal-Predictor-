import numpy as np
import pandas as pd

def analyze_crossovers(df):
    df['50_above_200'] = df['MA_50'] > df['MA_200']
    df['Crossover'] = df['50_above_200'].ne(df['50_above_200'].shift())
    
    crossovers = df[df['Crossover']].copy()
    crossovers['Type'] = np.where(crossovers['MA_50'] > crossovers['MA_200'], 
                                 'Golden Cross', 'Death Cross')
    
    results = []
    for i in range(1, len(crossovers)):
        prev = crossovers.iloc[i-1]
        current = crossovers.iloc[i]
        
        start_date = prev.name
        end_date = current.name
        days_between = (end_date - start_date).days
        
        start_price = df.loc[start_date, 'Close']
        end_price = df.loc[end_date, 'Close']
        percent_change = ((end_price - start_price) / start_price) * 100
        
        results.append({
            'Start Date': start_date,
            'End Date': end_date,
            'Start Type': prev['Type'],
            'End Type': current['Type'],
            'Days Between': days_between,
            'Start Price': start_price,
            'End Price': end_price,
            'Percentage Change': percent_change
        })
    
    return pd.DataFrame(results)

def print_crossover_analysis(results_df):
    print("\n=== Crossover Performance Analysis ===")
    for _, row in results_df.iterrows():
        direction = "↑ UP" if row['Percentage Change'] > 0 else "↓ DOWN"
        print(f"\n{row['Start Type']} on {row['Start Date'].date()}")
        print(f"  → {row['End Type']} on {row['End Date'].date()} ({row['Days Between']} days later)")
        print(f"  Price moved from ₹{row['Start Price']:.2f} to ₹{row['End Price']:.2f}")
        print(f"  {direction} {abs(row['Percentage Change']):.2f}%")
