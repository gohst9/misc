import pyperclip


copy_text = pyperclip.paste()#クリップボードから文字列を取得
center = len(copy_text) // 2#文字列の中央の位置を求める（適当）
output_text_lst = [] #後でjoinして出力するための文字列リスト

for i,c in enumerate(copy_text):
    if i != center:
        output_text_lst.append(("　" * center) + c)
    else:
        output_text_lst.append(copy_text)

output_text = "\n".join(output_text_lst)
print(output_text)
pyperclip.copy(output_text) #クリップボードにグランドクロス文字列を張り付ける

