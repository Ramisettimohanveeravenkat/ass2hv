import pandas as pd
a=[2,4,6,8]
b=[1,2,3,4]
Mydata1=pd.Series(a)
Mydata2=pd.Series(b)
print(Mydata1)
print(Mydata2)
sumOfseries=Mydata1+Mydata2
diffOfseries=Mydata1-Mydata2
divOfseries=Mydata1/Mydata2
mulOfseries=Mydata1*Mydata2
print("sum of two series ",sumOfseries)
print("difference of two series ",diffOfseries)
print("division of two series ",divOfseries)
print("multipilication of two series ",mulOfseries)