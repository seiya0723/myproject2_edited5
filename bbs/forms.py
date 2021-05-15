from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model     = Topic
        fields   = [ "title","comment","price","salary","spending","pay_dt" ] #←modelsにカラムを追加したら判定するものはこちらに追加。

#バリデーションOKになるには

"""
1、fieldsの内容が不足なくテンプレートのフォームから入力されていること(スペルミスも不足に含める)
2、継承元のモデルで指定したルールに、フォームから入力された内容が従っているかどうか

1かつ2の場合に限り、バリデーションOKと出る。



フォームクラスののfieldsにはないnameが指定された場合、バリデーション結果には影響しない

"""
