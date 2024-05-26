from app.auth import verify_password

def test_verify_password():
    hashed_password = "$2b$12$CdF17lV4vTVFLf.V5C9f1Ob4vTwPUG69i1b3Q6YgLopv3fJx.bXp6" # Hashed password for "password"
    assert verify_password("password", hashed_password) == True
    assert verify_password("wrongpassword", hashed_password) == False

