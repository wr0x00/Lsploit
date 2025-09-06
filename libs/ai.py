'''
 *@author: wr
 *@GitHub:https://github.com/wr0x00/Lsploit
 *@date: 2025.9.5
 *@description: ai对话功能
'''

if  not __name__ == '__main__':
	try:
		import json
		# 读入示例json数据
		j=open("libs/configs.json",encoding='utf-8')
		demo_json = json.loads(j.read())

		if demo_json["language"]=='cn'or demo_json["language"]=='CN': #中文
			from libs.strings import String_CN as Str
		
		if demo_json["language"]=='en'or demo_json["language"]=='EN': #英文
			from libs.strings import String_EN as Str

	except Exception as e:
		from libs.strings import String_EN as Str
		print("langrage_ERROR:"+format(e))
            
import os



from cozepy import COZE_CN_BASE_URL
from cozepy import Coze, TokenAuth, Message, ChatStatus, MessageContentType, ChatEventType  # noqa


user_id = '111'

def coze_chat_stream_API(coze,conversation,bot_id,text_input:str)->str:
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
            #    print("\033[1;30m"+event.message.content+"\033[0m", end="", flush=True)
            #if bot_id == bot_id_M:
            #    print("\033[1;36m"+event.message.content+"\033[0m", end="", flush=True)
            ends=ends + event.message.content

        if event.event == ChatEventType.CONVERSATION_CHAT_COMPLETED:
            #print("\nchat.id:",event.chat.id)
            #print("conversation.id:",conversation.id)
            #print("token usage:", event.chat.usage.token_count)
            break
    return ends,event.chat.id #str,返回chat_id以便对话记录
def coze_ai_cli():

    import json
    j= open('libs/configs.json', encoding='utf-8')
    dem_json = json.loads(j.read())

    bot_id=dem_json["bot_id"]
    coze_api_token=dem_json["coze_taken"]

    if bot_id==None:               print(Str.ERROR_AI_BOTID)
    if coze_api_token == None:     print(Str.ERROR_AI_USERAPI)

    coze_api_base = COZE_CN_BASE_URL
    try:
        coze = Coze(auth=TokenAuth(token=coze_api_token), base_url=coze_api_base)
        conversation = coze.conversations.create()

        while True:
            t=input("->")
            t,chat_id=coze_chat_stream_API(coze,conversation,bot_id,t)
            #t=s[1]'''
            print(f'{t}')
    except AssertionError:pass
