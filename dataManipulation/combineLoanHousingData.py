import polars as pl

## I will combine the data from reduced data combined and the merged housing data

loan_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/HMDA_Combined.csv")

housing_socio_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/reducedHousing.csv")

## Check to make sure it works

print(loan_data.head())
print(housing_socio_data.head())

result = loan_data.join(housing_socio_data, on="GISJOIN", how="inner")

print(result.head())

result.write_csv("merged_loan_housing_data.csv")

