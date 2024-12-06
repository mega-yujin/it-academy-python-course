is_admin = False
is_active = True
has_permission = False
is_blocked = True

is_allowed = is_blocked and (is_admin or (is_active and has_permission))

print(is_allowed)
