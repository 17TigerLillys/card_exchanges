# Validate the addresses?

import pandas as pd 
import math
from fuzzywuzzy import fuzz, process
import argparse

fourZipStates = ['MA', 'CT', 'NH', 'VT', 'RI', 'NJ', 'ME']
# we might be able to avoid this by importing it into excel better but for now this works
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
parser.add_argument('-new','--newData', help='File path of the data', required=True)
parser.add_argument('-old','--oldData', help='Optional file path of the old data for Stage 3', required=False)
args = vars(parser.parse_args())


newDict = pd.read_excel(args['newData'], sheet_name=None)
newDF = pd.concat(newDict.values(), names=newDict.keys()) # To-Do figure out how to get rid of this step

# print(newDF.columns)
if args['stage'] == '3':
	oldDict = pd.read_excel(args['oldData'], sheet_name=None)
	oldDF = pd.concat(oldDict.values(), names=oldDict.keys())
	# if (newDF["Email"] != newDF["Email Address"]) == True:
	# 	print(newDF["Email"], newDF["Email Address"])
	# print(newDF[newDF['Email'] != newDF['Email Address']]['Email'], newDF[newDF['Email'] != newDF['Email Address']]['Email Address'])
	# df[df['uid'] == query]

# Gut check to show any different emails
#---------------------------------------
# To-Do: make this a lambda function!!!!!!!!!!!!!
# for index, row in newDF.iterrows():
# 	if row['Email'] != row['Email Address']:
# 		print(row['Email Address'], '\t', row['Email'])



if args['stage'] == '1' or args['stage'] == 2:
	# Fix the messed up zip codes
	#----------------------------
	newDF['cleanZip'] = newDF.apply(lambda x: cleanZips(x.Zip_Code, x.State), axis=1) # once you fix this change the lines below to use clean zip


	# Create a new column for location and those that need to be manually fixed 
	newDF['location'] = newDF.apply(lambda x: determineLocation(x.City, x.State, x.cleanZip, x.international_address, x.envelope_name), axis=1)

if args['stage'] == '2':
	# Check for duplicates
	# First check for duplicates by email address
	catEmailDupes = newDF[newDF.duplicated('Email Address', keep=False)]
	if not catEmailDupes.empty:
		print('You may have duplicates by email, check!')
		print(catEmailDupes['Email Address'])

	# Next check by zip code to catch anyone who signed up with a different email address
	# to-do: Try fuzzy string matching on address line 1!!!!!
	#		Internationals will need to use international_address
	catZipDupes = newDF[newDF.duplicated('cleanZip', keep=False)].sort_values(['Zip_Code', 'envelope_name'])
	if not catZipDupes.empty:
		print('You may have duplicates by zip code, check!')
		print(catZipDupes[['envelope_name', 'Address Line 1', 'cleanZip']])

if args['stage'] == '3':
	# Check new emails against the emails from last year
	print(set(oldDF['Email Address']) - set(newDF['Email Address'])) 


# Different cases to check for
	# A1 is blank but they're not international



# print(newDF[['location', 'international_address']])
# for index, row in newDF.iterrows():
# 	if row['location'] == 'international':
# 		print(row['location'], '\t', row['international_address'])

# Notes for next year
#--------------------
# Label my email column "preffered email" so I know which is which
# Be careful pasting things into excel, it messes up the international addresses by putting
	#each line in it's own row, which is fucking annoying
# Go through and remove any entries in the international column that are actually duplicates



















