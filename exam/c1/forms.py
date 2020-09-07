from django import forms

from c1.models import users4
from c1.models import dress
from c1.models import advisor
from c1.models import book10

from c1.models import feedback1

class advisorform(forms.ModelForm):
    class Meta():
        model = advisor
        fields = "__all__"


class userform(forms.ModelForm):
    class Meta():
        model = users4
        fields = "__all__"

class dressform(forms.ModelForm):
        class Meta():
             model = dress
             fields = "__all__"


class bookform(forms.ModelForm):
    class Meta():
        model = book10
        fields = "__all__"
class feedbackform(forms.ModelForm):
    class Meta():
        model = feedback1
        fields = "__all__"
