from django import forms
import requests


class NameForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        site = 'http://127.0.0.1:8000/api/block_parameters/?block=1'
        r = requests.get(site)
        json = r.json()[0]
        self.fields['block_id'] = forms.CharField(widget=forms.HiddenInput())
        for k, v in json.items():
            if len(k) == 4 and v is not None:
                self.fields[k + '_value'] = forms.CharField(label=v, max_length=100)
        site = 'http://127.0.0.1:8000/api/blocks/?id=1'
        r = requests.get(site)
        json = r.json()[0]
        self.initial['block_id'] = '1'
        for k, v in json.items():
            if len(k) == 18 and v is not None:
                self.initial[k[:-8]] = v
