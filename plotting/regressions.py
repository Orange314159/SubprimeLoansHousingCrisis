import pandas                         as pd
import statsmodels.formula.api        as smf
from   statsmodels.iolib.summary2 import summary_col
import sys


file_name = sys.argv[1]
data = pd.read_csv(f"{file_name}")

def run_block_models(df, dependent_variable, independent_variables):
    formula = f"{dependent_variable} ~ {independent_variables}" ##  depending on what variables are being used, the formula might look different

    model = smf.ols(formula, data=df).fit(cov_type='HC3') ## I saw online that HC3 was good for controlling for heteroskedasticity
    return model

def generate_regression_table(models, names_models, variables, title="Regression Results"):
    regression_table = summary_col(
        models,
        stars=True, ## this makes it look fun! 
        model_names=names_models,
        info_dict = { 
            'N':              lambda x: f"{int(x.nobs)}",
            'R-squared':      lambda x: f"{x.rsquared:.3f}",
            'Adj. R-squared': lambda x: f"{x.rsquared_adj:.3f}"
        }, 
        regressor_order=variables
    )

    regression_table.title = title
    return regression_table


economic_variables = 'Unemployment_PCT + Poverty_Rate_PCT + Median_Household_Income'
demographic_variables = 'white_pct + black_pct + hispanic_pct + undergrad_pct'

model_overcrowding_baseline = run_block_models(data, 'Overcrowding_Rate', 'pct_subprime')
model_overcrowding_economic = run_block_models(data, 'Overcrowding_Rate', f'{economic_variables} + pct_subprime')
model_overcrowding_deomgrap = run_block_models(data, 'Overcrowding_Rate', f'{demographic_variables} + pct_subprime')
model_overcrowding_all      = run_block_models(data, 'Overcrowding_Rate', f'{demographic_variables} + {economic_variables} + pct_subprime')

economic_variables_l = ['Unemployment_PCT', 'Poverty_Rate_PCT', 'Median_Household_Income']
demographic_variables_l = ['white_pct', 'black_pct', 'hispanic_pct', 'undergrad_pct'] 

models = [model_overcrowding_baseline, model_overcrowding_economic, model_overcrowding_deomgrap, model_overcrowding_all]
names = ['Baseline', '(2)', '(3)', '(4)']

variables = economic_variables_l + demographic_variables_l + ['pct_subprime']
table = generate_regression_table(models, names, variables, title="Regression Results (Overcrowding Rate)")  
print(table)

print("Aliases:")
print("(2) --> Baseline + Economic")
print("(3) --> Baseline + Demographic")
print("(4) --> All Variables")

model_cost_baseline = run_block_models(data, 'Cost_Burden_PCT', 'pct_subprime')
model_cost_economic = run_block_models(data, 'Cost_Burden_PCT', f'{economic_variables} + pct_subprime')
model_cost_deomgrap = run_block_models(data, 'Cost_Burden_PCT', f'{demographic_variables} + pct_subprime')
model_cost_all      = run_block_models(data, 'Cost_Burden_PCT', f'{demographic_variables} + {economic_variables} + pct_subprime')

economic_variables_l = ['Unemployment_PCT', 'Poverty_Rate_PCT', 'Median_Household_Income']
demographic_variables_l = ['white_pct', 'black_pct', 'hispanic_pct', 'undergrad_pct'] 

models_cost = [model_cost_baseline, model_cost_economic, model_cost_deomgrap, model_cost_all]
names = ['Baseline', '(2)', '(3)', '(4)']

variables = economic_variables_l + demographic_variables_l + ['pct_subprime']
table = generate_regression_table(models, names, variables, title="Regression Results (Cost Burden)")  
print(table)

print("Aliases:")
print("(2) --> Baseline + Economic")
print("(3) --> Baseline + Demographic")
print("(4) --> All Variables")


"""
             Regression Results (Overcrowding Rate)
=================================================================
                         Baseline    (2)       (3)        (4)    
-----------------------------------------------------------------
Unemployment_PCT                  -0.0002**            -0.0008***
                                  (0.0001)             (0.0001)  
Poverty_Rate_PCT                  0.0009***            0.0002*** 
                                  (0.0000)             (0.0000)  
Median_Household_Income           0.0000***            0.0000*** 
                                  (0.0000)             (0.0000)  
white_pct                                   -0.0013*** -0.0013***
                                            (0.0000)   (0.0000)  
black_pct                                   -0.0012*** -0.0011***
                                            (0.0000)   (0.0000)  
hispanic_pct                                -0.0002*** -0.0002***
                                            (0.0000)   (0.0000)  
undergrad_pct                               -0.0004*** -0.0005***
                                            (0.0000)   (0.0000)  
pct_subprime            0.1562*** 0.1029*** 0.0062     0.0024    
                        (0.0048)  (0.0065)  (0.0074)   (0.0073)  
Intercept               0.0138*** 0.0039*** 0.1438***  0.1425*** 
                        (0.0005)  (0.0012)  (0.0028)   (0.0030)  
R-squared               0.0270    0.0581    0.3968     0.4044    
R-squared Adj.          0.0270    0.0580    0.3967     0.4043    
Adj. R-squared          0.027     0.058     0.397      0.404     
N                       44611     44489     44611      44489     
R-squared               0.027     0.058     0.397      0.404     
=================================================================
Standard errors in parentheses.
* p<.1, ** p<.05, ***p<.01
Aliases:
(2) --> Baseline + Economic
(3) --> Baseline + Demographic
(4) --> All Variables
                Regression Results (Cost Burden)
=================================================================
                         Baseline    (2)       (3)        (4)    
-----------------------------------------------------------------
Unemployment_PCT                  -0.0002**            -0.0008***
                                  (0.0001)             (0.0001)  
Poverty_Rate_PCT                  0.0009***            0.0002*** 
                                  (0.0000)             (0.0000)  
Median_Household_Income           0.0000***            0.0000*** 
                                  (0.0000)             (0.0000)  
white_pct                                   -0.0013*** -0.0013***
                                            (0.0000)   (0.0000)  
black_pct                                   -0.0012*** -0.0011***
                                            (0.0000)   (0.0000)  
hispanic_pct                                -0.0002*** -0.0002***
                                            (0.0000)   (0.0000)  
undergrad_pct                               -0.0004*** -0.0005***
                                            (0.0000)   (0.0000)  
pct_subprime            0.1562*** 0.1029*** 0.0062     0.0024    
                        (0.0048)  (0.0065)  (0.0074)   (0.0073)  
Intercept               0.0138*** 0.0039*** 0.1438***  0.1425*** 
                        (0.0005)  (0.0012)  (0.0028)   (0.0030)  
R-squared               0.0270    0.0581    0.3968     0.4044    
R-squared Adj.          0.0270    0.0580    0.3967     0.4043    
Adj. R-squared          0.027     0.058     0.397      0.404     
N                       44611     44489     44611      44489     
R-squared               0.027     0.058     0.397      0.404     
=================================================================
Standard errors in parentheses.
* p<.1, ** p<.05, ***p<.01
Aliases:
(2) --> Baseline + Economic
(3) --> Baseline + Demographic
(4) --> All Variables
"""

