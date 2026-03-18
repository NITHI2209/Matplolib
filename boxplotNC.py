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
finance_sal = df[df["Dept"]=="Finance"]["salary"]
plt.boxplot([hr_sal,it_sal,finance_sal], labels=["HR","IT","Finance"])
plt.legend()
plt.show()
#Refer figure 10