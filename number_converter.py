import argparse
import re
from typing import Union

import cn2an
import opencc


class NumberConverter(object):
    """數值格式化工具"""

    def __init__(self) -> None:
        self.__converter_t2s = opencc.OpenCC("t2s.json")
        self.__converter_s2t = opencc.OpenCC("s2t.json")
        self.__convert_chinese_to_number = lambda x: cn2an.cn2an(self.__converter_t2s.convert(x), "smart")

        # 統一使用的單位字元
        self.trans_map = {"拾": "十", "佰": "百", "仟": "千"}

        # 無法處理的例外字元
        self.special_word = {"參": "叁"}

    def __do_fill_zero(self, partial_money, default_unit):
        default_unit_pointer = 0
        tmp_result = []
        for text in partial_money:
            if text in default_unit[default_unit_pointer:]:
                adjust_index = [i for i, u in enumerate(default_unit[default_unit_pointer:]) if u == text][0]
                if adjust_index != 0:  # skip unit
                    tmp_result.append("零")
                    default_unit_pointer = default_unit_pointer + adjust_index
                default_unit_pointer += 1
            elif text in default_unit[:default_unit_pointer]:
                raise ValueError("Repeat unit occur.")
            tmp_result.append(text)
        if default_unit_pointer != len(default_unit):
            tmp_result.append("零")
        return tmp_result

    def add_zero_for_missing_unit(self, money: str) -> str:
        """將缺失單位補零

        Ex.:
            五萬六百二十五 -> 五萬零六百二十五

        Args:
            money (str): 中文型態的數字字串

        Returns:
            str: 補零後的中文型態數字字串
        """

        unit = ["十", "百", "千", "萬", "億", "兆"]
        unit_pointer = 3  # initial on 萬
        raw_money = list(reversed(re.sub("零", "", self.__converter_s2t.convert(money))))
        new_money = []
        tmp_money = []
        for text in raw_money:
            if text in unit[unit_pointer:]:
                adjust_index = [i for i, u in enumerate(unit[unit_pointer:]) if u == text][0]
                unit_pointer = unit_pointer + adjust_index
                tmp_money = self.__do_fill_zero(tmp_money, unit[:unit_pointer])
                new_money.extend(tmp_money)
                new_money.append(text)
                unit_pointer += 1
                tmp_money = []
            else:
                tmp_money.append(text)
        if tmp_money:
            tmp_money = self.__do_fill_zero(tmp_money, unit[:unit_pointer])
            new_money.extend(tmp_money)
        new_money.reverse()

        new_money = new_money if new_money[0] != "零" else new_money[1:]
        new_money = new_money if new_money[-1] != "零" else new_money[:-1]

        return new_money

    def format_to_chinese(self, money: str) -> str:
        """格式化數值：將金錢統一轉成中文。

        Ex.:
            150萬52 -> 一百五十萬零五十二

        Args:
            money (str): 簡體、繁體、中文型態數字字串，等等所有排列組合，只要是中文數字字串皆可。

        Returns:
            str: 標準化後的中文型態數字字串
        """

        found_chinese = re.finditer("[\u4e00-\u9fa5]+", money)
        last_start = 0
        final_money = []
        for each_found in found_chinese:
            start, end = each_found.span()
            number = []
            for index in range(last_start, start):
                number.append(money[index])
            if number:
                number = cn2an.an2cn("".join(number)) if number[0] != "0" else "零" + cn2an.an2cn("".join(number))
            else:
                number = ""
            for index in range(start, end):
                number += money[index]
            final_money.append(number)
            last_start = end

        adjust_tail = []
        if last_start != len(money) - 1:
            for index in range(last_start, len(money)):
                adjust_tail += money[index]
            if adjust_tail:
                adjust_tail = (
                    cn2an.an2cn("".join(adjust_tail))
                    if adjust_tail[0] != "0"
                    else "零" + cn2an.an2cn("".join(adjust_tail))
                )
        if adjust_tail:
            final_money.append(adjust_tail)

        return "".join([s for s in final_money])

    def convert_to_number(self, money: str) -> Union[str, int]:
        try:
            # 統一轉成中文
            final_money = list(self.format_to_chinese(money))

            # 統一中文字元
            for i, s in enumerate(final_money):
                if s in self.trans_map:
                    final_money[i] = self.trans_map[s]
                elif s in self.special_word:
                    final_money[i] = self.special_word[s]

            # 轉成阿拉伯數字
            final_money = self.add_zero_for_missing_unit("".join(final_money))
            final_money = int(self.__convert_chinese_to_number("".join(final_money)))
            return final_money
        except Exception:
            print(f"Cannot Convert Case: {money}")
            return money


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    number_converter = NumberConverter()
    parser.add_argument("--money", type=str)
    args = parser.parse_args()

    print(number_converter.convert_to_number(args.money))
