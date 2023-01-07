import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df1=pd.read_csv('book.csv')

df=df1.drop_duplicates()  #removing 

def bestof(author):
    authors=df['Author'].to_numpy()
    while (author in authors):
        rslt=df[(df['User Rating']>4.0)&(df['Author']==author)]
        return rslt
    else:
       return "Author not found."
#print(bestof("harsh"))

def graph(ds):
    genre=ds['Genre'].to_numpy()
    x=np.count_nonzero(genre=="Fiction")
    y=np.count_nonzero(genre=="Non Fiction")
    z=np.array([x,y])
    labels=["Fiction","Non-Fiction"]
    graphic=plt.pie(z,labels=labels)
    plt.show()

def cheap(lp,up):
    rslt=df[(df['Price']>=lp)&(df['Price']<up)]
    graph(rslt)
    return rslt
    
def allofauthor(auth):
    authors=df['Author'].to_numpy()
    while (auth in authors):
        rslt=df[df["Author"]==auth]
        return rslt
    else:
       return "Author not found."

print(allofauthor("Stephen Kendrick"))
#print(cheap(2,6))
#print(df.Author.unique())

#print(df1.head(10))
