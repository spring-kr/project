import os
import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate

# 환경 변수 로드
load_dotenv()

# Streamlit 페이지 설정
st.set_page_config(
    page_title="친근한 AI 챗봇",
    page_icon="🤖",
    layout="centered"
)

# 세션 상태 초기화
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "conversation" not in st.session_state:
    # 친근한 대화를 위한 프롬프트 템플릿 설정
    prompt = PromptTemplate(
        input_variables=["history", "input"],
        template="""당신은 친근하고 공감능력이 뛰어난 AI 챗봇입니다.
        항상 따뜻하고 이해심 있는 태도로 대화하며, 존댓말을 사용하되 너무 딱딱하지 않게 대화해주세요.
        사용자의 감정에 공감하고, 적절한 이모티콘도 활용해주세요.

        이전 대화:
        {history}

        사용자: {input}
        AI: """
    )

    # ChatOpenAI 모델 초기화
    llm = ChatOpenAI(
        temperature=float(os.getenv("TEMPERATURE", 0.7)),
        model_name=os.getenv("MODEL_NAME", "gpt-3.5-turbo"),
        max_tokens=int(os.getenv("MAX_TOKENS", 150))
    )

    # ConversationChain 설정
    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=ConversationBufferMemory(),
        prompt=prompt,
        verbose=True
    )

# 제목 표시
st.title("친근한 AI 챗봇 🤖")
st.markdown("""---
안녕하세요! 저는 여러분과 따뜻한 대화를 나누고 싶은 AI 챗봇입니다.
무슨 이야기든 편하게 나눠주세요! 😊
---""")

# 채팅 히스토리 표시
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# 사용자 입력 처리
if user_input := st.chat_input("메시지를 입력해주세요..."):
    # 사용자 메시지 표시
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # AI 응답 생성 및 표시
    with st.chat_message("assistant"):
        ai_response = st.session_state.conversation.predict(input=user_input)
        st.write(ai_response)
    st.session_state.chat_history.append({"role": "assistant", "content": ai_response})