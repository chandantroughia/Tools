from netCDF4 import Dataset
import numpy as np
import pandas as pd
# CSV Format is Label followed by 10.
# After reading the csv file, I exclude the labels and create 
# an array of just the 10 MFCCs. Those 10 mfccs are converted to 
# netCDF4 form
rawDump = np.array(pd.read_csv("Data Science Collection_Chandan_Troughia_DS1.csv", header=None))
data = rawDump[:, 0:]
# Create and open the netcdf dataset
root_grp = Dataset('Data Science Collection_Chandan_Troughia_DS1.nc', 'w', format='NETCDF4')
# Various attributes can be given to the group.
# Description, institution etc can be added.
root_grp.description =                     'Title: Monthly Expenses of the RPI Students based on their AGE and GENDER'
#=========================================================================
root_grp.Metadata_below = '==>'
root_grp.Creator ='Chandan Singh Troughia'
root_grp.Male_Female ='For indicating the gender of the participant'

root_grp.Timestamp_Format_Used    ='MM/DD/YYYY HH:MM:SS'
root_grp.Expenses_Format          ='Numerical(float)'
root_grp.Time_of_data_collection  ='27th September to 3rd October'
root_grp.US_Dollars               ='United States Currency ($)'
root_grp.empty_field_NAN         = 'indicates that those are included in the rent'

#==========================================================================
root_grp.Provenance_Data_Below    ='==>'
root_grp.Purpose_of_collection    ='To get an estimate of expenses of RPI students based on their age and gender'
root_grp.Participant_Information  ='RPI Students'
root_grp.Data_Collection_Modes    ='Online form and sheet of paper'
root_grp.Location_of_Survey       ='RPI Campus'
root_grp.Online_forms_used        ='google forms (https://www.google.com/forms/about/)'
root_grp.Online_spreadsheets_used ='googlesheets (https://www.google.com/sheets/about/)'
root_grp.Dropbox_storage_Link     ='https://www.dropbox.com/s/abaoxjchwd1qp0k/Data%20Science%20Collection_Chandan_Troughia.xlsx?dl=0'
root_grp.Google_Storage_Link      ='https://drive.google.com/open?id=0B5i8lsQoLYAdU1lEc0NsaGdRSzg'

#===========================================================================

# Since all my RPIs are of the same dimension (i.e. same number of RPIs for the 0th, 1st, 2nd and so on)
# I create only one dimension which will be used to describe all my RPIs.
root_grp.createDimension("Data", data.shape[0])

# The name of each variable is Age_in_years, Gender, Monthly_Rent, Food_Expenses, Internet_Expenses, Phone_Expenses
rpivariables = []
for i in range(data.shape[1]):
	if i == 0:
		rpivariables.append(root_grp.createVariable('Time', 'S30', ('Data',)))
	elif i == 1:
		rpivariables.append(root_grp.createVariable('Age_in_years', 'd', ('Data',)))
	elif i == 2:
		rpivariables.append(root_grp.createVariable('Gender', 'S30', ('Data',)))
	elif i == 3:
		rpivariables.append(root_grp.createVariable('Monthly_Rent', 'd', ('Data',)))
	elif i == 4:
		rpivariables.append(root_grp.createVariable('Food_Expenses', 'd', ('Data',)))
	elif i == 5:
		rpivariables.append(root_grp.createVariable('Internet_Expenses', 'd', ('Data',)))
	elif i == 6:
		rpivariables.append(root_grp.createVariable('Phone_Expenses', 'd', ('Data',)))
	elif i == 7:
		rpivariables.append(root_grp.createVariable('Laundry_Expenses', 'd', ('Data',)))
	elif i == 8:
		rpivariables.append(root_grp.createVariable('Other_Expenses', 'd', ('Data',)))
		
# The data for each variable is passed in this loop
for i in range(len(rpivariables)):
	rpivariables[i][:] = data[:, i]

# Close the netcdf dataset
root_grp.close()
#============================Metadata================================================
rawDump1 = np.array(pd.read_csv("Metadata_DS1.csv", header=None))
root_grp1 = Dataset('Metadata_DS1.nc', 'w', format='NETCDF4')
data1 = rawDump1[:, 0:]
root_grp1.createDimension("Metadata", data1.shape[0])
root_grp1.description = 'Metadata'
root_grp1.names_and_meaning ='This file contains the Metadata'
metavariables = []
for i in range(data1.shape[1]):
	if i == 0:
		metavariables.append(root_grp1.createVariable('Name', 'S100', ('Metadata',)))
	elif 1 == 1:
		metavariables.append(root_grp1.createVariable('Meaning', 'S100', ('Metadata',)))
for i in range(len(metavariables)):
	metavariables[i][:] = data1[:, i]

root_grp1.close()
#==========================Porvenance================================================
rawDump2 = np.array(pd.read_csv("Porvenance_DS1.csv", header=None))
root_grp2 = Dataset('Porvenance_DS1.nc', 'w', format='NETCDF4')
data2 = rawDump2[:, 0:]

root_grp2.description = 'Provenance'
root_grp2.names_and_meaning ='This file contains the Provenance data'
root_grp2.createDimension("Provenance", data2.shape[0])
provariables = []
for i in range(data2.shape[1]):
	if i == 0:
		provariables.append(root_grp2.createVariable('Name', 'S100', ('Provenance',)))
	elif 1 == 1:
		provariables.append(root_grp2.createVariable('Meaning', 'S100', ('Provenance',)))
for i in range(len(metavariables)):
	provariables[i][:] = data2[:, i]

root_grp2.close()