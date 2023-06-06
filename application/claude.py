# Made By Mercuria

from selenium import webdriver
from datetime import datetime
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

def short_sleep(min_time=2, max_time=5):
    time.sleep(random.uniform(min_time, max_time))

def long_sleep(min_time=10, max_time=15):
    time.sleep(random.uniform(min_time, max_time))

def find_element_with_retry(driver, by, locator, max_wait=15, retry_interval=2):
    wait = WebDriverWait(driver, max_wait)

    while True:
        try:
            element = wait.until(EC.presence_of_element_located((by, locator)))
            return element
        except:
            time.sleep(retry_interval)

def create_new_area(driver):
    short_sleep()

    create_button = find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="landing_view_confirm_button"]')
    create_button.click()

    short_sleep()

    textbox = find_element_with_retry(driver,By.ID,"setup-page-team-name")
    textbox.send_keys(Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE + Keys.BACKSPACE)
    textbox.send_keys(datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))

    short_sleep()

    next_button = find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="setup-page-team-name-submit"]')
    next_button.click()

    short_sleep()

    next_button = find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="setup-page-profile-submit"]')
    next_button.click()

    short_sleep()

    skip_button = find_element_with_retry(driver,By.CLASS_NAME,"c-link--button.p-setup_page__content_secondary_link.no_wrap.margin_left_0.margin_top_50")
    skip_button.click()

    short_sleep()

    confirm_button=find_element_with_retry(driver,By.CLASS_NAME,"c-button.c-button--danger.c-button--medium")
    confirm_button.click()

    short_sleep()


    textbox = find_element_with_retry(driver,By.ID,"setup-channel-name-input")
    textbox.click()
    textbox.send_keys("ztry")

    short_sleep()

    next_button = find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="step-channels-footer-next"]')
    next_button.click()


    short_sleep()

    confirm_button = find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="setup_flow_tada_coachmark_cta"]')
    confirm_button.click()

    short_sleep()

    browse_slack_menu= find_element_with_retry(driver,By.CLASS_NAME,"nudge_left_1.p-channel_sidebar__section_heading_more_label")
    browse_slack_menu.click()

    short_sleep()

    slack_connect_label=find_element_with_retry(driver,By.XPATH,"//div[text()='Slack Connect']")
    slack_connect_label.click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="sk_close_modal_button"]').click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="slack_connect_landing_page__channel_cta"]').click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="trial_entry_point_modal_start_trial_button"]').click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="modal_speed_bump_continue"]').click()

    short_sleep()

    textbox = find_element_with_retry(driver,By.ID,"channel-name")
    textbox.send_keys("try_claude")

    #此处必须long sleep，使用short sleep有概率报错。
    long_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="create-channel-next-button"]').click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="create-channel-next-button"]').click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="invite_to_workspace_skip_button"]').click()

    short_sleep()

    workspace_url = driver.current_url

    driver.get("https://slackbot.anthropic.com/slack/install")

    #必须long_sleep
    long_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="oauth_submit_button"]').click()

    short_sleep()

    driver.get(workspace_url)

    long_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="texty_mention_button"]').click()

    short_sleep()

    claude_label=find_element_with_retry(driver,By.CSS_SELECTOR,'span[data-qa="member_name__app"]')
    claude_label.click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="texty_send_button"]').click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="at_mention_invite_warning__invite_button"]').click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="texty_mention_button"]').click()

    short_sleep()

    claude_label=find_element_with_retry(driver,By.CSS_SELECTOR,'span[data-qa="member_name__app"]')
    claude_label.click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="texty_send_button"]').click()

    short_sleep()

    agree_label=find_element_with_retry(driver,By.XPATH,"//span[text()='Agree']")
    agree_label.click()

    short_sleep()

    find_element_with_retry(driver,By.CSS_SELECTOR,'button[data-qa="dialog_go"]').click()

    long_sleep()

    return

def main():

    email="a826944805@outlook.com"

    options = webdriver.EdgeOptions()
    options.add_argument("-inprivate")

    driver = webdriver.Edge(options=options)

    #打开登录页面，url为要打开的地址
    driver.get("https://slack.com/intl/zh-cn/get-started")

    #元素定位登录按钮

    textbox = find_element_with_retry(driver,By.ID,"creator_signup_email")
    #点击登录
    textbox.click()
    textbox.send_keys(email)

    #等待
    short_sleep()

    submit_button = find_element_with_retry(driver,By.ID,"submit_btn")
    submit_button.click()

    input("请手动输入验证码，按下回车键继续执行...")

    create_new_area(driver)

    while(1):
        driver.get("https://slack.com/intl/zh-cn/get-started")
        create_new_area(driver)
    
if __name__ == '__main__':
    main()