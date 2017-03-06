"""
Definition of urls for PythonTeste2.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^clientes/manutencao/$',app.views.clientes_manutencao, name='clientes_manutencao'), # GET TELA MANUTENÇÃO CLIENTES
    url(r'^clientes/manutencao_buscar/$',app.views.clientes_manutencao_buscar, name='clientes_manutencao_buscar'),
    url(r'^clientes/manutencao_inserir/$',app.views.clientes_manutencao_inserir, name='clientes_manutencao_inserir'), # GET TELA INSERIR CLIENTE
    url(r'^clientes/manutencao_consultar/(?P<id>\d+)/$',app.views.clientes_manutencao_consultar, name='clientes_manutencao_consultar'), # CONSULTAR DETALHES DO CLIENTE
    url(r'^clientes/manutencao_inserirCliente/$',app.views.inserir_cliente, name='inserir_cliente'), # INSERIR CLIENTE NO BANCO
    url(r'^clientes/manutencao_detalhes/(?P<id>\d+)/$',app.views.clientes_manutencao_detalhes, name='clientes_manutencao_detalhes'), # VIEW PARA REDIRECIONAR PARA ALTERAR OU DELETAR CLIENTES
    url(r'^clientes/manutencao_editar/(?P<id>\d+)/$',app.views.clientes_manutencao_editar, name='clientes_manutencao_editar'), # VIEW PARA ALTERAR CLIENTES
    url(r'^clientes/manutencao_deletar/(?P<id>\d+)/$',app.views.clientes_manutencao_deletar, name='clientes_manutencao_deletar'), # VIEW PARA DELETAR CLIENTES
    url(r'^clientes/get_cidades_json/$',app.views.get_cidades_json, name='get_cidades_json'),  # GET CIDADES DO BANCO by JSON
    url(r'^clientes/get_estados_json/$',app.views.get_estados_json, name='get_estados_json'),  # GET ESTADOS DO BANCO by JSON
    url(r'^representacoes/manutencao/$',app.views.repres_manutencao, name='repres_manutencao'), # GET TELA MANUTENÇÃO REPRESENTACOES
    url(r'^representacoes/manutencao_inserir/$',app.views.repres_manutencao_inserir, name='repres_manutencao_inserir'), # GET TELA INSERIR REPRESENTACAO
    url(r'^representacoes/manutencao_inserirRepres/$',app.views.inserir_repres, name='inserir_repres'), # INSERIR REPRESENTAÇÃO NO BANCO
    url(r'^representacoes/manutencao_consultar/(?P<id>\d+)/$',app.views.repres_manutencao_consultar, name='repres_manutencao_consultar'), # CONSULTAR DETALHES DA REPRESENTACAO
    url(r'^representacoes/manutencao_detalhes/(?P<id>\d+)/$',app.views.repres_manutencao_detalhes, name='repres_manutencao_detalhes'), # VIEW PARA REDIRECIONAR PARA ALTERAR OU DELETAR REPRESENTACAO
    url(r'^representacoes/manutencao_deletar/(?P<id>\d+)/$',app.views.repres_manutencao_deletar, name='repres_manutencao_deletar'), # VIEW PARA DELETAR CLIENTES
    url(r'^produtos/manutencao/$',app.views.produtos_manutencao, name='produtos_manutencao'), # GET TELA MANUTENÇÃO PRODUTOS
    url(r'^produtos/manutencao_inserir/$',app.views.produtos_manutencao_inserir, name='produtos_manutencao_inserir'), # GET TELA INSERIR PRODUTOS  
    url(r'^produtos/manutencao_inserirProduto/$',app.views.inserir_produtos, name='inserir_produtos'), # INSERIR PRODUTO NO BANCO
    url(r'^produtos/manutencao_detalhes/(?P<id>\d+)/$',app.views.produtos_manutencao_detalhes, name='produtos_manutencao_detalhes'), # VIEW PARA REDIRECIONAR PARA ALTERAR OU DELETAR PRODUTOS
    url(r'^produtos/manutencao_consultar/(?P<id>\d+)/$',app.views.produtos_manutencao_consultar, name='produtos_manutencao_consultar'), # CONSULTAR DETALHES DO CLIENTE
    url(r'^produtos/manutencao_deletar/(?P<id>\d+)/$',app.views.produtos_manutencao_deletar, name='produtos_manutencao_deletar'), # VIEW PARA DELETAR CLIENTES
    url(r'^produtos/get_representacoes_json/$',app.views.get_representacoes_json, name='get_representacoes_json'),  # GET REPRESENTACOES DO BANCO by JSON
    url(r'^pedidos/inserir_pedido/$',app.views.inserir_pedidos,name='inserir_pedidos'),  # INSERIR PEDIDO NO SISTEMA
    url(r'^pedidos/manutencao/$',app.views.pedidos_manutencao, name='pedidos_manutencao'), # GET TELA MANUTENÇÃO PEDIDOS    
    url(r'^pedidos/manutencao_inserir/$',app.views.pedidos_manutencao_inserir, name='pedidos_manutencao_inserir'), # GET TELA INSERIR PEDIDO
    url(r'^pedidos/manutencao_consultar/(?P<id>\d+)/$',app.views.pedidos_manutencao_consultar, name='pedidos_manutencao_consultar'), # CONSULTAR DETALHES DO CLIENTE
    url(r'^pedidos/get_produtos_by_repres_json/$',app.views.get_produtos_by_repres_json, name='get_produtos_by_repres_json'),  # GET CIDADES DO BANCO by JSON
    url(r'^prazos/controle/$',app.views.prazos_manutencao, name='prazos_manutencao'), # GET TELA CONTROLE PRAZOS, 
    url(r'^prazos/inserir_prazo/$',app.views.inserir_prazo,name='inserir_prazo'),  # INSERIR PEDIDO NO SISTEMA
    url(r'^prazos/get_prazo_by_id/$',app.views.get_prazo_by_id, name='get_prazo_by_id'),  # GET PRAZO DO BANCO by JSON
    url(r'^prazos/deletar_prazo/$',app.views.deletar_prazo, name='deletar_prazo'),  # DELETAR PRAZO DO BANCO
    url(r'^prazos/manutencao_editar/$',app.views.prazo_manutencao_editar, name='prazo_manutencao_editar'), # VIEW PARA ALTERAR PRAZOS
    url(r'^login/$', 
        django.contrib.auth.views.login,   
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
