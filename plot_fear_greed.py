import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


plt.style.use('seaborn')
sns.set_palette("husl")

def plot_fear_greed_index():
    try:
        
        if not os.path.exists('fear_greed_data.csv'):
            print("Error: fear_greed_data.csv not found!")
            return
            
        # Load the data
        print("Loading data from fear_greed_data.csv...")
        df = pd.read_csv('fear_greed_data.csv')
        print(f"Data loaded successfully. Shape: {df.shape}")
        print("\nFirst few rows of data:")
        print(df.head())
        
        # Convert date column to datetime
        df['date'] = pd.to_datetime(df['date'])
        
        # Create the plot
        plt.figure(figsize=(15, 8))
        
        # Plot the Fear & Greed Index values
        plt.plot(df['date'], df['value'], linewidth=2, label='Fear & Greed Index')
        
        # Add horizontal lines for different sentiment levels
        plt.axhline(y=50, color='gray', linestyle='--', alpha=0.3)
        plt.axhline(y=75, color='red', linestyle='--', alpha=0.3)
        plt.axhline(y=25, color='green', linestyle='--', alpha=0.3)
        
        # Customize the plot
        plt.title('Bitcoin Fear & Greed Index Over Time', fontsize=14, pad=20)
        plt.xlabel('Date', fontsize=12)
        plt.ylabel('Fear & Greed Index', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.legend()
        
        # Rotate x-axis labels for better readability
        plt.xticks(rotation=45)
        
        # Adjust layout to prevent label cutoff
        plt.tight_layout()
        
        # Save the plot
        plt.savefig('fear_greed_index.png', dpi=300, bbox_inches='tight')
        print("\nPlot saved as 'fear_greed_index.png'")
        
        # Show the plot
        plt.show()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    plot_fear_greed_index() 