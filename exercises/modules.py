import statistics as st
from collections import Counter
from itertools import accumulate

# Median
sales = [823, 934, 877, 540, 700]
print(st.median(sales))

# Counter
word = "antidisestablishmentarianism"
print(Counter(word).most_common(3))


numbers = [1, 2, 3, 4, 5]
print(list(accumulate(numbers)))
