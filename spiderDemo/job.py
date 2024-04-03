import requests

url='https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101270100&experience=&payType=&partTime=&degree=&industry=&scale=&stage=&position=100102&jobType=&salary=&multiBusinessDistrict=&multiSubway=&page={}&pageSize=30'

set_cookies='__zp_sseed__=4ofewTHibOaBobdqFm4Iq/a65WYC2zbPPz9C5YbiSKr6LNlV+PAmjvuLQftoQDl1zPMwVBBSn7z0pYF5RnY8fQ==; Path=/; Domain=.zhipin.com'

cookies={}

for item in set_cookies.split(';'):
    key, value=item.strip().split('=',maxsplit=1)
    cookies[key]=value

user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'

for i in range(1,11):
    resp=requests.get(url.format(i),headers={'User-Agent':user_agent},cookies=cookies).json()
    print(resp['zpData'])
    # for data in resp['zpData']['jobList']:
    #     print('areaDistrict: %s, jobName: %s' %(data['areaDistrict'],data['jobName']))
