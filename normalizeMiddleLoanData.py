import polars as pl

## I will include the schema for each year so the loading of the files happens much faster


schema_2006 = {
    'activity_year': pl.Int64, 'respondent_id': pl.String, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 
    'loan_purpose': pl.Int64, 'occupancy': pl.Int64, 'loan_amount': pl.Int64, 'action_taken': pl.Int64, 
    'msamd': pl.Int64, 'state_code': pl.Int64, 'county_code': pl.Int64, 'census_tract': pl.Float64, 
    'applicant_sex': pl.Int64, 'co_applicant_sex': pl.Int64, 'income': pl.String, 'purchaser_type': pl.Int64, 
    'denial_reason_1': pl.Int64, 'denial_reason_2': pl.Int64, 'denial_reason_3': pl.String, 
    'edit_status': pl.Int64, 'property_type': pl.Int64, 'preapproval': pl.Int64, 
    'applicant_ethnicity': pl.Int64, 'co_applicant_ethnicity': pl.Int64, 'applicant_race_1': pl.Int64, 
    'applicant_race_2': pl.Int64, 'applicant_race_3': pl.Int64, 'applicant_race_4': pl.Int64, 
    'applicant_race_5': pl.Int64, 'co_applicant_race_1': pl.Int64, 'co_applicant_race_2': pl.Int64, 
    'co_applicant_race_3': pl.Int64, 'co_applicant_race_4': pl.Int64, 'co_applicant_race_5': pl.Int64, 
    'rate_spread': pl.Float64, 'hoepa_status': pl.Int64, 'lien_status': pl.Int64, 'sequence_number': pl.Int64
}

schema_2005 = {
    'activity_year': pl.Int64, 'respondent_id': pl.String, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 
    'loan_purpose': pl.Int64, 'occupancy': pl.Int64, 'loan_amount': pl.Int64, 'action_taken': pl.Int64, 
    'msamd': pl.Int64, 'state_code': pl.Int64, 'county_code': pl.Int64, 'census_tract': pl.Float64, 
    'applicant_sex': pl.Int64, 'co_applicant_sex': pl.Int64, 'income': pl.String, 'purchaser_type': pl.Int64, 
    'denial_reason_1': pl.Int64, 'denial_reason_2': pl.Int64, 'denial_reason_3': pl.String, 
    'edit_status': pl.Int64, 'property_type': pl.Int64, 'preapproval': pl.Int64, 
    'applicant_ethnicity': pl.Int64, 'co_applicant_ethnicity': pl.Int64, 'applicant_race_1': pl.Int64, 
    'applicant_race_2': pl.Int64, 'applicant_race_3': pl.Int64, 'applicant_race_4': pl.Int64, 
    'applicant_race_5': pl.Int64, 'co_applicant_race_1': pl.Int64, 'co_applicant_race_2': pl.Int64, 
    'co_applicant_race_3': pl.Int64, 'co_applicant_race_4': pl.Int64, 'co_applicant_race_5': pl.Int64, 
    'rate_spread': pl.Float64, 'hoepa_status': pl.Int64, 'lien_status': pl.Int64, 'sequence_number': pl.Int64
}

schema_2004 = {
    'activity_year': pl.Int64, 'respondent_id': pl.String, 'agency_code': pl.Int64, 'loan_type': pl.Int64, 
    'loan_purpose': pl.Int64, 'occupancy': pl.Int64, 'loan_amount': pl.Int64, 'action_taken': pl.Int64, 
    'msamd': pl.Int64, 'state_code': pl.String, 'county_code': pl.Int64, 'census_tract': pl.Float64, 
    'applicant_sex': pl.Int64, 'co_applicant_sex': pl.Int64, 'income': pl.String, 'purchaser_type': pl.Int64, 
    'denial_reason_1': pl.Int64, 'denial_reason_2': pl.Int64, 'denial_reason_3': pl.String, 
    'edit_status': pl.Int64, 'property_type': pl.Int64, 'preapproval': pl.Int64, 
    'applicant_ethnicity': pl.Int64, 'co_applicant_ethnicity': pl.Int64, 'applicant_race_1': pl.Int64, 
    'applicant_race_2': pl.Int64, 'applicant_race_3': pl.Int64, 'applicant_race_4': pl.Int64, 
    'applicant_race_5': pl.Int64, 'co_applicant_race_1': pl.Int64, 'co_applicant_race_2': pl.Int64, 
    'co_applicant_race_3': pl.Int64, 'co_applicant_race_4': pl.Int64, 'co_applicant_race_5': pl.Int64, 
    'rate_spread': pl.Float64, 'hoepa_status': pl.Int64, 'lien_status': pl.Int64, 'sequence_number': pl.Int64
}

## Now this is how you select which file you want to read 
file_number = 2004
file_name = f"/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/LoanData/HMDA_DATA_SET/HMDA_{file_number}/HMDA_{file_number}.csv"


df = pl.read_csv(file_name, schema=schema_2004)


df_normal = df.select(['activity_year', 'loan_type', 'census_tract', 'income', 'applicant_race_1', 'rate_spread',
                       'hoepa_status', 'loan_amount', 'state_code', 'county_code'])

print(df_normal.head())

df_normal.write_csv("HMDA_2004_NORMAL.csv")



