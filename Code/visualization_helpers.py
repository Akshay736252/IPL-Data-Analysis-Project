import matplotlib.pyplot as plt
import seaborn as sns

def plot_total_runs(df, year_column='Year', runs_column='Runs'):
    """
    Plots total runs scored per year.
    """
    df_sorted = df.sort_values(by=year_column)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=year_column, y=runs_column, data=df_sorted, palette="coolwarm")
    plt.title("Virat Kohli - Total Runs Per Year")
    plt.xlabel("Year")
    plt.ylabel("Total Runs")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_top_batsmen(df, player_column='Batsman', runs_column='Runs', top_n=10):
    """
    Plots top N batsmen by total runs.
    """
    top_batsmen = df.groupby(player_column)[runs_column].sum().nlargest(top_n)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_batsmen.values, y=top_batsmen.index, palette="magma")
    plt.title(f"Top {top_n} Batsmen by Runs")
    plt.xlabel("Total Runs")
    plt.ylabel("Batsman")
    plt.tight_layout()
    plt.show()


def plot_batting_average(df):
    """
    Plots Virat Kohli's batting average over the years.
    """
    df_sorted = df.sort_values(by='Year')

    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df_sorted, x='Year', y='Average', marker='o', color='green')
    plt.title("Virat Kohli - Batting Average Per Year")
    plt.xlabel("Year")
    plt.ylabel("Average")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def plot_fifties_centuries(df):
    """
    Plots number of fifties and centuries per year.
    """
    df_sorted = df.sort_values(by='Year')

    plt.figure(figsize=(10, 6))
    sns.barplot(data=df_sorted, x='Year', y='Fifties', color='skyblue', label='Fifties')
    sns.barplot(data=df_sorted, x='Year', y='Centuries', color='orange', label='Centuries')
    plt.title("Virat Kohli - Fifties & Centuries Per Year")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def plot_centuries_vs_fifties(df):
    """
    Plots line chart of fifties vs centuries per year.
    """
    df_sorted = df.sort_values(by='Year')

    plt.figure(figsize=(10, 6))
    plt.plot(df_sorted['Year'], df_sorted['Fifties'], marker='o', label='Fifties', color='orange')
    plt.plot(df_sorted['Year'], df_sorted['Centuries'], marker='o', label='Centuries', color='red')
    plt.title('Fifties vs Centuries Per Year')
    plt.xlabel('Year')
    plt.ylabel('Count')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
