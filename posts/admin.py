from django.contrib import admin
from django.utils.safestring import mark_safe
from posts.models import Post, Comment


@admin.register(Post) #@를 붙이면 데코레이터
class Postadmin(admin.ModelAdmin): 
    list_display = ['title', 'content', 'image_tag']   #image가 화면에 보이게하려면 method로 넣어서 보이게해야함.보안상 장고가 막아두기때문

    def image_tag(self, post):
        if not post.image: 
            return mark_safe(f"<img src='' style = 'width: 500px'/>") #보안상 막아둔거 푸는작업


        return mark_safe(f"<img src={post.image.url} style = 'width: 500px'/>") #보안상 막아둔거 푸는작업
    
admin.site.register(Comment)
