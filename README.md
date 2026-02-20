# 💬 로컬 AI 채팅 GUI 프로젝트

### 프로젝트 개요

이 프로젝트는 Python과 Tkinter를 이용한 로컬 AI 채팅 프로그램입니다.

- Ollama 또는 로컬 LLaMA 기반 모델 연동
- 사용자 메시지에 대한 AI 응답 표시
- AI 감정을 판단하고 아스키 표정으로 시각화
- 대화 기록 JSON 파일에 저장
- 다크 테마 GUI와 유동적인 말풍선 레이아웃

## 🗂️ 프로젝트 구조

```
ai_playground.py
├─ ai
│  └─ chat.py
├─ config
│  └─ settings.py
├─ data
│  └─ chat_memory.json
├─ gui
│  ├─ widgets.py
│  └─ window.py
└─ main.py

```

## ⚙️ 설치 및 실행

1. 가상환경 생성

```
python -m venv venv
```

2. 가상환경 활성화

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

3. 필요 패키지 설치

```
pip install ollama
```

Tkinter는 Python 표준 라이브러리이므로 별도 설치 불필요

4. 실행

```
python main.py
```

## 🖥️ 기능

1. 대화 입력

- 하단 Entry에 메시지 입력 후 Enter 또는 전송 버튼 클릭
- AI 응답이 채팅 말풍선으로 표시됨

2. AI 감정 표시

- AI가 메시지를 분석해 감정 판단
- 감정에 맞는 아스키 표정 표시
- 감정 종류: 기쁨, 슬픔, 분노, 놀람, 혐오, 공포, 무관심, 기대

3. 대화 기록

- 모든 대화는 data/chat_memory.json에 저장
- 프로그램 재실행 시 이전 대화 불러오기 가능

4. 다크 테마 GUI

- 채팅 말풍선, 배경, 글자색 모두 다크 테마 적용
- 창 크기 변경 시 말풍선 wrap 자동 조정

5. AI 응답 로딩 표시

- AI가 답변 중일 때 “AI가 답장 중…” 표시
- 답변 완료 시 아스키 감정과 함께 업데이트

## 📝 참고

- Python 3.10 이상 권장
- Windows, macOS, Linux 모두 실행 가능
- Ollama API 키 필요 (또는 로컬 LLaMA 모델)
