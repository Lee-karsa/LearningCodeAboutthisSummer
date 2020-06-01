import requests
from bs4 import BeautifulSoup
import bs4
from tqdm import tqdm
import xlwt

def get_url_comment(url):
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                     "(KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 "
                     "Core/1.70.3741.400 QQBrowser/10.5.3863.400"
    }
    try:
        r = requests.get(url ,headers = headers, timeout = 30)#获得url的相关参数
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except Exception as e :
        return "网页爬取异常" , r.status_code ,e#返回状态码

def explain_url(url_content):
    i = 1
    linux_list_nametype = []
    linux_dict_factiontype = {}
    soup = BeautifulSoup(url_content, "html.parser")#解释
    linux_command_type = soup.find("ol").children#遍历o1下的li标签
    linux_command_faction = soup.find_all(["dt","dd"])
    for li in linux_command_type:
        if li.string == "Linux命令大全" or li.string == "<li >Data</p>" or li.string == "\n":#清洗数据
            pass
        else:
            linux_list_nametype.append(li.string)
    for dtdd in  linux_command_faction:
        if "<dt>" in str(dtdd):
            try:
                linux_dict_factiontype[dtdd.string] = linux_command_faction[i].text
                i += 2
            except:
                continue
    linux_list_nametype.append (linux_dict_factiontype)
    return linux_list_nametype

def write_excel(final_list):
    row  = 1
    book = xlwt.Workbook()
    sheet = book.add_sheet("linux命令大全")
    for each_1 in final_list:
        col = 0
        for each_2 in each_1:
            if isinstance(each_2 , dict):
                col_temp = 2
                for k , v in each_2.items():
                    sheet.write(row , col_temp , k+v)
                    col_temp += 1
            else:
                sheet.write(row, col, each_2)
                col += 1
        row += 1
    book.save(r"‪D:\桌面\Linux命令大全.xls".strip('\u202a'))

if __name__ == '__main__':
    linux_fianl_list = []
    for i in tqdm(range(1,316)):
        a = get_url_comment(r"http://www.ourlinux.net/index.php?mod=linuxcommand&act=show&id=" + str(i))
        linux_fianl_list.append(explain_url(a))
        write_excel(linux_fianl_list)

