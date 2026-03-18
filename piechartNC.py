import matplotlib.pyplot as plt
import pandas as pd
data = {
    "salary": [12000,23000,33000,43000,43200,45000,45500,50000,55000,60000],
   "Dept" : ["HR","Finance","IT","HR","IT","IT","HR","Finance","Finance","HR"],
   "Age" : [33,34,45,50,55,65,70,70,75,80]
}
df = pd.DataFrame(data)
salary_by_dept = df.groupby("Dept")["salary"].sum()
plt.pie(salary_by_dept,labels=salary_by_dept.index,colors=["grey","pink","yellow"],autopct="%1.2f",shadow = True,explode=[0.1,0.2,0.1])
plt.axis("equal")
plt.show()
#Refer figure 11