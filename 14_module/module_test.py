# __name__ : import 참조하는 파일명
# 또는 현재 실행되는 파일을 나타내는 __main__을 가지고 있는 변수

# __name__과 __main__차이점

import module

print('main_test.py __name__' , __name__)

# Hello 모듈 start
# module.py __name__:  module
# Hello 모듈 end
# main_test.py __name__ __main__

#module.py
# print('Hello 모듈 start')
# print('module.py __name__: ',__name__)
# print('Hello 모듈 end')
