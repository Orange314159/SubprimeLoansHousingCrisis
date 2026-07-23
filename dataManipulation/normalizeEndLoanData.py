import sys
import polars as pl

## I will include the schema for each year so the loading of the files happens much faster

schema_2010 = {
    'as_of_year': pl.Int64, 'respondent_id': pl.String, 'agency_name': pl.String, 
    'agency_abbr': pl.String, 'agency_code': pl.Int64, 'loan_type_name': pl.String, 'loan_type': pl.Int64, 
    'property_type_name': pl.String, 'property_type': pl.Int64, 'loan_purpose_name': pl.String, 
    'loan_purpose': pl.Int64, 'owner_occupancy_name': pl.String, 'owner_occupancy': pl.Int64, 
    'loan_amount_000s': pl.Int64, 'preapproval_name': pl.String, 'preapproval': pl.Int64, 
    'action_taken_name': pl.String, 'action_taken': pl.Int64, 'msamd_name': pl.String, 'msamd': pl.Int64, 
    'state_name': pl.String, 'state_abbr': pl.String, 'state_code': pl.Int64, 'county_name': pl.String, 
    'county_code': pl.Int64, 'census_tract_number': pl.Float64, 'applicant_ethnicity_name': pl.String, 
    'applicant_ethnicity': pl.Int64, 'co_applicant_ethnicity_name': pl.String, 
    'co_applicant_ethnicity': pl.Int64, 'applicant_race_name_1': pl.String, 'applicant_race_1': pl.Int64, 
    'applicant_race_name_2': pl.String, 'applicant_race_2': pl.String, 'applicant_race_name_3': pl.String, 
    'applicant_race_3': pl.String, 'applicant_race_name_4': pl.String, 'applicant_race_4': pl.String, 
    'applicant_race_name_5': pl.String, 'applicant_race_5': pl.String, 'co_applicant_race_name_1': pl.String, 
    'co_applicant_race_1': pl.Int64, 'co_applicant_race_name_2': pl.String, 'co_applicant_race_2': pl.String, 
    'co_applicant_race_name_3': pl.String, 'co_applicant_race_3': pl.String, 
    'co_applicant_race_name_4': pl.String, 'co_applicant_race_4': pl.String, 
    'co_applicant_race_name_5': pl.String, 'co_applicant_race_5': pl.String, 'applicant_sex_name': pl.String, 
    'applicant_sex': pl.Int64, 'co_applicant_sex_name': pl.String, 'co_applicant_sex': pl.Int64, 
    'applicant_income_000s': pl.Int64, 'purchaser_type_name': pl.String, 'purchaser_type': pl.Int64, 
    'denial_reason_name_1': pl.String, 'denial_reason_1': pl.String, 'denial_reason_name_2': pl.String, 
    'denial_reason_2': pl.String, 'denial_reason_name_3': pl.String, 'denial_reason_3': pl.String, 
    'rate_spread': pl.Float64, 'hoepa_status_name': pl.String, 'hoepa_status': pl.Int64, 
    'lien_status_name': pl.String, 'lien_status': pl.Int64, 'edit_status_name': pl.String, 
    'edit_status': pl.Int64, 'sequence_number': pl.Int64, 'population': pl.Int64, 
    'minority_population': pl.Float64, 'hud_median_family_income': pl.Int64, 
    'tract_to_msamd_income': pl.Float64, 'number_of_owner_occupied_units': pl.Int64, 
    'number_of_1_to_4_family_units': pl.Int64, 'application_date_indicator': pl.Int64
}

schema_2009 = {
    'as_of_year': pl.Int64, 'respondent_id': pl.String, 'agency_name': pl.String, 
    'agency_abbr': pl.String, 'agency_code': pl.Int64, 'loan_type_name': pl.String, 'loan_type': pl.Int64, 
    'property_type_name': pl.String, 'property_type': pl.Int64, 'loan_purpose_name': pl.String, 
    'loan_purpose': pl.Int64, 'owner_occupancy_name': pl.String, 'owner_occupancy': pl.Int64, 
    'loan_amount_000s': pl.Int64, 'preapproval_name': pl.String, 'preapproval': pl.Int64, 
    'action_taken_name': pl.String, 'action_taken': pl.Int64, 'msamd_name': pl.String, 'msamd': pl.Int64, 
    'state_name': pl.String, 'state_abbr': pl.String, 'state_code': pl.Int64, 'county_name': pl.String, 
    'county_code': pl.Int64, 'census_tract_number': pl.Float64, 'applicant_ethnicity_name': pl.String, 
    'applicant_ethnicity': pl.Int64, 'co_applicant_ethnicity_name': pl.String, 
    'co_applicant_ethnicity': pl.Int64, 'applicant_race_name_1': pl.String, 'applicant_race_1': pl.Int64, 
    'applicant_race_name_2': pl.String, 'applicant_race_2': pl.String, 'applicant_race_name_3': pl.String, 
    'applicant_race_3': pl.String, 'applicant_race_name_4': pl.String, 'applicant_race_4': pl.String, 
    'applicant_race_name_5': pl.String, 'applicant_race_5': pl.String, 'co_applicant_race_name_1': pl.String, 
    'co_applicant_race_1': pl.Int64, 'co_applicant_race_name_2': pl.String, 'co_applicant_race_2': pl.String, 
    'co_applicant_race_name_3': pl.String, 'co_applicant_race_3': pl.String, 
    'co_applicant_race_name_4': pl.String, 'co_applicant_race_4': pl.String, 
    'co_applicant_race_name_5': pl.String, 'co_applicant_race_5': pl.String, 'applicant_sex_name': pl.String, 
    'applicant_sex': pl.Int64, 'co_applicant_sex_name': pl.String, 'co_applicant_sex': pl.Int64, 
    'applicant_income_000s': pl.Int64, 'purchaser_type_name': pl.String, 'purchaser_type': pl.Int64, 
    'denial_reason_name_1': pl.String, 'denial_reason_1': pl.String, 'denial_reason_name_2': pl.String, 
    'denial_reason_2': pl.String, 'denial_reason_name_3': pl.String, 'denial_reason_3': pl.String, 
    'rate_spread': pl.Float64, 'hoepa_status_name': pl.String, 'hoepa_status': pl.Int64, 
    'lien_status_name': pl.String, 'lien_status': pl.Int64, 'edit_status_name': pl.String, 
    'edit_status': pl.Int64, 'sequence_number': pl.Int64, 'population': pl.Int64, 
    'minority_population': pl.Float64, 'hud_median_family_income': pl.Int64, 
    'tract_to_msamd_income': pl.Float64, 'number_of_owner_occupied_units': pl.Int64, 
    'number_of_1_to_4_family_units': pl.Int64, 'application_date_indicator': pl.Int64
}

schema_2008 = {
    'as_of_year': pl.Int64, 'respondent_id': pl.String, 'agency_name': pl.String, 
    'agency_abbr': pl.String, 'agency_code': pl.Int64, 'loan_type_name': pl.String, 'loan_type': pl.Int64, 
    'property_type_name': pl.String, 'property_type': pl.Int64, 'loan_purpose_name': pl.String, 
    'loan_purpose': pl.Int64, 'owner_occupancy_name': pl.String, 'owner_occupancy': pl.Int64, 
    'loan_amount_000s': pl.Int64, 'preapproval_name': pl.String, 'preapproval': pl.Int64, 
    'action_taken_name': pl.String, 'action_taken': pl.Int64, 'msamd_name': pl.String, 'msamd': pl.Int64, 
    'state_name': pl.String, 'state_abbr': pl.String, 'state_code': pl.Int64, 'county_name': pl.String, 
    'county_code': pl.Int64, 'census_tract_number': pl.Float64, 'applicant_ethnicity_name': pl.String, 
    'applicant_ethnicity': pl.Int64, 'co_applicant_ethnicity_name': pl.String, 
    'co_applicant_ethnicity': pl.Int64, 'applicant_race_name_1': pl.String, 'applicant_race_1': pl.Int64, 
    'applicant_race_name_2': pl.String, 'applicant_race_2': pl.String, 'applicant_race_name_3': pl.String, 
    'applicant_race_3': pl.String, 'applicant_race_name_4': pl.String, 'applicant_race_4': pl.String, 
    'applicant_race_name_5': pl.String, 'applicant_race_5': pl.String, 'co_applicant_race_name_1': pl.String, 
    'co_applicant_race_1': pl.Int64, 'co_applicant_race_name_2': pl.String, 'co_applicant_race_2': pl.Int64, 
    'co_applicant_race_name_3': pl.String, 'co_applicant_race_3': pl.String, 
    'co_applicant_race_name_4': pl.String, 'co_applicant_race_4': pl.String, 
    'co_applicant_race_name_5': pl.String, 'co_applicant_race_5': pl.String, 'applicant_sex_name': pl.String, 
    'applicant_sex': pl.Int64, 'co_applicant_sex_name': pl.String, 'co_applicant_sex': pl.Int64, 
    'applicant_income_000s': pl.Int64, 'purchaser_type_name': pl.String, 'purchaser_type': pl.Int64, 
    'denial_reason_name_1': pl.String, 'denial_reason_1': pl.String, 'denial_reason_name_2': pl.String, 
    'denial_reason_2': pl.String, 'denial_reason_name_3': pl.String, 'denial_reason_3': pl.String, 
    'rate_spread': pl.Float64, 'hoepa_status_name': pl.String, 'hoepa_status': pl.Int64, 
    'lien_status_name': pl.String, 'lien_status': pl.Int64, 'edit_status_name': pl.String, 
    'edit_status': pl.Int64, 'sequence_number': pl.Int64, 'population': pl.Int64, 
    'minority_population': pl.Float64, 'hud_median_family_income': pl.Int64, 
    'tract_to_msamd_income': pl.Float64, 'number_of_owner_occupied_units': pl.Int64, 
    'number_of_1_to_4_family_units': pl.Int64, 'application_date_indicator': pl.Int64
}

schema_2007 = {
    'as_of_year': pl.Int64, 'respondent_id': pl.String, 'agency_name': pl.String, 
    'agency_abbr': pl.String, 'agency_code': pl.Int64, 'loan_type_name': pl.String, 'loan_type': pl.Int64, 
    'property_type_name': pl.String, 'property_type': pl.Int64, 'loan_purpose_name': pl.String, 
    'loan_purpose': pl.Int64, 'owner_occupancy_name': pl.String, 'owner_occupancy': pl.Int64, 
    'loan_amount_000s': pl.Int64, 'preapproval_name': pl.String, 'preapproval': pl.Int64, 
    'action_taken_name': pl.String, 'action_taken': pl.Int64, 'msamd_name': pl.String, 'msamd': pl.Int64, 
    'state_name': pl.String, 'state_abbr': pl.String, 'state_code': pl.Int64, 'county_name': pl.String, 
    'county_code': pl.Int64, 'census_tract_number': pl.Float64, 'applicant_ethnicity_name': pl.String, 
    'applicant_ethnicity': pl.Int64, 'co_applicant_ethnicity_name': pl.String, 
    'co_applicant_ethnicity': pl.Int64, 'applicant_race_name_1': pl.String, 'applicant_race_1': pl.Int64, 
    'applicant_race_name_2': pl.String, 'applicant_race_2': pl.String, 'applicant_race_name_3': pl.String, 
    'applicant_race_3': pl.String, 'applicant_race_name_4': pl.String, 'applicant_race_4': pl.String, 
    'applicant_race_name_5': pl.String, 'applicant_race_5': pl.String, 'co_applicant_race_name_1': pl.String, 
    'co_applicant_race_1': pl.Int64, 'co_applicant_race_name_2': pl.String, 'co_applicant_race_2': pl.String, 
    'co_applicant_race_name_3': pl.String, 'co_applicant_race_3': pl.String, 
    'co_applicant_race_name_4': pl.String, 'co_applicant_race_4': pl.String, 
    'co_applicant_race_name_5': pl.String, 'co_applicant_race_5': pl.String, 'applicant_sex_name': pl.String, 
    'applicant_sex': pl.Int64, 'co_applicant_sex_name': pl.String, 'co_applicant_sex': pl.Int64, 
    'applicant_income_000s': pl.Int64, 'purchaser_type_name': pl.String, 'purchaser_type': pl.Int64, 
    'denial_reason_name_1': pl.String, 'denial_reason_1': pl.String, 'denial_reason_name_2': pl.String, 
    'denial_reason_2': pl.String, 'denial_reason_name_3': pl.String, 'denial_reason_3': pl.String, 
    'rate_spread': pl.Float64, 'hoepa_status_name': pl.String, 'hoepa_status': pl.Int64, 
    'lien_status_name': pl.String, 'lien_status': pl.Int64, 'edit_status_name': pl.String, 
    'edit_status': pl.Int64, 'sequence_number': pl.Int64, 'population': pl.Int64, 
    'minority_population': pl.Float64, 'hud_median_family_income': pl.Int64, 
    'tract_to_msamd_income': pl.Float64, 'number_of_owner_occupied_units': pl.Int64, 
    'number_of_1_to_4_family_units': pl.Int64, 'application_date_indicator': pl.Int64
}


## Now this is how you select which file you want to read 
##file_number = 2007
file_name = sys.argv[1]
## file_name = f"/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/LoanData/HMDA_DATA_SET/HMDA_{file_number}/HMDA_{file_number}.csv"


df = pl.read_csv(file_name, schema=schema_2007)


df_normal = df.select(['as_of_year', 'loan_type', 'census_tract_number', 'applicant_income_000s', 'applicant_race_1', 'rate_spread', 'hoepa_status', 'loan_amount_000s', 'state_code', 'county_code'])

print(df_normal.head())

df_normal.write_csv("HMDA_2007_NORMAL.csv")



