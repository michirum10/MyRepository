# =============
# エクセル操作
# =============

# ctrl+.でクイックフィックス
# ctrl+スペースで候補を表示

# https://pypi.org/
# で調べてインストールできる(偽物に注意)
# pip install openpyxl
# コンソールに貼り付けしてインストール

import openpyxl

# InputOutputフォルダを作る
# その中にExcelFile.xlsxができる
# ExcelFile.xlsxをエクスプローラーで開いて確認

# Excelのワークブックを作成
wb = openpyxl.Workbook()
# アクティブシートを取得
ws = wb.active
# A1セルに書き込み
ws["A1"] = "Excelこんにちは"
# ブックの保存
wb.save("InputOutput/ExcelFile.xlsx")

