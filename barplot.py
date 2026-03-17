import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary": [12000,23000,33000,43000,43200,45000,45500,50000,55000,60000],
   "Dept" : ["HR","Finance","IT","HR","IT","IT","HR","Finance","Finance","HR"],
   "Age" : [33,34,45,50,55,65,70,70,75,80]
}
df = pd.DataFrame(data)
sort_age= df.sort_values("Age")
plt.bar(sort_age["Age"],df["salary"],width = 2, color = "yellow",align="center")
plt.show()
#refer figure 9
