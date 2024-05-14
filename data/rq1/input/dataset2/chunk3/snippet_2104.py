#Source: https://stackoverflow.com/questions/63528707/attributeerror-unaryop-object-has-no-attribute-evaluate-when-using-eval-fun
for test_ind, case_data in test_df.iterrows():
      case_data = case_data.to_frame().T
      rule = "Ask_before>-0.4843681 & 0.5255821<=BidVol_before<=0.07581073 & Volume>0.1107559"
      print(case_data, "case_data")
      if case_data.eval(rule).all() == True:
          print("TRUE")