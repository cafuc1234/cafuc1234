from  bs4 import BeautifulSoup
# with open("./fg.html","r",encoding="utf-8") as f:
#      r=BeautifulSoup(f.read(),'lxml')
# res=r.find_all("p",class_="form-control-static")
# res1=r.find_all("label",class_="col-sm-4 control-label")
# count=0
# count1=0
#
# head=[]
# for i in res1:
#     count1+=1
#     #print(i.text.lstrip())
#     #head.append(i.text.lstrip())
#     r=i.text.replace("\n","\t")
#     m=r.lstrip()
#     v=m.strip()
#     head.append(v)
#
# data1=[]
# for i in res:
#     r = i.text.replace("\n", "\t")
#     m = r.lstrip()
#     v = m.strip()
#     data1.append(v)
# print(head)
# print(data1)
# i=8
# information={
#
# }
# while(i<len(head)):
#     information[head[i]]=data1[i-6]
#     i=i+1
# print(information)
def parser(html):
    r = BeautifulSoup(html, 'lxml')
    res = r.find_all("p", class_="form-control-static")
    res1 = r.find_all("label", class_="col-sm-4 control-label")
    count = 0
    count1 = 0

    head = []
    for i in res1:
        count1 += 1
        # print(i.text.lstrip())
        # head.append(i.text.lstrip())
        r = i.text.replace("\n", "\t")
        r=r.replace("：","\t")
        m = r.lstrip()
        v = m.strip()
        head.append(v)

    data1 = []
    for i in res:
        r = i.text.replace("\n", "\t")
        m = r.lstrip()
        v = m.strip()
        data1.append(v)
    #print(head)
    #print(data1)
    i = 8
    information = {

    }
    while (i < len(head)):
        information[head[i]] = data1[i - 6]
        i = i + 1
    #print(information)
    return  information
#with open("./fg.html","r",encoding="utf-8") as f:
    #print(parser(f.read()))