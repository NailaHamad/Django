from django import forms
from .models import activity, items, task

class ActivityForm(forms.ModelForm):
    class Meta:
        model = activity
        fields = ['name', 'category']
    name = forms.CharField(
        max_length=100,
        required=True,
        label='name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the name',
                'class':'activityclass',
                'id':'nameid',
            }
        )
    )
    category = forms.CharField(
        max_length=100,
        required=True,
        label='category'
    )

class ItemsForm(forms.ModelForm):
    class Meta:
        model = items
        fields = ['name', 'category', 'price']
        
    name = forms.CharField(
        max_length=100,
        required=True,
        label='name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the name',
                'class':'Itemsclass',
                'id':'nameid',
            }
        )
    )     
    category = forms.CharField(
        max_length=100,
        required=True,
        label='category'
    )
    price = forms.DecimalField(
        required=True,
        min_value= 20,
        max_value = 5000,
        label='price'
    )


class TaskForm(forms.ModelForm):
    class Meta:
        model = task
        fields = ['name', 'priority', 'category']

    name = forms.CharField(
        max_length=100,
        required=True,
        label='name',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the name',
                'class':'Taskclass',
                'id':'nameid',
            }
        )
    ) 
    
    priority = forms.CharField(
        max_length=50,
        required=True,
        label='priority',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the priority',
                'class':'Taskclass',
                'id':'priorityid',
            }
        )
    ) 
    category = forms.CharField(
        max_length=100,
        required=True,
        label='category'
    )