# 前提
|ソフト|バージョン|
|-|-|
|Mac OS Mojave|10.14.6|
|Python|3.7.3|
|pip|19.0.3|
|selenium|3.141.0|

今回はChromeでブラウザ操作をシミュレートする前提で進める。

なお、VSCodeでのコーディングを前提としているため、以下の拡張機能も入れておくこと。
* Python - Visual Studio Marketplace
https://marketplace.visualstudio.com/items?itemName=ms-python.python

以下のコマンドでpylintとanacondaも入れておくこと。
```bash
$ python -m pip install -U pylint
$ pip install anaconda
```

# 手順
## 必要ソフトの導入
Seleniumをインストールする。
```bash
$ pip install selenium
$ pip list
$ pip list
Package           Version
----------------- -------
anaconda          0.0.1.1
astroid           2.3.3
isort             4.3.21
lazy-object-proxy 1.4.3
mccabe            0.6.1
pip               19.0.3
pylint            2.4.4
selenium          3.141.0
setuptools        40.8.0
six               1.13.0
typed-ast         1.4.0
urllib3           1.25.7
wrapt             1.11.2
```

## コーディング
まずはchromedriverの場所を確認する。

```bash
$ which chromedriver
```

上記出力結果をもとに以下の通りコーディング。
```python
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
```

## 注意
Chromeとchromedriverのバージョンが一致しないと、プログラム実行時に以下のようなエラーが発生する。
```bash
This version of ChromeDriver only supports Chrome version 79
```

この場合はGoogleChromeをアップデートした上で、以下のコマンドでChromeDriverをアップデートすればいい。
```bash
$ chromedriver-update
```

# 参考
【超便利】PythonとSeleniumでブラウザを自動操作する方法まとめ | たぬハック
https://tanuhack.com/selenium/#Selenium
