#Source: https://stackoverflow.com/questions/43663206/typeerror-unsupported-operand-types-for-dict-values-and-int
import numpy as np
# Summarize the data about minutes spent in the classroom
total_minutes = total_minutes_by_account.values()
total_minutes = np.array(total_minutes)
print('Mean:', np.mean(total_minutes))
print('Standard deviation:', np.std(total_minutes))
print('Minimum:', np.min(total_minutes))
print('Maximum:', np.max(total_minutes))