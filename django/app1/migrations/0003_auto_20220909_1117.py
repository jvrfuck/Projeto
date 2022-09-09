# Generated by Django 4.1 on 2022-09-09 14:17

# Migração para podermos inserir/remover dados no BD do projeto, manualmente ou com funções.

from django.db import migrations

DEFAULT_Pessoas_Juridicas = {
    ('nome_ficticio','atividade_presente','1234561000-89','Rua da Saudade',
    '47 9999-9999','empresa@email.com','Django_service', 'Senha_aleatoria')

}

def add_empresa(apps,  schema_editor):
    empresa = apps.get_model('app1','Pessoas_Juridicas')
    
    for Vnome, Vatividade, Vcnpj, Vendereco, Vtelefone, Vemail, Vservico, Vsenha in DEFAULT_Pessoas_Juridicas:
        empresa = empresa(pessoa_nome=Vnome, pj_atividade=Vatividade, pj_cnpj=Vcnpj,
        pessoa_endereco=Vendereco, pessoa_telefone=Vtelefone, pessoa_email=Vemail, pj_servico=Vservico, pessoa_senha=Vsenha)
        empresa.save()
    pass

def remove_empresa():

    for Vnome, Vatividade, Vcnpj, Vendereco, Vtelefone, Vemail, Vservico, Vsenha in DEFAULT_Pessoas_Juridicas:
        empresa = empresa.objects(pessoa_nome=Vnome, pj_atividade=Vatividade, pj_cnpj=Vcnpj, 
        pessoa_endereco=Vendereco, pessoa_telefone=Vtelefone, pessoa_email=Vemail, pj_servico=Vservico, pessoa_senha=Vsenha)
        empresa.delete()
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_calendario_pessoas_pessoa_imagem_and_more'),
    ]

    operations = [
        migrations.RunPython(add_empresa, remove_empresa)
    ]
