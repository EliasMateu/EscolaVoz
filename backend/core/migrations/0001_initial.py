import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


def seed_data(apps, schema_editor):
    School = apps.get_model('core', 'School')
    DemandCategory = apps.get_model('core', 'DemandCategory')

    schools_data = [
        ("EE Professora Maria Silva", "Itapeva", "12001234"),
        ("EE José de Alencar", "Itapeva", "12002345"),
        ("EE Barão do Rio Branco", "Itapeva", "12003456"),
        ("EE Carlos Gomes", "Itapeva", "12004567"),
        ("EE Vila Independencia", "Itapeva", "12005678"),
    ]
    for name, city, inep in schools_data:
        School.objects.get_or_create(name=name, defaults={'city': city, 'inep_code': inep})

    categories_data = [
        ("Mobiliário", "Mesas, cadeiras, armários e equipamentos"),
        ("Reformas", "Pintura, elétrica, hidráulica e obras"),
        ("Merenda", "Alimentação escolar e cozinha"),
        ("Transporte", "Ônibus e vans escolares"),
        ("Material Didático", "Livros, cadernos e recursos pedagógicos"),
        ("Tecnologia", "Computadores, internet e equipamentos"),
        ("Infraestrutura", "Quadras, playgrounds e ambientes externos"),
    ]
    for name, desc in categories_data:
        DemandCategory.objects.get_or_create(name=name, defaults={'description': desc})


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('inep_code', models.CharField(max_length=20, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={'db_table': 'schools', 'ordering': ['name']},
        ),
        migrations.CreateModel(
            name='DemandCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
            ],
            options={'db_table': 'demand_categories', 'verbose_name_plural': 'Demand Categories'},
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='employee_profile', to=settings.AUTH_USER_MODEL)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='core.school')),
            ],
            options={'db_table': 'employees'},
        ),
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('open', 'Aberta'), ('in_progress', 'Em Andamento'), ('resolved', 'Resolvida'), ('rejected', 'Rejeitada')], default='open', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demands', to='core.demandcategory')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demands', to='users.employee')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demands', to='core.school')),
            ],
            options={'db_table': 'demands', 'ordering': ['-created_at']},
        ),
        migrations.RunPython(seed_data, reverse_func),
    ]