import pandas as pd
import sys

file_2004   = sys.argv[1]
file_2005   = sys.argv[2]
file_2006   = sys.argv[3]
file_2007   = sys.argv[4]
output_file = sys.argv[5]

files = []
data_frames = []


files.append(file_2004)
files.append(file_2005)
files.append(file_2006)
files.append(file_2007)

for file in files:
    data_frames.append(pd.read_csv(file))

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

final_df.to_csv(output_file)
