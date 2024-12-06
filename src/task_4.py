is_admin = True
is_active = True
has_permission = True
is_blocked = True
is_allowed = True if is_admin and is_active and has_permission and not is_blocked else False
print(is_allowed)
