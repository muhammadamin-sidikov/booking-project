import random
from django.utils import timezone
from django.core.mail import send_mail
from .models import EmailVerification

def send_verification_code(email):
    code = random.randint(100000, 999999)

    # Agar shu email bo‘yicha eski yozuv bo‘lsa, uni yangilaymiz
    obj, created = EmailVerification.objects.update_or_create(
        email=email,
        defaults={'code': code, 'created_at': timezone.now()}
    )

    send_mail(
        'Tasdiqlash kodi',
        f'Sizning tasdiqlash kodingiz: {code}',
        'muhammadaminsidiko6@gmail.com', [email]
    )
    return code
