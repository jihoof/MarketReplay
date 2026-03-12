import csv
import json
import os

def csv_to_json(csv_file_path, json_file_path=None):
    """
    CSV 파일을 읽어서 각 행을 딕셔너리로 변환 후 JSON 리스트로 반환.
    옵션으로 JSON 파일로 저장 가능.

    CSV 예시 행:
    "10/15/2024","131.60","137.87","138.57","128.74","377.83M","-4.69%"
    컬럼: date, open, high, low, close, volume, change
    """
    data = []

    # CSV 읽기
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for i, row in enumerate(reader):
            # 행이 비어있으면 무시
            if not row or i == 0:
                continue

            # 딕셔너리 변환
            record = {
                "date": row[0],
                "price": float(row[1]),
                "open": float(row[2]),
                "hight": float(row[3]),
                "low": float(row[4]),
                "vol.": row[5],
                "change": row[6]
            }
            data.append(record)

    # JSON 파일 저장 옵션
    if json_file_path:
        with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4, ensure_ascii=False)

    return data


if __name__ == '__main__':
    csv_data = csv_to_json("C:/Users/jihoo/Documents/Github/MarketReplay/data/NVDA_20240101-20251231.csv")
    print(json.dumps(csv_data, indent=4, ensure_ascii=False))
    