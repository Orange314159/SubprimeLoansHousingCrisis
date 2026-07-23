import sys
import polars as pl

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


input_file    = sys.argv[1]
output_file   = sys.argv[2]
schema_number = int(sys.argv[3])

schemas = [schema_2007, schema_2008, schema_2009, schema_2010]

print("-" * 20)
print(f"Normalizing {input_file}")

df = pl.read_csv(input_file, schema=schemas[schema_number])


df_normal = df.select(['as_of_year', 'loan_type', 'census_tract_number', 'applicant_income_000s', 'applicant_race_1', 'rate_spread', 'hoepa_status', 'loan_amount_000s', 'state_code', 'county_code'])

df_normal.write_csv(output_file)

print(f"{output_file} has been normalized")
