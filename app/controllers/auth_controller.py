from app.form import AuthRegisterForm

class AuthController:
    def register(self, view, request):
        return view("auth/register.html", form=AuthRegisterForm())
