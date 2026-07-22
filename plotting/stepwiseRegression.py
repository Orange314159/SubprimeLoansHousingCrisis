import numpy  as np 
import pandas as pd 

from sklearn.linear_model      import LinearRegression
from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.metrics           import r2_score



data = pd.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/merged_loan_housing_data.csv")

data = data.drop(columns=["GISJOIN", "weight"]).dropna()
## we don't want to use GISJOIN or weight to predict either of these variables



def forward_step_regression_ols(df, target_col):
    
    ## make list of all features that can be tried
    feature_candidates = [c for c in df.columns if c != target_col]

    ## we are using X to predict Y
    X = df[feature_candidates]
    Y = df[target_col]

    baseline = np.full_like(Y, fill_value=Y.mean()) ## baseline is no slope line 
    baseline_r2 = r2_score(Y, baseline)

    print(f"Baseline R^2 is {baseline_r2:.4f}\n")

    ## now we will start adding more variables that will (hopefully) improve the model 
    selected_features = []

    for k in range(1, len(feature_candidates) + 1): 
        if k < len(feature_candidates):

            sfs = SequentialFeatureSelector(
                estimator=LinearRegression(), ## we will be using linear regression (at least for now)
                n_features_to_select=k, ## we will use k number of features
                direction='forward', ## we will be adding variables not removing them 
                cv=5, ## cross validation 
                scoring='r2' ## use r^2 to make sure it is getting better 
            )

            sfs.fit(X,Y) ## greedy algorithm used to find the optimal k features 

            ## boolean mask of which cols to use --> actual list of those cols 
            current_mask = sfs.get_support()
            current_features = X.columns[current_mask].tolist()

            ## the only feature that was used that is not in the current_features
            new_feature = [f for f in current_features if f not in selected_features][0]
            selected_features.append(new_feature)
        else:
            ## if there is only one feature left we can just add that one
            new_feature = [f for f in feature_candidates if f not in selected_features][0]
            selected_features.append(new_feature)
        
        ## fit the data !!
        model = LinearRegression()
        model.fit(X[selected_features], Y)
        
        ## hopefully this is a good score 
        r2 = r2_score(Y, model.predict(X[selected_features]))

        print(f"{k}: Added: {new_feature}")
        print(f"   Current Features: {selected_features}")
        print(f"   Model R^2: {r2:.4f}")
        print("===" * 25)


forward_step_regression_ols(data, target_col="Cost_Burden_PCT")

print("===" * 25)
print("\n\n\n") # ================== Sometimes you just need space between your tests ==============#
print("===" * 25)

forward_step_regression_ols(data, target_col="Overcrowding_Rate")

"""
Baseline R^2 is 0.0000

1: Added: average_income
   Current Features: ['average_income']
   Model R^2: 0.1724
===========================================================================
2: Added: Overcrowding_Rate
   Current Features: ['average_income', 'Overcrowding_Rate']
   Model R^2: 0.3072
===========================================================================
3: Added: Bachelors_Or_Higher_PCT
   Current Features: ['average_income', 'Overcrowding_Rate', 'Bachelors_Or_Higher_PCT']
   Model R^2: 0.3197
===========================================================================
4: Added: Poverty_Rate_PCT
   Current Features: ['average_income', 'Overcrowding_Rate', 'Bachelors_Or_Higher_PCT', 'Poverty_Rate_PCT']
   Model R^2: 0.3255
===========================================================================
5: Added: Unemployment_PCT
   Current Features: ['average_income', 'Overcrowding_Rate', 'Bachelors_Or_Higher_PCT', 'Poverty_Rate_PCT', 'Unempl
oyment_PCT']
   Model R^2: 0.3317
===========================================================================
6: Added: pct_subprime
   Current Features: ['average_income', 'Overcrowding_Rate', 'Bachelors_Or_Higher_PCT', 'Poverty_Rate_PCT', 'Unempl
oyment_PCT', 'pct_subprime']
   Model R^2: 0.3320
===========================================================================
7: Added: Median_Household_Income
   Current Features: ['average_income', 'Overcrowding_Rate', 'Bachelors_Or_Higher_PCT', 'Poverty_Rate_PCT', 'Unempl
oyment_PCT', 'pct_subprime', 'Median_Household_Income']
   Model R^2: 0.3354
===========================================================================
===========================================================================




===========================================================================
Baseline R^2 is 0.0000

1: Added: Cost_Burden_PCT
   Current Features: ['Cost_Burden_PCT']
   Model R^2: 0.1394
===========================================================================
2: Added: Poverty_Rate_PCT
   Current Features: ['Cost_Burden_PCT', 'Poverty_Rate_PCT']
   Model R^2: 0.2178
===========================================================================
3: Added: Median_Household_Income
   Current Features: ['Cost_Burden_PCT', 'Poverty_Rate_PCT', 'Median_Household_Income']
   Model R^2: 0.2285
===========================================================================
4: Added: Unemployment_PCT
   Current Features: ['Cost_Burden_PCT', 'Poverty_Rate_PCT', 'Median_Household_Income', 'Unemployment_PCT']
   Model R^2: 0.2298
===========================================================================
5: Added: Bachelors_Or_Higher_PCT
   Current Features: ['Cost_Burden_PCT', 'Poverty_Rate_PCT', 'Median_Household_Income', 'Unemployment_PCT', 'Bachel
ors_Or_Higher_PCT']
   Model R^2: 0.2380
===========================================================================
6: Added: average_income
   Current Features: ['Cost_Burden_PCT', 'Poverty_Rate_PCT', 'Median_Household_Income', 'Unemployment_PCT', 'Bachel
ors_Or_Higher_PCT', 'average_income']
   Model R^2: 0.2384
===========================================================================
7: Added: pct_subprime
   Current Features: ['Cost_Burden_PCT', 'Poverty_Rate_PCT', 'Median_Household_Income', 'Unemployment_PCT', 'Bachel
ors_Or_Higher_PCT', 'average_income', 'pct_subprime']
   Model R^2: 0.2457
===========================================================================


"""
