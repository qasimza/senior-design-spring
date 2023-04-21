# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectMultipleField, DecimalField, BooleanField, IntegerField
from wtforms.validators import Email, DataRequired, NumberRange

# login, registration and search fields


class LoginForm(FlaskForm):
    username = StringField('Username',
                         id='username_login',
                         validators=[DataRequired()])
    password = PasswordField('Password',
                             id='pwd_login',
                             validators=[DataRequired()])


class CreateAccountForm(FlaskForm):
    username = StringField('Username',
                         id='username_create',
                         validators=[DataRequired()])
    email = StringField('Email',
                      id='email_create',
                      validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                             id='pwd_create',
                             validators=[DataRequired()])
    
class PerformSearchFrom(FlaskForm):
    
    # Prelimnary Search Options
    song_title = StringField('Songtitle', id='song_title')
    artist = StringField('Artist', id='artist')
    year = DateField('Year', id='year', format='%Y')
    genres = SelectMultipleField('Genre', choices=['', 'pop', 'rock', 'indie', 'metal', 'hip hop', 'rap', 'jazz', 'deep', 'folk', 'punk', 'classical', 'house',
          'classic', 'alternative', 'german', 'trap', 'swedish', 'modern', 'italian', 'japanese', 'country', 'blues', 'russian', 'french', 'latin', 'soul', 'black', 'techno',
          'brazilian', 'music', 'finnish', 'funk', 'uk', 'piano', 'contemporary', 'australian', 'dutch', 'dance', 'death', 'reggae', 'experimental', 'r&b', 'spanish', 'traditional', 'trance'], id='genres')
    themes = SelectMultipleField('Themes', choices=['', 'Heartbreak', 'Inspirational', 'Motivational', 'Melencholic', 'Lullaby', 'Religious', 'Holiday', 'Desire', 'Rebellion', 'Death', 'Pain', 'Nostalgia', 'Loss', 'Jealousy'], id='themes')
    num_tracks = IntegerField('NumberOfTracks', id='num_tracks')
    
    # Advanced Search Options
    popularity = DecimalField('Popularity', id='popularity')
    danceability = DecimalField('Danceability', id='danceability')
    energy = DecimalField('Energy', id='energy')
    loudness = DecimalField('Loudness', id='loudness')
    speechiness = DecimalField('Speechiness', id='speechiness')
    acoustics = DecimalField('Acoustics', id='acoustics')
    instrumentalness = DecimalField('Instrumentalness', id='instrumentalness')
    liveness = DecimalField('Liveness', id='liveness')
    valence = DecimalField('Valence', id='valence')
    tempo = DecimalField('Tempo', id='tempo')
    explicit = BooleanField('Explicit', id='explicit')



   