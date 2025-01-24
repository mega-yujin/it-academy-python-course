from models import Category, Article
from django.contrib.auth.models import User


bob = User(username='Bob', password='1234')
alice = User(username='Alice', password='qwerty')

bob.save()
alice.save()

Category.objects.create(name='journal', description='some letters')
Category.objects.create(name='weather', description='sunny')

Article.objects.create(title='Election', content='Who won', author=bob, category=Category.objects.get(id=1))
Article.objects.create(title='Election', content='Who won', author=alice, category=Category.objects.get(id=2))
