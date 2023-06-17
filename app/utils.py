from passlib.context import CryptContext

# Here we are creating which method to use for hashing the password.
# Here we use bcrypt. We will later use this info to hash the passwords passed to us in our API calls.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)
