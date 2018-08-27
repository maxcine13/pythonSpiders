# -*-coding:utf-8-*-
import myUtil.htmlUtil as html
import myUtil.fileutil as file

import re

words = '<li><span>白宇  \
<script>document.write("13510541315");</script>\
</span>\
</li>\
'
regex_str = "/[\{4e00}-\{9fa5}]+/u"
match_obj = re.findall(u"[\u4e00-\u9fa5]*",words)
# if match_obj:
#     print(match_obj.group(1))
print match_obj
