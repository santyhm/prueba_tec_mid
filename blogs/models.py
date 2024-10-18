from django.db import models
from django.contrib.auth.models import AbstractUser

class AuthRol(models.Model):
    rol = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Rol'

    def __str__(self):
        return self.rol

class User(AbstractUser):
    rol = models.ForeignKey(AuthRol, models.SET_NULL, blank=True, null=True, related_name="user_rol_auth")

    username = models.CharField(
        max_length=150, 
        unique=True,
        null=False,
        blank=False,
        help_text='Required. You can use any character here.',
        error_messages={
            'unique': "A user with that username already exists.",
        }
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',  # Cambia el related_name aquí
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',  # Cambia el related_name aquí
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = 'Usuario'

class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    tags = models.ManyToManyField('Tag', blank=True, verbose_name="Etiquetas")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Blog'

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments', verbose_name="Blog")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_author", verbose_name="Autor")
    content = models.TextField(verbose_name="Contenido")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"
    
    class Meta:
        verbose_name = 'Comentario'

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name="Nombre")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Etiqueta'
