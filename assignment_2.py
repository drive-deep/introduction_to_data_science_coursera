##

def answer_one():
    
    return df['Gold'].argmax()
answer_one()

def answer_two():
    k=df['Gold']-df['Gold.1']
    return abs(k).argmax()

answer_two()

def answer_three():
    copy_df=df.copy()
    k=copy_df[(copy_df['Gold.1'] > 0) & (copy_df['Gold'] >0)]
    k1=(k['Gold']-k['Gold.1'])/(k['Gold']+k['Gold.1']+k['Gold.2'])
    return abs(k1).argmax()
answer_three()

def answer_four():
    return (df['Gold.2'].sum()*3 + df['Silver.2'].sum()*2+df['Bronze.2'])
answer_four()

def answer_five():
    census_df.set_index('COUNTY')
    census_df.sort_index()
    p=census_df['COUNTY'].max()
    k=census_df[census_df['COUNTY']==p]
    return k.iloc[0]['STNAME']


answer_five()


def answer_five():
    df=census_df[census_df['SUMLEV']==50]
    d={}
    ans=''
    mx=0
    for i in range(len(df)):
        
        l1=df.iloc[i]['STATE']
        l2=df.iloc[i]['COUNTY']
        #print(l1,l2)
        if(l1 in d):
            
            if l2 not in d[l1]:
                d[l1].append(l2)
        else:
            d[l1]=[l2]
        if(len(d[l1])>mx):
            mx=len(d[l1])
            ans=df.iloc[i]['STNAME']
    return ans

answer_five()
def answer_six():
    df=census_df[census_df['SUMLEV'] == 50]
    df1=df.sort(['STNAME','POPESTIMATE2015'],ascending=False).groupby('STNAME').head(3).copy()
    df2 = df1.reset_index().groupby("STNAME").sum().sort(['POPESTIMATE2015'],ascending=False).head(3).copy()
    return list(df2.index.values)
answer_six()    
answer_six()
        
        
def answer_seven():
    df=census_df[census_df['SUMLEV']==50]
    k=df[['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].std(axis=1)
        
    return df.loc[k.idxmax()]['CTYNAME']
answer_seven()


def answer_eight():
    df=census_df[((census_df['REGION'] ==1) | (census_df['REGION'] ==2)) & (census_df['POPESTIMATE2015']>census_df['POPESTIMATE2014']) & (census_df['CTYNAME'].str.startswith('Washington')) ]
    
    return df[['STNAME','CTYNAME']]
answer_eight()
