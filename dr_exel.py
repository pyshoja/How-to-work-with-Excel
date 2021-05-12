
import requests
a=requests.get('http://dr-ir.ir/list-of-hospitals/157-%D9%84%DB%8C%D8%B3%D8%AA-%D9%BE%D8%B2%D8%B4%DA%A9%D8%A7%D9%86-%D9%85%D8%AA%D8%AE%D8%B5%D8%B5-%D8%A7%D8%B3%D8%AA%D8%A7%D9%86-%D9%82%D9%85.html')
print (a.text)
a1=a.text

b=0
lista=[]

for x in range (115):
    sh1=a1.find('<td width="167">',b+1)
    p1=a1.find('</p>',sh1)
    b=sh1
    dic1=a1[sh1+21:p1]

    sh2=a1.find('<td width="102">',b+1)
    p2=a1.find('</p>',sh2)
    b=sh2
    dic2=a1[sh2+21:p2]

    sh3=a1.find('<td width="127">',b+1)
    p3=a1.find('</p>',sh3)
    b=sh3
    dic3=a1[sh3+21:p3]

    sh4=a1.find('<td width="474">',b+1)
    p4=a1.find('</p>',sh4)
    b=sh4
    dic4=a1[sh4+21:p4]

    lista.append([dic1,dic2,dic3,dic4])

from openpyxl import Workbook
wb = Workbook()
ws = wb.active
for z in lista:
    ws.append(z)
wb.save('list_dr_qom.xlsx')

