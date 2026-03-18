from django.shortcuts import render,redirect,get_object_or_404
from .models import Note
from .forms import NoteForm, SignupForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q

# Create your views here.

@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)

    query = request.GET.get('q')
    if query:
        notes = notes.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query)
        )

    notes = notes.order_by('-created_at')
    return render(request, 'notes/lista-notas.html', {'notes': notes})

# Criar nova nota
@login_required
def create_note(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user  # associa ao usuário logado
            note.save()
            messages.success(request, "Nota criada com sucesso!")
            return redirect('lista-notas')
    else:
        form = NoteForm()
    return render(request, 'notes/criar-notas.html', {'form': form})

# Editar nota existente
@login_required
def edit_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, "Nota atualizada com sucesso!")
            return redirect('lista-notas')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/criar-notas.html', {'form': form})

# Deletar nota
@login_required
def delete_note(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    note.delete()
    messages.success(request, "Nota deletada com sucesso!")
    return redirect('lista-notas')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Conta criada com sucesso!")
            return redirect('lista-notas')
    else:
        form = SignupForm()

    return render(request, 'notes/signup.html', {'form': form})

@login_required
def toggle_favorite(request, id):
    note = get_object_or_404(Note, id=id, user=request.user)
    note.is_favorite = not note.is_favorite
    note.save()
    return redirect('lista-notas')

@login_required
def favorite_notes(request):
    # Pega só as notas do usuário que estão marcadas como favoritas
    notes = Note.objects.filter(user=request.user, is_favorite=True).order_by('-created_at')
    
    # Mantém a pesquisa por título se quiser
    query = request.GET.get('q')
    if query:
        notes = notes.filter(title__icontains=query)
    
    return render(request, 'notes/favoritas-notas.html', {'notes': notes})