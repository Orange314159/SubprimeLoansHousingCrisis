import pandas as pd  
import seaborn as sns 
import matplotlib.pyplot as plt 
import sys 

file_name = sys.argv[1]
df = pd.read_csv(f"{file_name}")
## df = pd.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/merged_loan_housing_data.csv")

print(df.head())

cols = [
    'pct_subprime',
    'Overcrowding_Rate',
    'Cost_Burden_PCT',
    'Unemployment_PCT',
    'Poverty_Rate_PCT',
    'Bachelors_Or_Higher_PCT',
    'Median_Household_Income'
]


df_plot = df[cols].dropna()

## the plot would be too cluttered with the ~60,000 dots and random sample is ok for a general picture
df_sampled = df_plot.sample(n=min(5000, len(df)), random_state=70) ## kinda a weird random state  

g = sns.pairplot(
    df_sampled, 
    height=2.2, ## there might be a better value for this, i just got it to something acceptable 
    corner=True, ## we only need half of the plots to render to get the full picture 
    plot_kws={'s': 6, 'alpha': 0.15, 'edgecolor': 'none', 'color': '#1f77b4'}, ## some random blue
    diag_kws={'color': '#1f77b4'}
)

g.fig.suptitle("Subprime Loan Pairplot (Sampled N=5,000)", y=1.03, fontsize=14)

## I want the side axes to be rotated slightly for ease of reading 
for ax in g.axes.flat:
    if ax is not None:
        ax.set_xlabel(ax.get_xlabel(), rotation=20, horizontalalignment='right', fontsize=8)
        ax.set_ylabel(ax.get_ylabel(), rotation=0, horizontalalignment='right', fontsize=8)

plt.subplots_adjust(
    left=0.18,    
    bottom=0.15,
    hspace=0.25,
    wspace=0.25
)

plt.show()

