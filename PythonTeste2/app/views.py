"""
Definition of views.
"""

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from app.models import Cliente, Estado, Cidade,Endereco, Contato, Representacao, Produto, Produto, Pedido, Prazo
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from django.core.serializers import json
import simplejson
import pickle
from _collections import defaultdict
import json
from django.db.models.base import Model
from django.views.decorators.csrf import csrf_protect, csrf_exempt


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def clientes_manutencao(request):  # FUNÇÃO PARA BUSCAR E RETORNAR TODOS OS REGISTROS 
     
     clientesLista = {}

     if request.method == 'POST':
         clientesLista = Cliente.objects.filter(nome_fantasia = request.POST.get('campoNomeBuscar'))
         return render(request,'app/pages/clientes/manutencao.html', {'clientesLista':clientesLista})  
           # se não tiver cliente na busca, então recupera todos 
    
     clientesLista = Cliente.objects.all()  
     return render(request,'app/pages/clientes/manutencao.html', {'clientesLista': clientesLista})

def clientes_manutencao_buscar(request):   #  FUNÇÃO AINDA NÃO UTILIZADA
        
     clientesSelected = {}
     
     if request.method == 'POST':
        clientesSelected = Cliente.objects.filter(nome_fantasia = request.POST.get('campoNomeBuscar'))
      
     return render(request,'app/pages/clientes/manutencao.html', {'data':clientesSelected})  

def get_estados_json(request):
        
        estadosData = defaultdict(dict)
        estadosData = list(Estado.objects.all())
        estadosData2 = serializers.serialize('json',estadosData)  
      
        data = estadosData2
     
        return HttpResponse(data , content_type = "application/json")   # RETORNANDO DADOS EM JSON POR AJAX
           

def clientes_manutencao_inserir(request):
        
        estadosData = {}
        estadosData = Estado.objects.all()
                
        return render(request,'app/pages/clientes/inserir.html', {'estadosData': estadosData})


def get_cidades_json(request):      

        cidadesData = defaultdict(dict)
        cidadesData = list(Cidade.objects.filter(estado_id = request.GET.get('id_estado',None)))
        cidadesData2 = serializers.serialize('json',cidadesData)  
      
        data = cidadesData2
     
        return HttpResponse(data , content_type = "application/json")   # RETORNANDO DADOS EM JSON POR AJAX

def inserir_cliente(request):   # VIEW PARA INSERIR CLIENTE NO BANCO DE DADOS
        
        if request.method == 'POST':
            nCliente = Cliente()
            nEndereco = Endereco()
            nContato = Contato()            

            nCliente.nome_fantasia = request.POST.get('nome_fantasia')      
            nCliente.cnpj =  request.POST.get('cnpj')
            nCliente.razao_social = request.POST.get('razao_social')
            nCliente.inscri_municipal = request.POST.get('inscri_municipal')
            nCliente.inscri_estadual = request.POST.get('inscri_estadual')
            nCliente.status = request.POST.get('status')
                        
            nEndereco.rua = request.POST.get('rua')
            nEndereco.numero = request.POST.get('numero')             
            nEndereco.referencia = request.POST.get('referencia')
            nEndereco.cep = int(request.POST.get('cep')) if request.POST.get('cep') else None # SE FOR STRING VAZIA, ENTÃO RECEBE NONE/NULLO
            nEndereco.bairro = request.POST.get('bairro')            
            nEndereco.cidade_id = request.POST.get('cidade')
            nEndereco.estado_id = request.POST.get('estado')  
            nEndereco.save() 
            nCliente.endereco = nEndereco
            
            nContato.email = request.POST.get('email')
            nContato.celular1 = request.POST.get('celular1')
            nContato.celular2 = request.POST.get('celular2')
            nContato.telefone1 = request.POST.get('telefone1')
            nContato.telefone2 = request.POST.get('telefone2')
            nContato.site = request.POST.get('site') 
            nContato.save()           
            nCliente.contato = nContato            
          
            
            nCliente.save()  # SALVANDO NO BANCO DE DADOS
             
            
        return redirect('clientes_manutencao_inserir')

def clientes_manutencao_consultar(request,id):
     
     cliente = Cliente.objects.get(id = id)
                                
     return render(request,'app/pages/clientes/detalhes.html',{'cliente' : cliente})
                 
def clientes_manutencao_editar(request,id):    

      if request.method == 'POST':

            nCliente =  Cliente.objects.get(id = id)
            nEndereco = Endereco.objects.get(id = nCliente.endereco_id) 
            nContato = Contato.objects.get(id = nCliente.contato_id)                         

            nCliente.nome_fantasia = request.POST.get('nome_fantasia')      
            nCliente.cnpj = request.POST.get('cnpj')
            nCliente.razao_social = request.POST.get('razao_social')
            nCliente.inscri_municipal = request.POST.get('inscri_municipal')
            nCliente.inscri_estadual = request.POST.get('inscri_estadual')
            nCliente.status = request.POST.get('status')
                        
            nEndereco.rua = request.POST.get('rua')
            nEndereco.numero = request.POST.get('numero')             
            nEndereco.referencia = request.POST.get('referencia')
            nEndereco.cep = int(request.POST.get('cep')) if request.POST.get('cep') else None # SE FOR STRING VAZIA, ENTÃO RECEBE NONE/NULLO
            nEndereco.bairro = request.POST.get('bairro')            
            nEndereco.cidade_id = request.POST.get('cidade')
            nEndereco.estado_id = request.POST.get('estado')  
            nEndereco.save()  # SALVANDO ENDERECO 
            
      
            nCliente.save() # SALVANDO CLIENTE
            
            nContato.email = request.POST.get('email')
            nContato.celular1 = request.POST.get('celular1')
            nContato.celular2 = request.POST.get('celular2')
            nContato.telefone1 = request.POST.get('telefone1')
            nContato.telefone2 = request.POST.get('telefone2')
            nContato.site = request.POST.get('site') 
            nContato.save()         # SALVANDO CONTATO     
           
      return redirect('clientes_manutencao')
         
def clientes_manutencao_deletar(request,id):
     
      cliente = Cliente.objects.filter(id=id)
      cliente.delete()

      return redirect('clientes_manutencao')

@csrf_exempt    # FUNÇÃO PARA ISENTAR A VIEW DE UM CSRF FAIL    
def clientes_manutencao_detalhes(request,id):    # REDIRECIONAR O CLIENTE PARA SE DELETADO OU ALTERADO   
   
          
        if request.method=='POST' and 'BtnSave_edit' in request.POST:
       # return  redirect('clientes_manutencao_editar',id)
         return clientes_manutencao_editar(request,id)  # REDIRECIONANDO PARA EDITAR CLIENTES // ESSE É O MODO PARA LEVAR OS DADOS DO REQUEST POST
        elif request.method=='POST' and 'BtnDelete' in request.POST:
         return  redirect('clientes_manutencao_deletar',id)   # REDIRECIONANDO PARA DELETAR CLIENTES
        
 
        return redirect('clientes_manutencao')
        
def repres_manutencao(request):  # FUNÇÃO PARA BUSCAR E RETORNAR TODOS OS REGISTROS 
     
     represLista = {}

     if request.method == 'POST':
         represLista = Representacao.objects.filter(nome_fantasia = request.POST.get('campoNomeBuscar'))
         return render(request,'app/pages/representacoes/manutencao.html', {'represLista':represLista})  
           # se não tiver cliente na busca, então recupera todos 
    
     represLista = Representacao.objects.all()  
     return render(request,'app/pages/representacoes/manutencao.html', {'represLista': represLista})  

def repres_manutencao_inserir(request):

     estadosData = {}
     estadosData = Estado.objects.all()

     return render(request,'app/pages/representacoes/inserir.html', {'estadosData': estadosData})


def inserir_repres(request):  # VIEW PARA INSERIR REPRESENTACAO NO BANCO DE DADOS

       if request.method == 'POST':
            nRepres = Representacao()
            nEndereco = Endereco()
            nContato = Contato()            

            nRepres.nome_fantasia = request.POST.get('nome_fantasia')      
            nRepres.cnpj =  request.POST.get('cnpj')
            nRepres.razao_social = request.POST.get('razao_social')
            nRepres.inscri_estadual = request.POST.get('inscri_estadual')
            nRepres.status = request.POST.get('status')
                        
            nEndereco.rua = request.POST.get('rua')
            nEndereco.numero = request.POST.get('numero')             
            nEndereco.referencia = request.POST.get('referencia')
            nEndereco.cep = int(request.POST.get('cep')) if request.POST.get('cep') else None # SE FOR STRING VAZIA, ENTÃO RECEBE NONE/NULLO
            nEndereco.bairro = request.POST.get('bairro')            
            nEndereco.cidade_id = request.POST.get('cidade')
            nEndereco.estado_id = request.POST.get('estado')  
            nEndereco.save() 
            nRepres.endereco = nEndereco
            
            nContato.email = request.POST.get('email')
            nContato.celular1 = request.POST.get('celular1')
            nContato.celular2 = request.POST.get('celular2')
            nContato.telefone1 = request.POST.get('telefone1')
            nContato.telefone2 = request.POST.get('telefone2')
            nContato.site = request.POST.get('site') 
            nContato.save()           
            nRepres.contato = nContato            
          
            
            nRepres.save()  # SALVANDO NO BANCO DE DADOS
             
            
       return redirect('repres_manutencao_inserir')

def repres_manutencao_consultar(request,id):
      
      repres = Representacao.objects.get(id = id)        

      return render(request,'app/pages/representacoes/detalhes.html', {'repres': repres })

@csrf_exempt   # FUNÇÃO PARA ISENTAR A VIEW DE UM CSRF FAIL    
def repres_manutencao_detalhes(request,id):
        
        if request.method=='POST' and 'BtnSave_edit' in request.POST:
       # return  redirect('repres_manutencao_editar',id)
         return repres_manutencao_editar(request,id)  # REDIRECIONANDO PARA EDITAR REPRESENTAÇÕES // ESSE É O MODO PARA LEVAR OS DADOS DO REQUEST POST
        elif request.method=='POST' and 'BtnDelete' in request.POST:
         return  redirect('repres_manutencao_deletar',id)   # REDIRECIONANDO PARA DELETAR REPRESENTAÇÕES
        
 
        return redirect('repres_manutencao')

def repres_manutencao_editar(request,id):   # ALTERANDO OS DADOS DA REPRESENTAÇÃO NA TELA DETALHES

     if request.method == 'POST':

            nRepres =  Representacao.objects.get(id = id)
            nEndereco = Endereco.objects.get(id = nRepres.endereco_id) 
            nContato = Contato.objects.get(id = nRepres.contato_id)                         
            
            nRepres.nome_fantasia = request.POST.get('nome_fantasia')      
            nRepres.cnpj = request.POST.get('cnpj')
            nRepres.razao_social = request.POST.get('razao_social')
            nRepres.inscri_estadual = request.POST.get('inscri_estadual')
            nRepres.status = request.POST.get('status')
                        
            nEndereco.rua = request.POST.get('rua')
            nEndereco.numero = request.POST.get('numero')             
            nEndereco.referencia = request.POST.get('referencia')
            nEndereco.cep = int(request.POST.get('cep')) if request.POST.get('cep') else None # SE FOR STRING VAZIA, ENTÃO RECEBE NONE/NULLO
            nEndereco.bairro = request.POST.get('bairro')            
            nEndereco.cidade_id = request.POST.get('cidade')
            nEndereco.estado_id = request.POST.get('estado')  
            nEndereco.save()  # SALVANDO ENDERECO             
      
            nRepres.save() # SALVANDO REPRESENTACAO
            
            nContato.email = request.POST.get('email')
            nContato.celular1 = request.POST.get('celular1')
            nContato.celular2 = request.POST.get('celular2')
            nContato.telefone1 = request.POST.get('telefone1')
            nContato.telefone2 = request.POST.get('telefone2')
            nContato.site = request.POST.get('site') 
            nContato.save()         # SALVANDO CONTATO     
           
     return redirect('repres_manutencao')


def repres_manutencao_deletar(request,id):
    
      repres = Representacao.objects.filter(id=id)
      repres.delete()

      return redirect('repres_manutencao')

def produtos_manutencao(request):  # FUNÇÃO PARA BUSCAR E RETORNAR TODOS OS REGISTROS 
     
     produtosLista = {}

     if request.method == 'POST':
         produtosLista = Produto.objects.filter(nome = request.POST.get('campoNomeBuscar'))
         return render(request,'app/pages/produtos/manutencao.html', {'produtosLista':produtosLista})  
           # se não tiver cliente na busca, então recupera todos 
    
     produtosLista = Produto.objects.all().order_by('nome');  
     return render(request,'app/pages/produtos/manutencao.html', {'produtosLista': produtosLista})  


def produtos_manutencao_inserir(request):
            
     represData = Representacao.objects.all()               
   
     return render(request,'app/pages/produtos/inserir.html',{'represData':represData})


def inserir_produtos(request):  # VIEW PARA INSERIR REPRESENTACAO NO BANCO DE DADOS
                
       if request.method == 'POST':
            nProduto = Produto()
             
            p1 = request.POST.get('preco1') 
            p2 = request.POST.get('preco2')        
            p3 = request.POST.get('preco3')                 

            nProduto.nome = request.POST.get('nome')      
            nProduto.preco1 = str.replace(p1,',','.') if p1 else None
            nProduto.preco2 = str.replace(p2,',','.') if p2 else None
            nProduto.preco3 = str.replace(p3,',','.') if p3 else None
            nProduto.status = request.POST.get('status')
            nProduto.representacao_id = request.POST.get('representacao')             
           
            nProduto.save()  # SALVANDO NO BANCO DE DADOS
             
            
       return redirect('produtos_manutencao_inserir')  

def produtos_manutencao_consultar(request,id):       
     
        produto = Produto.objects.get(id = id)
        
        return render(request,'app/pages/produtos/detalhes.html',{'produto':produto})


def get_representacoes_json(request):      

        represData = defaultdict(dict)
        represData = list(Representacao.objects.all().order_by('nome_fantasia'))
        represData2 = serializers.serialize('json',represData)  
      
        data = represData2
        
        return HttpResponse(data , content_type = "application/json")   # RETORNANDO DADOS EM JSON POR AJAX

@csrf_exempt   # FUNÇÃO PARA ISENTAR A VIEW DE UM CSRF FAIL    
def produtos_manutencao_detalhes(request,id):
        
        if request.method=='POST' and 'BtnSave_edit' in request.POST:
       # return  redirect('repres_manutencao_editar',id)
         return produtos_manutencao_editar(request,id)  # REDIRECIONANDO PARA EDITAR REPRESENTAÇÕES // ESSE É O MODO PARA LEVAR OS DADOS DO REQUEST POST
        elif request.method=='POST' and 'BtnDelete' in request.POST:
         return  redirect('produtos_manutencao_deletar',id)   # REDIRECIONANDO PARA DELETAR REPRESENTAÇÕES
        
 
        return redirect('produtos_manutencao')

def produtos_manutencao_deletar(request,id):

      produto = Produto.objects.get(id = id)
      produto.delete()  

      return redirect('produtos_manutencao')

def produtos_manutencao_editar(request,id):

     if request.method == 'POST':

            nProduto =  Produto.objects.get(id = id)
            nRepresentacao = Representacao.objects.get(id = nProduto.representacao_id) 
          
            nProduto.nome = request.POST.get('nome')      
            nProduto.preco1 = request.POST.get('preco1')
            nProduto.preco2 = request.POST.get('preco2')
            nProduto.preco3 = request.POST.get('preco3')
            nProduto.status = request.POST.get('status')
            nProduto.representacao_id = request.POST.get('representacao')            
               
            nProduto.save() # SALVANDO REPRESENTACAO
            
     
     return redirect('repres_manutencao')


def pedidos_manutencao(request):
    
     pedidosLista = {}

     if request.method == 'POST':
         pedidosLista = Pedido.objects.filter(nome = request.POST.get('campoNomeBuscar'))
         return render(request,'app/pages/pedidos/manutencao.html', {'pedidosLista':pedidosLista})  
           # se não tiver cliente na busca, então recupera todos 
    
     pedidosLista = Pedido.objects.all()  
     return render(request,'app/pages/pedidos/manutencao.html', {'pedidosLista': pedidosLista})  

def pedidos_manutencao_consultar(request,id):

   return render(request,'app/pages/pedidos/manutencao.html',{'pedidosLista':pedidosLista}) 

def inserir_pedidos(request):  # VIEW PARA INSERIR REPRESENTACAO NO BANCO DE DADOS
                
       if request.method == 'POST':
            nProduto = Produto()                      

            nProduto.nome = request.POST.get('nome')      
            nProduto.preco1 = str.replace(request.POST.get('preco1'),',','.')
            nProduto.preco2 = str.replace(request.POST.get('preco2'),',','.')
            nProduto.preco3 = str.replace(request.POST.get('preco3'),',','.')
            nProduto.status = request.POST.get('status')
            nProduto.representacao_id = request.POST.get('representacao')             
           
            nProduto.save()  # SALVANDO NO BANCO DE DADOS
             
            
       return redirect('pedidos_manutencao_inserir')  

def pedidos_manutencao_inserir(request):

        represLista = Representacao.objects.all().order_by('nome_fantasia')
        prazoLista =  Prazo.objects.all().order_by('descricao')
        clientesLista = Cliente.objects.all().order_by('nome_fantasia')           
    
        return render(request,'app/pages/pedidos/inserir.html',{'represLista':represLista, 'prazoLista':prazoLista,'clientesLista':clientesLista})


def get_produtos_by_repres_json(request):
        
        idRepres = request.GET.get('idRepres',None)
        produtosLista = list(Produto.objects.filter(representacao_id = idRepres).order_by('nome'))
        produtosLista2 = serializers.serialize('json',produtosLista)  
      
        return HttpResponse(produtosLista2 , content_type = "application/json")   # RETORNANDO DADOS EM JSON POR AJAX


def prazos_manutencao(request):

     prazosLista = Prazo.objects.all().order_by('descricao')

     return render(request,'app/pages/prazos/manutencao.html',{'prazosLista':prazosLista})

@csrf_exempt
def inserir_prazo(request):
                
      if request.POST and request.is_ajax():
        nPrazo = Prazo()
        nPrazo.descricao = request.POST.get('prazo','')
        nPrazo.save()
        

      prazosLista = list(Prazo.objects.all().order_by('descricao'))
      prazosLista2 = serializers.serialize('json',prazosLista)   
            
  
      return HttpResponse(prazosLista2,content_type="application/json")


def get_prazo_by_id(request):

     
    prazo = list(Prazo.objects.filter(id = request.GET.get('idPrazo',None)))
    prazo2 = serializers.serialize('json',prazo)

    return HttpResponse(prazo2, content_type="application/json")

def deletar_prazo(request):
  
    prazo = Prazo.objects.filter(id = request.GET.get('prazoIdCampo',None))
    prazo.delete() 
        
    response = serializers.serialize('json',{})

    return HttpResponse(response,content_type="application/json")


def prazo_manutencao_editar(request):

    if request.POST:
        nPrazo = Prazo.objects.get(id = request.POST.get('id',''))
        nPrazo.descricao = request.POST.get('descricao','')       
        nPrazo.save()
        response = serializers.serialize('json',{})
     
        return HttpResponse(response,content_type='application/json')
  
