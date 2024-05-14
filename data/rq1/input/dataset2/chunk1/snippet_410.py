#Source: https://stackoverflow.com/questions/55369147/another-work-around-this-typeerror-cannot-iterate-over-a-scalar-tensor-for-ma
plt.bar(days_range, data, color=TFColor[3])
plt.bar(tau - 1, data[tau - 1], color="r", label="user behaviour changed")
plt.xlim(0, 80);