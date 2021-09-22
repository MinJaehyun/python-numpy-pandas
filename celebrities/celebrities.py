import pandas as pd

two_dimentional_list = [
    ["Taylor Swift", "December 13, 1989", "Singer-songwriter"],
    ["Aaron Sorkin", "June 9, 1961", "Screenwriter"],
    ["Harry Potter","July 31, 1980","Wizard"],
    ["Ji-Sung Park", "February 25, 1981", "Footballer"],
]

df = pd.DataFrame(two_dimentional_list, columns=["name", "birthday", "occupation"])

# 정답 출력
df


# 순서. 1. pd 를 가져온다 2. list 지정한다. 3. pd.DataFrame 에 list 를 가져온다
# 이차원 배열 만들고 가져오는 방법
