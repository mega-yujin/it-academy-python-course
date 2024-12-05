user = {
    'is_admin' : int(input('Является админом? (1/0)')),
    'is_active' : int(input('Является активным пользователем? (1/0)')),
    'has_permissio' : int(input('Имеет разрешение? (1/0)')),
    'is_blocked' : int(input('Заблокирован? (1/0)'))
}
is_allowed = False

if not user['is_blocked'] and (user['is_admin'] or (user['is_active'] and user['has_permission'])):
    is_allowed = True
