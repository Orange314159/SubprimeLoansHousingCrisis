import polars as pl
import time

## This is just here for benchmakring


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

schemas = [schema_2000, schema_2001, schema_2002, schema_2003, schema_2004, schema_2005, schema_2006, schema_2007, schema_2008, schema_2009, schema_2010]



## Now this is how you select which file you want to read 
start_time = time.perf_counter()
file_number = 2009
file_name = f"/home/matt/Desktop/Projects/InternshipProject/LoanData/HMDA_DATA_SET/HMDA_{file_number}/HMDA_{file_number}.csv"
schema_number = file_number - 2000 ## because index 0 of the schemas is the year 2000


df = pl.read_csv(file_name, schema=schemas[schema_number])


print(df.head)
df.clear()

## Finish timing the run
end_time = time.perf_counter()
total_time = end_time - start_time
print(f"This execution took {total_time:.6f}")

