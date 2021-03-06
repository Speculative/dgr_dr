"""
# Copyright 2013 Jeffrey Tao, Maxwell Huang-Hobbs, William Saulnier, 2013
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Dgr_dr
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
"""

from app import app
from flask import render_template, request, redirect, url_for, send_from_directory
import os, random, string
import imageDecay
import pickle

ALLOWED_TYPES = [
    "png",
    "jpg",
    "jpeg",
    "gif"
    ]

APP_ROOT = os.environ["OPENSHIFT_REPO_DIR"] + "wsgi/app/"

@app.route('/')
@app.route('/index')
def index():
    images = [i.split(".thumbnail")[0] for i in os.listdir(APP_ROOT + "static/img") if i.endswith("thumbnail")]
    random.shuffle(images)
    im_dict = pickle.load(open(APP_ROOT + "static/im.p", "rb"))
    new_dict = {}
    for i in images[0:min(20, len(images))]:
        new_dict[i] = im_dict[i] if i in im_dict.keys() else 0
    return render_template("index.html", dic = new_dict)

@app.route('/views')
def get_views():
    im_dict = pickle.load(open(APP_ROOT + "static/im.p", "rb"))
    return str(im_dict)

@app.route('/upload', methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = make_filename(file.filename.split(".")[-1])
            file.save(os.path.join(APP_ROOT + "static/img/", filename))
            imageDecay.makeThumbnail(os.path.join(APP_ROOT + "static/img/", filename))
            return redirect("/")
        else:
            return "Bad Filetype Probably?"
        return "ok"
    else:
        return render_template("upload.html")

def allowed_file(filename):
    return filename.split(".")[-1] in ALLOWED_TYPES

def random_id(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for c in range(size))

def make_filename(extension):
    fileid = random_id() + "." + extension
    while os.path.isfile(APP_ROOT + "static/img/" + fileid):
        fileid = random_id() + "." + extension
    return fileid

@app.route('/<img_id>')
def view_image(img_id):
    inc_views(img_id)
    imageDecay.corruptImage(os.path.join(APP_ROOT, "static/img/") + img_id, 4)
    path = "/i/" + img_id
    return render_template("imgpage.html", img=path)

def inc_views(img_id):
    dic = pickle.load(open(APP_ROOT + "static/im.p", "rb"))
    if img_id in dic.keys():
        dic[img_id] += 1
    else:
        dic[img_id] = 1
    pickle.dump(dic, open(APP_ROOT + "static/im.p", "wb"))

@app.route('/i/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(APP_ROOT, "static/img/"), filename)
