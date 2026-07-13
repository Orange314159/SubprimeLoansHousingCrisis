# Notes On My Project

-- Matthew Robson 

## Goal of the Project

Study the long term impacts of the major increases in subprime loans in the early 2000s on the housing market in 2020-2025.


## Methodologies and Data Collection

### Data Collection

For this project we need subprime loan data from the early 2000s (2000 - 2010). For this, we will use the HMDA data set given out by the government. This data set will provide us with most of the information that is needed to classify different regions based on the percentage of subprime loans. To classify loans as subprime we will consider the rate spread and the hoepa_status. The issue here comes from the 2000 to 2003 data which does not have either of these metrics. This is because before 2004 the HMDA did not require information about the rate of the loan so none of that information was collected or stored. In order to identify loans from these periods we will use the HUD subprime lenders list because it is a reliable source of lender that loan out primarily subprime loans and it is the only real metric we have.  
Data will not be stored in the repository as this project has in excess of 40GB of data.

### Data Analysis + Tools

To do the data analysis for this project I will be using Python with the Polars package. Polars has been selected for its high level of performance and ease of use / integration with other tools. There will be some use of other packages such as `requests` in order to perform some of the API requests for data.

### Data Sources

The data for this project primarily comes from the Housing Mortgage Disclosure Act (HMDA). 
We found data on the years [2000 - 2006] on OPENICPSR:  
[OPENICPSR Data] (https://www.openicpsr.org/openicpsr/project/151921/version/V1/view?flag=follow&path=/openicpsr/151921/fcr:versions/V1&type=project&pageSize=50&sortOrder=(?title)&sortAsc=true)

The HMDA data for the years [2007 - 2010] was found on the government's Consumer Financial Protection Bureau:
[cfpb Data] (https://www.consumerfinance.gov/data-research/hmda/historic-data/)

Additional sources were used as primary reading to back up the reliability of the above sources. Noteably we considered Ronald Utt's *The Subprime Mortgage Market Collapse: A Primer on the Causes and Possible Solutions*  
[Source] (https://www.heritage.org/report/the-subprime-mortgage-market-collapse-primer-the-causes-and-possible-solutions)

Finally, in order to determine the subprime loans made before the additional reporting added to the HMDA in 2004 we used Subprime lender list from the HUD.  
[HUD Subprime Lender Data] (https://www.huduser.gov/archives/portal/datasets/manu.html)
