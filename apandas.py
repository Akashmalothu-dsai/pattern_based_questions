import pandas as pd
marks=pd.Series([1,2,4],index=["maths","chemistry","physics"])
adata={"name":["akash","ravi","ashok"],"age":[12,12,390],"id":["B25DS020","B25DS030","B25CS039"]}
data=pd.DataFrame(adata)

r=pd.read_csv("student.csv")
print(r)
data.to_csv("student.csv",index=False)
print(r)
import numpy as num
a=num.array([[1,2,3,4]])
print(a[a==2])#----------data stored in the row or coloumn wise in the array form 
