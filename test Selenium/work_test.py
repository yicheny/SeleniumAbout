from time import sleep
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import xlwt

ERROR_INFOS = []
SUCCESS_INFO = []


def work_test(callback):
    try:
        # print('========' + process + '========')
        print('========测试用例开始执行========')
        driver = webdriver.Chrome()
        driver.maximize_window()
        callback(driver)
        # test_drag_resize(driver)
        # test_full_screen_png(driver)
        # test_full_screen_info(driver)
        sleep(100)
    finally:
        save_xls()
        # print(ERROR_INFOS,SUCCESS_INFO)


def login(driver, url):
    print("=======登录========")
    driver.get('http://localhost:3000/#/login?return=' + url)
    driver.find_element_by_css_selector('input[placeholder="用户名"]').send_keys('99990')
    driver.find_element_by_css_selector('input[placeholder="密码"]').send_keys('666666')
    driver.find_element_by_css_selector('.login_form__2RUnZ>.button').click()
    sleepStep()
    if (driver.current_url == 'http://localhost:3000/#/option/risk-hedging'):
        suc_print('登录成功：' + url)
    else:
        error_print('登录失败：' + url)


def login_risk_hedging(driver):
    login(driver, '/option/risk-hedging')


def test_drag_resize(driver):
    login_risk_hedging(driver)
    print('=======测试拖拽伸缩功能=======')
    dragEle = driver.find_element_by_css_selector('.Resize_resize__3Trai>div>div')
    positionRiskEle = driver.find_element_by_css_selector('.PositionRisk_view__DiUmd')
    init_height = positionRiskEle.get_property('offsetHeight')

    step = 30
    count = 3
    i = 0
    while (i < count):
        i = i + 1
        ActionChains(driver).move_to_element(dragEle).click_and_hold(dragEle).move_by_offset(0, step).perform()

    current_height = positionRiskEle.get_property('offsetHeight')
    offset = current_height - init_height
    expect_offset = step * count
    if (offset == expect_offset):
        suc_print("拖拽功能正常！")
    else:
        suc_print("拖拽功能出错！")


def test_full_screen_png(driver):
    print('=======测试全屏功能--截图=======')
    login_risk_hedging(driver)
    buttons = driver.find_elements_by_css_selector('.position-risk>.tab-header>.right .iconButton')
    full_screen_button = buttons[len(buttons) - 1]
    full_screen_button.click()
    save_png(driver, '全屏展开')
    sleepStep()
    full_screen_button.click()
    save_png(driver, '全屏收起')


def test_full_screen_info(driver):
    def get_menu_size():
        return driver.find_element_by_css_selector('.left-menu').size

    def get_order_deal_size():
        return driver.find_element_by_css_selector('.hedging-deal').size

    def compare_size(source, target):
        return source.get('width') == target.get('width') & source.get('height') == target.get('height')

    print('=======测试全屏功能--数据=======')
    login_risk_hedging(driver)
    init_menu_size = get_menu_size()
    init_order_deal_size = get_order_deal_size()
    buttons = driver.find_elements_by_css_selector('.position-risk>.tab-header>.right .iconButton')
    full_screen_button = buttons[len(buttons) - 1]
    full_screen_button.click()
    current_menu_size = get_menu_size()
    current_order_deal_size = get_order_deal_size()
    if (current_order_deal_size.width == 0 & current_menu_size.width == 49):
        suc_print('展开全屏状态正常！')
    else:
        error_print('展开全屏状态异常！')
    sleepStep()
    full_screen_button.click()
    current_menu_size = get_menu_size()
    current_order_deal_size = get_order_deal_size()
    if (compare_size(init_menu_size, current_menu_size) & compare_size(init_order_deal_size, current_order_deal_size)):
        suc_print('收起全屏状态正常！')
    else:
        error_print('收起全屏状态异常！')


def sleepStep():
    sleep(5)


def save_png(driver, name):
    picture_time = get_now()
    img_name = './imgs/' + name + '_' + picture_time + '.png'
    driver.save_screenshot(img_name)
    print(img_name + " 保存成功！")


def error_print(info):
    print(info)
    ERROR_INFOS.append(info)


def suc_print(info):
    print(info)
    SUCCESS_INFO.append(info)


def save_xls():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('测试结果')
    ws.write(0, 0, '记录信息')
    infos = ERROR_INFOS
    for s in SUCCESS_INFO:
        infos.append(s)
    row_index = 0
    while (row_index < len(infos)):
        ws.write(0, row_index + 1, infos[row_index])
    wb.save('./records/测试结果_' + get_now() + '.xls')


def get_now():
    return time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
