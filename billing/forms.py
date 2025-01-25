from django import forms
from .models import Bill
from sports_spaces.models import SportsSpace
from areas.models import Area

class BillForm(forms.ModelForm):
    space = forms.ModelChoiceField(
        queryset=SportsSpace.objects.none(),
        label="Espacio Deportivo",
        empty_label="Seleccione un espacio deportivo"
    )

    class Meta:
        model = Bill
        fields = ['full_name', 'identification', 'total_amount', 'status', 'space']
        labels = {
            'full_name': 'Nombre',
            'identification': 'Cédula',
            'total_amount': 'Monto Total',
            'status': 'Estado',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Remove user type check
        if user:
            areas = Area.objects.filter(user=user)
            self.fields['space'].queryset = SportsSpace.objects.filter(area__in=areas)
