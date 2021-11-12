from django.urls                                                    import path

from .views                                                         import HomeView, ContactView, \
                                                                        AboutView, Kaps404View

app_name = "home"

urlpatterns = [

    path('',                                            HomeView.as_view(),                 name="home"),
    path('contact/',                                    ContactView.as_view(),              name="contact"),
    path('about/',                                      AboutView.as_view(),                name="about"),
    path('404/',                                        Kaps404View.as_view(),              name='404'),
]