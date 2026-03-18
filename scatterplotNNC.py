import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary": [12000,23000,33000,43000,43200,45000,45500,50000,55000,60000],
   "Dept" : ["HR","Finance","IT","HR","IT","IT","HR","Finance","Finance","HR"],
   "Age" : [33,34,45,50,55,65,70,70,75,80]
}
df = pd.DataFrame(data)
df["exprience"] = [1,1.5,1.7,1.8,2,2.5,3,3.5,4,5]
plt.scatter(df["Age"],df["salary"],c = df["Dept"].map({"HR":"skyblue","IT":"black","Finance":"orange"}))
plt.xlabel("Age")
plt.ylabel("Salary")
plt.title("Age vs salary vs dept")
plt.show()
#refer figure 14
