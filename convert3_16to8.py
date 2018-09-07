#-*-coding:utf8-*-
# 2016, June
# writer: Jo Eun Kyoung
# etc: This works in Python 3.X

import os, glob

def convert_utf16_utf8(fn, ofn):
    #fp = open(fn).read()
    fp = open(fn,encoding='utf-16').read()
    outfile = open(ofn, 'w', encoding='utf-8')
    outfile.write(fp)
    #outfile.write(fp.decode('utf-16').encode('utf8'))
    outfile.close()

def convert_all(in_dir, out_dir):
    fn_list = glob.glob(in_dir +'/*.txt')
    if os.path.exists(out_dir) != True:
        os.mkdir(out_dir)
    for f in fn_list:
        convert_utf16_utf8(f, f.replace(in_dir, out_dir))

if __name__ == "__main__":
    convert_all('TXT', 'para')
