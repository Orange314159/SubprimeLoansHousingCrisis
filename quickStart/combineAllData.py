import polars as pl
import sys

loan_file = sys.argv[1]
loan_data = pl.read_csv(f"{loan_file}")

housing_socio_file = sys.argv[2]
housing_socio_data = pl.read_csv(f"{housing_socio_file}")

race_file = sys.argv[3]
race_data = pl.read_csv(f"{race_file}")

school_file = sys.argv[4]
school_data = pl.read_csv(f"{school_file}")

output_file = sys.argv[5]

result = loan_data.join(housing_socio_data, on="GISJOIN", how="inner")
result = result.join(race_data, on="GISJOIN", how="inner")
result = result.join(school_data, on="GISJOIN", how="inner")



result.write_csv(output_file)

print("All Complete!!")
