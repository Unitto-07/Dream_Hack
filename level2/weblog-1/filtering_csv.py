#!/usr/bin/env python3

import pandas as pd
import re

# 특정 값이 존재하는 행 필터링(단일 값)
def remove_rows_with_value(df, column_name, value_to_remove):
    """
    df : 수정할 DataFrame
    column_name: 값을 검색할 열(단일)
    value_to_remove: 삭제할 기준 값(리스트)
    """
    try:
        # 열 이름 및 값 확인
        print('선택한 값')
        for value in value_to_remove:
            print(f"{column_name}: {value}")
            
        # 특정 값이 포함된 행 삭제
        df = df[~df[column_name].isin(value_to_remove)]  # isin()을 사용하여 한 번에 제거
        
        print('특정 값(value) 필터링 성공')
        return df
    
    # 에러 출력
    except KeyError:
        print(f"Error: 열 이름 '{column_name}'이 데이터프레임에 없습니다.")
        return df
    except Exception as e:
        print(f"Error: 알 수 없는 문제가 발생했습니다. {e}")
        return df

# 특정 열 제거 (리스트)
def remove_columns(df, del_column_name):
    '''
    df : 수정할 DataFrame
    column_name: 삭제할 열 이름(리스트)
    '''
    try:
        df = df.drop(columns=del_column_name, errors='ignore')  # errors='ignore'는 열이 없을 경우 에러를 무시

        print('특정 열(column) 필터링 성공')
        return df
    
    except Exception as e:
        print(f"Error: 알 수 없는 문제가 발생했습니다. {e}")
        return df

# 특정 값이 존재하는 행 필터링 (단일 값)
def filter_rows_with_value(df, column_name, value_to_include):
    """
    df : 수정할 DataFrame
    column_name: 값을 검색할 열(단일)
    value_to_include: 포함할 기준 값
    """
    try:
        # 해당 열에서 특정 값을 포함한 행만 선택
        filtered_df = df[df[column_name] == value_to_include]
        
        if filtered_df.empty:
            print(f"경고: '{value_to_include}' 값을 가진 행이 없습니다.")
        else:
            print(f"'{value_to_include}' 값을 가진 행이 {len(filtered_df)}개가 있습니다.")
        
        return filtered_df  # 필터링된 DataFrame 반환
    
    except KeyError:
        print(f"Error: 열 이름 '{column_name}'이 데이터프레임에 없습니다.")
        return df
    except Exception as e:
        print(f"Error: 알 수 없는 문제가 발생했습니다. {e}")
        return df

input_file = input('불러올 csv 파일의 경로 -> ')
output_file = input('저장할 csv 파일의 경로 -> ')

df = pd.read_csv(input_file)

while True:
    print('remove value: 1')
    print('remove column: 2')
    print('filtering value: 3')
    print('save csv: 4')
    print('exit: 5')
    work_num = int(input())

    if work_num == 1:
        column_name = input('삭제할 값이 있는 열 이름 -> ')
        value_to_remove_input = input('삭제할 기준이 될 값들(따옴표 ""로 구분) -> ').strip()

        value_to_remove = re.findall(r'"([^"]*)"', value_to_remove_input)

        df = remove_rows_with_value(df, column_name, value_to_remove)
    
    elif work_num == 2:
        del_column_name_input = input('삭제할 열 이름들(따옴표 ""로 구분)').strip()

        del_column_name = re.findall(r'"([^"]*)"', del_column_name_input)

        df = remove_columns(df, del_column_name)
    
    elif work_num == 3:
        column_name = input('필터링할 값이 있는 열 이름 -> ')
        value_to_include_input = input('필터링할 값 -> ').strip()

        # 숫자로 변환을 시도
        try:
            # 숫자로 변환 가능한 값은 int 또는 float로 처리
            if '.' in value_to_include_input:
                value_to_include = float(value_to_include_input)  # 실수 처리
            else:
                value_to_include = int(value_to_include_input)  # 정수 처리

        except ValueError:
            # 숫자가 아닌 경우는 그대로 문자열로 처리
            value_to_include = value_to_include_input

        df = filter_rows_with_value(df, column_name, value_to_include)

    elif work_num == 4:
        try:
            df.to_csv(output_file, index=False)
            print('저장 완료')
            break

        except Exception as e:
            print(f"Error: {e}")

    elif work_num == 5:
        break

    else:
        print('알맞은 값을 입력하세요')



