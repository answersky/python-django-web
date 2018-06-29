#项目启动命令;
    python manage.py runserver 0.0.0.0:8000

#访问地址：
    http://localhost:8000/login

#静态文件：
    放在static目录下
    配置：
        STATIC_URL = '/static/'
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR,'static'),
        ]
    页面访问方式 static/css/loaders.css