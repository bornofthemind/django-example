from django import forms
from django.core import validators
from django import forms
from first_app.models import TestUsers

class NewUser(forms.ModelForm):
	class Meta:
		model = TestUsers
		fields = '__all__'

def check_for_z(value):
	if value[0].lower() != 'z':
		raise forms.ValidationError("Name needs to start with 'z'")

class FormName(forms.Form):
	name = forms.CharField(validators=[check_for_z])
	email = forms.EmailField()
	verify_email = forms.EmailField(label='Verify E-mail:')
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.ValidationError('E-mails do not match')

	botcatcher = forms.CharField(required=False,
								widget=forms.HiddenInput,
								validators=[validators.MaxLengthValidator(0)])

	def clean_botcatcher(self):
		botcatcher = self.cleaned_data['botcatcher']
		if len(botcatcher) > 0:
			raise forms.ValidationError("GOTCHA BOT!")