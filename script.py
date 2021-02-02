import clr

# Imports the necessary modules for the text input dialog box in Revit
from rpw.ui.forms import TextInput

clr.AddReference('RevitAPI') 
clr.AddReference('RevitAPIUI') 
from Autodesk.Revit.DB import * 
from Autodesk.Revit.UI import *

app = __revit__.Application
doc = __revit__.ActiveUIDocument.Document

elements = list(FilteredElementCollector(doc, doc.ActiveView.Id))

#Changes element to color yellow
colorStr = TextInput("Enter Color", description="Please enter a RGB color value:", default= "255,0,0")
colorByte = bytes(colorStr,"utf-8").split(",")
color = Color(colorByte[0], colorByte[1], colorByte[2])
ogs = OverrideGraphicSettings().SetProjectionFillColor(color)

t = Transaction(doc, 'Color Walls')
t.Start()
try:
    for i in elements:
    	#print(i.Name)
        #Selects the wall element with name of "PC225A"
        if i.Name == 'PC225A' or i.Name == 'PC250A':
          doc.ActiveView.SetElementOverrides((i.Id), ogs)
         # print 'element overridden'
except Exception as e:
    print '- Failed to override -'
    print '- ' + str(e) + ' -'
t.Commit()