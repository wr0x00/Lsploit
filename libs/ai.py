import os

import json
j= open('libs/configs.json', encoding='utf-8')
demo_json = json.loads(j.read())


from cozepy import COZE_CN_BASE_URL
from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType, ChatEventType  # noqa

coze_api_token = ''
bot_id = ''

coze_api_base = COZE_CN_BASE_URL
coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)
conversation = coze.conversations.create()



user_id = '111'
def coze_chat_stream_API(bot_id,text_input:str)->str:
    ends=""
    for event in coze.chat.stream(
        bot_id=bot_id,
        user_id=user_id,
        conversation_id=conversation.id,
        auto_save_history=True,
        additional_messages=[
        Message.build_user_question_text(text_input),
        ],
    ):
        if event.event == ChatEventType.CONVERSATION_MESSAGE_DELTA:
            #if bot_id == bot_id_F:
            #    print("\033[1;30m"+event.message.content+"\033[0m", end="", flush=True
            #if bot_id == bot_id_M:
            #    print("\033[1;36m"+event.message.content+"\033[0m", end="", flush=True
            ends=ends + event.message.content

        if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
            #print("\nchat.id:",event.chat.id)
            #print("conversation.id:",conversation.id)
            #print("token usage:", event.chat.usage.token_count)
            break
    return ends,event.chat.id #str,返回chat_id以便对话记录


while True:
    t=input("->")
    t,chat_id=coze_chat_stream_API(bot_id,t)
    print(f'user:{t}')
