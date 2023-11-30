from djoser import email


class ActivationEmail(email.ActivationEmail):
    template_name = 'users/activation.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['domain'] = '127.0.0.1:3000'
        context['site_name'] = 'intouch'
        return context


class ConfirmationEmail(email.ConfirmationEmail):
    template_name = 'users/confirmation.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['domain'] = '127.0.0.1:3000'
        context['site_name'] = 'intouch'
        return context

class PasswordResetEmail(email.PasswordResetEmail):
    template_name = 'users/reset_password.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['domain'] = '127.0.0.1:3000'
        context['site_name'] = 'intouch'
        return context

class PasswordChangedConfirmationEmail(email.PasswordChangedConfirmationEmail):
    template_name = 'users/password_changed_confirmation.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['domain'] = '127.0.0.1:3000'
        context['site_name'] = 'intouch'
        return context
