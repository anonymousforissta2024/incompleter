#Source: https://stackoverflow.com/questions/63981530/i-get-typeerror-cant-multiply-sequence-by-non-int-of-type-numpy-float64-when
# This is my code that creates the plot
moving_avg = np.convolve(list_of_results, np.ones((100,)) / 100, mode="valid")
plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel('Remaining Pins')
plt.xlabel('Games played')
plt.grid()
plt.savefig('English_10000.pdf', dpi='300')