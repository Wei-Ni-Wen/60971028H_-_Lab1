# 定義reverse()
def reverse(number):
    enter_List = []     # 令 enter_List 為空的 List
    enter_List.extend(str(number))      # number 以字串的形式加入 enter_List
    # 將 enter_List 中的元素從最後面到最前面印出
    for i in enter_List[::-1]:
        print(i, end="")

# 程式執行
if __name__ == '__main__':
    number = int(input('Enter an integer: '))   # 輸入:整數
    reverse(number)     # 反轉輸入的整數並印出
