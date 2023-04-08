"""
按键预设:
    1. 结算 和 提交订单
    2. 返回
    3. 我知道了

1. 天猫超市, 茅台加入购物车
2. 雷电模拟器, 打开淘宝天猫超市购物车页面, 在 结算 按钮处, 设置 预设按键:1
3. 程序在 时间到了 抢购时间后, 自动点击 1 (即结算)
        若点击时间过早, 会出现 失效宝贝, 则点2 返回
4. 判断页面中是否有(同一时间下单人数过多...我知道了)
      若有, 则点击 我知道了, 回到购物车.
      若无, 则自动点击1 (即提交订单)
"""

import pyautogui
from datetime import datetime
from datetime import timedelta
import time
import random


start_time_a = '2023-01-18 20:00:00'    # 抢购时间
start_time = datetime.strptime(start_time_a, '%Y-%m-%d %H:%M:%S')
end_time = start_time + timedelta(seconds=5)    # 开始5秒钟后,即结束

pyautogui.click(402, 4)    # 将模拟器设置焦点  # 模拟器位置 (402,4)

while True:
    time_now = datetime.now()
    print(time_now)

    if time_now >= end_time:    # 结束时间, 停止抢购
        print('抢购失败!!')
        break
    elif time_now >= start_time:
        pyautogui.press('1')    # 雷电模拟器, 点击 天猫超市购物车中的结算按钮

        if pyautogui.locateOnScreen('sum0.png', confidence=0.6, grayscale=True):
            pyautogui.press('2')    # 点早了, 失效订单, 返回到购物车页面
            time.sleep(random.uniform(0.1, 0.3))    # 等待 0.1--0.3秒
        else:
            time.sleep(0.5)    # 0.2秒不够, '前方拥挤'窗口尚未弹出
            if pyautogui.locateOnScreen('busy.png', confidence=0.8, grayscale=True):    # 前方拥堵
                pyautogui.press('3')    # 点击我知道了, 返回购物车页面
                print('已点击键盘3')
            else:
                pyautogui.press('1')  # 提交订单
                print('已点击键盘1')
                time.sleep(0.4)
                if pyautogui.locateOnScreen('busy.png', confidence=0.8, grayscale=True):    # 前方拥堵
                    pyautogui.press('3')  # 点击我知道了, 返回购物车页面
                    print('已点击键盘3(第二个)')
                else:
                    time.sleep(0.4)
                    if not pyautogui.locateOnScreen('busy.png', confidence=0.8, grayscale=True):
                        print('抢购成功!!!')
                        break


