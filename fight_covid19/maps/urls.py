from django.urls import path
from fight_covid19.maps import views as map_views
from django.views.generic import TemplateView


urlpatterns = [
    path("", TemplateView.as_view(template_name="maps/maps.html"), name="home"),
    path(
        "wellness_entry_form/", map_views.WellnessEntryCreateView, name="wellness_entry"
    ),
    path("my_health", map_views.MyHealthView, name="my_health"),
]
