# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/47152691/how-can-i-pivot-a-dataframe
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
_c_(1545075, _a_(1545073, _c_(1545072, _a_(1545070, _c_(1545068, _a_(1545065, _n_(1545064, "df", lambda: df), "groupby"), _n_(1545066, "rows", lambda: rows)+_n_(1545067, "cols", lambda: cols))[_n_(1545069, "vals", lambda: vals)], "agg"), _n_(1545071, "aggfuncs", lambda: aggfuncs)), "unstack"), _n_(1545074, "cols", lambda: cols))
_l_(1545076)
# equivalently,
_c_(1545083, _a_(1545078, _n_(1545077, "df", lambda: df), "pivot_table"), _n_(1545079, "vals", lambda: vals), _n_(1545080, "rows", lambda: rows), _n_(1545081, "cols", lambda: cols), _n_(1545082, "aggfuncs", lambda: aggfuncs))
_l_(1545084)

_c_(1545093, _a_(1545091, _c_(1545089, _a_(1545086, _n_(1545085, "df", lambda: df), "set_index"), _n_(1545087, "rows", lambda: rows)+_n_(1545088, "cols", lambda: cols))[_n_(1545090, "vals", lambda: vals)], "unstack"), _n_(1545092, "cols", lambda: cols))
_l_(1545094)
# equivalently, 
_c_(1545100, _a_(1545096, _n_(1545095, "df", lambda: df), "pivot"), _n_(1545097, "rows", lambda: rows), _n_(1545098, "cols", lambda: cols), _n_(1545099, "vals", lambda: vals))
_l_(1545101)

df = _c_(1545104, _a_(1545103, _n_(1545102, "pd", lambda: pd), "DataFrame"), {'A': [1, 1, 1, 2, 2, 2], 'B': [*'xxyyzz'], 
                   'C': [*'CCDCDD'], 'E': [100, 200, 300, 400, 500, 600]})
_l_(1545105)
rows, cols, vals = ['A', 'B'], ['C'], 'E'
_l_(1545106)

# using pivot syntax
df1 = _c_(1545129, _a_(1545128, _c_(1545127, _a_(1545126, _c_(1545125, _a_(1545124, _c_(1545123, _a_(1545122, _c_(1545121, _a_(1545117, _c_(1545116, _a_(1545108, _n_(1545107, "df", lambda: df), "assign"), ix=_c_(1545115, _a_(1545114, _c_(1545113, _a_(1545110, _n_(1545109, "df", lambda: df), "groupby"), _n_(1545111, "rows", lambda: rows)+_n_(1545112, "cols", lambda: cols)), "cumcount"))), "pivot"), [*_n_(1545118, "rows", lambda: rows), 'ix'], _n_(1545119, "cols", lambda: cols), _n_(1545120, "vals", lambda: vals)), "fillna"), 0, downcast='infer'), "droplevel"), -1), "reset_index")), "rename_axis"), columns=None)
_l_(1545130)

# equivalently, using set_index + unstack syntax
df1 = _c_(1545151, _a_(1545150, _c_(1545149, _a_(1545148, _c_(1545147, _a_(1545146, _c_(1545145, _a_(1545144, _c_(1545142, _a_(1545132, _n_(1545131, "df", lambda: df), "set_index"), [*_n_(1545133, "rows", lambda: rows), _c_(1545140, _a_(1545139, _c_(1545138, _a_(1545135, _n_(1545134, "df", lambda: df), "groupby"), _n_(1545136, "rows", lambda: rows)+_n_(1545137, "cols", lambda: cols)), "cumcount")), *_n_(1545141, "cols", lambda: cols)])[_n_(1545143, "vals", lambda: vals)], "unstack"), fill_value=0), "droplevel"), -1), "reset_index")), "rename_axis"), columns=None)
_l_(1545152)

df1 = _c_(1545169, _a_(1545168, _c_(1545166, _a_(1545163, _c_(1545162, _a_(1545154, _n_(1545153, "df", lambda: df), "assign"), ix=_c_(1545161, _a_(1545160, _c_(1545159, _a_(1545156, _n_(1545155, "df", lambda: df), "groupby"), _n_(1545157, "rows", lambda: rows)+_n_(1545158, "cols", lambda: cols)), "cumcount"))), "pivot"), _n_(1545164, "rows", lambda: rows), [*_n_(1545165, "cols", lambda: cols), 'ix'])[_n_(1545167, "vals", lambda: vals)], "fillna"), 0, downcast='infer')
_l_(1545170)
df1 = _c_(1545178, _a_(1545177, _c_(1545176, _a_(1545172, _n_(1545171, "df1", lambda: df1), "set_axis"), [f"{_n_(1545173, 'c', lambda: c)[0]}_{_n_(1545174, 'c', lambda: c)[1]}" for c in _n_(1545175, "df1", lambda: df1)], axis=1), "reset_index"))
_l_(1545179)

# equivalently, using the set_index + unstack syntax
df1 = _c_(1545199, _a_(1545193, _c_(1545191, _a_(1545181, _n_(1545180, "df", lambda: df), "set_index"), [*_n_(1545182, "rows", lambda: rows), _c_(1545189, _a_(1545188, _c_(1545187, _a_(1545184, _n_(1545183, "df", lambda: df), "groupby"), _n_(1545185, "rows", lambda: rows)+_n_(1545186, "cols", lambda: cols)), "cumcount")), *_n_(1545190, "cols", lambda: cols)])[_n_(1545192, "vals", lambda: vals)], "unstack"), [-1, *_c_(1545198, _n_(1545194, "range", lambda: range), -2, -_c_(1545197, _n_(1545195, "len", lambda: len), _n_(1545196, "cols", lambda: cols))-2, -1)], fill_value=0)
_l_(1545200)
df1 = _c_(1545208, _a_(1545207, _c_(1545206, _a_(1545202, _n_(1545201, "df1", lambda: df1), "set_axis"), [f"{_n_(1545203, 'c', lambda: c)[0]}_{_n_(1545204, 'c', lambda: c)[1]}" for c in _n_(1545205, "df1", lambda: df1)], axis=1), "reset_index"))
_l_(1545209)

df1 = _c_(1545223, _a_(1545222, _c_(1545221, _a_(1545220, _c_(1545219, _a_(1545218, _c_(1545217, _a_(1545211, _n_(1545210, "df", lambda: df), "set_index"), ['A', _c_(1545216, _a_(1545215, _c_(1545214, _a_(1545213, _n_(1545212, "df", lambda: df), "groupby"), 'A'), "cumcount"))])['E'], "unstack"), fill_value=0), "add_prefix"), 'Col'), "reset_index"))
_l_(1545224)

pv_1 = _c_(1545231, _a_(1545226, _n_(1545225, "df", lambda: df), "pivot_table"), index=_n_(1545227, "rows", lambda: rows), columns=_n_(1545228, "cols", lambda: cols), values=_n_(1545229, "vals", lambda: vals), aggfunc=_n_(1545230, "aggfuncs", lambda: aggfuncs), fill_value=0)
_l_(1545232)
# internal operation of `pivot_table()`
gb_1 = _c_(1545246, _a_(1545245, _c_(1545244, _a_(1545242, _c_(1545241, _a_(1545239, _c_(1545237, _a_(1545234, _n_(1545233, "df", lambda: df), "groupby"), _n_(1545235, "rows", lambda: rows)+_n_(1545236, "cols", lambda: cols))[_n_(1545238, "vals", lambda: vals)], "agg"), _n_(1545240, "aggfuncs", lambda: aggfuncs)), "unstack"), _n_(1545243, "cols", lambda: cols)), "fillna"), 0, downcast="infer")
_l_(1545247)
_c_(1545251, _a_(1545249, _n_(1545248, "pv_1", lambda: pv_1), "equals"), _n_(1545250, "gb_1", lambda: gb_1)) # True
_l_(1545252) # True

