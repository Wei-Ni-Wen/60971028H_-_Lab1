# 匯入random函數
import random

# 程式執行
if __name__ == '__main__':
    a_List = ['Rock','Paper','Scissors']    # a_List紀錄電腦的隨機出拳
    b_List = ['r','p','s']      # b_List紀錄玩家的出拳
    print("Welcome to Rock, Paper, Scissors game!")     # 印出:歡迎來到猜拳遊戲
    times_ties = 0  # 計算平手的次數
    times_lose = 0  # 計算玩家輸掉的次數
    game = True     # 用來決定遊戲是否繼續的參數
    # 在玩家勝利一次之前持續進行猜拳遊戲
    while game == True:
        Yourmove = input("\nPlease enter your move: (r)ock (p)aper (s)cissors ")    # 輸入:玩家的出拳
        RPS_number = random.randint(0, 2)  # RPS_number 為一個 0 到 2 間的隨機數字
        print(a_List[b_List.index(Yourmove)], 'versus ', a_List[RPS_number])    # 印出:該次出拳狀態
        # 判斷輸贏
        if (b_List.index(Yourmove) == RPS_number):      # 如果玩家出拳和隨機出拳一樣
            print('It is a tie!')   # 印出:平手
            times_ties += 1     # 平手的次數+1
        elif (b_List.index(Yourmove) == 1 and RPS_number == 2) \
            or (b_List.index(Yourmove) == 2 and RPS_number == 3) \
            or (b_List.index(Yourmove) == 3 and RPS_number == 1):       # 如果玩家輸給隨機出拳
            print('You lose!')      # 印出:你輸了!
            times_lose += 1     # 玩家輸掉的次數+1
        else:   # 玩家勝利
            print('You win! You have', times_ties, 'ties and', times_lose, 'losses before your first win.')
            # 印出:你贏了! 你在 times_ties 次平手和 times_lose 次 輸掉後第一次勝利!
            game = False    # 令 game 為 False 跳出 while，結束程式
