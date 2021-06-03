# 1. Yesterday 가사가 저장되어 있는 텍스트 파일을 읽어 가사에 사용되고 있는
# 단어들의  목록을 알파벳 순서로 출력하고, 각 단어들이 몇 개씩 사용되고 있는지
# 단어별 개수를  출력하는 프로그램 작성
# 리스트, 세트, 딕셔너리 등의 자료구조를 이용
# 단어들은 모두 소문자로 변환하여 사용다.
# lyrics= [
#     {"Yesterday all my troubles seemed so far away. Now it looks as though they're here to stay. "
#      "Oh, I believe in yesterday. Suddenly I'm not half the man I used to be. There's a shadow hanging over me. "
#      "Oh, yesterday came suddenly. Why she had to go, I don't know, she wouldn't say. "
#      "I said something wrong, now I long for yesterday. Yesterday love was such an easy game to play. "
#      "Now I need a place to hide away. Oh, I believe in yesterday. Why she had to go, I don't know,"
#      "she wouldn't say. I said something wrong, now I long for yesterday. Yesterday love was"}]
# lyricsD = dict(lyrics)
# print(lyrics)
# # lyricsS = lyrics.split()
# print('lyricsS')
# print("[출력결과 : 단어별 빈도]\n")

with open('yesterday.txt', 'r', encoding='utf-8') as f: textFile = f.readlines()
wordCounter = dict()
for line in textFile:
 if line.endswith("\n"): line = line[:-1]
 wordList = line.lower().split(' ')
 for word in wordList:
  if word in wordCounter:
   wordCounter[word] += 1
  else:
   wordCounter[word] = 1

print(wordCounter)

with open('yesterday.txt', 'r', encoding='utf-8') as f:
 # 딕셔너리로 저장해서 출력
 dic = dict()

 # 모든 파일을 불러와서 공백기준으로 쪼개기
 # lines에 있는 모든요소를 소문자
 lines = list(f.read().split())
 lines = list(map(lambda x: x.lower(), lines))

 # key값을 나타내기 위해 set으로 중복제거 후 리스트변환
 # 그 리스트를 오름차순 정렬
 temp_lines = list(set(lines))
 temp_lines.sort()

 # key값을 하나씩 불러와서 lines리스트 중 단어를 count한 값을 저장
 for line in temp_lines:
  dic[line] = lines.count(line)

# dic을 item으로 불러와 차례대로 출력
print("[출력결과 : 단어별 빈도]")
for k, v in dic.items():
 print(f"'{k}': {v}")

print('------3번------')


# 2. 한 줄에 두 개의 숫자가 저장되어 있는 파일을 읽어 와 한 줄의 두 숫자를
# 더한 후 연산 결과를 파일로 내 보내는 프로그램 작성
# 파일을 읽어오고 파일에 쓰고, 숫자에 대해 연산 하는 기능은 함수 sum()을 정의하여
# 사용한다.
#  sum(inputfile 객체,저장파일명)

#import