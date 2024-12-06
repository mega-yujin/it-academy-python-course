#Напишите выражение для проверки доступа у пользователя, удовлетворяющее следующим условиям:
#если пользователь админ (is_admin), то ему разрешается
#если пользователь активен (is_active), и у него есть разрешение (has_permission), то ему разрешается
#если пользователь заблокирован (is_blocked), то ему ничего не разрешается, даже если он админ или если у него есть пермишен

is_admin = False
is_active = True
has_permission = False
is_blocked = True

is_allowed = is_blocked and (is_admin or (is_active and has_permission))

print(is_allowed)
