#!/usr/bin/env python
# coding: utf-8

# In[334]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[335]:


pd.options.display.float_format = '{:.4f}'.format


# In[336]:


df=pd.read_csv("Forbes Billionaires.csv")


# In[337]:


df.columns


# In[338]:


df["Industry"].unique()


# In[339]:


#strip whitespace
df['Industry'] = df['Industry'].str.replace(" ", "")
df["Industry"].unique()
df.columns=df.columns.str.replace(" ","")
df.columns


# In[340]:


df.describe()


# In[341]:


df.isna().sum()
#We have no NA's in our dataset
df.columns


# In[342]:


dfagg=df.groupby("Industry").agg(
    mean_networth=pd.NamedAgg(column="Networth", aggfunc="mean"),
    count_networth=pd.NamedAgg(column="Networth", aggfunc="count"),
    std_networth=pd.NamedAgg(column="Networth", aggfunc="std"),
    min_rank=pd.NamedAgg(column="Rank",aggfunc="min"),
    max_rank=pd.NamedAgg(column="Rank",aggfunc="max")
)
dfagg


# In[343]:


dfagg.sort_values(by="mean_networth",ascending=False)


# The highest average worth is found in the Automotive industry, whereas the lowest mean worth is in Construction and 
# engineering. Most billionaires are in the Finance & Investments industry, followed by the Technology and Manufacturing industries. 

# In[344]:


dfagg["worth_mean_ratio"]=dfagg['mean_networth']/df["Networth"].mean()
dfagg["worth_std_ratio"]=dfagg['std_networth']/df["Networth"].std()
dfagg.sort_values(by="worth_mean_ratio",ascending=False)


# By comparing the means and standard deviations of each Industry against the overall mean and standard deviation we can see that there is an overall trend of increasing volatility as the mean net worth increaces

# In[345]:


sns.regplot(x="worth_mean_ratio",y="worth_std_ratio",data=dfagg)


# In[346]:


plt.figure(figsize=(20, 10))
ax=sns.boxplot(x = "Industry",
            y = "Networth",
            data = df)


ax.set_xticklabels(ax.get_xticklabels(), rotation=40, ha="right")
plt.show()


# # Overall distirbution of net worth

# In[347]:


sns.displot(df, x="Networth", kind="kde")


# The overall distirbution of net worth is heavily skewed to the right with a long tail

# In[348]:


plt.figure(figsize=(20,10))
sns.boxplot(data=df,y="Networth")


# In[349]:


sns.histplot(df, x="Networth")


# In[350]:


plt.figure(figsize=(20, 10))
sns.ecdfplot(df, x="Networth")


# In[351]:


df["cumperc"]=(df["Networth"].cumsum()/df["Networth"].sum())
df["worthratio"]=(df["Networth"]/df["Networth"].sum())
df.sort_values("worthratio",ascending=False)


# In[352]:


df.loc[df["cumperc"]>0.5,]


# Out of 2599 billionaires, 287 account for 50% of the total networth. Thus 11% of billionaires account for 50% of the total networth in our dataset.

# # Networth Distirbutions by Industry

# In[353]:


sns.ecdfplot(x="Networth",data=df.loc[df["Industry"]=="Automotive",])


# In[354]:


plotgrid = sns.FacetGrid(df, row="Industry",height=1.7, aspect=4)
plotgrid.map(sns.ecdfplot, "Networth")


# In[355]:


cond=["Energy","Construction&Engineering","Sports"]

plotgrid = sns.FacetGrid(df.loc[df["Industry"].isin(cond)], row="Industry",height=1.7, aspect=4)
plotgrid.map(sns.ecdfplot, "Networth")


# In[356]:


sns.ecdfplot(x="Networth",data=df.loc[df["Industry"]=="Sports"])


# In[357]:


sns.histplot(x="Networth",data=df.loc[df["Industry"]=="Sports"])


# In[358]:


sns.displot(x="Networth",data=df.loc[df["Industry"]=="Sports"],kind="kde")


# The right skewed distirbution holds for all industries in differing levels of skewness. The most diversified distirbution is found in the sports industry. It is highly propable that if we had more data on billionaires of the Sports Industry the above finding would change and the aforementionded cumulative distirbution would align with the overall finding of fat tailed distirbutions of net worth.

# # Net worth Distirbution by Country

# In[359]:


dfagg=df.groupby("Country").agg(
    mean_networth=pd.NamedAgg(column="Networth", aggfunc="mean"),
    count_networth=pd.NamedAgg(column="Networth", aggfunc="count"),
    std_networth=pd.NamedAgg(column="Networth", aggfunc="std"),
    total=pd.NamedAgg(column="Networth",aggfunc="sum"),
    min_rank=pd.NamedAgg(column="Rank",aggfunc="min"),
    max_rank=pd.NamedAgg(column="Rank",aggfunc="max")
)
dfagg.sort_values("mean_networth",ascending=False)


# In[360]:


dfagg.sort_values("total",ascending=False)


# Most billionaires are found in the USA, followed by China. The net worth per capita is highest in France, followed by Mexico
