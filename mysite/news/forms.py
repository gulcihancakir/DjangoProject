from django import forms

from .models import News,Category,Comment



class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ('id',  'name',)


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'context',  'image',  'category',  'created_date',  'published_date',)

class CommentsForm(forms.ModelForm):
  
        
    class Meta:
        model=Comment
        fields=('text','name',)

   


