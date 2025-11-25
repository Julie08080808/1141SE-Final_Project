def print_simple_greeting():
    """單純輸出早安。"""
    print("☀️ 午安！ ☀️")

def print_pyramid(layer=7):
    """
    列印指定層數的星號金字塔。
    """
    print("\n--- 七層金字塔 ---")
    
    # 計算金字塔底部的最大寬度
    max_width = layer * 2 - 1
    
    for i in range(1, layer + 1):
        # 計算星號數量 (2*i - 1)
        stars = 2 * i - 1
        # 計算置中所需的空格數量
        spaces = (max_width - stars) // 2
        
        # 印出對齊後的行
        line = " " * spaces + "*" * stars
        print(line)

# 執行主要功能
print_simple_greeting()
print_pyramid(layers=5)