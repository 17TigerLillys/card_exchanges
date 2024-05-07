# card_exchanges.py
This contains the code needed to clean and process the results of a google survey and then assign people to groups for several card exchanges. Note that there are several manual rounds to ensure accuracy. 

### How to Run
`python ./card_exchanges/card_exchanges.py -type petsParents -stage 1  -newData "./data_to_run.xlsx"`

## Parameters to pass:
* **type:** petsParents or allAlumns (the latter will have additional columns)
* **stage:** 1-4
* **newData:** File path to the data you want to clean
* **oldData:** Optional file path of the old data for Stage 3

## Stages:
Note that when you paste from google be sure to 'paste special' and then select 'text' 
		to avoid the issue with international addresses in multiple cells!!!!
1) **Early fixes:**  
*Input:* raw file from Google  
*Output:* a spreadsheet ready to be manually checked and fixed 
	1) **Manual fixing**  
	*Input:* spreadsheet from 1A  
	*Output:* spreadsheet ready for duplicate checking
2) **Unpack data & identify possible duplicates**  
	*Input:* manually cleaned spreadsheet from 1.5  
	*Output:* spreadsheet with possible duplicates highlighted
	1) **Manually remove any duplicates identified in 2**  
	*Input:* spreadsheet from 2  
	*Output:* completely clean spreadsheet!!!
3) **Check emails against the emails from last year**  
	*Input:* cleaned and fixed spreadsheet  
	*Output:* a list of emails 
4) **Assign people to groups**  
	*Input:* cleaned and de-duped spreadsheet  
	*Outputs:* master spreadsheet with groups labeled  
			individual spreadsheets for each group in a folder

### Stage 1:
* Change the column headers from Google's questions to shorter names
* Identify issues:
	A1 is blank but not international/used A2 wrong
	Used the international column but not international
	Find manual additions
	Messed up international addresses (those should be fine if I paste correctly)
* Shorten any data (non-religious, non-sending members)
* Fix the zip codes

### Stage 1.5 (Manual):
* Fill in blank A1's

### Stage 4:
* Re-run determine location to update anyone I added manually? Either that or change it 
	myself
* Evenly distribute the international members
* Put people into non-religious and/or religious groups
* Evenly distribute the non-sending members!!

## Columns: 
* preferred_email, envelope_name, address_one, address_two, city, state, clean_zip, international_address, non_sending, non-religious, other_info, gmail_address,
* **Additional columns for all alumns:** class year, houses	







