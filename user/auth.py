from fastapi_users.authentication import JWTAuthentication

SECRET = "Sdasdad3w#RmF34ef43%E5&*6DV%$5DSvBF*fY9V(y*&VNFdfBU(t8DnfDS"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)
