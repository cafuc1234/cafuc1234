import time
print(int(time.time()*1000))
import requests
from bs4 import BeautifulSoup
from yy import parser
import random
from Crypto.Cipher import  AES
import base64
import os
from Crypto import Random
#https://211-83-131-132.vpn.cafuc.edu.cn:8118/xtgl/index_cxYhxxIndex.html?xt=jw&localeKey=zh_CN&_=1669170240998&gnmkdm=index&su=20190813129&sf_request_type=ajax
a="ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678"
def rds(num):
    f=""
    for i in range(num):
        f+=a[random.randint(0,47)]
    return f
class Encrypt:
    def __init__(self, key, iv):
        self.key = key.encode('utf-8')
        self.iv = iv.encode('utf-8')

    # @staticmethod
    def pkcs7padding(self, text):
        """明文使用PKCS7填充 """
        bs = 16
        length = len(text)
        bytes_length = len(text.encode('utf-8'))
        padding_size = length if (bytes_length == length) else bytes_length
        padding = bs - padding_size % bs
        padding_text = chr(padding) * padding
        self.coding = chr(padding)
        return text + padding_text

    def aes_encrypt(self, content):
        """ AES加密 """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        # 处理明文
        content_padding = self.pkcs7padding(content)
        # 加密
        encrypt_bytes = cipher.encrypt(content_padding.encode('utf-8'))
        # 重新编码
        result = str(base64.b64encode(encrypt_bytes), encoding='utf-8')
        return result


    def aes_decrypt(self, content):
        """AES解密 """
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        content = base64.b64decode(content)
        text = cipher.decrypt(content).decode('utf-8')
        return text.rstrip(self.coding)

def login(username,password):
    person0=requests.get("https://vpn.cafuc.edu.cn/public/cas_login?entry_id=1",allow_redirects=False,verify=False)
    person1=requests.get(person0.headers["Location"],verify=False)
    person1_cookies={}
    for i in person1.cookies:
        person1_cookies[i.name]=i.value
        print(i.name)
    bs=BeautifulSoup(person1.text,"lxml")
    print(bs.find_all("input"))
    params=[]
    for i in bs.find_all("input"):

        if i.get("value")==None or i.get("value")=="":
            continue
        params.append(i.get("value"))
    print(params)
    headers2={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Cookie":"route="+person1_cookies["route"]+"; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; JSESSIONID="+person1_cookies["JSESSIONID"]
    }
    data={
        "username":username,
         "password":"",
        "lt":params[0],
        "dllt":"userNamePasswordLogin",
        "execution":params[2],
        "_eventId":"submit",
        "rmShown":"1"

    }
    key=params[5]
    print("key是",key)
    iv=rds(16)
    print("iv是",iv)
    password=rds(64)+password
    a=Encrypt(key,iv)
    data["password"]=a.aes_encrypt(password)
    person2=requests.post("https://authserver-cafuc-edu-cn-s.vpn.cafuc.edu.cn:8118/authserver/login?service=https%3A%2F%2Fvpn.cafuc.edu.cn%2Fauth%2Fcas_validate%3Fentry_id%3D1",headers=headers2,data=data,allow_redirects=False,verify=False)
    if(person2.status_code==200):
        return  False
    print(person2.headers)
    person2_cookies={}
    for i in person2.cookies:
        person2_cookies[i.name]=i.value
    print(person2_cookies)
    headers3={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Cookie":"language=zh_CN; iPlanetDirectoryPro_-_wisedu.com.cn="+person2_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]
    }
    person3=requests.get(person2.headers["Location"],headers=headers3,verify=False,allow_redirects=False)
    print(person3.headers)
    person3_cookies={}
    for i in person3.cookies:
        person3_cookies[i.name]=i.value
    print(person3_cookies)
    headers4={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Cookie": "CASTGC="+person2_cookies["CASTGC"]+"; route="+person1_cookies["route"]+"; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; JSESSIONID="+person1_cookies["JSESSIONID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person2_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]+"; TWFID="+person3_cookies["TWFID"]
    }
    person4=requests.get("https://authserver-cafuc-edu-cn-s.vpn.cafuc.edu.cn:8118/authserver/login?service=http://ehall.cafuc.edu.cn/login?service=http://ehall.cafuc.edu.cn/new/index.html",headers=headers4,verify=False,allow_redirects=False)
    print(person4.headers)
    person4_cookies={}
    for i in person4.cookies:
        person4_cookies[i.name]=i.value
    print(person4_cookies)
    headers5={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
       "Cookie": "amp.locale=undefined; TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person4_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]
    }
    person5=requests.get(person4.headers["Location"],headers=headers5,allow_redirects=False,verify=False)
    print(person5.headers)
    person5_cookies={}
    for i in person5.cookies:
        person5_cookies[i.name]=i.value
    print(person5_cookies)
    headers6={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
       "Cookie": "amp.locale=undefined; TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person4_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]+"; MOD_AUTH_CAS="+person5_cookies["MOD_AUTH_CAS"]
    }
    person6=requests.get(person5.headers["Location"],headers=headers6,allow_redirects=False,verify=False)
    print(person6.headers)
    person6_cookies={}
    for i in person6.cookies:
        person6_cookies[i.name]=i.value
    print(person6_cookies)
    headers7={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Cookie": "TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person4_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]+"; MOD_AUTH_CAS="+person5_cookies["MOD_AUTH_CAS"]+"; route="+person6_cookies["route"]+"; asessionid="+person6_cookies["asessionid"]+"; amp.locale=undefined"
    }
    person7=requests.get("https://ehall-cafuc-edu-cn.vpn.cafuc.edu.cn:8118/jsonp/userDesktopInfo.json?type=&_=1669176123214&sf_request_type=ajax",verify=False,headers=headers7,allow_redirects=False)
    print(person7.headers)
    person7_cookies={}
    for i in person7.cookies:
        person7_cookies[i.name]=i.value
    print(person7_cookies)
    headers8={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Cookie": "TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person4_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]+"; MOD_AUTH_CAS="+person5_cookies["MOD_AUTH_CAS"]+"; route="+person6_cookies["route"]+"; asessionid="+person6_cookies["asessionid"]+"; amp.locale=undefined; JSESSIONID="+person7_cookies["JSESSIONID"]
    }
    person8=requests.get("https://ehall-cafuc-edu-cn.vpn.cafuc.edu.cn:8118/appShow?appId=5580980827959025",verify=False,headers=headers8,allow_redirects=False)
    print(person8.headers)
    person8_cookies={}
    for i in person8.cookies:
        person8_cookies[i.name]=i.value
    print(person8_cookies)
    headers9={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Cookie": "TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person4_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]
    }
    person9=requests.get(person8.headers["Location"],headers=headers9,allow_redirects=False,verify=False)
    print(person9.headers["Location"])
    headers10={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    "Cookie": "CASTGC="+person2_cookies["CASTGC"]+"; route="+person1_cookies["route"]+"; org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE=zh_CN; JSESSIONID="+person1_cookies["JSESSIONID"]+"; TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person4_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]
    }
    person10=requests.get(person9.headers["Location"],headers=headers10,allow_redirects=False,verify=False)
    print(person10.headers)
    person10_cookies={}
    for i in person10.cookies:
        person10_cookies[i.name]=i.value
    print(person10_cookies)
    headers11={
        "Cookie": "TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person10_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"],
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }
    person11=requests.get(person10.headers["Location"],headers=headers11,allow_redirects=False,verify=False)
    print(person11.headers)
    person11_cookies={}
    for i in person11.cookies:
        person11_cookies[i.name]=i.value
    print(person11_cookies)
    headers12={
        "Cookie": "JSESSIONID="+person11_cookies["JSESSIONID"]+"; TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person10_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"],
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }
    person12=requests.get(person11.headers["Location"],headers=headers12,allow_redirects=False,verify=False)
    print(person12.headers)
    person12_cookies={}
    for i in person12.cookies:
        person12_cookies[i.name]=i.value
    print(person12_cookies)
    headers13={
        "Cookie": "TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person10_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"],
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
    }
    person13=requests.get(person12.headers["Location"],headers=headers13,allow_redirects=False,verify=False)
    print(person13.headers)
    person13_cookies={}
    for i in person13.cookies:
        person13_cookies[i.name]=i.value
    print(person13_cookies)
    headers14={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "Cookie": "TWFID="+person3_cookies["TWFID"]+"; iPlanetDirectoryPro_-_wisedu.com.cn="+person10_cookies["iPlanetDirectoryPro_-_wisedu.com.cn"]+"; JSESSIONID="+person13_cookies["JSESSIONID"]
    }
    person14=requests.get("https://211-83-131-132.vpn.cafuc.edu.cn:8118/xsxxxggl/xsgrxxwh_cxXsgrxx.html?gnmkdm=N100801&layout=default&su="+data["username"],headers=headers14,allow_redirects=False,verify=False)

    information=parser(person14.text)

    return information
    # r=BeautifulSoup(person14.text,'lxml')
    # res=r.find_all("p",class_="form-control-static")
    # res1=r.find_all("label",class_="col-sm-4 control-label")
    # for i in res:
    #     print(i.text.lstrip())
    #
    # for i in res1:
    #     print(i.text.lstrip())
#information=login("20190813129","Ss1009751628")
#print(information)