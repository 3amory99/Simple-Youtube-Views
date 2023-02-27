from selenium import webdriver
import time


def main():
    url = input("Please enter the video url: ")
    # it would be recommended not to be more than 500 views
    views = int(input("Please enter the number of views: "))
    # it would be recommended not to be more than 10 seconds
    waitting = int(input("Please enter the time between each view: "))

    for i in range(waitting):
        browser = webdriver.Chrome()
        browser.get(url)
        time.sleep(waitting)
        browser.close()

if __name__ == '__main__':
    main()
