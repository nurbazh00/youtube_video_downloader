from django import forms


class DownloadForm(forms.ModelForm):
    url = forms.RegexField(
        regex=r'^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+$',
        widget=forms.TextInput(attrs={
            'placeholder': 'Вставьте ссылку для скачивания'}),
        label=False, required=True, max_length=500)
