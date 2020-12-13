#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Kinddle
import re, os

def fun(path, patterns:list):
    # path为待修改的文件路径 匹配类似于herf="\static\..."的相对地址， 修改为herf="{% static '...'%}" 其中herf可以修改为src等
    for pattern in patterns:
        with open(path, 'r+', encoding='utf-8') as F:
            file_tmp=""
            for line in F:
                print(line)
                chgset=re.findall(pattern+"=\"static.*?\"", line)
                if len(chgset)!=0:
                    chgset = chgset[0]
                    tmp = re.split(chgset, line)
                    paths=re.findall(pattern+'="static(.*?)"', chgset)[0]
                    chgset_ = pattern+"=\"{% static '"+paths[1:]+"' %}\""
                    newline = tmp[0]+chgset_+tmp[1]
                    file_tmp+=newline
                else:
                    file_tmp+=line
            F.seek(0)
            F.truncate()
            F.write(file_tmp)
            print(file_tmp)

def fun2(root):
    filelist = os.listdir(root)
    filelist = [i for i in filelist if i[-5:]==".html"]
    return filelist

template_root="../template"

filelist = fun2(template_root)
for file in filelist:
    fun(template_root+"/"+file, patterns=["href", "src"])

# fun("../template/index.html", patterns= ['href',"src"])







