import  matplotlib.pyplot as plt


charges = ['Chelsea','Arsenal','United','Liverpool']
fans    =[20000,40000,3500,80000]

plt.pie(fans,labels=charges, autopct = "%.2f")
plt.axes().set_aspect("equal")
plt.show()