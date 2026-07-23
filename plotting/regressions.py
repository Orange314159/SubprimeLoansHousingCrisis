import numpy                          as np 
import pandas                         as pd 
import statsmodels.api                as sm 
import statsmodels.formula.api        as smf
from   statsmodels.iolib.summary2 import summary_col
import sys 

file_name = sys.argv[1]

data = pd.read_csv(f"{file_name}")
## data = pd.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/merged_all_data.csv")


def run_block_models(df, dependent_variable, independent_variables):
    
    formula = f"{dependent_variable} ~ {independent_variables}" ## depending on what variables are being used, the formula might look different

    model = smf.ols(formula, data=df).fit(cov_type='HC3') ## I saw online that HC3 was good for controlling for heteroskedasticity

    return model

def generate_regression_table(models, names_models, variables, title="Regression Results"):
    regression_table = summary_col(
        models,
        stars=True, ## this makes it look fun!
        model_names=names_models,
        info_dict = { ## use lambda for each of the individual models 
            'N':              lambda x: f"{int(n.nobs)}",
            'R-squared':      lambda x: f"{x.rsquared:.3f}",
            'Adj. R-squared': lambda x: f"{x.rsquared_adj:.3f}"
        }, 
        regressor_order=variables
    )

    regression_table.title = title
    return regression_table


economic_variables = ['Unemployment_PCT','Poverty_Rate_PCT','Median_Household_Income']
demographic_variables = ['white_pct', 'black_pct', 'hispanic_pct', 'undergrad_pct']

model_overcrowding_baseline = run_block_models(data, '', '')


