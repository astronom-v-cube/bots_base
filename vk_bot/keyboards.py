from vk_api.keyboard import VkKeyboard, VkKeyboardColor

keyboard = VkKeyboard(one_time = True)
keyboard.add_button('Кнопка', color=VkKeyboardColor.SECONDARY)
keyboard.add_button('Кнопка', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()  # Переход на вторую строку
keyboard.add_button('Кнопка', color=VkKeyboardColor.PRIMARY)

keyboard_two = VkKeyboard()
keyboard_two.add_button('Подписаться', color=VkKeyboardColor.POSITIVE)
keyboard_two.add_button('Отписаться', color=VkKeyboardColor.SECONDARY)
keyboard_two.add_button('Стоп', color=VkKeyboardColor.NEGATIVE)
keyboard_two.add_line()  # Переход на вторую строку
keyboard_two.add_button('Баг-репорт', color=VkKeyboardColor.NEGATIVE)
keyboard_two.add_button('В начало', color=VkKeyboardColor.NEGATIVE)
