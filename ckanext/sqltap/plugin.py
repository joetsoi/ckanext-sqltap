from ckan import plugins
from ckan.plugins import toolkit

from sqltap.wsgi import SQLTapMiddleware


class SqltapPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IMiddleware, inherit=True)

    def make_error_log_middleware(self, app, config):
        if toolkit.asbool(config.get('debug', False)):
            app = SQLTapMiddleware(app)
        return app
