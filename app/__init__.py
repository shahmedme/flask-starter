from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    with app.app_context():
        from .general.views import general_bp
        from .blog.views import blog_bp
        from .admin.views import admin_bp

        app.register_blueprint(general_bp)
        app.register_blueprint(blog_bp, url_prefix='/blog')
        app.register_blueprint(admin_bp, url_prefix='/admin')

        return app