is_admin = False
is_active = True
has_permission = True
is_blocked = False
is_allowed = not is_blocked and (is_admin or (is_active and has_permission))
print(is_allowed)
