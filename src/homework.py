is_admin = False

is_blocked = True
is_registered = True


has_permission = True if is_registered and not is_blocked else False
print(has_permission)
