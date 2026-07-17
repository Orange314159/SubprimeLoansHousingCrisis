import polars as pl 

df = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/HousingData/clean_merged_data.csv")

header_map = {
    "B25002": "OccupancyStatus",
    "B25009": "TenureByHouseholdSize",
    "B25021": "MedianNumberOfRoomsByTenure",
    "B25024": "UnitsInStructure",
    "B25032": "TenureByUnitsInStructure",
    "B25036": "TenureByYearStructureBuilt",
    "B25037": "MedianYearStructureBuiltByTenure",
    "B25041": "Bedrooms",
    "B25042": "TenureByBedrooms",
    "B25056": "ContractRent",
    "B25058": "MedianContractRent",
    "B25068": "BedroomsByGrossRent",
    "B25077": "MedianValue",
    "B25097": "MortgageStatusByMedianValue(Dollars)",
    "B25123": "TenureBySelectedPhysicalAndFinancialConditions",
    ## End of Housing Header Map 
    "B08013": "AggregateTravelTimeToWorkOfWorkersBySex",
    "B08303": "TravelTimeToWork",
    "B17019": "PovertyStatusInThePast12MonthsOfFamiliesByHouseholdTypeByTenure",
    "B17021": "PovertyStatusOfIndividualsInThePast12MonthsByLivingArrangement",
    "B19001": "HouseholdIncomeInThePast12Months",
    "B19013": "MedianHouseholdIncomeInThePast12Months",
    "B19025": "AggregateHouseholdIncomeInThePast12Months",
    "B19113": "MedianFamilyIncomeInThePast12Months",
    "B19202": "MedianNon-familyHouseholdIncomeInThePast12Months",
    "B23001": "SexByAgeByEmploymentStatusForThePopulation16YearsAndOver",
    "B25014": "TenureByOccupantsPerRoom",
    "B25026": "TotalPopulationInOccupiedHousingUnitsByTenureByYearHouseholderMovedIntoUnit",
    "B25106": "TenureByHousingCostsAsAPercentageOfHouseholdIncomeInThePast12Months",
    "C24010": "SexByOccupationForTheCivilianEmployedPopulation16YearsAndOver",
    "B20004": "MedianEarningsInThePast12Months(In2015Inflation-AdjustedDollars)BySexByEducationalAttainmentForThePopulation25YearsAndOver",
    "B23006": "EducationalAttainmentByEmploymentStatusForThePopulation25To64Years",
    "B24021": "OccupationByMedianEarningsInThePast12Months(In2015Inflation-AdjustedDollars)ForTheFull-TimeYear-RoundCivilianEmployedPopulation16YearsAndOver"
    ## End of Socioeconomic Header Map 
}

## I don't think pl rename would work because the headers have suffixes... might be wrong
exact_rename_map = {}
for col in df.columns:
    for prefix, descriptive_name in header_map.items():
        if col.startswith(prefix):
            exact_rename_map[col] = col.replace(prefix, descriptive_name)
            break

df_updated = df.rename(exact_rename_map, strict=False)

df_updated.write_csv("merged_housing_2.csv")
