import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary": [12000,23000,33000,43000,43200,45000,45500,50000,55000,60000],
   "Dept" : ["HR","Finance","IT","HR","IT","IT","HR","Finance","Finance","HR"],
   "Age" : [33,34,45,50,55,65,70,70,75,80]
}
df = pd.DataFrame(data)
sort_age = df.sort_values("Age")
fig , axs = plt.subplots(1,3,figsize =(15,5))
#lineplot
axs[0].plot(sort_age["Age"],df["salary"],color = "red",marker = "*",linewidth = "2",markersize = 2)
axs[0].grid()
axs[0].set_title("Lineplot")
axs[0].set_xlabel("Age")
axs[0].set_ylabel("Salary")
#Histogram
axs[1].hist(df["salary"],bins = 5,color = "skyblue")
axs[1].set_title("Histogram")
axs[1].set_xlabel("Salary")
axs[1].set_ylabel("Frequency")
#Boxplot
axs[2].boxplot(df["salary"])
axs[2].set_title("Boxplot")
axs[2].set_xlabel("salary")

plt.show()
#Refer figure 15
