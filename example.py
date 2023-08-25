from number_converter import NumberConverter

number_converter = NumberConverter()

# Case 1, 純中文
origin_text = "五千"
expected_text = 5000
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 2, 純數字
origin_text = "628904"
expected_text = 628904
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 3, 純繁體中文數字
origin_text = "八百零五萬三十二"
expected_text = 8050032
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 4, 純簡體中文數字
origin_text = "六百七十三万五百零七"
expected_text = 6730507
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 5, 中文數字參雜
origin_text = "706億52萬03"
expected_text = 70600520003
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 6, 中文數字參雜，不完整敘述
origin_text = "52萬320"
expected_text = 520320
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 7, 不同繁體中文數字
origin_text = "壹億參仟肆佰伍拾貳萬玖仟捌佰柒拾陸元"
expected_text = 134529876
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 8, 中文數字全形半形繁體簡體
origin_text = "肆万８千5百零叁"
expected_text = 48503
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 9, 中文數字全形半形繁體簡體
origin_text = "八拾參亿伍佰33万４千兩百玖十捌"
expected_text = 8305334298
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")


# Case 10, 中文數字全形半形繁體簡體
origin_text = "壹千5百零６亿四千5百97萬兩佰三十"
expected_text = 150645970230
result = number_converter.convert_to_number(origin_text)
print(f"origin: {origin_text}, after: {result}. Does convert correct: {result==expected_text}")
