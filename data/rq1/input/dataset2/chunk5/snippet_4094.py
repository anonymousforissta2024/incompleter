#Source: https://stackoverflow.com/questions/58135417/pyjwt-raises-typeerror
auth_token = user.encode_auth_token(user.id)
self.assertTrue(isinstance(auth_token, str))