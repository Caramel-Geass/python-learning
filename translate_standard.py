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

from googletrans import Translator
import time

translator = Translator()
destDict = {'ar_EG\n': 'ar', 'bn_BD\n': 'bn', 'bn_IN\n': 'bn', 'cs_CZ\n': 'cs', 'da_DK\n': 'da', 'de_DE\n': 'de',
            'el_GR\n': 'el', 'en_GB\n': 'en', 'en_IN\n': 'en', 'en_US\n': 'en',
            'es_ES\n': 'es', 'es_US\n': 'es', 'et_EE\n': 'et', 'fa_IR\n': 'fa', 'fi_FI\n': 'fi',
            'fr_FR\n': 'fr', 'gu_IN\n': 'gu', 'hi_IN\n': 'hi', 'hu_HU\n': 'hu', 'hy_AM\n': 'hy', 'in_ID\n': 'id',
            'it_IT\n': 'it', 'iw_IL\n': 'iw', 'kk_KZ\n': 'kk', 'km_KH\n': 'km', 'kn_IN\n': 'kn', 'ko_KR\n': 'ko',
            'lt_LT\n': 'lt', 'lv_LV\n': 'lv', 'ml_IN\n': 'ml', 'mr_IN\n': 'mr', 'ms_MY\n': 'ms', 'my_MM\n': 'my',
            'nb_NO\n': 'no', 'ne_IN\n': 'ne', 'ne_NP\n': 'ne', 'nl_NL\n': 'nl', 'pa_IN\n': 'pa', 'pl_PL\n': 'pl',
            'pt_BR\n': 'pt', 'pt_PT\n': 'pt', 'ro_RO\n': 'ro', 'ru_RU\n': 'ru', 'sk_SK\n': 'sk', 'sr_RS\n': 'sr',
            'sv_SE\n': 'sv', 'ta_IN\n': 'ta', 'te_IN\n': 'te', 'th_TH\n': 'th', 'tr_TR\n': 'tr', 'uk_UA\n': 'uk',
            'ur_IN\n': 'ur', 'ur_PK\n': 'ur', 'vi_VN\n': 'vi', 'zh_CN\n': 'zh-cn', 'zh_HK\n': 'zh-tw',
            'zh_TW\n': 'zh-tw', 'as_IN\n': 'as_IN', 'or_IN\n': 'or_IN', 'si_LK\n': 'si', 'am_ET\n': 'am'}


# 返回目标语种文本行数
def line_number(target_language):   # 参数为目标语种文本文件路径
    with open(target_language, 'r') as f:
        lineNumber = 0
        while f.readline():
            lineNumber = lineNumber + 1
        return lineNumber


# 执行一次翻译工作,并把翻译结果保存到指定位置
def translation(source_msg, dest, src, result_path):    # 参数为待翻译文本、目标语种、待翻译语种简码、结果保存路径。其中，
                                                        # 待翻译文本建议使用英语（简码已给出），目标语种不需要输入（执行中生成）
    if dest == 'as_IN':  # 两种 google translate 不可翻译的语言用 null 给出
        result_one= '%s \t' % dest + ''
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
targetPath = input('输入目标语种文本文件路径：')
targetTranslate = input('输入待翻译语句：')
resultPath = input('输入结果保存路径：')
standardCodes = open(targetPath)    # 输入目标语种文本文件路径
lineNumber = line_number(targetPath)    # 输入目标语种文本文件路径
while lineNumber > 0:
    dest = destDict[standardCodes.readline()]
    if dest != '':
        translation(targetTranslate, dest=dest, src='en', result_path=resultPath)    # 输入待翻译文本（建议使用英语，简码已给出）和结果保存路径
    lineNumber = lineNumber - 1
standardCodes.close()
print('Done.')  # 翻译结束后会在显示器上显示 Done.
