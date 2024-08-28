import schedule
import time as tm
import pyautogui


def click():
    pyautogui.click(50, 1150, duration=1)
    pyautogui.click(50, 1150, duration=1)


def main():
    schedule.every(4).minutes.do(click)

    while True:
        schedule.run_pending()
        tm.sleep(1)


if __name__ == "__main__":
    main()
