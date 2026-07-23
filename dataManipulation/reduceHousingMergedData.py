import polars as pl

## I will add / remove any cols that I need or don't 

## important cols

## = = = = = = = = Geographical data = = = = = = = = ##

## GEOID --> need to add a G as prefix to col so it works with my other data


## = = = = = = = = Housing Insecurity  = = = = = = = ##

## Overcrowding comes from 
    # TenureByOccupantsPerRoom_MODCROWD_O +
    # TenureByOccupantsPerRoom_SEVCROWD_O +
    # TenureByOccupantsPerRoom_MODCROWD_R +
    # TenureByOccupantsPerRoom_SEVCROWD_R +
    # and all divided by Total Households

## Cost Burden comes from 
    # TenureByHousingCostsAsAPercentageOfHouseholdIncomeInThePast12Months_CB_GT35_PCT


## = = = = = = = = Other Factors = = = = = = = = = = ##

## Unemployment comes from 
    # SexByAgeByEmploymentStatusForThePopulation16YearsAndOver_UE_PCT

## Poverty Rate comes from 
    # PovertyStatusOfIndividualsInThePast12MonthsByLivingArrangementEST2_PCT --> pct that have income below Poverty line in the past 12 months 

## Education 
    # EducationalAttainmentByEmploymentStatusForThePopulation25To64YearsEST1 --> Total 
    # EducationalAttainmentByEmploymentStatusForThePopulation25To64YearsEST23 --> Bachelor's or Higher
    # then find percent of EST23 out of EST1

## Income comes from 
    # MedianHouseholdIncomeInThePast12MonthsEST1 --> Median Household income 
import sys 

file_name = sys.argv[1] 
## df = pl.read_csv("/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/HousingData/merged_housing_2.csv")
df = pl.read_csv(f"{file_name}")

df_reduced = df.select(
    ## add the G to the beginning 
    (pl.lit("G")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(0, 2)
        + pl.lit("0")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(2, 3)
        + pl.lit("0")
        + pl.col("GEOID").cast(pl.String).str.zfill(11).str.slice(5, 6)
    ).alias("GISJOIN"),


    ((
        pl.col("TenureByOccupantsPerRoom_MODCROWD_O")
        + pl.col("TenureByOccupantsPerRoom_SEVCROWD_O")
        + pl.col("TenureByOccupantsPerRoom_MODCROWD_R")
        + pl.col("TenureByOccupantsPerRoom_SEVCROWD_R")
    )   / pl.col("OccupancyStatusEST1")
    ).alias("Overcrowding_Rate"),
    
    ## we will let the cost burden happen at 35 percent
    pl.col("TenureByHousingCostsAsAPercentageOfHouseholdIncomeInThePast12Months_CB_GT35_PCT")
    .alias("Cost_Burden_PCT"),
    
    ## this is regular U3 unemployment 
    pl.col("SexByAgeByEmploymentStatusForThePopulation16YearsAndOver_UE_PCT")
    .alias("Unemployment_PCT"),
    
    ## poverty 
    pl.col("PovertyStatusOfIndividualsInThePast12MonthsByLivingArrangementEST2_PCT")
    .alias("Poverty_Rate_PCT"),
    
    ## percent that get Bachelors or higher
    (
        pl.col("EducationalAttainmentByEmploymentStatusForThePopulation25To64YearsEST27")
    ).alias("Bachelors_Or_Higher_PCT"),
    
    ## income 
    pl.col("MedianHouseholdIncomeInThePast12MonthsEST1")
    .alias("Median_Household_Income")
)


print(df_reduced.head())

##df_reduced.write_csv('/home/matt/Desktop/Projects/SubprimeLoansHousingCrisis/reducedHousing.csv')
df_reduced.write_csv('reducedHousing.csv')


