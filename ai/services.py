import openai
from events.models import Registration , Events
from decouple import config

client = openai.OpenAI(api_key=config("OPENAI_API_KEY"))

def get_user_event_history(user):
    registrations = Registration.objects.filter(user=user).select_related('event')
    return [(r.event.title, r.event.content) for r in registrations]

def build_prompt(event_history):
    all_events = Events.objects.all() 
    prompt = "給你參考我目前資料庫中所有的活動及標題\n"
    for idx, event in enumerate(all_events, 1):
        prompt += f"{idx}. 標題：{event.title}\n內容：{event.content}\n"

    prompt += "接下來我會給你這個使用者參加過的所有活動，請你根據使用者參加過的活動標題、活動內容，來判斷我資料庫中有哪些活動適合這個使用者，並推薦三個活動給他\n"
    for idx, (title, content) in enumerate(event_history, 1):
        prompt += f"{idx}. 標題：{title}\n內容：{content}\n"

    prompt += "\n請直接列出推薦活動標題與簡要說明。"
    return prompt

def get_llm_recommendations(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",  # 或 "gpt-4o"
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300,
        temperature=0.7,
    )
    return response.choices[0].message.content

def recommend_events_for_user(user):
    history = get_user_event_history(user)
    if not history:
        return "尚無參加紀錄，請先參加活動！"
    prompt = build_prompt(history)
    recommendations = get_llm_recommendations(prompt)
    return recommendations