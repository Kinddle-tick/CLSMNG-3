from django import forms


from .models import  FeedBack, OrderModel

# class TopicForm(forms.ModelForm):
#     class Meta:
#         model = Topic
#         fields = ['text']
#         labels = {'text': ''}
#
# class EntryForm(forms.ModelForm):
#     class Meta:
#         model = Entry
#         fields = '__all__'
#         labels = {'text': '',
#                   'test':'test'
#                   }
#         widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class FeedBackForm1(forms.ModelForm):
    text = forms.CharField(
        label='jubao',
        max_length=64,
        widget=forms.widgets.TextInput(attrs={'class': 'form-control'})
    )
    reason = forms.ModelChoiceField(
        label='reason',
        queryset=FeedBack.objects.all(),
        widget=forms.widgets.Select(attrs={'class':'form-control'})
    )
    class Meta:
        model = FeedBack
        fields = ['text']
        labels = {'text': ''}

# class FeedBackForm(forms.ModelForm):
#     class Meta:
#         model = FeedBack
#         fields = '__all__'
#         labels = {
#             'reason':'reason',
#             'text':'text'
#         }

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'
        labels = {
            '申请教室':'申请教室',
            '申请时间':'申请时间',
            '申请理由': '申请理由',
            '申请单位': '申请单位',
            '是否可拼教室': '是否可拼教室',
        }