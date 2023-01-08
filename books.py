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

#print(allofauthor("Leo Tolstoy"))
#print(cheap(2,6))
#print(df.Author.unique())

#print(df1.head(10))
print('''Please enter your choice:
1.) BEST WORKS OF YOUR FAVOURITE AUTHOR
2.) ALL AVAILABLE WORKS OF YOUR FAVOURITE AUTHOR
3.) BOOKS WITHIN YOUR PRICE RANGE''')
ch="yes"
while (ch!="no"):
    ch=input("Do you want to enter you choice?")
    while (ch=="yes"):
        x=int(input("Enter your choice:"))
        l=[1,2,3]
        if (x in l):
            if (x==1):
                a=input("Please enter author's name:")
                print(bestof(a))
                break
            elif(x==2):
                b=input("Please enter author's name:")
                print(allofauthor(b))
                break
            elif(x==3):
                c=int(input("Enter the lower end of your price range:"))
                d=int(input("Enter the upper end of your price range:"))
                print(cheap(c,d))
                break
            else:
                break
            ch=input("Do you want to see more books?(yes/no)")
        else:
            print("Invalid choice")
else:
    print("Thank you! Bye!")

    