from random import randint


print('카지노에 오신걸 환영합니다.')

computer_number = randint(1,5)


while True:

  user_number = int(input('숫자를 입력해주세요!'))
  if user_number == computer_number:
    print('승리!')
    break
  elif user_number < computer_number:
    print('작습니다 ㅠㅠ 실패')
  else:
    print('큽니다 ㅠㅠ 실패')



