#
# Seleniumを使って、Chromeでブラウザ操作をシミュレートする
#

# 例
# [要素の指定]
# id属性で指定する
# driver.find_element_by_id('ID')
#
# class属性で指定する
# driver.find_element_by_class_name('CLASS_NAME')
#
# name属性で指定する
# driver.find_element_by_name('NAME')
#
# [要素の操作]
# クリックする
# driver.find_element_by_id('ID').click
#
# テキストを入力する
# driver.find_element_by_id('ID').send_keys('文字列')
#
# テキストを取得する
# driver.find_element_by_id('ID').text
#
# テキストをクリアする
# driver.find_element_by_id('ID').clear()

# ==================================
# 事前準備

# Selemiumのドライバをインポート
from selenium import webdriver

# キーボード操作を行うためのライブラリをインポート
from selenium.webdriver.common.keys import Keys

# ==================================
# 関数

# ==================================
# メイン処理
driver = webdriver.Chrome('/Users/watson/.rbenv/shims/chromedriver')

# Googleにアクセス
driver.get('https://www.ruby-lang.org/ja/')

# 検索キーワードを入力
search_box=driver.find_element_by_class_name('field')
search_box.send_keys('テスト')

# Enterを押す
search_box.send_keys(Keys.RETURN)
