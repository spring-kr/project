# 친근한 AI 챗봇 프로젝트 🤖

이 프로젝트는 LangChain과 OpenAI를 활용하여 만든 따뜻하고 친근한 대화형 AI 챗봇입니다.

## 주요 기능

- 친근하고 자연스러운 대화 스타일
- 사용자의 감정에 공감하는 응답
- 대화 기록 유지
- 이모티콘을 활용한 친근한 커뮤니케이션

## 설치 방법

1. 프로젝트 클론 또는 다운로드

2. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

3. 환경 변수 설정
- `.env` 파일에서 `your_api_key_here`를 실제 OpenAI API 키로 변경
- 필요한 경우 다른 환경 변수도 조정 가능

## 실행 방법

```bash
streamlit run app.py
```

## 환경 변수 설정

`.env` 파일에서 다음 설정을 조정할 수 있습니다:

- `OPENAI_API_KEY`: OpenAI API 키
- `MODEL_NAME`: 사용할 모델 (기본값: gpt-3.5-turbo)
- `TEMPERATURE`: 응답의 창의성 정도 (0.0 ~ 1.0)
- `MAX_TOKENS`: 응답의 최대 길이

## 주의사항

- OpenAI API 키는 절대로 공개되지 않도록 주의해주세요.
- `.env` 파일은 버전 관리 시스템에 포함되지 않도록 주의해주세요.