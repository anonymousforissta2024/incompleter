#Source: https://stackoverflow.com/questions/70313176/how-to-fix-typeerror-order-must-be-str-not-int
outfile.writeframes(int16(output.ravel(1)*32767.0).tostring())