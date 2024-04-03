import requests

# session and cookies
def Request():
    url='https://login2.scrape.center/login'
    data={'username': 'admin', 'password': 'admin'}
    session=requests.session()
    resp=session.post(url=url, data=data,allow_redirects=False)
    cookies=resp.cookies
    print('cookies: ', cookies, 'status_code: ',resp.status_code)

    response_index=session.get('https://login2.scrape.center/')
    print('Response Status', response_index.status_code)
    print('Response URL', response_index.url)

if __name__ == '__main__':
    Request()