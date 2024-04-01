from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.


class musician(models.Model):
    name =models.CharField(max_length=40)
    instrument=models.CharField(max_length=50)
    age=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(150)])
    salary=models.IntegerField(default=100,validators=[MinValueValidator(0)])
    
    def __str__(self) -> str:
        return f"name:{self.name} instrument:{self.instrument} age:{self.age} salary:{self.salary}"