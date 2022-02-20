import jwt
import datetime
from django.conf import settings


def generate_access_token(user):
    payload = {
        'user_id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        "iat": datetime.datetime.now(tz=datetime.timezone.utc)
    }

    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
