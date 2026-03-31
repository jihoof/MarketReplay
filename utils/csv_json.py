import csv
from datetime import datetime
from db import stocks  # 설정하신 db 모듈의 stocks 컬렉션

def load_csv_to_mongodb(csv_file_path, stock_name):
    """
    CSV 데이터를 읽어 MongoDB에 datetime 형식으로 저장합니다.
    """
    data_list = []

    try:
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            # 첫 줄(헤더)을 건너뛰기 위해 DictReader 대신 일반 reader 사용
            reader = csv.reader(csvfile)
            header = next(reader) # 헤더 스킵

            for row in reader:
                if not row: continue

                # 날짜 처리: "MM/DD/YYYY" -> datetime 객체
                # 만약 CSV 날짜 형식이 "YYYY-MM-DD"라면 "%Y-%m-%d"로 수정하세요.
                try:
                    parsed_date = datetime.strptime(row[0], "%m/%d/%Y")
                except ValueError:
                    # 다른 흔한 형식인 YYYY-MM-DD 시도
                    parsed_date = datetime.strptime(row[0], "%Y-%m-%d")

                record = {
                    "date": parsed_date,        # MongoDB Date 객체로 저장
                    "close": float(row[1].replace(',', '')), # 천단위 콤마 제거 후 float
                    "open": float(row[2].replace(',', '')),
                    "high": float(row[3].replace(',', '')),
                    "low": float(row[4].replace(',', '')),
                    "volume": row[5],
                    "change": row[6]
                }
                data_list.append(record)

        # 1. 기존에 같은 이름(예: NVDA)의 데이터가 있다면 삭제 (중복 방지)
        stocks.delete_one({"name": stock_name})

        # 2. 새로운 데이터 삽입
        final_document = {
            "name": stock_name,
            "data": data_list,
            "last_updated": datetime.now()
        }
        
        result = stocks.insert_one(final_document)
        
        print(f"✅ {stock_name} 데이터 적재 완료!")
        print(f"   - 총 데이터 개수: {len(data_list)}개")
        print(f"   - MongoDB ID: {result.inserted_id}")

    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {csv_file_path}")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")

# --- 실행부 ---
if __name__ == "__main__":
    # 경로를 본인의 환경에 맞게 수정하세요.
    target_csv = "C:/Users/jihoo/Documents/Github/MarketReplay/data/NVDA_20240101-20251231.csv"
    load_csv_to_mongodb(target_csv, "NVDA")