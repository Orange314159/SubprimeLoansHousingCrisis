import sys
import polars as pl

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


input_file    = sys.argv[1]
output_file   = sys.argv[2]
schema_number = int(sys.argv[3])

print("-" * 20)
print(f"Normalizing {input_file}")

schemas = [schema_2004, schema_2005, schema_2006]

df = pl.read_csv(input_file, schema=schemas[schema_number])

df_normal = df.select(['activity_year', 'loan_type', 'census_tract', 'income', 'applicant_race_1', 'rate_spread',
                       'hoepa_status', 'loan_amount', 'state_code', 'county_code'])


df_normal.write_csv(output_file)

print(f"{output_file} has been normalized")
