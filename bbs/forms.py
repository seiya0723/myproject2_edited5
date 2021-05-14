from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model     = Topic
        #fields    = ['comment',]
        fields   = [ "title","comment","price","salary","spending","pay_dt" ] #←modelsにカラムを追加したら判定するものはこちらに追加。
