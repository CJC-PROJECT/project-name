import  requests
import  requests.cookies
import  json

# jar = requests.cookies.RequestsCookieJar()
#
# jar.set('tasty_cookie','yum',domain='httpbin.org',path='/cookies')
# jar.set('gross_cookies','blech',domain='httpbin.org',path='/elsewhere')
# url = 'http://httpbin.org/cookies'
#
# r =requests.get(url,cookies = jar)
#
# print(r.text)

# r = requests.get('http://httpbin.org/status/404')
#
# # print(r.status_code)
# # print(r.status_code==requests.codes.ok)
# print(r.status_code)

payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.request('post',"http://httpbin.org/post", data=payload)
print(r.text)