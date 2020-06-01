import requests
from bs4 import BeautifulSoup
import wordcloud
from imageio import imread

def get_url_comment(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"
    }
    try:
        r = requests.get(url ,headers = headers, timeout = 30)#获得url的相关参数
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print ("网页获取成功",r.status_code )
        return r.text
    except Exception as e :
        return "网页爬取异常" , r.status_code ,e#返回状态码

def explain_HTML_comment(text):
    global lst
    lst = []
    soup = BeautifulSoup(text, "html.parser")  # 解释
    for item in soup.find_all("d"):
        lst.append(item.get_text())

def analysis_wordcloud(text):
    print ("执行图像处理中....")
    mk = imread(r"C:\Users\Dell\Desktop\u=3054214792,672612295&fm=26&gp=0.jpg")
    w = wordcloud.WordCloud(width = 1500,
                            height = 1500,
                            background_color = 'white',
                            font_path = 'msyh.ttc',
                            max_words = 1000,
                            mask = mk,
                            contour_width = 5,
                            contour_color = 'red'
                            );  # 配置对象参数
    w.generate(text)  # 加载词云文本
    w.to_file(r"C:\Users\Dell\Desktop\yuntu1.jpg")
    print ("执行结束,已保存至桌面")

if __name__ == '__main__':
    url = [r"https://api.bilibili.com/x/v1/dm/list.so?oid=145005943",
           "https://api.bilibili.com/x/v1/dm/list.so?oid=145317727",
           "https://api.bilibili.com/x/v1/dm/list.so?oid=145567103"]
    text = ""
    text1 = ""
    for each in url:
        text += get_url_comment(each)
    explain_HTML_comment(text)
    text1 += ','.join(lst)
    analysis_wordcloud(text1)
