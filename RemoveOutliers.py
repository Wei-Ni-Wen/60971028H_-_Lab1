# 定義remove_outliers()
def remove_outliers(n):
    print('\nThe original data: ', a_list)    # 印出原始的 a_list
    i = 0   # 用於計數的參數
    # 當 i < n時，持續執行程式
    while i < n:
        b_list.append(min(a_list))  # 將 a_list 的最小值加入 b_list
        a_list.remove(min(a_list))  # 將 a_list 的最小值移除
        b_list.append(max(a_list))  # 將 a_list 的最大值加入 b_list
        a_list.remove(max(a_list))  # 將 a_list 的最大值移除
        i += 1  # i 加 1
    b_list.sort()   # 將 b_list 從小排到大
    print('The data with the outliers removed:', a_list)    # 印出拿掉最大最小值的 a_list
    print('The outliers: ', b_list)     # 印出被拿掉的數字List: b_list
# 程式執行
if __name__ == '__main__':
    a_list = []     # 令 a_list 為空的 List
    b_list = []     # 令 b_list 為空的 List
    n = int(input('Enter the number of smallest and largest values to remove: '))   # 輸入:整數(最大及最小值要移除的數量)
    number_enter = input('\nEnter a value(q or Q to quit): ')     # 輸入
    # 當輸入不為 Q 或 q 時，持續執行程式
    while number_enter != 'Q' and number_enter != 'q':
        a_list.append(int(number_enter))    # 將輸入的數值加入 a_list 最後面
        number_enter = input('Enter a value(q or Q to quit): ')     # 輸入:整數
    remove_outliers(n)   # 執行 remove_outliers()













