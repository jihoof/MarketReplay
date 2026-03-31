import random
import os
import time
import sys
from typing import Any, Iterable, Mapping, Sequence, Optional, Union
import random
import os
import time
import sys

from typing import Any, Iterable, Mapping, Sequence, Optional, Union
from rich.console import Console
from rich.table import Table
from rich import box

def enter(): #엔터키 입력받았을 때 clear
    while True:
        print("\n계속하려면 엔터를 눌러주세요...")
        enter = input("")
        if enter == "":
            os.system('cls' if os.name == 'nt' else 'clear')
            break

def input_int(minn, maxx, custom_input, custom_error):
    while True:
        try:
            select = int(input(custom_input))
            if minn <= select <= maxx:
                break
            else:
                print(custom_error)
        except:
            print(custom_error)
    return select

def input_str(custom_input, custom_error, input_list):
    while True:
        try:
            select = input(custom_input)
            if select in input_list:
                break
            else:
                print(custom_error)
        except:
            print(custom_error)
    return select

def input_all(minn, maxx, custom_input, custom_error, input_list):
    input_list = list(input_list)
    while True:
        try:
            select = input(custom_input)
            if select in input_list:
                break
            try:
                select = int(select)
            except:
                select = float(select)
            if minn <= select <= maxx:
                break
            else:
                print(custom_error)
        except:
            print(custom_error)
    return select

def chance(percent: float) -> bool:
    """percent 확률(%)로 True를 반환하는 함수"""
    return random.random() < (percent / 100)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_scissors():
    print("┌────────────────────┐")
    print("│               ▩▩   │")
    print("│       ▩▩    ▩▩▩▩▩  │")
    print("│     ▩▩▩▩▩  ▩▩▩▩▩▩▩ │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩         │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩       │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│   ▩▩▩▩▩▩▩ ▩▩▩▩▩▩▩  │")
    print("│    ▩▩▩▩▩▩   ▩▩▩▩▩  │")
    print("│      ▩▩▩      ▩▩   │")
    print("└────────────────────┘")

def print_rock():
    print("┌────────────────────┐")
    print("│                    │")
    print("│     ▩▩▩▩▩          │")
    print("│    ▩▩▩▩▩▩▩▩▩       │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩      │")
    print("│   ▩▩▩▩▩▩▩▩▩▩       │")
    print("│    ▩▩▩▩▩▩▩         │")
    print("│                    │")
    print("└────────────────────┘")
    
def print_paper():
    print("┌───────────────────┐")
    print("│                   │")
    print("│     ▩▩▩▩▩         │")
    print("│    ▩▩▩            │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩▩  │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│  ▩▩▩▩▩▩▩▩▩▩▩▩▩▩   │")
    print("│  ▩▩▩▩▩▩▩▩▩        │")
    print("│   ▩▩▩▩▩▩▩▩▩▩▩     │")
    print("│    ▩▩▩▩▩          │")
    print("│                   │")
    print("└───────────────────┘")

def shut_down():
    time.sleep(1)
    clear()
    print('게임을 종료합니다.')
    time.sleep(0.5)
    print()
    print()
    time.sleep(0.5)
    print("게임을 종료 중...", end='', flush=True)  # flush 추가
    for _ in range(random.randint(5, 10)):
        print(".", end='', flush=True)
        time.sleep(1)
    print()
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit()

def beautiful_table(
    data: Sequence[Any],
    *,
    title: str | None = None,
    caption: str | None = None,
    headers: Sequence[str] | None = None,
    use_first_row_as_header: bool = True,
    show_index: bool = False,
    index_name: str = "#",
    console: Console | None = None,
    box_style=box.ROUNDED,
) -> None:
    """
    다양한 리스트 형태를 Rich Table로 예쁘게 출력.

    지원 입력:
    1) list[dict]         -> dict keys = columns, each dict = row
    2) list[list/tuple]   -> 2D rows, first row header(기본) 또는 headers로 지정
    3) list[scalar]       -> 1D values, single column

    Args:
        data: 출력할 데이터(리스트).
        title/caption: 테이블 제목/캡션.
        headers: 강제 헤더 지정.
        use_first_row_as_header: 2D일 때 첫 행을 헤더로 사용할지.
        show_index: 좌측 인덱스 컬럼 추가 여부.
        index_name: 인덱스 컬럼명.
        console: 출력할 Console(없으면 기본 Console()).
        box_style: 테이블 테두리 스타일.
    """
    console = console or Console()
    table = Table(title=title, caption=caption, box=box_style, show_lines=False)

    if not data:
        # 빈 데이터 처리
        table.add_column("Empty")
        table.add_row("(no rows)")
        console.print(table)
        return

    first = data[0]

    def add_index_column_if_needed():
        if show_index:
            table.add_column(index_name, justify="right", style="dim", no_wrap=True)

    # 1) list[dict]
    if isinstance(first, Mapping):
        # 컬럼 순서: headers 지정 > 첫 dict의 키 순서
        cols = list(headers) if headers else list(first.keys())

        add_index_column_if_needed()
        for c in cols:
            table.add_column(str(c))

        for i, row in enumerate(data):
            if not isinstance(row, Mapping):
                raise TypeError("list[dict] 형태로 보이지만, 중간에 dict가 아닌 원소가 있습니다.")
            values = [row.get(c, "") for c in cols]
            values = ["" if v is None else str(v) for v in values]
            if show_index:
                table.add_row(str(i), *values)
            else:
                table.add_row(*values)

        console.print(table)
        return

    # 2) list[list/tuple] (2D)
    if isinstance(first, (list, tuple)):
        rows = [list(r) if isinstance(r, (list, tuple)) else [r] for r in data]

        # 헤더 결정
        if headers is not None:
            cols = [str(h) for h in headers]
            body_rows = rows
        else:
            if use_first_row_as_header:
                cols = [str(x) for x in rows[0]]
                body_rows = rows[1:]
            else:
                # 컬럼 수 기준으로 기본 헤더 생성
                max_len = max((len(r) for r in rows), default=0)
                cols = [f"col_{i}" for i in range(max_len)]
                body_rows = rows

        add_index_column_if_needed()
        for c in cols:
            table.add_column(str(c))

        for i, r in enumerate(body_rows):
            # 열 개수 맞추기(부족하면 빈칸 채우고, 많으면 잘라냄)
            r = list(r)
            if len(r) < len(cols):
                r += [""] * (len(cols) - len(r))
            else:
                r = r[: len(cols)]
            r = ["" if v is None else str(v) for v in r]

            if show_index:
                table.add_row(str(i), *r)
            else:
                table.add_row(*r)

        console.print(table)
        return

    # 3) 1D 리스트(스칼라)
    col_name = headers[0] if headers else "value"
    add_index_column_if_needed()
    table.add_column(str(col_name))

    for i, v in enumerate(data):
        s = "" if v is None else str(v)
        if show_index:
            table.add_row(str(i), s)
        else:
            table.add_row(s)

    console.print(table)

def force_quit():
    print('Unexpected fatal error occured. error code: -1')
    time.sleep(2)
    print('Rebooting faliure')
    time.sleep(0.5)
    print('System forced shutdown')
    time.sleep(2)
    shut_down()