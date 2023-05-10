from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('addproduct/', views.addproduct, name='addproduct'),
    path('addcommande/', views.addcommande, name='addcommande'),
    path('addfournisseur/', views.addfournisseur, name='addfournisseur'),
    path('search/', views.search, name='search'),
    path('Catalogue/', views.Catalogue, name='Catalogue'),
    path('produit/<int:produit_id>/', views.produit_detail, name='produit_detail'),
    path('categories/', views.categorie_list, name='categorie_list'),
    path('categorie/<int:categorie_id>/', views.categorie_detail, name='categorie_detail'),
    path('fournisseur/<int:fournisseur_id>/', views.fournisseur_detail, name='fournisseur_detail'),
    path('fournisseurs/', views.fournisseur_list, name='fournisseur_list'),
    path('commande/<int:commande_id>/', views.commande_detail, name='commande_detail'),
    path('commande/', views.commande_list, name='commande_list'),
    path('register/',views.register, name = 'register'), 
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
  
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
    path('contact/', views.contact, name='contact'),
]
