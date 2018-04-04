from django import forms
from .models import Comment


# 表单类 表单类必须继承自 forms.Form 类或者 forms.ModelForm 类
class CommentForm(forms.ModelForm):
    class Meta:
        #表明这个表单对应的数据库模型
        model = Comment
        #fields 表明表单需要显示的字段
        fields = ['name', 'email', 'url', 'text']
