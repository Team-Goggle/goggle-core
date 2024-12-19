# goggle-core

- **24-2 캡스톤디자인과창업프로젝트A**
- Team 6 Goggle: 한사랑, 김희서, 임가현
- LangChain 기반 AI 바둑 복기(復棋) 서비스의 핵심 기술 저장소

### 주요 기능
- SGF 바둑 기보 파일 분석
- 수순별 승률 변화 추적
- AI 기반 대국 해설 생성

### 프로젝트 구조
```
📁 my-sgf/              # SGF, analyzed-SGF 파일 저장을 위한 디렉토리
📁 sgf-winrates/        # 분석된 SGF에서 win rates를 추출하기 위한 디렉토리
📁 analysis-results/    # 해설 생성 결과와 json 객체 저장을 위한 디렉토리
🐍 Analyze-sgf.ipynb    # 전체 작업 실행을 위한 파이썬 스크립트
```

### 설치 방법
1. 저장소 복제
```bash
git clone https://github.com/[username]/goggle-core.git
cd goggle-core
```
2. 가상환경 설정
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 사용 방법
0. Analyze-sgf 설치 및 KataGo 연동
1. my-sgf 디렉토리에 분석할 SGF 파일 업로드
2. OpenAI API 키 설정
3. Analyze-sgf.ipynb 노트북 실행
