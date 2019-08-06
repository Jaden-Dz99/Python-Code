#______________________________________________________________
            #INSTALLATION REQUIREMENTS / COMMANDS
#______________________________________________________________


#  pip install pandas
#  pip install tk
#  pip install openpyxl==2.6.2
#  python -m pip install --upgrade pip

#______________________________________________________________

import pandas as pd

file_path = "./python.xlsx"

data_frame = pd.read_excel('C:/Users/USER/Desktop/python.xlsx', index_col=None, header=None)



data_frame[2,3] = 59  # Over writes data on cmd not excel (seems to delete the whole row)

def change_value_cell(cell):
    if cell==59:
        return 1337
    return cell

data_frame_2 = pd.read_excel("trial.xlsx", "Sheet3", converters = {
    'Unnamed: 0.1': change_value_cell
})

data_frame.update(data_frame_2)

print(data_frame)

test = data_frame.at[2, 2]
print(test)

data_frame.at[3,4] = 0.1
data_frame.at[2,3] = 'Schmear'

print(data_frame)

data_frame.to_excel("new.xlsx",sheet_name="SheetNew")


#______________________________________________________________
            #TEST CODE
#______________________________________________________________
        #  xlsx = pd.ExcelFile(PATH\python.xlsx)

        #  sheet1 = xlsx.parse(0)

        #  column = sheet1.icol(0).real

        #  row = sheet1.irow(0).real

        #  pd.read_excel;('python.xlsx')

        #  df =pd.read_excel(open('python.xlsx','rb'), sheetname=1)

        #  pd.read_excel('python.xlsx')
      
        #  df.to_excel('dir/python.xlsx', sheet_name='Sheet1')

        #  DataFrame = pd.read_excel("Desktop\python.xlsx", sheetname=0)

        #  writer = pd.ExcelWriter('trial.xlsx')  # Creating an output file

        #  data_frame.to_excel(writer, 'Sheet3')  # re-naming the sheet

        #  writer.save()
