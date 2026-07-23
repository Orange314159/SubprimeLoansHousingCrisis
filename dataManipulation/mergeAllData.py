import polars as pl
import sys 
## I will combine the data from reduced data combined and the merged housing data

loan_file = sys.argv[1]
## loan_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/HMDA_Combined.csv")
loan_data = pl.read_csv(f"{loan_file}")

housing_socio_file = sys.argv[2]
##  housing_socio_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/reducedHousing.csv")
housing_socio_data = pl.read_csv(f"{housing_socio_file}")

race_file = sys.argv[3]
## race_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/reducedRace.csv")
race_data = pl.read_csv(f"{race_file}")

school_file = sys.argv[4]
## school_data = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/ReducedData/reducedSchool.csv")
school_data = pl.read_csv(f"{school_file}")

## Check to make sure it works

print(loan_data.head())
print(housing_socio_data.head())
print(race_data.head())
print(school_data.head())


result = loan_data.join(housing_socio_data, on="GISJOIN", how="inner")
result = result.join(race_data, on="GISJOIN", how="inner")
result = result.join(school_data, on="GISJOIN", how="inner")

print(result.head())

result.write_csv("merged_all_data.csv")

