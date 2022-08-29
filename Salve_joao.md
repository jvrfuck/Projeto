Achamos um site para fazer os Front-end e ficar melhor visualmente, segue abaixo
o link (para editar precisa passar o email tipo o trello):
https://www.figma.com/file/2undYJBZkFPcE7gZCSOqrj/PROJETO?node-id=0%3A1


Feito na aula, Criado algumas classes novas e varios modelos do arquivo models 
para o projeto (colocar futuramento so o que usar), segue abaixo os exemplo;

<<No arquivo do app models.py>> Criar nova CLASS
class Alunos(Pessoas):
    cogido_alunos = models.CharField(max_length=10,null=True,)
    

<<apos para funcionar colocar na pasta admin.py>>
from .models import Alunos 
admin.site.register(Alunos)

Os proximos sao exemplos dos principais para inserir nas tabelas, ai so vou passar
o passo do models.py, pq o do admin e igual e eu to com preguiça:
<<Na class Pessoas:>>
 PessoaCreated = models.DateTimeField(verbose_name="TimeStamp", auto_now_add=True)
 Ativo = models.CharField(max_length =1)
<<Na class Turmas>>
class Turmas(models.Model):
    Turma_nome = models.CharField(max_length = 40)
    Ativo = models.CharField(max_length =1)
<<Na class Alunos:>>
    Ativo = models.CharField(max_length =1)
    Codigo_alunos = models.CharField(max_length=10,null=True,)
    Aluno_data = models.DateField()
    Media_geral = models.IntegerField()
    Genero = [
        {"M", "Masculino"},
        {"F","Feminino"},
        {"O", "Outros"}
    ]
    Tipo = models.CharField(max_length=1,choices=Genero)
    Equipe = models.TextChoices("OdinPower", "ThorPower")
    Turma= models.ForeignKey(Turmas,on_delete=models.CASCADE)

## USAR ISSO EM "TODOS" OS CODIGOS
EX: Def ele subistitui a formataçao para n ficar vindo objeto1, objeto2,etc.. ali
ele mostra como vai ser exibido.

    def __str__(self):
        return '%s %s' % (self.pessoa_nome, self.pessoa_idade)

No class meta e o que vai ordenar como vai vir os campos(da a ordem)

    class Meta:
        ordering = ('pessoa_nome', 'pessoa_idade')
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'

```markdown
#https://docs.djangoproject.com/en/4.1/topics/db/models/ 
## LINK que tem os exemplos dos modelos da documentaçao oficial 

RESUMINHO DO QUE E CADA COISA 
# CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
# PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
# RESTRICT: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)
# SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
# SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.
# SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
# DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION. (2)
```markdown
 