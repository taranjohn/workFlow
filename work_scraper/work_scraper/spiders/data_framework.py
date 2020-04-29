import pandas as pd

def TradeMe():
    df = pd.read_json('/Users/TJ/Documents/GitHub/workFlow/work_scraper/work_scraper/spiders/trademe.jl', lines = True)

    # fix date
    df['StartDate'] = df['StartDate'].replace(to_replace= '.*\((\d+).*', value=r"\1", regex=True)
    df['StartDate'] = pd.to_datetime(df['StartDate'], unit='ms')
    
    # url 
    df['URL'] = pd.json_normalize(df['JobApplicationDetails'])['ApplyViaTradeMe']

    # bullet points
    df['BulletPoints'] = pd.json_normalize(df['AdditionalData'])['BulletPoints']

    for i in range(0, len(df['BulletPoints'])):
        temp = ''
        for point in df['BulletPoints'][i]:
            temp += point
            temp += ', '
        df['BulletPoints'][i] = temp
    
    # source
    df['Source'] = 'TradeMe'
    
    # construct df
    tradeMe_df = df[['ListingId', 'Title', 'Company', 'StartDate', 'Region', 'Suburb', 'JobType', 'Body', 'URL', 'Source', 'BulletPoints']]
    tradeMe_df = tradeMe_df.rename(columns = {'ListingId': 'JobID', 'StartDate': 'ListingDate', 'Body': 'Abstract', 'Region': 'City', 'Suburb': 'Area', 'URL': 'Link'})

    return tradeMe_df

def Seek():
    df = pd.read_json('/Users/TJ/Documents/GitHub/workFlow/work_scraper/work_scraper/spiders/seek.jl', lines = True)

    # fix date
    df['listingDate'] = pd.Timestamp('2020-02-13T13:00:00Z').strftime('%Y-%m-%d %H:%M:%S')

    # company 
    df['Company'] = pd.json_normalize(df['advertiser'])['description']

    # bullet points
    for i in range(0, len(df['bulletPoints'])):
        temp = ''
        for point in df['bulletPoints'][i]:
            temp += point
            temp += ', '
        df['bulletPoints'][i] = temp

    # construct link
    df['Link'] = 'https://www.seek.co.nz/job/'
    for i in range(0, len(df['id'])):
        df['Link'][i] += str(df['id'][i]) 
    print(df['Link'][3])       

    # source 
    df['Source'] = 'Seek'

    # construct df
    seek_df = df[['id', 'title', 'Company', 'listingDate', 'location', 'area', 'workType', 'teaser', 'Link', 'Source', 'bulletPoints']]
    seek_df = seek_df.rename(columns = {'id': 'JobID', 'title': 'Title', 'listingDate': 'ListingDate', 'location': 'City', 'area': 'Area', 'workType': 'JobType', 'teaser': 'Abstract', 'bulletPoints': 'BulletPoints'})

    return seek_df

def sql(tradeMe_df, seek_df):
    
    # upload dataframes to sql database
    tradeMe_df.to_sql('Job_Blueprint', 'mysql://root@localhost/job_data', index = False, if_exists = 'replace')
    seek_df.to_sql('Job_Blueprint', 'mysql://root@localhost/job_data', index = False, if_exists = 'replace')

def main():
    tradeMe_df = TradeMe()
    seek_df = Seek()
    sql(tradeMe_df, seek_df)

main()

