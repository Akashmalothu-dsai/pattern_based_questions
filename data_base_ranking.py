import pandas as pd
data={"id":[1,100,49,193],"score":[200.0,300.0,300.0,218.0]}
data=pd.DataFrame(data)
data["rank"]=data["score"].rank(method="dense",ascending=False).astype(int)
data.drop("id",axis=1,inplace=True)
data=data.sort_values("rank")
print(data)