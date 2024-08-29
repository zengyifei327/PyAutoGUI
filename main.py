import schedule
import time as tm
from datetime import datetime
import pyautogui


def click():
    pyautogui.click(50, 1150, duration=1)
    pyautogui.click(50, 1150, duration=1)


def main():
    schedule.every(4).minutes.do(click)

    while True:
        current_time = datetime.now().time()

        # Define the time range (9 AM to 4 PM)
        start_time = datetime.strptime("09:00", "%H:%M").time()
        end_time = datetime.strptime("16:00", "%H:%M").time()

        if start_time <= current_time <= end_time:
            schedule.run_pending()

        tm.sleep(1)


if __name__ == "__main__":
    main()
