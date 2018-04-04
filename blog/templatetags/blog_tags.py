from ..models import Post, Category,Tag
from django import template
from django.db.models.aggregates import Count

# 实例化了一个 template.Library 类 用于自定义模板标签
register = template.Library()


# 修饰  这样就可以在模板中使用语法 {% get_recent_posts %} 调用这个函数了
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)