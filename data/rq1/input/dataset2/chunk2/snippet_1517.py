#Source: https://stackoverflow.com/questions/47204175/lane-departure-warning-system-for-autonomous-driving-typeerror-expected-non-em
left_fit = np.polyfit(lefty, leftx, 2)
right_fit = np.polyfit(righty, rightx, 2)