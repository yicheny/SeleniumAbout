# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from time import sleep

from selenium import webdriver


# 测试元素定位
def test_positioning_elements():
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')  # 打开百度页面
    sleep(3)  # 注意，如果没有这里的等待，下面获取元素可能会失败的，因为DOM树还没构建出来
    driver.find_element_by_css_selector('#kw').send_keys('react')  # 获取搜索框并输入 react
    driver.find_element_by_css_selector('#su').click()  # 触发搜索按钮click时间
    sleep(5)  # 等待5秒
    driver.quit()  # 退出浏览器


# 测试浏览器全屏
def test_window_max():
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')
    driver.maximize_window()
    sleep(5)
    driver.quit()


# 测试设置浏览器尺寸
def test_set_window_size(width, height):
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')
    driver.set_window_size(width, height)
    sleep(5)
    driver.quit()


# 测试页面跳转
def test_jmp_page():
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')  # 进入百度首页
    sleep(1)
    driver.get('https://www.zhihu.com')  # 进入知乎首页
    sleep(1)
    driver.back()  # 退回一页
    sleep(1)
    driver.forward()  # 前进一页
    sleep(5)
    driver.quit()


# 测试页面刷新
def test_refresh():
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')  # 进入百度首页
    sleep(3)
    driver.refresh()
    sleep(5)
    driver.quit()


# 测试driver属性：url和标题
def test_driver_page_info():
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')  # 进入百度首页
    sleep(3)
    print("=============这是第1个页面============")
    first_url = driver.current_url
    first_title = driver.title
    print("第1个页面的url是：" + first_url)
    print("第1个页面的标题是：" + first_title)
    navs = driver.find_elements_by_css_selector('.mnav')  # 获取百度导航栏
    map_nav = navs[2]  # 导航栏第三项是 地图【百度地图】
    driver.get(map_nav.get_property('href'))  # 跳转百度地图
    sleep(3)
    print("=============这是第2个页面============")
    second_url = driver.current_url
    second_title = driver.title
    print("第2个页面的url是：" + second_url)
    print("第2个页面的标题是：" + second_title)
    sleep(5)
    driver.quit()


# 测试 是否进入预期页面
def test_except_title():
    driver = webdriver.Chrome()
    driver.get('http:/www.zhihu.com')  # 进入知乎首页
    sleep(3)
    current_title = driver.title
    except_title = '百度一下，你就知道'
    if current_title == except_title:
        print('成功进入百度首页！')
    else:
        print('没有进入百度首页，当前首页是' + current_title)
    sleep(5)
    driver.quit()


# 测试 浏览器类型
def test_browser_type():
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')  # 进入知乎首页
    sleep(3)
    print('当前运行的浏览器平台是：' + driver.name)
    sleep(5)
    driver.quit()


# 测试 关闭当前窗口
def test_close_current_tab():
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')
    sleep(3)
    navs = driver.find_elements_by_css_selector('.mnav')  # 获取百度导航栏
    navs[2].click()  # 进入百度地图
    sleep(5)
    driver.close()  # 如果只有一个会被关闭


# 测试 退出浏览器
def test_quit_browser():
    driver = webdriver.Chrome()
    driver.get('http:/www.baidu.com')
    sleep(5)
    driver.quit()


if __name__ == '__main__':
    test_close_current_tab()
