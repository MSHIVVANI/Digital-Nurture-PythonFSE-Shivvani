# OAuth2 Authorization Code Flow

1. User clicks Login with Google.
2. Browser redirects to Google login page.
3. User authenticates with Google.
4. Google returns authorization code.
5. Backend exchanges code for access token.
6. Backend fetches user information.
7. User is logged in.

---

## Difference between OAuth2 and JWT Login

JWT Login:
- Username and password are verified directly.
- Application generates token itself.
- Simpler implementation.

OAuth2:
- Delegates authentication to another provider.
- Uses authorization code exchange.
- More secure and suitable for enterprise systems.