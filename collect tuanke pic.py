#-*- encoding:utf-8 -*-
from tqdm import tqdm
import xlrd
import xlwt
import pytesseract
from PIL import Image
import jieba
import os

def pic_ocr( path ):#图片识别
    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\tesseract\\tesseract.exe'
    tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\tesseract\\tessdata"'
    file = os.path.splitext(path)
    filename, type = file
    if type == ".jpg" or type == ".png":
        code = pytesseract.image_to_string(Image.open(path), lang='chi_sim', config=tessdata_dir_config)
        stuta_list = list(set(jieba.lcut(code)))#识别文件库了的内容
        return stuta_list
    else:
        print ("读取到未知文件格式：" + type)
        return []

def file_rename(name_dict):
    code_doxc = []
    os.chdir(r"‪D:\桌面\物联网18-2班团课截图".strip('\u202a'))
    for i in tqdm(os.listdir()):
        pic_path = os.getcwd() + '\\' + i
        file = os.path.splitext(pic_path)
        filename, type = file
        code_doxc.extend(list(set(pic_ocr(pic_path))))
        for key, value in name_dict.items():
            try:
                if key in code_doxc or value in code_doxc:
                    os.rename(filename + ".jpg", key + ".jpg")
            except:
                pass

def execl_handle(data_list):
    print ("执行读取Excel中...")
    data = xlrd.open_workbook(r"D:\桌面\物联网18-2班团课截图\1.物联网18-2班级名单.xls",
                              encoding_override='utf-8')  # 打开表格
    data_sheet1 = data.sheet_by_index(0)  # 获取sheet
    name_list = data_sheet1.col_values(1)  # 获取每列的信息
    student_id_list = data_sheet1.col_values(2)

    print ("执行写入Excel中...")
    book = xlwt.Workbook(encoding='utf-8')
    sheet_1 = book.add_sheet(sheetname='上交名单' , cell_overwrite_ok=True)
    for i in tqdm(range(37)):
        sheet_1.write(i , 0 , i+1)
        sheet_1.write(i, 1 , name_list[i])
        sheet_1.write(i, 2 , student_id_list[i])
        if name_list[i] in data_list or student_id_list[i] in data_list:
            style = xlwt.easyxf('pattern: pattern solid, fore_colour bright_green')
            sheet_1.write(i, 3, "已完成", style)
        else:
            style = xlwt.easyxf('pattern: pattern solid, fore_colour dark_red ')
            sheet_1.write(i, 3 , "未完成", style)
    book.save(r"D:\桌面\物联网18-2班团课截图\2.团课截图上交统计.xls")
    print("表格制作成功")
    return name_list , student_id_list

if __name__ == '__main__':
    code_txt = []
    os.chdir(r"‪D:\桌面\物联网18-2班团课截图".strip('\u202a'))  # 更改图区路径
    for i in tqdm(os.listdir()):
        pic_path = os.getcwd() + '\\' + i
        code_txt.extend(pic_ocr(pic_path))
    for times in range(5):  # 优化识别数据库
        for each in code_txt:
            if len(each) == 1 or len(each) == 4 or "10" <= each <= "200000" :
                code_txt.remove(each)
    final_data = list(set(code_txt))
    name , id_stu = execl_handle(final_data)
    dic = {}
    for i in range(37):
        dic[name[i]] = id_stu[i]
    file_rename(dic)
