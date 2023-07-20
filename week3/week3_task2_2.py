#get data from url
import urllib.request as req
import bs4
import re
index_url = "https://www.ptt.cc/bbs/movie/index.html"
request = req.Request(index_url,headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")
    root = bs4.BeautifulSoup(data,"html.parser")

    #要取出首頁的詳細網址（含有頁碼編號）
    #這是首頁的前一頁的網址
    index_url_with_num = "https://www.ptt.cc" + root.find_all("a",class_="btn wide")[1]["href"]
    url_format = re.search("[0-9]+",index_url_with_num).group()

#抓三頁    
for x in range(3):
    url = "https://www.ptt.cc/bbs/movie/index"+ str(int(url_format)+1-x) +".html"
    print(url)
    request = req.Request(url,headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")

    import bs4

    root = bs4.BeautifulSoup(data,"html.parser")
    posts = root.find_all("div",class_="r-ent")
    for post in posts:
        #標題
        titles = post.find("div",class_="title")
        #貼文數
        count = post.find("div",class_="nrec")
        #去除掉已刪文的部分
        if titles.a != None:
            #時間
            #先進到文章內，再抓時間的class="article-meta-value"
            tag_a = post.find("a")
            everyUrl = "https://www.ptt.cc"+ tag_a["href"]
            #get into the article
            import urllib.request as req    
            request = req.Request(everyUrl,headers={
                "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
            })
            with req.urlopen(request) as response:
                dataInPost = response.read().decode("utf-8")
            rootInPost = bs4.BeautifulSoup(dataInPost,"html.parser")
            #time in the article
            time = rootInPost.find_all("span",class_="article-meta-value")

            print(titles.a.string,",",count.string,",",time[3].string)




