from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user

from flask_app import db
from flask_app.community.forms import PostForm
from flask_app.models import Post, User
from sqlalchemy import desc

import datetime

community_bp = Blueprint("community", __name__, url_prefix="/community")


@community_bp.route("/")
@login_required
def index():
    return render_template("community.html", title="Community")  # not implemented


@community_bp.route("/forum", methods=["GET", "POST"])
@login_required
def forum():
    form = PostForm()

    if form.validate_on_submit():
        post = Post(
            title=form.title.data,
            contents=form.content.data,
            date=datetime.datetime.today(),
            user_id=current_user.id,
            author=current_user,
        )
        form.title.data = " "
        form.content.data = " "
        try:
            db.session.add(post)
            db.session.commit()
            flash(f"Your post has been published!", "success")
        except Exception as e:
            db.session.rollback()
            flash(f"Error, unable to post", "error")
            return redirect(url_for("community.forum"))
    return render_template(
        "forum.html",
        form=form,
        posts=Post.query.order_by(Post.date.desc()).all(),
        title="Forum",
        USER=User,
    )
