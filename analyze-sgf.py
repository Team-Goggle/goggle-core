import os
import subprocess

def process_sgf_files():
    # 나의 sgf 파일 디렉토리 경로 설정
    input_dir = 'my-sgf/'
    
    # analyze-sgf에 전달할 공통 옵션
    common_args = [
        'analyze-sgf', 
        '-a', 'maxVisits:50',  # 첫 번째 분석의 최대 방문 횟수
        '-g', 'minWinrateDropForVariations:8',  # 변형 분석을 위한 승률 드롭 임계값
        '-r', '200'  # 재분석 시 최대 방문 횟수
    ]
    
    # input 디렉토리의 모든 .sgf 파일 순회
    for filename in os.listdir(input_dir):
        if filename.endswith('.sgf'):
            # 입력 파일의 전체 경로
            input_path = os.path.join(input_dir, filename)
            
            # 최종 명령어 구성 (common_args + 입력 파일 경로)
            full_command = common_args + [input_path]
            
            try:
                # subprocess를 사용해 analyze-sgf 실행
                result = subprocess.run(
                    full_command, 
                    capture_output=True, 
                    text=True
                )
                
                # 모듈의 stdout/stderr 출력
                if result.stdout:
                    print("Module stdout:", result.stdout)
                if result.stderr:
                    print("Module stderr:", result.stderr)
                
            except subprocess.CalledProcessError as e:
                # 모듈 실행 중 오류 발생 시
                print(f"Error processing {filename}: {e}")
            except Exception as e:
                # 기타 예외 처리
                print(f"Unexpected error with {filename}: {e}")

# 스크립트 실행
if __name__ == '__main__':
    process_sgf_files()