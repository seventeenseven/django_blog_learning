from django import forms
from .models import Article, Commentaire


class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, required=True,
    label="Nom complet")
    email = forms.EmailField(required=True, label="Adresse e-mail")
    password = forms.CharField(widget=forms.PasswordInput,
    min_length=8, label="Mot de passe")

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu', 'categorie', 'image']
        #fields = '__all__'
        
    def clean_titre(self):
        titre = self.cleaned_data.get('titre')
        print("in method")
        if '$' in titre:
            print("in if")
            raise forms.ValidationError("Le titre de votre post ne doit pas contenir de signe.")
        return titre