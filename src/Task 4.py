is_admin: bool = True
is_active: bool = True
is_blocked: bool = True
has_permission: bool = False
has_access: bool = (not is_blocked) and (is_admin or (is_active and has_permission))

message = "доступ разрешён" if has_access else "доступ отклонён"
print(message)
