from django.forms import ModelForm
from .models import Solution

# este es un formulario que Django te da por defecto para que el usuario pueda rellenar
# diferentes campos y crear la solución
class SolutionForm(ModelForm):
    class Meta:
        model = Solution
        exclude = ['problem', 'user', 'created', 'updated']