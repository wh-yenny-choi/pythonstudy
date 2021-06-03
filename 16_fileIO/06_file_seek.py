#파일 내에서 검색
#seek(offset, whence)함수

print('-----파일 내에서 검색 seek()-----')

#한글 ut-8 : 3byte씩, utf-16 : 2byte씩
f = open('text2_utf16.txt','r',encoding='utf-16') #텍스트 파일 자체가 utf-16으로 저장
f = open('text2.txt','r',encoding='utf-8')
# f.seek(0,0)  #시작위치 0행,0열
# f.seek(1,0)  #오류 발생 : UnicodeDecodeError: 'utf-8' codec can't decode byte 0xbb in position 0: invalid start byte
# f.seek(7,0)
# f.seek(15,0)
# f.seek(14,0)
# f.seek(17,0)
f.seek(16,0)

lines = f.readlines()
print(lines)
f.close()

