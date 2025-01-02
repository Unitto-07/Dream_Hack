import csv
import re

# 텍스트 파일을 읽고 로그를 CSV로 변환하는 함수
def convert_log_to_csv(input_file, output_file):
    # CSV 파일을 위한 헤더 정의
    headers = ['IP Address', 'Login Name', 'Authenticated User', 'Date and Time', 'Request', 'Response Code', 'Response Size', 'Referer', 'User-Agent']
    
    # 텍스트 파일 열기
    with open(input_file, 'r') as file:
        log_data = file.readlines()

    # CSV 파일 열기
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        # 로그 데이터 처리
        for line in log_data:
            # 정규식으로 로그에서 필요한 부분을 추출
            match = re.match(r'(\S+) (\S+) (\S+) \[([^\]]+)\] "(.*?)" (\d{3}) (\d+) "(.*?)" "(.*?)"', line)

            if match:
                ip, login_name, auth_user, date_time, request, status, size, referer, user_agent = match.groups()
                writer.writerow([ip, login_name, auth_user, date_time, request, status, size, referer, user_agent])

    print(f"CSV 파일로 저장되었습니다: {output_file}")

# 텍스트 파일과 출력 CSV 파일 경로 설정
input_file = 'access.log'  # 로그 텍스트 파일 경로
output_file = 'web_log.csv'  # 결과로 저장할 CSV 파일 경로

# 함수 실행
convert_log_to_csv(input_file, output_file)