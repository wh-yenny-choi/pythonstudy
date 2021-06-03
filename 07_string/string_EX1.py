#email type 체크

email = input('input email : ')
if (email.find('@') == -1 or                        # @ 없는 경우
        email.find('.') == -1 or                    # . 없는 경우
        email.index('@') > email.index('.') or      # @과 . 위치가 바뀐경우
        email.index('.') - email.index('@') < 2 or  # @과 . 사이에 문자가 없는 경우
        email.index('@') == 0 or                    # @앞에 문자 없는 경우
        len(email) - email.index('.') <= 1 or       # . 뒤에 문자가 없는 경우
        email.count('@') >= 2 or                    # @ 두 번 이상 있는 경우
        email.count('.') >= 2 ):                    # . 두 번 이상 있는 경우우    print('이메일 형식이 아닙니다.')
print('입력한 이메일 : %s' %email)