is_admin = True
is_active = True
has_permission = True
is_blocked = True

is_allowed = not is_blocked and (is_admin or (is_active and has_permission))

print(is_allowed)
