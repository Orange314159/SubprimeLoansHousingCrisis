import polars as pl
import sys 
## I will include the schema for each year so the loading of the files happens much faster

schema_2003 = {
    'activity_year': pl.Int64, 'respondent_id': pl.String, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 
    'loan_purpose': pl.Int64, 'occupancy_type': pl.Int64, 'loan_amount': pl.String, 'action_taken': pl.Int64, 
    'msamd': pl.String, 'state_code': pl.String, 'county_code': pl.String, 'census_tract': pl.String, 
    'applicant_race_1': pl.Int64, 'co_applicant_race_1': pl.Int64, 'applicant_sex': pl.Int64, 
    'co_applicant_sex': pl.Int64, 'income': pl.String, 'purchaser_type': pl.Int64, 'denial_reason_1': pl.Int64, 
    'denial_reason_2': pl.Int64, 'denial_reason_3': pl.Int64, 'edit_status': pl.Int64, 
    'sequence_number': pl.Int64
}

schema_2002 = {
    'activity_year': pl.Int64, 'respondent_id': pl.String, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 
    'loan_purpose': pl.Int64, 'occupancy_type': pl.Int64, 'loan_amount': pl.String, 'action_taken': pl.Int64, 
    'msamd': pl.String, 'state_code': pl.String, 'county_code': pl.String, 'census_tract': pl.String, 
    'applicant_race_1': pl.Int64, 'co_applicant_race_1': pl.Int64, 'applicant_sex': pl.Int64, 
    'co_applicant_sex': pl.Int64, 'income': pl.String, 'purchaser_type': pl.Int64, 'denial_reason_1': pl.Int64,
    'denial_reason_2': pl.Int64, 'denial_reason_3': pl.Int64, 'edit_status': pl.Int64, 
    'sequence_number': pl.Int64
}

schema_2001 = {
    'activity_year': pl.Int64, 'respondent_id': pl.String, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 
    'loan_purpose': pl.Int64, 'occupancy_type': pl.Int64, 'loan_amount': pl.String, 'action_taken': pl.Int64, 
    'msamd': pl.String, 'state_code': pl.String, 'county_code': pl.String, 'census_tract': pl.String, 
    'applicant_race_1': pl.Int64, 'co_applicant_race_1': pl.Int64, 'applicant_sex': pl.Int64, 
    'co_applicant_sex': pl.Int64, 'income': pl.String, 'purchaser_type': pl.Int64, 'denial_reason_1': pl.Int64, 
    'denial_reason_2': pl.Int64, 'denial_reason_3': pl.Int64, 'edit_status': pl.Int64, 
    'sequence_number': pl.Int64
}

schema_2000 = {
    'activity_year': pl.Int64, 'respondent_id': pl.String, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 
    'loan_purpose': pl.Int64, 'occupancy_type': pl.Int64, 'loan_amount': pl.String, 'action_taken': pl.Int64, 
    'msamd': pl.String, 'state_code': pl.String, 'county_code': pl.String, 'census_tract': pl.String, 
    'applicant_race_1': pl.Int64, 'co_applicant_race_1': pl.Int64, 'applicant_sex': pl.Int64, 
    'co_applicant_sex': pl.Int64, 'income': pl.String, 'purchaser_type': pl.Int64, 'denial_reason_1': pl.Int64, 
    'denial_reason_2': pl.Int64, 'denial_reason_3': pl.Int64, 'edit_status': pl.Int64, 
    'sequence_number': pl.Int64
}



## Now this is how you select which file you want to read 
# file_number = 2000
# file_name = f"/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/LoanData/HMDA_DATA_SET/HMDA_{file_number}/HMDA_{file_number}.csv"

file_name = sys.argv[1]

df = pl.read_csv(file_name, schema=schema_2000)

df_normal = df.select(['activity_year', 'agency_code', 'loan_type', 'loan_amount', 'census_tract', 'income', 
                       'applicant_race_1', 'state_code', 'county_code'])

print(df_normal.head())

df_normal.write_csv("HMDA_2000_NORMAL.csv")

