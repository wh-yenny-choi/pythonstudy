#파일생성 : 파일명만 적기
# f=open('file1.txt','w')
# f.close()
# #생성된 file1.txt 파일은 빈 파일

#경로 수정 : 디렉토리가 존재하지 않는 경우

# f=open("c:/pythonstudy/file1.txt",'w')
# f.close()
# FileNotFoundError: [Errno 2] No such file or directory: 'c:/python/file1.txt'

#디렉토리 경로 설정 시 오류 \ 사용하면 오류 발생 => \\또는 /
#파일의 절대경로
#f=open("c:/pythonstudy\file1.txt",'w')
f=open("c:/pythonstudy\\file1.txt",'w')
f.close()
# OSError: [Errno 22] Invalid argument: 'c:/pythonstudy\x0cile1.txt'

# 상대경로 표현
f=open("../file1.txt",'w')  # . > 바로 상위에 있는 폴더 표현
f.close()
#C:/pythonstudy/16_fileIO/01_file_기본.py