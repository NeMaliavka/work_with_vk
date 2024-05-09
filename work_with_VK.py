import requests
class VK:
    def __init__(self, access_token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def users_info(self):
        url = 'https://api.vk.com/method/users.get'
        params = {'user_ids': self.id}
        response = requests.get(url, params={**self.params, **params})
        return response.json()


access_token = 'vk1.a.tsSNGJXMTwjuWeeIaMr7mhnd3EQ4anAbHTFm25Qr7uxZNV4ebERJN4-LHTde-pGJ0_BRtbXSx_q_sU-sa8M5okjkePO2ZxcmCkEX4V8yMqGTiGmPOB4i7rKBXJqnsd6j3MCY_QGQHp4x6tAwUup5SWo8DQpkYwOUG7txYArK55YLbwo1iqIXcHKaUO-LaNIx'
user_id = '672707836'
vk = VK(access_token, user_id)

print(vk.users_info())
# токен полученный из инструкции
