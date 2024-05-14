#Source: https://stackoverflow.com/questions/66365065/typeerror-unhashable-type-bunch-appears-after-selecting-value-from-ipywidget
import ipywidgets as widgets
from IPython.display import display
from branca.colormap import linear

dropdownMenu = widgets.Dropdown(options=['mean','median'],value='mean',description='Column:')
widgetOutput = widgets.Output()

def colEvent(col):   
    widgetOutput.clear_output()
    colorDic = {}
    namesList = ['A', 'B', 'C', 'D', 'E']
    with widgetOutput:
        colormap = linear.YlGn_09.scale(
            min(nest[col] for nest in testDict.values()),
            max(nest[col] for nest in testDict.values()))
        for name in namesList:
            if testDict.get(name):        
                colorDic[name] = {}
                colorDic[name]=colormap(testDict.get(name).get(col))
            else:
                colorDic[name] = {}
                colorDic[name] = '#ffffffff'

dropdownMenu.observe(colEvent, names='value')
display(dropdownMenu)
display(widgetOutput)