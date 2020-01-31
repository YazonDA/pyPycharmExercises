import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

# 'yazonda.29@gmail.com'
# '71gPSdwv8V'
# '8ba73ff82d629d2d9aa50122dc2f39f419845f74184362ca7fd2d805b9942b6fa01545d78b50bf7ddda33'

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# API-ключ созданный ранее
token = "8ba73ff82d629d2d9aa50122dc2f39f419845f74184362ca7fd2d805b9942b6fa01545d78b50bf7ddda33"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            
            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")