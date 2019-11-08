# -*- coding:utf-8 -*-

# import area
from selenium import webdriver
import time


# class area
class DoubleElevn(object):

    def __init__(self):
        self.url = 'http://credit.cmbond.com/enjoy/return/index.html'  # 乐游天下抽奖主页URL
        self.imitate_time = 1.0  # 模拟人工操作延时

        self.jd_url_dict = {
            'Intel i5 9400': 'https://item.jd.com/100006434034.html',
            'Intel i5 9400F': 'https://item.jd.com/100002657042.html',
            'Intel i7 9700': 'https://item.jd.com/100003838555.html',
            'Intel i7 9700F': 'https://item.jd.com/100005600582.html',
            'Intel i7 9700K': 'https://item.jd.com/100000634417.html',
            'Intel i7 9700KF': 'https://item.jd.com/100002106617.html',
            'EVGA GeForce RTX 2080 Black GAMING': 'https://item.jd.com/100007306836.html',
            'EVGA GeForce RTX 2080 XC Ultra GAMING ': 'https://item.jd.com/100003557953.html',
            '华硕 DUAL-RTX2070-O8G-EVO OC ': 'https://item.jd.com/100004000682.html',
            '华硕 DUAL-RTX2070S-O8G-EVO OC 2070 SUPER ': 'https://item.jd.com/100003849939.html',
            '华硕 ROG-STRIX-RTX2070S-O8G-GAMING 2070 SUPER': 'https://item.jd.com/100006513892.html',
            '技嘉 AORUS GeForce RTX 2070 SUPER': 'https://item.jd.com/100006532574.html',
            '技嘉 AORUS GeForce RTX 2080 小雕': 'https://item.jd.com/100000767679.html',
            '技嘉 GeForce RTX 2070 GAMING OC': 'https://item.jd.com/100000902612.html',
            '技嘉 GeForce RTX 2070 SUPER WINDFORCE OC': 'https://item.jd.com/100008129152.html',
            '技嘉 GeForce RTX 2080 GAMING OC': 'https://item.jd.com/8945581.html',
            '技嘉 GeForce RTX 2080 SUPER WINDFORCE OC ': 'https://item.jd.com/100008129154.html',
            '铭瑄 MS-GeForce RTX2070 Super iCraft OC ': 'https://item.jd.com/100009181534.html',
            '铭瑄 MS-GeForce RTX2080 Super iCraft': 'https://item.jd.com/100008403128.html',
            '铭瑄 MS-GeForce RTX2080 Super iCraft OC': 'https://item.jd.com/100009181536.html',
            '七彩虹 Colorful GeForce RTX 2070': 'https://item.jd.com/100002622223.html',
            '七彩虹 Colorful GeForce RTX 2080SUPER Gaming ES': 'https://item.jd.com/100006881986.html',
            '七彩虹 iGame GeForce RTX 2070': 'https://item.jd.com/100002673918.html',
            '七彩虹 iGame GeForce RTX 2070 SUPER Vulcan X OC': 'https://item.jd.com/100006564774.html',
            '七彩虹 iGame GeForce RTX 2080 RNG Edition': 'https://item.jd.com/100002583012.html',
            '七彩虹 iGame GeForce RTX 2080 SUPER Advanced OC': 'https://item.jd.com/100006807602.html',
            '索泰 RTX2070 X-GAMING G3': 'https://item.jd.com/100002238509.html',
            '微星 黑龙 GeForce RTX 2070 SUPER DUKE 暗黑龙爵': 'https://item.jd.com/100007256672.html',
            '微星 黑龙 GeForce RTX 2080 8G DUKE 龙爵': 'https://item.jd.com/8928861.html',
            '微星 魔龙Z GeForce RTX 2070 GAMING Z': 'https://item.jd.com/100001057406.html',
            '微星 万图师 GeForce RTX 2070 VENTUS': 'https://item.jd.com/100005472062.html',
            '微星 万图师 GeForce RTX 2080 SUPER VENTUS OC': 'https://item.jd.com/100004021857.html',
            '微星 万图师 GeForce RTX 2080 VENTUS 8G V2': 'https://item.jd.com/100000971960.html',
            '西部数据 紫盘 1T': 'https://item.jd.com/4118191.html',
            '西部数据 紫盘 2T': 'https://item.jd.com/4934568.html',
            '西部数据 紫盘 3T': 'https://item.jd.com/4934566.html',
            '西部数据 紫盘 4T': 'https://item.jd.com/4934558.html',
            '金士顿 DDR4 2666 8G': 'https://item.jd.com/3180109.html',
            '金士顿 DDR4 2400 8G': 'https://item.jd.com/2121097.html',
            '金士顿 DDR4 2666 16G': 'https://item.jd.com/8391349.html',
            '金士顿 DDR4 3200 16G': 'https://item.jd.com/100005089420.html',
            '金士顿 DDR4 2400 16G': 'https://item.jd.com/2551276.html',
            '三星 500G M.2(NVMe) 970 EVO Plus': 'https://item.jd.com/100003181110.html',
            '三星 500G M.2(NVMe) 970 EVO': 'https://item.jd.com/7234518.html',
            '三星 512G M.2(NVMe) 970 EVO Pro': 'https://item.jd.com/7233972.html',
            '西部数据 500G M.2(NVMe) Black系列 SN750': 'https://item.jd.com/100003226990.html',
            '西部数据 500G M.2(NVMe) Blue SN500': 'https://item.jd.com/100004542168.html',
            '西部数据 500G M.2(NVMe) Black SN750': 'https://item.jd.com/100002945641.html',
            '九州风神 堡垒240 CPU水冷散热器': 'https://item.jd.com/6757751.html',
            '九州风神 水元素240T CPU水冷散热器': 'https://item.jd.com/6454809.html',
            '九州风神 大霜塔CPU散热器': 'https://item.jd.com/689273.html',
            '九州风神 大霜塔RGB风冷CPU散热器': 'https://item.jd.com/4893995.html',
            '酷冷至尊 T610P CPU风冷散热器': 'https://item.jd.com/5258627.html',
            '微星 MAG B365M MORTAR迫击炮': 'https://item.jd.com/100006611280.html',
            '技嘉 B365 M AORUS ELITE “小雕” ': 'https://item.jd.com/100003406477.html',
            '微星 B360M MORTAR迫击炮 ': 'https://item.jd.com/6833426.html',
            '华硕 TUF B360M-PLUS GAMING S ': 'https://item.jd.com/8074512.html',
            '华硕 PRIME B365-PLUS': 'https://item.jd.com/100005694450.html',
            '微星 MAG Z390 TOMAHAWK 战斧导弹': 'https://item.jd.com/100000616094.html',
            '玩家国度 ROG STRIX B365-G GAMING': 'https://item.jd.com/100005694452.html',
            '微星 MPG Z390 GAMING PRO CARBON 暗黑板': 'https://item.jd.com/100000616012.html',
            '华硕 TUF B365M-PLUS GAMING': 'https://item.jd.com/100005694456.html',
            '玩家国度  ROG STRIX B365-F GAMING ': 'https://item.jd.com/100003440821.html',
            '玩家国度 ROG STRIX Z390-E GAMING ': 'https://item.jd.com/100000561582.html',
            '华硕 PRIME Z390-A ': 'https://item.jd.com/100000542145.html',
            '技嘉 Z390 AORUS PRO WIFI “电竞专家”': 'https://item.jd.com/100000612305.html',
            '微星 MEG Z390 ACE 战神板': 'https://item.jd.com/100000578097.html',
            '技嘉 Z390 AORUS MASTER “电竞大师”': 'https://item.jd.com/100000668218.html',
            '玩家国度 ROG MAXIMUS XI HERO (WI-FI) ': 'https://item.jd.com/100000542035.html',
            '玩家国度 ROG STRIX Z390-F GAMING': 'https://item.jd.com/100000561834.html',
            '先马 黑洞 玻璃版 电脑游戏主机箱': 'https://item.jd.com/6076598.html',
            '先马 坦克3 电脑主机箱': 'https://item.jd.com/100003124872.html',
            'Tt 挑战者H2 黑色 机箱水冷电脑主机': 'https://item.jd.com/100000400393.html',
            '航嘉 金牌600W WD600K电脑电源': 'https://item.jd.com/100004924768.html',
            '鑫谷 额定600W GP700G黑金版电源': 'https://item.jd.com/1033531.html',
            '安钛克 HCG650金牌全模组 台式机电脑主机机箱电源650W': 'https://item.jd.com/6828139.html',
        }

    @staticmethod
    def browser_driver():
        """
        浏览器驱动设置
        :return: driver:浏览器驱动
        """

        try:
            driver_option = webdriver.ChromeOptions()
            driver_option.headless = True
            driver = webdriver.Chrome(options=driver_option)
            # driver = webdriver.Chrome()
            driver.set_page_load_timeout(300)
            driver.implicitly_wait(30)
            # driver.delete_all_cookies()  # 清除浏览器cookies
        except Exception as err:
            print('Start driver error:%s \n' % err)
            return None

        return driver

    @staticmethod
    def close_driver(driver):
        """
        关闭浏览器驱动
        :param driver: 浏览器驱动
        :return: None
        """

        try:
            driver.close()
        except Exception as err:
            print('Close driver error:%s \n' % err)
        return None

    @staticmethod
    def jd_item_info(driver, url):

        try:
            driver.get(url)  # 加载URL
            price_xpath_str = '//div[@class="summary-price-wrap"]/div[1]/div[2]/span[1]/span[2]'
            item_price = driver.find_element_by_xpath(price_xpath_str).text
            # print(url, item_price)
            print(item_price)
        except Exception as err:
            err_str = '打开JD商品信息页面报错！ 报错信息：%s URL:%s\n' % (err, url)
            print(err_str)
            return None

        return

    def jd_process(self):

        driver = self.browser_driver()
        for each_key in self.jd_url_dict.keys():
            each_url = self.jd_url_dict[each_key]
            self.jd_item_info(driver, each_url)
            time.sleep(self.imitate_time)
        self.close_driver(driver)

        return None

    def main(self):

        self.jd_process()

        return None


# main area
if __name__ == '__main__':
    de = DoubleElevn()
    de.main()
