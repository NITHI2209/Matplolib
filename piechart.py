import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary": [12000,23000,33000,43000,43200,45000,45500,50000,55000],
   "Dept" : ["HR","Finance","IT","HR","IT","IT","HR","Finance","Finance"]

}
df = pd.DataFrame(data)
count = df["Dept"].value_counts()
plt.pie(count,labels= count.index,autopct="%1.2f",explode=[0,0.1,0.2])
plt.show()
#Refer figure 6