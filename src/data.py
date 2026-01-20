from pathlib import Path
import pandas as pd

def load_xlsx(xlsx_path: Path) -> dict[str, pd.DataFrame]:
    file = pd.ExcelFile(xlsx_path)

    data = {}
    for sheet in file.sheet_names:
        df = pd.read_excel(file, sheet_name=sheet)

        data[sheet] = df
    
    return data