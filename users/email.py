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
