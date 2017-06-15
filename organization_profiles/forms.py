# coding=utf-8
from django import forms
from organization_profiles.models import OrganizationTemplate, BASIC_FIELDS
from django.utils.translation import ugettext_lazy as _


class OrganizationTemplateForm(forms.ModelForm):
    title = forms.CharField(label=u"Nombre de tu organización",
                            required=False,
                            widget=forms.TextInput(attrs={'placeholder': _(u'Organización Organizada')}))
    sub_title = forms.CharField(label=u"Descripción de la organización",
                                required=False,
                                widget=forms.Textarea(attrs={'placeholder': _(u'Ayúdanos a que te conozcan! En esta sección podrás contarnos sobre tu organización para informar a otros sobre tu labor social.')}))
    org_url = forms.URLField(label="Web de la organización",
                             required=False,
                            widget=forms.TextInput(attrs={'placeholder': _(u'https://miorganizacion.org')}))
    facebook = forms.URLField(label="FanPage de la organización",
                              required=False,
                            widget=forms.TextInput(attrs={'placeholder': _(u'https://www.facebook.com/miorganizacion/')}))
    twitter = forms.URLField(label="Twitter de la organización",
                             required=False,
                            widget=forms.TextInput(attrs={'placeholder': _(u'https://www.twitter.com/miorganizacion/')}))
    instagram = forms.URLField(label="Instagram de la organización",
                               required=False,
                            widget=forms.TextInput(attrs={'placeholder': _(u'https://www.instagram.com/miorganizacion/')}))

    primary_color = forms.CharField(label="Color primario",
                                    widget=forms.TextInput(attrs={'placeholder': '#CCDDCC',
                                                           'type': 'color'}))
    secondary_color = forms.CharField(label="Color del texto",
                                      widget=forms.TextInput(attrs={'placeholder': '#2DDC22',
                                                                    'type': 'color'}))
    class Meta:
        model = OrganizationTemplate
        fields = BASIC_FIELDS
