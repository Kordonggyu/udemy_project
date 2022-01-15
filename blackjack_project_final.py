import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
user_cards = [random.choice(cards) for i in range(2)]
computer_cards = [random.choice(cards) for i in range(2)]

print("유저가 뽑은 카드의 숫자 : %s" % user_cards)
print("유저가 뽑은 카드의 숫자 합 : %s" % sum(user_cards))
print("딜러가 뽑은 카드의 숫자 : [%s, *]" % computer_cards[0])

if sum(user_cards) >= 22 :
    if 11 in user_cards :
        user_cards.remove(11)
        user_cards.append(1)

if sum(computer_cards) >= 22 :
    if 11 in user_cards :
        computer_cards.remove(11)
        computer_cards.append(1)

if sum(computer_cards) == 21 :
    print("-----딜러가 이겼습니다!-----")
elif sum(user_cards) == 21 :
    print("-----당신이 이겼습니다!-----")
elif sum(user_cards) == sum(computer_cards) == 21 :
    print("-----비겼습니다!-----")


while True :
    draw_question = input("한 장의 카드를 더 요구하시겠습니까? (네, 아니오) : \n")
    if draw_question == "네" :
        user_cards.extend([random.choice(cards) for i in range(1)])
        print("유저가 뽑은 카드의 숫자 : %s" % user_cards)
        print("유저가 뽑은 카드의 숫자 합 : %s" % sum(user_cards))
        
        if 11 in user_cards :
            if sum(user_cards) >= 22 :
                user_cards.remove(11)
                user_cards.append(1)
                print("유저가 뽑은 카드의 숫자 : %s" % user_cards)
                print("유저가 뽑은 카드의 숫자 합 : %s" % sum(user_cards))
        
        if sum(user_cards) >= 22 :
            print("-----딜러가 이겼습니다!-----")
            break
        else :
            continue
    else : 
        break

while True :
    if sum(computer_cards) < 16 :
        computer_cards.extend([random.choice(cards) for i in range(1)])
        if sum(computer_cards) >= 22 :
            if 11 in user_cards :
                computer_cards.remove(11)
                computer_cards.append(1)
            else :
                print("-----당신이 이겼습니다!-----")
                break
        else :
            continue
    else :
        break

print("유저가 뽑은 카드의 숫자 : %s" % user_cards)
print("유저가 뽑은 카드의 숫자 합 : %s" % sum(user_cards))
print("딜러가 뽑은 카드의 숫자 : %s" % computer_cards)
print("딜러가 뽑은 카드의 숫자 합 : %s" % sum(computer_cards))


if sum(computer_cards) and sum(user_cards) <= 21 :
    if sum(computer_cards) > sum(user_cards) :
        print("-----딜러가 이겼습니다!-----")
    elif sum(computer_cards) < sum(user_cards) :
        print("-----당신이 이겼습니다!-----")
    else :
        sum(computer_cards) == sum(user_cards) 
        print("-----비겼습니다!-----")

while True :
    again_question = input("한 판 더 하시겠습니까? (네, 아니오) : \n")
    if again_question == "네" :
        print("f5를 누르세요")
        break
    else :
        print("안녕히가세요^^")
        break

        




