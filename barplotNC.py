import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary": [12000,23000,33000,43000,43200,45000,45500,50000,55000,60000],
   "Dept" : ["HR","Finance","IT","HR","IT","IT","HR","Finance","Finance","HR"],
   "Age" : [33,34,45,50,55,65,70,70,75,80]
}
df = pd.DataFrame(data)
hr_sal = df[df["Dept"]=="HR"]["salary"]
it_sal = df[df["Dept"]=="IT"]["salary"]
fin_sal = df[df["Dept"]=="Finance"]["salary"]

hr_mean = sum(hr_sal)/len(hr_sal)
it_mean = sum(it_sal)/len(it_sal)
fin_mean = sum(fin_sal)/len(fin_sal)
plt.bar(["HR","IT","Finance"],[hr_mean,it_mean,fin_mean],color=["blue","grey","yellow"])
plt.show()
#Refer figure 12