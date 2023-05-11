"""
This is the module for handling requests related to pyduck.
"""

from http import HTTPMethod, HTTPStatus
from flask import Blueprint, render_template, g
from flow2and4.pyduck.auth.views import bp as bp_auth
from flow2and4.pyduck.community.views import bp as bp_community

bp = Blueprint(
    "pyduck",
    __name__,
    template_folder="templates",
    static_folder="static",
    url_prefix="/",
)
bp.register_blueprint(bp_auth)
bp.register_blueprint(bp_community)


@bp.errorhandler(HTTPStatus.NOT_FOUND)
def not_found_errorhandler(e):
    return render_template("pyduck/errors/404.html.jinja"), HTTPStatus.NOT_FOUND


bp.register_error_handler(HTTPStatus.NOT_FOUND, not_found_errorhandler)


@bp.route("/")
def index():
    """Show pyduck main index page."""

    return render_template("pyduck/index.html.jinja")
