from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="finance"),
    path('add-bilan', views.add_bilan, name="add-bilan"), 
    path('edit-bilan/<int:id>', views.bilan_edit, name="edit-bilan"),
    path('bilan-delete/<int:id>', views.delete_bilan, name="bilan-delete"),
    path('bilan_summary', views.bilan_summary, name="bilan_summary"),
    path('stats', views.stats_view, name="stats")
]