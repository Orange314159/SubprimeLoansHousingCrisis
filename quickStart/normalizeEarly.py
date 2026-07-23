import polars as pl
import sys

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



input_file    = sys.argv[1]
output_file   = sys.argv[2]
schema_number = int(sys.argv[3])

schemas = [schema_2000, schema_2001, schema_2002, schema_2003]

print("-" * 20)
print(f"Normalizing {input_file}")
df = pl.read_csv(input_file, schema=schemas[schema_number])

df_normal = df.select(['activity_year', 'agency_code', 'loan_type', 'loan_amount', 'census_tract', 'income',
                       'applicant_race_1', 'state_code', 'county_code'])

df_normal.write_csv(output_file)
print(f"{output_file} has been normalized")
