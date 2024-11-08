import os
import django
import random

# Configure Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()
from django_seed import Seed

seeder = Seed.seeder(locale='en_US')
from blog.models import AuthorModel, CategoryModel, PostModel



seeder.add_entity(AuthorModel, 5, {
    'id': lambda x: random.randint(1, 5),
    'first_name': lambda x: seeder.faker.name().split(' ')[0],
    'last_name': lambda x: seeder.faker.name().split(' ')[1],
    'status': True,
    'avatar': lambda x: f'https://avatar.iran.liara.run/public/{ random.randint(1, 100)}',
    'email': lambda x: seeder.faker.email(),
} )

seeder.add_entity(CategoryModel, 10, {
    'id': lambda x: random.randint(1, 10),
    'name': lambda x: seeder.faker.text(),
    'status': True,
    'image': lambda x: f'https://picsum.photos/1200/800?random={ random.randint(1, 100)}',
    'description': lambda x: seeder.faker.text()
} ) 

seeder.add_entity(PostModel, 60, {
    'title': lambda x: seeder.faker.text(),
    'slug': lambda x: seeder.faker.slug(),
    'content': lambda x: seeder.faker.text(),
    'author': lambda x: AuthorModel.objects.order_by('?').first(),
    'category': lambda x:  CategoryModel.objects.order_by('?').first(),
    'description': lambda x: seeder.faker.text(),
    'status': True,
    'image': lambda x: f'https://picsum.photos/800/600?random={ random.randint(1, 100)}',
} )



seeder.execute()