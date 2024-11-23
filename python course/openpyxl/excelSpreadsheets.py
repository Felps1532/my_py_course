# we have downloaded this module (openpyxl) on the terminal (pip install openpyxl)
import openpyxl as xl
from openpyxl.chart import BarChart, Reference

wb = xl.load_workbook('transactions.xlsx')
# Here we specify the name of the sheet we want
# this object is the reference of our entire 'sheet1'
sheet1 = wb['Planilha1']

# coordinate of a cell
sheet1['a1']
# it returns the same of above
cell = sheet1.cell(1, 1)
print(cell.value)
# now my objective is to iterate over all the rows and get the values of the third column (price) and multiply it by 0.9

# at first, I need to know how many rows are there
print(sheet1.max_row)  # 4 rows

print('-'*20)

# start in the second so you don't get the title
for row in range(2, sheet1.max_row + 1):  # '+ 1' to include the number 4
    cell = sheet1.cell(row, 3)  # collumn
    corrected_price = cell.value * 0.9
    corrected_price_cell = sheet1.cell(row, 4)
    corrected_price_cell.value = corrected_price
    
# 
values = Reference(sheet1,
          min_row=2,
          max_row=sheet1.max_row,
          min_col=4,
          max_col=4)

chart = BarChart()
chart.add_data(values)
sheet1.add_chart(chart, 'e2')

wb.save('transactions2.xlsx')
