# Validate the addresses?

import pandas as pd # if you install more than a few packages make a dev environment!!
import math
from fuzzywuzzy import fuzz, process
import argparse
	

fourZipStates = ['MA', 'CT', 'NH', 'VT', 'RI', 'NJ', 'ME']
def cleanZips(zipCode, state):
	if not math.isnan(zipCode):
		zipCode = int(zipCode) # cast them to an int
		if len(str(zipCode)) == 4 and state in fourZipStates:
			cleanZip = '0' + str(zipCode)
		elif len(str(zipCode)) == 4 and state not in fourZipStates:
			print(zipCode, state)
			cleanZip = zipCode 
		elif len(str(zipCode)) == 5:
			cleanZip = zipCode
	else:
		cleanZip = float('nan')
	return cleanZip

# Check for nans that aren't guarenteed to be a float
def isNaN(thing):
    return thing != thing

def determineLocation(city, state, zipCode, intAddress, envName):
	location = ''
	# These are people that were added manually and need their info filled in
	if isNaN(city) and isNaN(state) and isNaN(zipCode) and isNaN(intAddress):
		print('Please add information for: ' + envName)
		print('--------------------------------------------------')
		location = 'addInfoManually'
	elif isNaN(city) and isNaN(state) and isNaN(zipCode):
		# print(intAddress)
		# print('=============================')
		location = 'international'
	else: 
		location = 'domestic'
	return location

parser = argparse.ArgumentParser(description='This program cleans and processes survey data for card exchanges')
parser.add_argument('-t','--type', help='Options are petsParents or allAlums', required=True)
parser.add_argument('-s','--stage', help='Number 1-4 corresponding to the desired stage', required=True)
args = vars(parser.parse_args())

catsDF = pd.read_excel('./swlc_cleanish_data copy.xlsx', sheet_name=None) # New Data
# print(catsDF.columns)
dogsDF = pd.read_excel('./swld_rough_data.xlsx', sheet_name=None) # Old Data
	# if (catsDF["Email"] != catsDF["Email Address"]) == True:
	# 	print(catsDF["Email"], catsDF["Email Address"])
	# print(catsDF[catsDF['Email'] != catsDF['Email Address']]['Email'], catsDF[catsDF['Email'] != catsDF['Email Address']]['Email Address'])
	# df[df['uid'] == query]

# Gut check to show any different emails
#---------------------------------------
# This should be a lambda function!!!!!!!!!!!!!
# for index, row in catsDF.iterrows():
# 	if row['Email'] != row['Email Address']:
# 		print(row['Email Address'], '\t', row['Email'])



if args['stage'] == '1':
	# Fix the messed up zip codes
	#----------------------------
	catsDF['cleanZip'] = catsDF.apply(lambda x: cleanZips(x.Zip_Code, x.State), axis=1)


	# Create a new column for location and those that need to be manually fixed 
	catsDF['location'] = catsDF.apply(lambda x: determineLocation(x.City, x.State, x.cleanZip, x.international_address, x.envelope_name), axis=1)

if args['stage'] == '2':
	# Check for duplicates
	# First check for duplicates by email address
	catEmailDupes = catsDF[catsDF.duplicated('Email Address', keep=False)]
	if not catEmailDupes.empty:
		print('You may have duplicates by email, check!')
		print(catEmailDupes['Email Address'])

	# Next check by zip code to catch anyone who signed up with a different email address
	# to-do: Try fuzzy string matching on address line 1!!!!!
	#		Internationals will need to use international_address
	catZipDupes = catsDF[catsDF.duplicated('cleanZip', keep=False)].sort_values(['Zip_Code', 'envelope_name'])
	if not catZipDupes.empty:
		print('You may have duplicates by zip code, check!')
		print(catZipDupes[['envelope_name', 'cleanZip']])

if args['stage'] == '3':
	# Check new emails against the emails from last year
	print(set(dogsDF['Email Address']) - set(catsDF['Email Address'])) 


# Different cases to check for
	# A1 is blank but they're not international



# print(catsDF[['location', 'international_address']])
# for index, row in catsDF.iterrows():
# 	if row['location'] == 'international':
# 		print(row['location'], '\t', row['international_address'])

# Notes for next year
#--------------------
# Label my email column "preffered email" so I know which is which
# Be careful pasting things into excel, it messes up the international addresses by putting
	#each line in it's own row, which is fucking annoying
# Go through and remove any entries in the international column that are actually duplicates



















