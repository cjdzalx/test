# -*- coding: utf-8 -*-

# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色的外星人
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    print(alien_number)
for alien in aliens:
    print(alien)
