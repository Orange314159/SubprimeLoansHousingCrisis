import pandas as pd 


files = []
data_frames = []


for i in range(2004,2008):
    files.append(f"/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedLoanData/HMDA_{i}_small.csv")
    data_frames.append(pd.read_csv(files[i-2004]))
    print(data_frames[i-2004].head())

## combine all data_frames in the list
combined_df = pd.concat(data_frames, ignore_index=True)

## these are the cols that we actually care about
target_cols = ['pct_subprime', 'average_income']

## scale the cols based weight
for col in target_cols:
    combined_df[f'{col}_product'] = combined_df[col] * combined_df['weight']

## group by GISJOIN like before using sum so we can divide later
grouped = combined_df.groupby('GISJOIN', as_index=False).agg({
    'pct_subprime_product': 'sum',
    'average_income_product': 'sum',
    'weight': 'sum' ## we don't reall need this, but it is not that hard to keep 
})

## now divide the cols by the weight to scale back to a percentage 
for col in target_cols:
    grouped[col] = grouped[f'{col}_product'] / grouped['weight']

## clean up by getting a final df
final_df = grouped[['GISJOIN', 'pct_subprime', 'average_income', 'weight']]

final_df.to_csv(f"/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedLoanData/HMDA_Combined.csv")
