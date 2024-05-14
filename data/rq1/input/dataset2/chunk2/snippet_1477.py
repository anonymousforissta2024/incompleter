#Source: https://stackoverflow.com/questions/76454850/attributeerror-property-object-has-no-attribute-get-when-using-depends-in
def authenticate_request(request: Request) -> User:
    cookie1 = request.cookies.get("x")
    cookie2 = request.cookies.get("y")
    if cookie1 is not None and cookie2 is not None:
        tenant = get_tenant(request)
        if user := authenticate_cookies(cookie1, cookie2, tenant):
            if not tenant.startswith(user.tenant):
                print("Unauthorized: Token hostname mismatch")
                raise Exception("Token hostname mismatch")
            return user
    print("Unauthorized: please login")
    raise HTTPException(status_code=401, detail="Unauthorized: please login")