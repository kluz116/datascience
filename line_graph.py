import matplotlib.pyplot as plt

month = ['Jan','Feb','Mar','Apr','May','June','July','Aug']
sales = [20000,40000,50000,89020,90000,50000,40000,70000]

plt.bar(month,sales)
plt.title('Sales Made Per Month In YTD')
plt.ylabel('Sales YTD')
plt.xlabel('Month')
plt.show()