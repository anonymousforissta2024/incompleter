#Source: https://stackoverflow.com/questions/58848048/attributeerror-class-object-has-no-attribute-outside-loop
for region in regions:
  if region == '1':
    for region in regions:
        for col in range(prelim_sheet.ncols):
          if (prelim_sheet.cell_value(0, col) == r.region_name):
           ...
          else:
            for state in state_list:
                if state.strip() == 'NewHampshire':  
                    s = state_class(state)
                    if ((prelim_sheet.cell_value(0, col)).replace(" ", "") == s.state_name):
                        s.state_col = col
                        print(s.state_col)
                        ...