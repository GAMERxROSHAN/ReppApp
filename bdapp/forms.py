from django import forms

class NawForm(forms.Form):
	CHOICES = [('Ambivali', 'Ambivali'),('Kalyan', 'Kalyan'),('Shahad', 'Shahad'),('Worli', 'Worli'),
	('Andheri', 'Andheri'),('Andheri', 'Dadar'),
	('Asangoan', 'Asangoan'),
	('Powai', 'Powai'),
	('Ghatkopar', 'Ghatkopar'),('Malad','Malad'),
	('Dombivali', 'Dombivali'),('Thane','Thane')]
	loc = forms.ChoiceField(label="Please choose location which you want to stay ? ", widget=forms.RadioSelect,choices=CHOICES,)

	area=forms.IntegerField(label="Enter your area ", widget=forms.NumberInput(attrs={"min":400.0, "max":2000}))
	bd=forms.IntegerField(label="Enter No. Bedroom ", widget=forms.NumberInput(attrs={"min":1.0, "max":4}))
	CHOICES = [('1', 'Yes'), ('0', 'No'),]
	nr = forms.ChoiceField(label="Do you want new real estate ? ", widget=forms.RadioSelect,choices=CHOICES, )
	g = forms.ChoiceField(label="Do you want gym service ", widget=forms.RadioSelect,choices=CHOICES, )
	la = forms.ChoiceField(label="Do you want lift ?  ", widget=forms.RadioSelect,choices=CHOICES, )
	cp = forms.ChoiceField(label="Do you want car parking ?", widget=forms.RadioSelect,choices=CHOICES, )
	ms = forms.ChoiceField(label="Do you want maintenance ?", widget=forms.RadioSelect,choices=CHOICES, )
	se = forms.ChoiceField(label="Do you want security ?", widget=forms.RadioSelect,choices=CHOICES, )
	ca = forms.ChoiceField(label="Do you want children playground ?", widget=forms.RadioSelect,choices=CHOICES, )
	cl = forms.ChoiceField(label="Do you want clubhouse ?", widget=forms.RadioSelect,choices=CHOICES, )
	inte = forms.ChoiceField(label="Do you want telephone service ?", widget=forms.RadioSelect,choices=CHOICES, )
	lg = forms.ChoiceField(label="Do you want garden ?", widget=forms.RadioSelect,choices=CHOICES, )
	ig = forms.ChoiceField(label="Do you want Indoor Games ?", widget=forms.RadioSelect,choices=CHOICES, )
	gc = forms.ChoiceField(label="Do you want Gas connection ?", widget=forms.RadioSelect,choices=CHOICES, )
	jt = forms.ChoiceField(label="Do you want Jogging track ?", widget=forms.RadioSelect,choices=CHOICES, )
	sp = forms.ChoiceField(label="Do you want  swimming pool ?", widget=forms.RadioSelect,choices=CHOICES, )



