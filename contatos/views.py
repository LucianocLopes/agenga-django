from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Contato


@login_required(redirect_field_name='login')
def index(request):
    contatos = Contato.objects.order_by('-id').filter(
        ativo=True
    )
    paginator = Paginator(contatos, 30)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


@login_required(redirect_field_name='login')
def ver_contato(request, contato_id):
    
    contato = get_object_or_404(Contato, id=contato_id)
    
    if not contato.ativo:
        raise Http404()
    
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    })
    # try:
        # contato = Contato.objects.get(id=contato_id)
        
        # return render(request, 'contatos/ver_contato.html', {
            # 'contato': contato
        # })
    # except Contato.DoesNotExist as e:
        # raise Http404()

@login_required(redirect_field_name='login')
def busca(request):
    termo = request.GET.get('termo')
    
    if not termo or termo is None:
        messages.add_message(
            request,
            messages.ERROR,
            'Busca não pode ser realizada sem nenhuma informação!',
        )
        messages.add_message(
            request,
            messages.SUCCESS,
            'Você foi redirecionado para a pagina inicial da agenda!',
        )
        return redirect('index')
    
    campos = Concat('nome', Value(' '), 'sobrenome')
    # print(termo)
    
    contatos = Contato.objects.annotate(
        completo=campos,
    ).filter(
        Q(completo__icontains=termo) | Q(telefone__icontains=termo)
    )


    paginator = Paginator(contatos, 15)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })
