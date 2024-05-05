# card_exchanges
This contains the code needed to clean and process the results of a google survey and then assign people to groups for several card exchanges

# Parameters to pass:
 	Type: Pets & Parents or All Alumns (the latter will have additional columns)
	Stage: 1-4 or stage names

# STAGES:
	0.5) When you paste from google be sure to 'paste special' and then select 'text' 
			to avoid the issue with international addresses in multiple cells!!!!
	1) Early fixes:
		Input: raw file from Google
		Output: a spreadsheet ready to be manually checked and fixed 
	1.5) Manual fixing
		Input: spreadsheet from 1A
		Output: spreadsheet ready for duplicate checking
	2) Unpack data & identify possible duplicates
		Input: manually cleaned spreadsheet from 1.5
		Output: spreadsheet with possible duplicates highlighted
	2.5) Manually remove any duplicates identified in 2
		Input: spreadsheet from 2
		Output: completely clean spreadsheet!!!
	3) Check emails against the emails from last year
		Input: cleaned and fixed spreadsheet
		Output: a list of emails 
	4) Assign people to groups
		Input: cleaned and fixed spreadsheet
		Outputs: master spreadsheet with groups labeled
				individual spreadsheets for each group in a folder

# Stage 1:
 	* Change the column headers from Google's questions to shorter names
	* Identify issues:
		A1 is blank but not international/used A2 wrong
		Used the international column but not international
		Find manual additions
		Messed up international addresses (those should be fine if I paste correctly)
	* Shorten any data (non-religious, non-sending members)
 	* Fix the zip codes

# Stage 1.5:
 	* Fill in blank A1's
	* 

# Stage 4:
#---------
 	* Re-run determine location to update anyone I added manually? Either that or change it 
		myself
	* Evenly distribute the international members
	* Put people into non-religious and/or religious groups
	* Evenly distribute the non-sending members!!

# Desired columns: 
preferred_email, envelope_name, address_one, address_two, city, state, clean_zip, international_address, non_sending, non-religious, other_info, gmail_address,
# Additional columns for all alumns: 
class year, houses	