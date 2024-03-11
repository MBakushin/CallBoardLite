from allauth.account.forms import SignupForm


class BasicSignupForm(SignupForm):
    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        user.save()
        return user
