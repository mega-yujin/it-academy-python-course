is_admin = True
is_active = True
has_permission = True
is_blocked = False
is_allowed = not is_blocked and (is_active and has_permission or is_admin)
print(is_allowed)
