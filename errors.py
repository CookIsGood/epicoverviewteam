from start import *


@application.errorhandler(404)
def error_404(error):
    return render_template('errors/error404.html'), 404


@application.errorhandler(413)
def request_entity_too_large(error):
    return render_template('errors/error404.html'), 413


@application.errorhandler(500)
def no_reply_from_server(error):
    return render_template('errors/error500.html'), 500
