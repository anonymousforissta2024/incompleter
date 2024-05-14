#Source: https://stackoverflow.com/questions/56440957/how-do-i-fix-typeerror-unhashable-type-rqm-cell-auto-generated-class
import python_jsonschema_objects as pjs
schema = {}
schema['Rqm'] = 'rqm.json'
builder = pjs.ObjectBuilder(schema['Rqm'])
ns = builder.build_classes()
Cell = ns.RqmCell
CellSet = ns.RqmCellset
cellSet = None
GSMCell = Cell(rat='GSM', bandwidth='BW_1_4_MHZ')
cellSet = CellSet(cellsToDeploy=[GSMCell])