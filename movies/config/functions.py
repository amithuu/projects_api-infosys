from datetime import datetime
from hashlib import sha224
from random import randint, shuffle
from datetime import datetime
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
import math, random
from django.utils.text import slugify

# from users.models import OtpLog, CustomUser

# def generate_token(email = ''):
#         token = ''
#         try: 
#             alpha = [c for c in 'abcdefghijklmnopqrstuwxyz']
#             shuffle(alpha)
#             word = ''.join([a for a in alpha if randint(0, 1) == 1])
#             token = str(sha224(bytes(email + str(datetime.now()) + str(randint(1000, 9999)) + word, 'utf-8')).hexdigest())
#             return token
#         except Exception:
#             return token

# def generate_otp() :
#     digits = "0123456789"
#     OTP = str(random.randint(1, 9))
#     for i in range(5) :
#         OTP += str(digits[math.floor(random.random() * 10)])
#     return OTP

# def send_otp_email(email):
#         token = None
#         try:
#             url = settings.FRONTEND_URL
#             token = generate_token(email=email)
#             otp = generate_otp()
#             print(otp)
#             subject, from_email = 'Verify your email', settings.EMAIL_HOST_USER
#             text_content = ''
#             html_content = render_to_string('email/verification_email.html', {'email': email, 'url': url, 'otp': otp})
#             mail = EmailMultiAlternatives(subject, text_content, from_email, [email])
#             mail.attach_alternative(html_content, "text/html")
#             mail.send()
#             create_otp_log(token=token, email=email, otp=otp, type='email_otp')
#             return token
#         except Exception:
#             return token  

# def create_otp_log(user = None, email = None, otp = None, token = None, type = None, country_code = None, contact = None):
#         OtpLog.objects.filter(email=email).delete()
#         otp_log = OtpLog.objects.create(
#             user = user, 
#             email = email, 
#             otp = otp, 
#             token = token, 
#             type = type, 
#             country_code = country_code, 
#             contact = contact
#         )
#         return otp_log

# def generate_unique_username(name:str):
#         unique_username = slugify(name)
#         num = 1
#         while CustomUser.objects.filter(username=unique_username).exists():
#             unique_username = '{}-{}'.format(unique_username, num)
#             num += 1
#         return unique_username

def remove_item_from_list(key:str, list:list):
        if key in list:
            list.remove(key)
        return list
