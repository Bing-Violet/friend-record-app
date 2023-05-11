from django.shortcuts import render
from rest_framework.views import APIView
from django.core.mail import EmailMessage, send_mail
from django.conf import settings
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import Http404
from django.utils.html import strip_tags
from django.template.loader import render_to_string
# import smtplib
# import ssl


class SendVerificationEmail:
    def __init__(self, request):
        self.rediredtURL = settings.VERIFICATION_URL
        self.token = request['verification_token']
        self.email_to = request["email"]
        self.title = "Thank you for your registration"
        self.message = f'''
        <html>
            <body style="display:flex; justify-content: center; bsckground: gray;">
                <div style="width:auto;margin:1rem;padding:1rem;border:solid gray;display:float; text-align:center;">
                    <h1>You're on your way!
                        Let's confirm your email address.
                    </h1>
                    <p  style="color: gray">
                        You're on your way!
                        Let's confirm your email address.
                        By clicking on the following link, you are confirming your email address.
                    </p>
                    <button style="display:block;margin:auto; padding:0.5rem; background:orange; border:solid naby; font-weight: bold;">
                        <a href="{self.rediredtURL+"/"+self.token}" style="text-decoration: none; color:darkblue;">
                            Confirm Email Address
                        </a>
                    </button>
                </div>
            </body>
        </html>
        '''
    def send(self):
        print("SENDEV")
        context = {}
        # token = request['verification_token']
        # refresh_token = request['refresh_token']
        # rediredtURL = settings.VERIFICATION_URL
        # message = render_to_string("templates/confirmation_email.html", context)
        # html_message = render_to_string("templates/confirmation_email.html", context)
        # message = f'''
        # <html>
        #     <body style="display:flex; justify-content: center; bsckground: gray;">
        #         <div style="width:auto;margin:1rem;padding:1rem;border:solid gray;display:float; text-align:center;">
        #             <h1>You're on your way!
        #                 Let's confirm your email address.
        #             </h1>
        #             <p  style="color: gray">
        #                 You're on your way!
        #                 Let's confirm your email address.
        #                 By clicking on the following link, you are confirming your email address.
        #             </p>
        #             <button style="display:block;margin:auto; padding:0.5rem; background:orange; border:solid naby; font-weight: bold;">
        #                 <a href="{rediredtURL+"/"+token}" style="text-decoration: none; color:darkblue;">
        #                     Confirm Email Address
        #                 </a>
        #             </button>
        #         </div>
        #     </body>
        # </html>
        # '''
        print("set",settings.EMAIL_HOST_USER,settings.EMAIL_HOST_PASSWORD )
        # email_to = request["email"]
        EmInstance = EmailMessage(
            self.title,
            self.message,
            settings.EMAIL_HOST_USER,
            [self.email_to],
        )
        try:
            EmInstance.content_subtype = "html"
            mail_sender = EmInstance.send(fail_silently=True)
            if mail_sender:
                return {"message":"successfully sent", "sent":True}
            else:
                return {"message":"couldn't send message", "sent":False}

        except Exception as e:
            return {"message":"something went wrong! couldn't send message", "sent":False}


class SendPasswordReset(SendVerificationEmail):
    def __init__(self, request):
        self.rediredtURL = settings.PASSWORD_CHANGE_URL
        self.token = request['verification_token']
        self.email_to = request["email"]
        self.title = request['title']
        self.message = f'''
        <html>
            <body style="display:flex; justify-content: center; bsckground: gray;">
                <div style="width:auto;margin:1rem;padding:1rem;border:solid gray;display:float; text-align:center;">
                    <h1>You're on your way!
                        Let's change your password.
                    </h1>
                    <p  style="color: gray">
                        You're on your way!
                        Let's change your password.
                        By clicking on the following link, you are confirming your email address.
                    </p>
                    <button style="display:block;margin:auto; padding:0.5rem; background:orange; border:solid naby; font-weight: bold;">
                        <a href="{self.rediredtURL+"/"+self.token}" style="text-decoration: none; color:darkblue;">
                            Change password
                        </a>
                    </button>
                </div>
            </body>
        </html>
        '''
