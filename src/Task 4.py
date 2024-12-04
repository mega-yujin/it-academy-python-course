is_admin: bool = True
is_active: bool = True
is_blocked: bool = True
has_permission: bool = False
has_access: bool

if is_blocked:
    has_access = False
elif is_admin:
    has_access = True
elif is_active and has_permission:
    has_access = True

if has_access:
    print ("доступ разрешён")
else:
    print ("доступ отклонён")