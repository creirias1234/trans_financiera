#from app_registro.views import clientes
from django.db import models
from django.contrib.auth.models import User



'''
    Tipos de datos para los campos de los modelos:
    - Todos los campos se obtienen de models
    -> CharField(max_lenght=25, default='Jack', null=True, blank=True)
    -> TextField()
    -> IntegerField()
    -> DecimalField(max_digits=5, decimal_places=2)
    -> PositiveIntegerField()
    -> SmallIntegerField()
    -> BooleanField(default=True)
    -> EmailField()
    -> ImageField(upload_to='fotos')
    -> FileField(upload_to='archivos')
    -> SlugField(): Tesla ha afectado el precio del Bitcoin >> tesla-ha-afectado-....

    Campos para establecer relaciones entre Modelos:
    -> ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    -> OneToOneField()
    -> ManyToManyField()

'''

class Clientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    telefono = models.CharField(max_length=30)
    correo = models.EmailField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    
    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Cuenta(models.Model):
    ESTADOS = (
        ('1', 'Activa'),
        ('2', 'Inactiva'),
    )
    fecha_registro = models.DateTimeField(auto_now_add=True)
    saldo=models.DecimalField(max_digits=10, decimal_places=2)
    clientes= models.ForeignKey(Clientes, on_delete=models.CASCADE, null=True)
    #clientes = models.ManyToManyField(Clientes, blank=True)
    estado = models.CharField(max_length=1, choices=ESTADOS, default='1')

    @property
    def saldo_actual(self):
        cant_deposito = self.depocito_set.count
        return self.saldo - cant_deposito


    def __str__(self):
        return f'Cuenta; {self.fecha_registro} - Clientes: {self.clientes}'
    
class Depocito(models.Model):

    fecha_depocito= models.DateTimeField(auto_now_add=True)
    cantidad=models.DecimalField(max_digits=10, decimal_places=2)
    cuenta=models.ForeignKey(Cuenta, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.conferencia} | {self.participante}'

class Retiro(models.Model):
    fecha_retiro = models.DateTimeField(auto_now_add=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.fecha_retiro}'

    
    # class Meta:
    #     unique_together = ('conferencia', 'participante')




# Create your models here.
