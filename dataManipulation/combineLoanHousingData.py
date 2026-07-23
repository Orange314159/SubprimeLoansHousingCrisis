import polars as pl
import sys 
## I will combine the data from reduced data combined and the merged housing data

loan_file = sys.argv[1] 
housing_socio_file = sys.argv[2]

## loan_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/HMDA_Combined.csv")
loan_data = pl.read_csv(f"{loan_file}")


## housing_socio_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/reducedHousing.csv")
housing_socio_data = pl.read_csv(f"{housing_socio_file}")

## Check to make sure it works

print(loan_data.head())
print(housing_socio_data.head())

result = loan_data.join(housing_socio_data, on="GISJOIN", how="inner")

print(result.head())

result.write_csv("merged_loan_housing_data.csv")

