from snippets.api.viewsets import SnippetViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('snippets',SnippetViewSet,basename='snippet')

# for url in router.urls:
#     print(url,'\n')