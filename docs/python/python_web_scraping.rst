Python Web Scraping
===================

beautifulsoup
-------------


urllib
------


Selenium
--------

pip3 install selenium

Example::

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    from time import sleep
    from selenium import webdriver

    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")

    driver.find_element_by_id("kw").send_keys("Selenium2")
    driver.find_element_by_id("su").click()                     # search "Selenium2"

    sleep(1)
    driver.get_screenshot_as_file('./search_result.png')

    driver.implicitly_wait(10)
    driver.find_element_by_xpath(".//*[@id='1']/h3/a").click()  # goto the first result

    sleep(3)
    driver.quit()

.. note::

    | Fix issue that firefox 47.0 in ubuntu 16.04 is not supported yet.
    | If you have also some problems when run above example, please have try:
    |     $ sudo apt-get purge firefox  # remove current firefox 47.0
    |     $ sudo apt-cache show firefox | grep Version  # checke valid versions
    |     $ sudo apt-get install firefox=45.0.2+build1-0ubuntu1 # install this 45.0 version
    |     $ sudo apt-mark hold firefox  # mark that will not update firefox
    | If you want to update firefox later:
    |     $ sudo apt-mark unhold firefox
    |     $ sudo apt-get upgrade
    |


Scrapy
------


pyspider
--------

http://docs.pyspider.org/en/latest/

https://www.figotan.org/2016/08/10/pyspider-as-a-web-crawler-system/?hmsr=toutiao.io&utm_medium=toutiao.io&utm_source=toutiao.io

