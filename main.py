from libs import module, auth
from utils import chart, csv_json
from db import stocks
from datetime import datetime
import tkinter as tk
from tkinter import filedialog

def main():
    while True:
        print("\n=== 증권 시뮬레이터 ===")
        print("0. 로그인/회원가입")
        print("1. 증권 관리")
        print("2. 시뮬레이션 시작하기")
        print("3. 종료하기")
        select = module.input_int(0, 3, "선택: ", "잘못된 입력입니다. 다시 입력해주세요.")

        if select == 0:
            print("\n[ 인증 센터 ]")
            print("0. 회원 가입")
            print("1. 로그인")
            print("2. 회원 탈퇴")

            select3 = module.input_int(0, 2, "선택: ", "잘못된 입력입니다. 다시 입력해주세요.")
            if select3 == 0:
                #TODO
                pass
            elif select3 == 1:
                #TODO
                pass
            elif select3 == 2:
                #TODO
                pass    
            
        if select == 1:
            while True: 
                print("\n[ 증권 관리 ]")
                print("0. 증권 조회")
                print("1. 증권 추가")
                print("2. 증권 삭제")

                select2 = module.input_int(0, 2, "선택: ", "잘못된 입력입니다. 다시 입력해주세요.")
                
                if select2 == 0:
                    stock_list = [stock["name"] for stock in stocks.find({}, {"name": 1, "_id": 0})]
                    view_list = [(idx, name) for idx, name in enumerate(stock_list)]
                    print()
                    module.beautiful_table(data = view_list, title = "증권 목록")
                    
                    name_idx = int(input("증권 번호를 입력하세요: "))
                    stock_data = stocks.find_one({"name": stock_list[name_idx - 1]})
                    if not stock_data:
                        print("해당 증권을 찾을 수 없습니다.")
                        module.enter()
                        continue
                    else:
                        print(f"{stock_list[name_idx - 1]} 증권을 찾았습니다.")
                        try:
                            start_date_str = input("확인 하고 싶은 시작 날짜를 입력하세요 (YYYY/MM/DD): ")
                            end_date_str = input("확인 하고 싶은 종료 날짜를 입력하세요 (YYYY/MM/DD): ")

                            start_date = datetime.strptime(start_date_str, "%Y/%m/%d")
                            end_date = datetime.strptime(end_date_str, "%Y/%m/%d")

                        except ValueError:
                            print("날짜 형식이 올바르지 않습니다. YYYY/MM/DD 형식으로 입력해주세요.")
                            module.enter()
                            continue
                        
                        if start_date > end_date:
                            print("시작 날짜는 종료 날짜보다 이전이어야 합니다.")
                            module.enter()
                            continue

                        first_data_date = stock_data["data"][-1]["date"] # 보통 과거 데이터가 뒤에 있음
                        last_data_date = stock_data["data"][0]["date"]  # 최근 데이터가 앞에 있음

                        if start_date < first_data_date or end_date > last_data_date:
                            print(f"날짜 범위가 증권 데이터 범위를 벗어났습니다.")
                            print(f"가능한 범위: {first_data_date.strftime('%Y/%m/%d')} ~ {last_data_date.strftime('%Y/%m/%d')}")
                            module.enter()
                            continue
                        
                        print(f"{stock_list[name_idx - 1]} 증권의 {start_date_str}부터 {end_date_str}까지의 차트를 표시합니다.")
                        module.enter()
                        chart.plot_stock(stock_data["data"], start_date, end_date)

                        module.enter()
                
                elif select2 == 1:
                    
                    root = tk.Tk()
                    root.withdraw()

                    csv_file_path = filedialog.askopenfilename(
                        title="CSV 파일 선택",
                        filetypes=[("CSV 파일", "*.csv")]
                    )

                    if csv_file_path:
                        print(csv_file_path)
                    pass
                
                    # TODO
                
                elif select2 == 2:
                    # TODO
                    pass

        elif select == 2:
            # TODO
            # 여기는 따로 시뮬레이션 함수 제작해서 호출
            pass

        elif select == 3:
            module.shut_down()

main()