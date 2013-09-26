
In[1]:

```
import pandas as pd
%pylab inline
import matplotlib.pyplot as plt
```


    Populating the interactive namespace from numpy and matplotlib


In[2]:

```
data = pd.read_csv('data/prod_1000.csv', header= None, names = ['prod_type','date','rating'],
                   parse_dates =[1])
```

In[24]:

```
# build a histogram using value counts
counts = data['prod_type'].value_counts()
fig, ax = plt.subplots(figsize = (12,7))
rects1 = ax.bar(np.arange(5), counts)
ax.set_title("Review Histogram for Product Types")
ax.set_ylabel("Number of reviews", fontsize = 14)
ax.set_xticks([0.5,1.5,2.5,3.5,4.5])
ax.set_xticklabels( (counts.index) )

```




    [<matplotlib.text.Text at 0x108fa0b90>,
     <matplotlib.text.Text at 0x108fa7e90>,
     <matplotlib.text.Text at 0x108fc1a90>,
     <matplotlib.text.Text at 0x108fc5210>,
     <matplotlib.text.Text at 0x108fc5950>]




[!image]()


In[4]:

```
grouped = data.groupby(['prod_type'])
grouped_date = grouped['date']
dates = data['date']
grouped_counts = grouped_date.value_counts()
```

In[25]:

```
fig, ax = plt.subplots(figsize = (14,8))
for prod_type in (grouped.groups.keys()):
    if prod_type == "Toy":
        continue
    df = pd.DataFrame(grouped_counts.ix[prod_type])
    df["Dates"] = df.index
    df = df.sort("Dates")
    ax.plot(df["Dates"],df[0],linewidth = .8, label = prod_type)
plt.legend()
plt.title("Number of Amazon Reviews", fontsize = 18)
ax.set_xlabel("Date", fontsize = 18)
ax.set_ylabel("Number of Reviews", fontsize = 18)
savefig("first_vis.png")
```



[!image]()


In[5]:

```

```
