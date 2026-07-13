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


