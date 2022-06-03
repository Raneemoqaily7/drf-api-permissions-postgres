from rest_framework.generics import (
    ListCreateAPIView ,
    RetrieveUpdateDestroyAPIView,
                                    )
from blog.models import Article
from .permissions import IsOwnerOrReadOnly ,OwnerOnly,OwnerLogin

from .serializers import ArticleSerializer

class ArticleListView (ListCreateAPIView):
    queryset =Article.objects.all()
    serializer_class =ArticleSerializer
    permission_classes=(OwnerLogin, )

   
    



class ArticleDetailView (RetrieveUpdateDestroyAPIView):
    queryset =Article.objects.all()
    serializer_class =ArticleSerializer
    permission_classes=(OwnerOnly , )








