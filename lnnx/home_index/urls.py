from django.conf.urls import patterns, url

urlpatterns = patterns('lnnx.home_index.views',
    
    url(r'^$', 'index', name='index'),
    
)