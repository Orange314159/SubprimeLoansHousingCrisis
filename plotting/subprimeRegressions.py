import matplotlib.pyplot as plt
import pandas as pd
import bambi as bmb 

## same things i did in data science course
if __name__ == '__main__':
    df = pd.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/merged_loan_housing_data.csv").dropna()

    model_poly_1 = bmb.Model("Overcrowding_Rate ~ pct_subprime", df, family="gaussian")
    idata_poly_1 = model_poly_1.fit(record_likelihood=True)

    fig, ax = plt.subplots()

    ax.scatter(df["pct_subprime"], df["Overcrowding_Rate"], color="C2", alpha=0.5, zorder=-3)

    p = bmb.interpret.plot_predictions(
        model_poly_1, 
        idata_poly_1, 
        "pct_subprime"
    )

    p.on(ax).show()

    model_poly_3 = bmb.Model("Cost_Burden_PCT ~ pct_subprime", df, family="gaussian")
    idata_poly_3 = model_poly_3.fit(record_likelihood=True)

    fig, ax = plt.subplots()

    ax.scatter(df["pct_subprime"], df["Cost_Burden_PCT"], color="C2", alpha=0.5, zorder=-3)

    p = bmb.interpret.plot_predictions(
        model_poly_3, 
        idata_poly_3, 
        "pct_subprime"
    )
    p.on(ax).show()



    ## now lets find the r2
    import statsmodels.formula.api as smf

    model = smf.ols(formula="Overcrowding_Rate ~ pct_subprime", data=df).fit()
    print(model.summary())


    model = smf.ols(formula="Cost_Burden_PCT ~ pct_subprime", data=df).fit()
    print(model.summary())

        
"""                            OLS Regression Results                            
=============================================================================
Dep. Variable:      Overcrowding_Rate   R-squared:                       0.027
Model:                            OLS   Adj. R-squared:                  0.027
Method:                 Least Squares   F-statistic:                     1230.
Date:                Wed, 22 Jul 2026   Prob (F-statistic):          7.21e-266
Time:                        09:51:20   Log-Likelihood:                 71360.
No. Observations:               44489   AIC:                        -1.427e+05
Df Residuals:                   44487   BIC:                        -1.427e+05
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept        0.0138      0.001     24.209      0.000       0.013       0.015
pct_subprime     0.1563      0.004     35.074      0.000       0.148       0.165
==============================================================================
Omnibus:                    33006.159   Durbin-Watson:                   1.099
Prob(Omnibus):                  0.000   Jarque-Bera (JB):           657841.397
Skew:                           3.444   Prob(JB):                         0.00
Kurtosis:                      20.534   Cond. No.                         19.6
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
                            OLS Regression Results                            
==============================================================================
Dep. Variable:        Cost_Burden_PCT   R-squared:                       0.031
Model:                            OLS   Adj. R-squared:                  0.031
Method:                 Least Squares   F-statistic:                     1430.
Date:                Wed, 22 Jul 2026   Prob (F-statistic):          6.06e-308
Time:                        09:53:48   Log-Likelihood:            -1.7002e+05
No. Observations:               44489   AIC:                         3.400e+05
Df Residuals:                   44487   BIC:                         3.401e+05
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
================================================================================
                   coef    std err          t      P>|t|      [0.025      0.975]
--------------------------------------------------------------------------------
Intercept       20.4591      0.130    157.847      0.000      20.205      20.713
pct_subprime   -38.2782      1.012    -37.810      0.000     -40.263     -36.294
==============================================================================
Omnibus:                     6145.896   Durbin-Watson:                   0.899
Prob(Omnibus):                  0.000   Jarque-Bera (JB):             9332.679
Skew:                           1.000   Prob(JB):                         0.00
Kurtosis:                       4.017   Cond. No.                         19.6
==============================================================================

Notes:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.

"""

