user = {"is_admin" : bool(input("Является админом? (True/False)")),
        "is_active" : bool(input("Является активным пользователем? (True/False)")),
        "has_permission" : bool(input("Имеет разрешение? (True/False)")),
        "is_blocked" : bool(input("Заблокирован? (True/False)"))}
is_allowed = False

if not user["is_blocked"] and (user["is_admin"] or (user["is_active"] and user["has_permission"])):
    is_allowed = True
