def new_password(oldpassword, newpassword):
    if newpassword != oldpassword and len(newpassword) >= 6:
        oldpassword = newpassword