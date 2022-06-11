import vk_api
from my_token import token
token = token                #Вставьте свой токен или токен страницы из которой вы производите анализ
session = vk_api.VkApi(token=token)
vk = session.get_api()

#ввод ссылки на аккаунт, вырезание из нее , короткого имени и нахождение по нему id
link=input()
link_s = link.split(sep = "/")
screen_name = link_s[3]
user_name = session.method("utils.resolveScreenName" , {"screen_name":screen_name})
user_id = user_name["object_id"]

# Вывод id и даты рождения , если она указана
user_tv = session.method("users.get" , {"user_ids":user_id , "name_case":"ins" , "fields":"bdate"})
print("id : " + str(user_tv[0]["id"]))
if "bdate" in user_tv[0]:
    print("Дата рождения :" + str(user_tv[0]["bdate"]))

# Функция для нахождения друзей из одного уника
def List_study_communications(user_id):
    user = session.method("users.get" , {"user_ids":user_id ,"fields":"education"}) 
    User_Univer = user[0]["university_name"]
    friends = session.method("friends.get" , {"user_id":user_id , "fields": "education"})
    print("Вместе с " + user_tv[0]["first_name"]+" в "+ User_Univer + " учатся:" )
    for friend in friends["items"]:
        f_Univer="не указан"
        user_f = session.method("users.get" , {"user_ids":friend["id"],"fields":"education"})
        if "university_name" in user_f[0]:
            f_Univer = user_f[0]["university_name"]
        if (User_Univer==f_Univer):
            print( user_f[0]["first_name"] +"  "+ user_f[0]["last_name"]) 


# Проверка на наличие информации о институте у пользователя
user_ed = session.method("users.get" , {"user_ids":user_id ,"fields":"education"})
if "university_name" in user_ed[0]:
    List_study_communications(user_id)
else:
        print("У объекта не указана информация о месте обучения:(")




# Функция для нахождения друзей в одном городе с пользвателем
def List_city(user_id):
    user = session.method("users.get" , {"user_ids":user_id ,"fields":"city"}) 
    User_City = user[0]["city"]
    friends = session.method("friends.get" , {"user_id":user_id , "fields": "city"})
    print("Вместе с " + user_tv[0]["first_name"]+" в городе \" "+ User_City["title"] + " \" живут:" )
    for friend in friends["items"]:
        f_city="не указан"
        user_f = session.method("users.get" , {"user_ids":friend["id"],"fields":"city"})
        if "city" in user_f[0]:
            f_city = user_f[0]["city"]
        if (User_City==f_city):
            print( user_f[0]["first_name"] +"  "+ user_f[0]["last_name"])  


# Проверка на наличие информации о городе у пользователя
user_city = session.method("users.get" , {"user_ids":user_id ,"fields":"city"})
if "city" in user_city[0]:
    print("город : " + str(user_city[0]["city"]["title"]))
    List_city(user_id)
else:
    print("У объекта не указана информация о городе:(")

