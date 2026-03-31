from libs import module, auth
from utils import chart, csv_json
from db import stocks
from datetime import datetime
                

def main():
    day = "2024/01/01"

    while True:
        print("1. 증권 조회")
        print("2. 계좌 확인하기")
        print("3. 시뮬레이션 종료하기")
        select = module.input_int(1, 3, "선택: ", "잘못된 입력입니다. 다시 입력해주세요.")

        if select == 1:
            name = input("증권 이름을 입력하세요: ")
            stock_data = stocks.find_one({"name": name})
            if not stock_data:
                print("해당 증권을 찾을 수 없습니다.")
                module.enter()
                continue

            else:
                print(f"{name} 증권을 찾았습니다.")

                # 1. 사용자 입력을 받고 datetime 객체로 변환
                try:
                    start_date_str = input("확인 하고 싶은 시작 날짜를 입력하세요 (YYYY/MM/DD): ")
                    end_date_str = input("확인 하고 싶은 종료 날짜를 입력하세요 (YYYY/MM/DD): ")

                    # 문자열을 datetime 객체로 변환
                    start_date = datetime.strptime(start_date_str, "%Y/%m/%d")
                    end_date = datetime.strptime(end_date_str, "%Y/%m/%d")

                except ValueError:
                    print("날짜 형식이 올바르지 않습니다. YYYY/MM/DD 형식으로 입력해주세요.")
                    module.enter()
                    continue

                # 2. 날짜 논리 체크 (객체끼리 직접 비교 가능)
                if start_date > end_date:
                    print("시작 날짜는 종료 날짜보다 이전이어야 합니다.")
                    module.enter()
                    continue

                # 3. 데이터 범위 체크 
                # stock_data["data"]의 첫 번째와 마지막 날짜를 가져와 범위 확인
                # (데이터가 날짜순으로 정렬되어 있다고 가정할 때)
                first_data_date = stock_data["data"][-1]["date"] # 보통 과거 데이터가 뒤에 있음
                last_data_date = stock_data["data"][0]["date"]  # 최근 데이터가 앞에 있음

                if start_date < first_data_date or end_date > last_data_date:
                    print(f"날짜 범위가 증권 데이터 범위를 벗어났습니다.")
                    print(f"가능한 범위: {first_data_date.strftime('%Y/%m/%d')} ~ {last_data_date.strftime('%Y/%m/%d')}")
                    module.enter()
                    continue

                # 4. 차트 출력 실행
                print(f"{name} 증권의 {start_date_str}부터 {end_date_str}까지의 차트를 표시합니다.")
                print("차트가 생성 되면 웹사이트로 이동 됩니다.")
                module.enter()
                print("차트 생성 중...")

                # chart.plot_stock 함수 내부에서도 datetime 객체로 필터링하도록 설계되어 있어야 합니다.
                chart.plot_stock(stock_data["data"], start_date, end_date)

                module.enter()

        elif select == 2:
            pass
        elif select == 3:
            module.shut_down()

main()