from django.shortcuts import render, redirect
from .form import personaForm

# Create your views here.

def registerUser(request):
    if request.method == 'post':
        form = personaForm(request.post)
        if form.is_valid():
            form.save()
            return redirect ('listarUsuarios')
    else:
        form = personaForm()
        return render(request,'registroUsuario.html',{'form':personaForm})
