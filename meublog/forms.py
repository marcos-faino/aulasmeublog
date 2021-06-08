from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from meublog.models import Comentario


class EmailPost(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField()
    destino = forms.EmailField()
    coments = forms.CharField(required=False,
                              widget=forms.Textarea)

    def enviar_email(self, meupost):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        destino = self.cleaned_data['destino']
        coments = self.cleaned_data['coments']

        conteudo = f"Recomendo ler o post: {meupost.titulo}\n" \
                   f"Comentários: {coments}"
        mail = EmailMessage(
            subject=f"Recomendo este post",
            body=conteudo,
            from_email='contato@meublog.com.br',
            to=[destino,],
            headers={'Reply-to': email}
        )
        mail.send()


class ComentarioModelForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome','email','corpo']

    def salvar_comentario(self, post):
        novo_coment = self.save(commit=False)
        novo_coment.post = post # vinculando comentario ao post
        novo_coment.nome = self.cleaned_data['nome']
        novo_coment.email = self.cleaned_data['email']
        novo_coment.corpo = self.cleaned_data['corpo']
        return novo_coment.save()


class CadUsuarioForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email']
