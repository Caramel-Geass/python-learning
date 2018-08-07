"""
需要第三方库 googletrans
~~~~~~~~~~~~~~~~~~~~~~
* 功能说明
按照给定语种顺序，使用 google translate 自动批量化翻译输入文本内容（英语），并把结果保存在指定目录下的文本文件中。
"""


from googletrans import Translator
import time

translator = Translator()


# 执行一次翻译工作,并把翻译结果保存到指定位置
def translation(source_msg, dest, src, result_path):    # 参数为待翻译文本、目标语种、待翻译语种简码、结果保存路径。其中，
                                                        # 待翻译文本建议使用英语（简码已给出），目标语种不需要输入（执行中生成）
    result = translator.translate(source_msg, dest=dest, src=src)
    result_one = '%s \t' % dest + result.text
    print(result_one)
    with open(result_path, mode='a') as f:
        f.write(result_one + '\n')
    time.sleep(0.1)     # 不暂停的话似乎会有网络问题，反而更慢


# 批量翻译执行代码段
targetTranslate = input('输入待翻译语句：')
resultPath = input('输入结果保存路径：')
destDictAll = 'en af am ar Assamese Maithili bn Tibetan bodo cs da de Dogri el es et fa fi fr Canadian-French gu hi ' \
              'hu hy id it iw Jawa kk km kn ko Konkani Kashmiri lo lt lv Maithili ml Manipuri mr ms my no ne nl ' \
              'oriya pa pl pt pt ro ru Sanskrit Santali sd si sk sr su sv sw ta te th Tagalog tr uk ur vi zh-cn ' \
              'zh-tw zh-tw'.split()
destDictYes = 'en af am ar bn cs da de el es et fa fi fr gu hi hu hy id it iw kk km kn ko lo lt lv ' \
              'ml mr ms my no ne nl pa pl pt pt ro ru sd si sk sr su sv sw ta te th tr uk ur vi zh-cn ' \
              'zh-tw zh-tw'.split()
for dest in destDictAll:
    if dest in destDictYes:
        translation(targetTranslate, dest=dest, src='en', result_path=resultPath)    # 输入待翻译文本（建议使用英语，简码已给出）和结果保存路径
    else:
        print('%s \t' % dest + '')
        with open(resultPath, mode='a') as f:
            f.write('%s \t' % dest + '\n')
print('Done.')  # 翻译结束后会在显示器上显示 Done.
