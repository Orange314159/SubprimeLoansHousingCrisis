
## First check to ensure they have python and pip installed

sudo apt install python3 python3-pip python3-venv -y

python3 --version
pip3 --version

## Now we must unzip all of the files and get them ready for processing

unzip 151921-V1.zip
unzip hmda_2007_nationwide_first-lien-owner-occupied-1-4-family-records_labels.zip
unzip hmda_2008_nationwide_first-lien-owner-occupied-1-4-family-records_labels.zip
unzip hmda_2009_nationwide_first-lien-owner-occupied-1-4-family-records_labels.zip
unzip hmda_2010_nationwide_first-lien-owner-occupied-1-4-family-records_labels.zip

## Now we must unzip the specific files that we need from 2000 to 2010

unzip HMDA_LAR_2000.zip
unzip HMDA_LAR_2001.zip
unzip HMDA_LAR_2002.zip
unzip HMDA_LAR_2003.zip
unzip HMDA_LAR_2004.zip
unzip HMDA_LAR_2005.zip
unzip HMDA_LAR_2006.zip

## Now we can move all of the important files to a folder away from the rest of the junk

mkdir ImportantFiles
mv HMDA_LAR_2000.txt ImportantFiles
mv HMDA_LAR_2001.txt ImportantFiles
mv HMDA_LAR_2002.txt ImportantFiles
mv HMDA_LAR_2003.txt ImportantFiles
mv HMDA_LAR_2004.txt ImportantFiles
mv HMDA_LAR_2005.txt ImportantFiles
mv HMDA_LAR_2006.txt ImportantFiles
mv hmda_2007_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv ImportantFiles
mv hmda_2008_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv ImportantFiles
mv hmda_2009_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv ImportantFiles
mv hmda_2010_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv ImportantFiles

## Now we can remove all of the other files here

rm -rf 15*
rm -rf HMDA*
rm -rf hmda*

## Now to make things easier we will rename all of these files

mv ImportantFiles/* .
rm -rf ImportantFiles

mv HMDA_LAR_2000.txt HMDA_2000.txt
mv HMDA_LAR_2001.txt HMDA_2001.txt
mv HMDA_LAR_2002.txt HMDA_2002.txt
mv HMDA_LAR_2003.txt HMDA_2003.txt
mv HMDA_LAR_2004.txt HMDA_2004.txt
mv HMDA_LAR_2005.txt HMDA_2005.txt
mv HMDA_LAR_2006.txt HMDA_2006.txt

mv hmda_2007_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv HMDA_2007.txt
mv hmda_2008_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv HMDA_2008.txt
mv hmda_2009_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv HMDA_2009.txt
mv hmda_2010_nationwide_first-lien-owner-occupied-1-4-family-records_labels.csv HMDA_2010.txt

## Now we have to fix the vertical bars in the HMDA 2000 - 2006 data files

## This will require using python though, so we will now create that environment

python3 -m venv .venv
source .venv/bin/activate

pip install matplotlib
pip install numpy
pip install scikit-learn
pip install pandas
pip install polars
pip install networkx
pip install seaborn
pip install geopandas
pip install statsmodels
pip install bambi
pip install pyarrow

## Ok now we can run our file to fix the vertical bars

python3 barsToCommas.py HMDA_2000.txt HMDA_2000.csv
python3 barsToCommas.py HMDA_2001.txt HMDA_2001.csv
python3 barsToCommas.py HMDA_2002.txt HMDA_2002.csv
python3 barsToCommas.py HMDA_2003.txt HMDA_2003.csv
python3 barsToCommas.py HMDA_2004.txt HMDA_2004.csv
python3 barsToCommas.py HMDA_2005.txt HMDA_2005.csv
python3 barsToCommas.py HMDA_2006.txt HMDA_2006.csv

## Now to remove those extra ones

rm -rf HMDA_2000.txt
rm -rf HMDA_2001.txt
rm -rf HMDA_2002.txt
rm -rf HMDA_2003.txt
rm -rf HMDA_2004.txt
rm -rf HMDA_2005.txt
rm -rf HMDA_2006.txt

## Now to work on the 2007 to 2010 data
## We first must remove the extra quotations

python3 removeQuotes.py HMDA_2007.txt HMDA_2007.csv
python3 removeQuotes.py HMDA_2008.txt HMDA_2008.csv
python3 removeQuotes.py HMDA_2009.txt HMDA_2009.csv
python3 removeQuotes.py HMDA_2010.txt HMDA_2010.csv

## Now that we have those files corrected we can remove the old files

rm -rf HMDA_2007.txt
rm -rf HMDA_2008.txt
rm -rf HMDA_2009.txt
rm -rf HMDA_2010.txt

## Next step is to start working on normalizing the data (getting all of the same columns)

python3 normalizeEarly.py HMDA_2000.csv HMDA_2000_Normal.csv 0
python3 normalizeEarly.py HMDA_2001.csv HMDA_2001_Normal.csv 1
python3 normalizeEarly.py HMDA_2002.csv HMDA_2002_Normal.csv 2
python3 normalizeEarly.py HMDA_2003.csv HMDA_2003_Normal.csv 3

## Now that those are normalized, we can remove the old ones

rm -rf HMDA_2000.csv
rm -rf HMDA_2001.csv
rm -rf HMDA_2002.csv
rm -rf HMDA_2003.csv

## Now we must normalize the middle files

python3 normalizeMiddle.py HMDA_2004.csv HMDA_2004_Normal.csv 0
python3 normalizeMiddle.py HMDA_2005.csv HMDA_2005_Normal.csv 1
python3 normalizeMiddle.py HMDA_2006.csv HMDA_2006_Normal.csv 2

## Now we must remove the old files

rm -rf HMDA_2004.csv
rm -rf HMDA_2005.csv
rm -rf HMDA_2006.csv

## Finally for normalization we have to clean up the late files 2007 - 2010

python3 normalizeLate.py HMDA_2007.csv HMDA_2007_Normal.csv 0
python3 normalizeLate.py HMDA_2008.csv HMDA_2008_Normal.csv 1
python3 normalizeLate.py HMDA_2009.csv HMDA_2009_Normal.csv 2
python3 normalizeLate.py HMDA_2010.csv HMDA_2010_Normal.csv 3

## Finally remove the final old files

rm -rf HMDA_2007.csv
rm -rf HMDA_2008.csv
rm -rf HMDA_2009.csv
rm -rf HMDA_2010.csv

## This is the point at which we part from the early data
## In this final project we do not need the 2000 - 2003 data so we will not be editing those files anymore
## The next step to compress all of this information into a single row per tract

python3 reduceNormalized.py HMDA_2004_Normal.csv HMDA_2004_Reduced.csv 2004
python3 reduceNormalized.py HMDA_2005_Normal.csv HMDA_2005_Reduced.csv 2005
python3 reduceNormalized.py HMDA_2006_Normal.csv HMDA_2006_Reduced.csv 2006
python3 reduceNormalized.py HMDA_2007_Normal.csv HMDA_2007_Reduced.csv 2007
python3 reduceNormalized.py HMDA_2008_Normal.csv HMDA_2008_Reduced.csv 2008
python3 reduceNormalized.py HMDA_2009_Normal.csv HMDA_2009_Reduced.csv 2009
python3 reduceNormalized.py HMDA_2010_Normal.csv HMDA_2010_Reduced.csv 2010

## Now we can remove all of the old normal files

rm -rf HMDA_2004_Normal.csv
rm -rf HMDA_2005_Normal.csv
rm -rf HMDA_2006_Normal.csv
rm -rf HMDA_2007_Normal.csv
rm -rf HMDA_2008_Normal.csv
rm -rf HMDA_2009_Normal.csv
rm -rf HMDA_2010_Normal.csv

## Great! now we can work on combining all of those together
## We are only caring about the years 2004-2007 so rest of the input won't ever involve 2008-2010

python3 combineReduced.py HMDA_2004_Reduced.csv HMDA_2005_Reduced.csv HMDA_2006_Reduced.csv HMDA_2007_Reduced.csv HMDA_Combined.csv

## Ok perfect!! that is the end of the loan data work
## Lets start by getting undergrad percetage

python3 reduceSchoolData.py ACS_5YR_ESTIMATES_SOCIOECONOMIC_TRACT_-4830078498712968728.csv reducedSchool.csv

## Now let's get the rest of that data

python3 reduceMostData.py ACS_5YR_ESTIMATES_HOUSING_TRACT_-6586867065303880862.csv ACS_5YR_ESTIMATES_SOCIOECONOMIC_TRACT_-4830078498712968728.csv reducedMostData.csv

## Finally, we can get the race data

python3 reduceRaceData.py ACS_5YR_ESTIMATES_DEMOGRAPHIC_TRACT_-85781284450125383.csv reducedRace.csv

## Ok! now we can combine all of this data

python3 combineAllData.py HMDA_Combined.csv reducedMostData.csv reducedRace.csv reducedSchool.csv reducedAllData.csv

## and that's it! Have fun plotting this data using the plotting folder



