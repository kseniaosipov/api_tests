# Валидные данные для авторизации
valid_email = '123@gmail.com'
valid_password = '123'
# ------------------------------------------------------------------------------------------------

# Не валидные данные для авторизации
invalid_email = '123@gmail.ru'
invalid_password = '321'
invalid_auth_key = {
  "key": "ea738148a1f19838e1c3731380e733e877b0ae876"
}
rotten_auth_key = {
  "d50005452208f3dd9b7a23589d281be101e7fb75eebb1a0755b62c97"
}
# -----------------------------------------------------------------------------------------------


# Данные для добавления питомца
add_name = 'Шу'
add_age = '12'
add_animal_type = 'qwert'
add_pet_photo = 'images/fenek.jpeg'
# -----------------------------------------------------------------------------------------------

# Данные для обновления информации о питомце
update_name = 'Ко'
update_age = '5'
update_animal_type = 'asd'
update_pet_photo = 'images/ко.jpeg'
# ----------------------------------------------------------------------------------------------


def generate_string(num):
    return "x" * num


def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def english_chars():
    return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'







