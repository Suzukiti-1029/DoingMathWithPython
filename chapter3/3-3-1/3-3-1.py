simplelist = [4, 2, 1, 3, 4]
from collections import Counter
c = Counter(simplelist)
c.most_common()

c.most_common(1)
c.most_common(2)

mode = c.most_common(1)
mode
mode[0]
mode[0][0]