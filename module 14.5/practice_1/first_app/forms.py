from django import forms
import datetime

birthday = ['2001','2002','2003']
colors = [
    ('blue','Blue'),
    ('red','Red'),
    ('green', 'Green'),
]
food = [
    ('burger','Burger'),
    ('sandwitch','Sandwitch'),
    ('milk', 'Milk'),
    ('coffee', 'Coffee'),
]

class PracticeForm(forms.Form):
    name = forms.CharField(initial='Your name')
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField()
    agree = forms.BooleanField()
    Date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=birthday))
    value = forms.DecimalField()
    last_name = forms.CharField(max_length=10)
    Today = forms.DateField(initial=datetime.date.today)
    choice_color = forms.ChoiceField(widget=forms.RadioSelect, choices=colors)
    favourit_food = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=food)
    roll_number = forms.IntegerField(help_text="Enter 6 digit roll Numbers")
    password = forms.CharField(widget=forms.PasswordInput())

    