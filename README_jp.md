# Maya_CustomUVEditor  

目次
-----------------

  * [Description](#description)  
  * [Requirement](#requirement)  
  * [Infomation about Python Script](#infomation-about-python-script)  
  * [Install](#install)  
  * [Usage](#usage)  
  * [License](#license)  
  * [Author](#author)  

Description  
------------  
## 解説
このツールはMaya2017以上用のカスタムUVエディタです。

![custom_uveditor](https://user-images.githubusercontent.com/29208747/48949236-aa7a7200-ef7a-11e8-9162-ffab26dc337f.jpg)

Requirement  
------------  
## 必要条件
 Maya 2017 以上  


Infomation about Python Script
------------
## スクリプトについて
このツールはMaya2017に実装されたUVエディタの上部にパネルを追加し
UV値の取得と設定の項目、幾つかのUV値設定のボタン、などが表示されます。 


Install  
------------  
## インストール

1,  
ri_Custom_UV_Editor.py をMayaのスクリプトエディターにドラッグ＆ドロップし、
```py
custom_uv_editor()   
```
を追加、全てを選択して、Maya のシェルフボタンをPythonの種類で作成します。  

あるいは  

2,  
Maya のパスが通ったディレクトリーに ri_Custom_UV_Editor.py をコピーし、  

225行をコメントアウト(無効)にし  
226行を有効にして　モジュールを import　するようにします。  
最後の行に  

```py
custom_uv_editor()  
```
を用いて起動します。  


Usage  
------------  
## 使い方

### SUITE USERS NOTE　のWebサイトをご覧ください。
  https://www.comtec.daikin.co.jp/DC/UsersNotes/Ritaro/tutorial/maya_12/index.html


Licence  
------------  
## ライセンス
[MIT] (https://github.com/O-Ritaro/Maya_CustomUVEditor/blob/master/LICENSE)

Author  
------------  
## 記載者
Ritaro (https://github.com/O-Ritaro)