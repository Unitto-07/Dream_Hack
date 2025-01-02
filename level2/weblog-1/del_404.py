import csv

# CSV 파일에서 404 응답 코드가 있는 행을 제거하는 함수
def remove_404_from_csv(input_file, output_file):
    # CSV 파일 읽기
    with open(input_file, mode='r') as file:
        reader = csv.reader(file)
        header = next(reader)  # 헤더를 읽어놓고, 나중에 그대로 저장
        filtered_data = [header]  # 헤더는 유지

        # 각 행을 읽어 응답 코드가 404인 경우를 제외하고 필터링
        for row in reader:
            if row[5] != '404':  # 응답 코드(6번째 열)가 404가 아닌 경우
                filtered_data.append(row)

    # 필터링된 데이터를 새로운 CSV 파일로 저장
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(filtered_data)

    print(f"404 응답 코드를 제외한 CSV 파일이 저장되었습니다: {output_file}")

# CSV 파일 경로 설정
input_file = 'web_log.csv'  # 원본 CSV 파일 경로
output_file = 'filtered_web_log.csv'  # 404를 제외한 새로운 CSV 파일 경로

# 함수 실행
remove_404_from_csv(input_file, output_file)