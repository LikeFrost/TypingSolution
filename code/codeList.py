import pinyin

for i in range(0x4e00,0x9fa5,1):
    c=('\\u{:04x}'.format(i)).encode().decode('unicode_escape')
    data = open("unicode.txt", 'a+')
    print(pinyin.get(c,format='strip'), file=data)
    data.close()
    print(c)
    print (pinyin.get(c,format='strip'))