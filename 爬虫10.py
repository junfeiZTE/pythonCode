from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")       # define headless

driver = webdriver.Chrome(chrome_options=chrome_options)

# 将刚刚复制的帖在这
driver.get("https://morvanzhou.github.io/")
driver.find_element_by_xpath(u"//img[@alt='强化学习 (Reinforcement Learning)']").click()
driver.find_element_by_link_text("About").click()
driver.find_element_by_link_text(u"赞助").click()
driver.find_element_by_link_text(u"教程 ▾").click()
driver.find_element_by_link_text(u"数据处理 ▾").click()
driver.find_element_by_link_text(u"网页爬虫").click()

# 得到网页 html, 还能截图
html = driver.page_source       # get html
driver.get_screenshot_as_file("D:\\Python36-32\菜鸟\selenium1.png")
driver.close()

#firefox 的 katalon recorder 中test_untitiled_test_case 可以生成python代码
#selenium 还需要 安装driver
