import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VKTools
from tokens import acces_token, comunity_token


class BotInterface():
    def __init__(self, acces_token, comunity_token):
        self.bot = vk_api.VkApi(token=comunity_token)
        self.api = VkTools(acces_token)
        self.params = None

    def message_send(self, user_id, message, attachment=None):
        self.bot.method('messages.send',
                        {'user_id': user_id,
                         'random_id': get_random_id(),
                         'attachment': attachment,
                         })

    def handler(self):
        longpull = VkLongPoll(self.bot)

        for event in longpull.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                message = event.text.lower()

                if message == 'привет':
                    self.params = self.api.get_profile_info(event.user_id)
                    self.message_send(event.user_id, f'привет {self.params["name"]}')
                    date_of_birth = event.text.lower()
                    if params['bdate'] == None:
                        self.message_send(event.user_id, f'Введите дату рождения в формате: 00.00.0000')
                        params['bdate'] = date_of_birth
                    your_gender = event.text.lower()
                    if params['sex'] == None:
                        self.message_send(event.user_id, f'Введите свой пол в формате: 1 или 2')
                        params['sex'] = your_gender
                    city_of_residence = event.text.lower()
                    if params['city'] == None:
                        self.message_send(event.user_id, f'Введите город проживания')
                        params['city'] = city_of_residence
                    return params

                elif message == 'поиск':
                    self.message_send(event.user_id, f'Начинаем поиск')
                    found_questionnaries = questionnaries()
                    # проверка базы данных
                    saved_profiles = check_user()
                    while saved_profiles == True:
                        found_questionnaries

                    photos_user = self.api.get_photos(user['id'])

                    attachment = ''
                    for num, photo in enumerate(photos_user):
                        attachment += f'photo{photo["owner_id"]}_{photo["id"]}'
                        if num == 2:
                            break
                    self.message_send(event.user_id, f'Встречайте {user["name"]} ссылка: vk.com/{user["id"]}',
                                      attachment=attachment
                                      )
                    # запись в базу данных
                    add_user()
                elif message == 'пока':
                    self.message_send(event.user_id, 'всего доброго')
                else:
                    self.message_send(event.user_id, 'неизвестная команда')

