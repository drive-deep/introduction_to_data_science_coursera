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

def answer_six():
    census_df.set_index('CENSUS2010POP')
    census_df.sort_index()
    return [census_df.iloc[-4:-1]['STNAME']]

answer_six()

def answer_seven():
    an=0
    p=len(census_df)
    
    for i in range(0,p):
        
        k=(census_df['POPESTIMATE2010'])
        
        k1=int(k.iloc[i])
        
        k=(census_df['POPESTIMATE2011'])
        k2=int(k.iloc[i])
        
        k7=(census_df['POPESTIMATE2012'])
        k3=int(k.iloc[i])
        k=(census_df['POPESTIMATE2013'])
        k4=int(k.iloc[i])
        k=(census_df['POPESTIMATE2014'])
        k5=int(k.iloc[i])
        k=(census_df['POPESTIMATE2015'])
        k6=int(k.iloc[i])
        
        tmp=[k1,k2,k3,k4,k5,k6]
        #tmp
        mx=max(tmp)-min(tmp)
        #print(mx)
        if(mx>an):
            an=mx
            ans=census_df.iloc[i]['CTYNAME']
            #print(mx,ans)
        
    return ans
        
        
        
answer_seven()
        
        
        
answer_seven()


def answer_eight():
    df=census_df[((census_df['REGION'] ==1) | (census_df['REGION'] ==2)) & (census_df['POPESTIMATE2015']>census_df['POPESTIMATE2014']) & (census_df['CTYNAME'].str.startswith('Washington')) ]
    
    return df[['STNAME','CTYNAME']]
answer_eight()
