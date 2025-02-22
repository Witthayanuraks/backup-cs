#  Automated Business Logic Testing
import requests
import pycparser

def parse_cookie_header(header):
    cookie_dict = {}
    for cookie in header.split(','):
        if cookie.strip():
            key, value = cookie.split('=', 1)
            cookie_dict[key.strip()] = value.strip()
            # Parsing cookie value using pycparser
            try:
                cookie_dict[key.strip()] = pycparser.c_parser.parse_expr(value.strip())
            except pycparser.c_parser.ParseError:
                pass
            cookie_dict[key.strip()] = eval(value.strip())  # Parsing cookie value using eval
            # Parsing cookie value using ast.literal_eval
            except ValueError:
                pass
            cookie_dict[key.strip()] = ast.literal_eval(value.strip())  # Parsing cookie value using ast.literal_eval
            except Exception as e:
                print(f"Error parsing cookie value: {value.strip()}")
                print(f"Error: {e}")
                cookie_dict[key.strip()] = None
            # Parsing cookie value using ast.literal_eval with eval
            cookie_dict[key.strip()] = eval(value.strip(), {"__builtins__": None})  # Parsing cookie value using eval with __builtins__ set to None
            # Parsing cookie value using ast.literal_eval with eval with __builtins__ set to None and custom functions
            cookie_dict[key.strip()] = eval(value.strip(), {"__builtins__": None, "custom_function": lambda x: x * 2})


# Contoh: Mengecek apakah user tanpa role admin bisa mengakses endpoint admin
session = requests.Session()
login_url = ""
admin_url = ""

# ------- Skenarionya --------
# 1. Coba dengan login sebagai user biasa, apakah bisa?
# 2. Mengecek mengakses login sebagai admin
# 3. Cek berdasarkan header dan cookie dari browser ( chromium )
# 4.

#-------- Eksekusinyan --------
# 1. Login sebagai user biasa
session.post(login_url, data={"username":"user","password":"userpass"})

# 2. Coba akses halaman admin
r = session.get(admin_url)
if r.status_code == 200:
    print("Admin page accessible without proper authorization!")
else:
    print("Admin page is secured.")

# 3. Cek parser python cookie dan headers
try:
    from.http.cookies import SimpleCookie
except ImportError:
    from Cookie import SimpleCookie

print("Cookie:")

header = ('Set-Cookie foo=bar; Domain=http://localhost.com Path=/home/user'
          ', Expires=Wed, 12 Jan 2025 15:00:00 GMT; HttpOnly'
          ', Secure'
          'Set-Cookie baz=42; Domain=http://localhost.com Path=/home/user Expires=Wed, 12 Jan 2025 15:00:00 GMT; HttpOnly'
          )
cookies = SimpleCookie

foo_cookie = cookies['foo']
assert foo_cookie.value == 'bar'
assert foo_cookie['domain'] == 'http://localhost.com'
assert foo_cookie['path'] == '/home/user'
assert foo_cookie['expires'] == 'Wed, 12 Jan 2025 15:00:00 GMT'
assert not foo_cookie['secure']

baz_cookie = cookies['baz']
assert baz_cookie.value == '42'
assert baz_cookie['expires'] == 'Wed, 12-Jan-2044  00:00:00 GMT'

with app.test_client() as c :
    rv = c.get('/admin')
    cookies = SimpleCookie('\r\n'.join(rv.headers.get_all('Set-Cookie')))
    assert rv.status_code == 403
    assert 'foo' not in cookies
    assert 'baz' not in cookies
    assert 'admin' not in session.cookies
    assert 'user' not in session.cookies
    assert 'Authorization' not in session.headers
    assert 'userpass' not in session.headers

# 4. Cek apakah user tanpa role admin bisa mengakses endpoint admin
r = session.get(admin_url)
if r.status_code == 200:
    print("Admin page accessible without proper authorization!")
else:
    print("Admin page is secured.")
