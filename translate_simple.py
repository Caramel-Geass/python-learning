"""
需要第三方库 googletrans
~~~~~~~~~~~~~~~~~~~~~~
* 功能说明
从目标文本文件中读取翻译语种目标，使用 google translate 自动批量化翻译并把结果保存在指定目录下的文本文件中
* 使用说明
1. 从 google drive 中直接复制目标语种代码列，粘贴到文本编辑器中（如 sublime），在最后一行加一个 enter 并保存，这个文本文件的内容即形如
‘ar_EG\nbn_BD\n...zh_TW\n’
2. 来到批量翻译执行代码段， 在对应位置输入目标语种文本文件路径和结果保存路径，随后执行代码
eg: standardCodes = open('/Users/huomingyu/Desktop/target_language')
    lineNumber = line_number('/Users/huomingyu/Desktop/target_language')
    while lineNumber > 0:
        dest = destDict[standardCodes.readline()]
        if dest != '':
            translation('Mission complete!', dest=dest, src='en', result_path='/Users/huomingyu/Desktop/result')
        else:
            print('Done.')
        lineNumber = lineNumber - 1
3. 打开保存的结果，全选，直接粘贴到 google drive 中即可
"""

"""
from googletrans import Translator
import time

translator = Translator()


# 执行一次翻译工作,并把翻译结果保存到指定位置
def translation(source_msg, dest, src, result_path):    # 参数为待翻译文本、目标语种、待翻译语种简码、结果保存路径。其中，
                                                        # 待翻译文本建议使用英语（简码已给出），目标语种不需要输入（执行中生成）
    if dest == 'as_IN':  # 两种 google translate 不可翻译的语言用 null 给出
        result_one = '%s \t' % dest + ''
        print(result_one)
    elif dest == 'or_IN':
        result_one = '%s \t' % dest + ''
        print(result_one)
    else:
        result = translator.translate(source_msg, dest=dest, src=src)
        result_one = '%s \t' % dest + result.text
        print(result_one)
    with open(result_path, mode='a') as f:
        f.write(result_one + '\n')
    time.sleep(0.1)     # 不暂停的话似乎会有网络问题，反而更慢


# 批量翻译执行代码段
targetTranslate = input('输入待翻译语句：')
resultPath = input('输入结果保存路径：')
destDict = 'am ar as_IN bn bn cs da de el en en en es es et fa fi fr gu hi hu hy id it iw ' \
           'kk km kn ko lt lv ml mr ms my no ne ne nl or_IN pa pl pt pt ro ru si sk sr sv ' \
           'ta te th tr uk ur ur vi zh-cn zh-tw zh-tw'.split()
for dest in destDict:
    if dest != '':
        translation(targetTranslate, dest=dest, src='en', result_path=resultPath)    # 输入待翻译文本（建议使用英语，简码已给出）和结果保存路径
print('Done.')  # 翻译结束后会在显示器上显示 Done.
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
