# 中文數字統一轉換工具

🚩 **只要是中文數字或阿拉伯數字，一律統一轉成阿拉伯數字，無論全形半形繁體簡體、或任何 Mix 格式皆可當作輸入**
🚩 **數字單位在「億」以內的都能支援**

這是一個能夠將不同格式的繁體、簡體、繁簡合併以及包含數字的字串，統一轉換成數字的工具。這對於在中文環境中進行文本處理，特別是需要將不同格式的數字統一成標準格式時，非常有用。

**只需將 number_converter.py 放至自己專案底下的資料夾即可呼叫使用！**

## 功能特點

- 輕量、簡單、快速、準確的轉換工具
- 將繁體字轉換為數字。
- 將簡體字轉換為數字。
- 將繁體字和簡體字合併後的字串統一轉換為數字。
- 處理包含數字的繁體、簡體、繁簡合併的混合字串，將其轉換為統一的數字格式。

## 範例
1. 中文型態字串
- 輸入：「五萬零五」
```
python number_converter.py --number 五萬零五
```
 - 輸出：50005

2. 中文數字參雜
- 輸入：「150萬5002」
```
python number_converter.py --number 150萬5002
```
 - 輸出：15005002

3. 中文數字簡體繁體全形半形參雜
- 輸入：「6千參佰零陸万４仟０貳」
```
python number_converter.py --number 6千參佰零陸万４仟０貳
```
 - 輸出：63064002

## 套件需求

requirementx.txt
```
OpenCC
cn2an
```

## 如何使用

** 歡迎參考 example.py **

### 1. 下載 github 文件
``` git
git clone git@github.com:kiangkiangkiang/Chinese-to-Number.git
```
```
cd Chinese-to-Number
```

### 2. 下載所需套件

```
pip install -r requirements.txt
```

### 3.1 CLI 執行
```
python number_converter.py --number YOUR_NUMBER
```
- YOUR_NUMBER：任意「中文數字簡體繁體的字串」，例如「9萬5千」
### 3.2 使用 Python 模組

```python
from number_converter import NumberConverter

my_converted = NumberConverter()
ANY_NUMBER = "五千六百萬"
my_converted.convert_to_number(ANY_NUMBER)
```

#### 詳細轉換結果可參考 example.py
