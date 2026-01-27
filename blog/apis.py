from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from blog.models import Post
from blog.serializers import PostSerializer

# GET - read
# PUT - update
# POST - receive
# DELETE - delete

@api_view(['GET'])
def all_posts(request: Request):

    print(request.user)
    
    posts = Post.objects.all()
    serialized_posts = PostSerializer(posts, many=True)
    data = serialized_posts.data
    
    # data = PostSerializer(Post.objects.all(), many=True).data
    # 
    return Response(data)
