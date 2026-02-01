import pandas as pd
from pathlib import Path

print("hello")

# プロジェクトのルートパス
BASE_DIR = Path(__file__).resolve().parent.parent

# inputフォルダのパス
INPUT_DIR = BASE_DIR / "sample" / "input"

# inputフォルダ内のExcelファイル一覧を取得
excel_files = INPUT_DIR.glob("*.xlsx")

print(list(excel_files))

for file_path in excel_files:
    print(f"読み込み中: {file_path.name}")

    df = pd.read_excel(file_path)

    print(df.head())
    print("-" * 30)
