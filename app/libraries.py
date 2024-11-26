from flask import Flask, render_template, send_from_directory, abort, redirect, url_for, request, session, flash,jsonify
from werkzeug.utils import secure_filename
from flask_pymongo import PyMongo
from flask_login import current_user, login_user, login_required, logout_user, LoginManager, UserMixin
from flask_mail import Mail, Message
from app.database.db import save_user, get_user, User,MONGO_URI,save_song, search_song,songs_collection,get_all_songs
import os
from bson.objectid import ObjectId