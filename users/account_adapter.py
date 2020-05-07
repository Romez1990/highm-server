from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.utils import user_email, user_username, user_field

from highm_server.settings import CLIENT_URL
from .models import User, Profile, Student, Teacher


class AccountAdapter(DefaultAccountAdapter):
    def new_user(self, request):
        return User()

    def save_user(self, request, user, form, commit=True):
        data = form.cleaned_data
        unregistered_user = data.get('unregistered_user')
        first_name = unregistered_user.first_name
        last_name = unregistered_user.last_name
        is_staff = unregistered_user.is_staff
        email = data.get('email')
        username = email
        user_email(user, email)
        user_username(user, username)
        user_field(user, 'first_name', first_name)
        user_field(user, 'last_name', last_name)
        user_field(user, 'is_staff', is_staff)
        if 'password1' in data:
            user.set_password(data['password1'])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            user.save()

        Profile.objects.create(user=user)

        if is_staff:
            Teacher.objects.create(user=user)
        else:
            Student.objects.create(user=user, group=unregistered_user.group)

        unregistered_user.delete()

        return user

    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        key = emailconfirmation.key
        activate_url = f'{CLIENT_URL}/confirm-email/{key}'
        ctx = {
            'user': emailconfirmation.email_address.user,
            'activate_url': activate_url,
            'current_site': current_site,
            'key': key,
        }
        if signup:
            email_template = 'account/email/email_confirmation_signup'
        else:
            email_template = 'account/email/email_confirmation'
        self.send_mail(email_template, emailconfirmation.email_address.email,
                       ctx)

    def render_mail(self, template_prefix, email, context):
        subject = render_to_string('{0}_subject.html'.format(template_prefix),
                                   context)
        # remove superfluous line breaks
        subject = " ".join(subject.splitlines()).strip()
        subject = self.format_email_subject(subject)

        from_email = self.get_from_email()

        template_name = '{0}_message.html'.format(template_prefix)
        body = render_to_string(template_name, context).strip()
        msg = EmailMessage(subject, body, from_email, [email])
        msg.content_subtype = 'html'
        return msg

    # def get_from_email(self):
    #     return 'HighM МИФИ'
