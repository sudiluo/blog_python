import os
import pymysql

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'svjp5(e4rw)zt3#z9p#_x%p(5d^twu0-i(_y!34e5f3y)#$tp('

DEBUG = True

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = [
    # 'grappelli', # 美化库 必须在'django.contrib.admin'之前
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'haystack',
    'blog',
    'comments',
    'users',
    'backstage',
]

# ENGINE 指定了 django haystack 使用的搜索引擎
# PATH 指定了索引文件需要存放的位置
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'blog.whoosh_cn_backend.WhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    },
}
# 指定如何对搜索结果分页，这里设置为每 10 项结果为一页
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
# 作用是每当有文章更新时就更新索引。由于博客文章更新不会太频繁，因此实时更新没有问题。
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # 'web_base.SimpleMiddleware.SimpleMiddleware'
]

ROOT_URLCONF = 'ulife.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ulife.wsgi.application'

# mysql5.0以上版本支持三种sql_mode模式：ANSI、TRADITIONAL和STRICT_TRANS_TABLES。
# ANSI模式：宽松模式，对插入数据进行校验，如果不符合定义类型或长度，对数据类型调整或截断保存，报warning警告。
# TRADITIONAL模式：严格模式，当向mysql数据库插入数据时，进行数据的严格校验，保证错误数据不能插入，报error错误。用于事物时，会进行事物的回滚。
# STRICT_TRANS_TABLES模式：严格模式，进行数据的严格校验，错误数据不能插入，报error错误
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'python_test',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/
# 把英文改为中文
LANGUAGE_CODE = 'zh-hans'
# 把国际时区改为中国时区
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/backstage/signin/'
# session设置
SESSION_COOKIE_NAME = "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）

SESSION_COOKIE_PATH = "/"  # Session的cookie保存的路径（默认）

SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）

SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）

SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）

SESSION_COOKIE_AGE = 60 * 30  # Session的cookie失效日期（2周）（默认）

SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）

SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存（默认）

# 配置自定义user
AUTH_USER_MODEL = 'users.User'
# 配置 Backend  对用户的凭据信息进行验证
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'users.backends.EmailBackend',
)
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# 关联根目录和 static 文件夹
STATIC_URL = '/static/'
STATIC_ROOT = (os.path.join(BASE_DIR, 'static'))

# 上传图片
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
# MEDIA_URL = '/media/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/" #把admin的静态文件,由原来的admin目录,改为映射到static目录下的
