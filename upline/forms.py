from django import forms
from upline.models import *
from suit.widgets import AutosizedTextarea

class MemberRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Member
        fields = ('birthday','name','gender','phone')

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        widgets = {
            'note': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'})
        }
        fields = '__all__'
        exclude = ('members','invited')
    
class TrainingStepForm(forms.ModelForm):
    class Meta:
        widgets = {
            'description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_1_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_2_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_3_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_4_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_5_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_6_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_7_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_14_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'day_28_notification_description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }
        model = TrainingStep
        fields = '__all__'
        

class LevelForm(forms.ModelForm):
    class Meta:
        widgets = {
            'description': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
            'gift': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }
        model = Level
        fields = '__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

class MemberTrainingStepForm(forms.ModelForm):
    class Meta:
        widgets = {
            'answer': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }
        model = MemberTrainingStep
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        widgets = {
            'content': AutosizedTextarea(attrs={'rows': 3, 'class': 'input-xlarge'}),
        }
        model = Post
        fields = '__all__'
