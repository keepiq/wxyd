# -*- coding: utf-8 -*
'''
cron: 15 */16 * * * wskey.py
new Env('wskey转换');
'''
import lzma, base64
f = open("./wscat_implicit.py",'a')

#print(
f.writelines(bytes.decode(lzma.decompress(base64.b64decode('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'))))
f.close()
