from django.urls                                        import path, include


urlpatterns = [
    path('',                                    include('kapshop.apps.web.urls')),
    #path('api/',                                include('kapshop.apps.api.urls')),
    #path('autocomplete/',                       include('kapshop.apps.autocomplete.urls')),
]
