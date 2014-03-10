# -*- coding: utf-8 -*-
from django import forms
 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
 
 
class UnsubscribeForm(forms.Form):
    email = forms.EmailField()
 
    # Uni-form
    helper = FormHelper()
    helper.form_class = 'form-horizontal'
    helper.layout = Layout(
        Field('text_input', css_class='input-xlarge'),
        Field('email', 'Email'),
        FormActions(
        Submit('save_changes', 'Unsubscribe', css_class="btn-primary"),
        )
    )