from numpy import save
from pylab import plot, savefig
x = [1, 2, 3]
y = [2, 4, 6]
plot(x, y)

# 作業ディレクトリは/Users/junyasuzuki/local_Document/Programming/DoingMathWithPython

# savefig('mygraph.png') 作業ディレクトリに保存される
savefig('./chapter2/2-3-5/mygraph.png')
