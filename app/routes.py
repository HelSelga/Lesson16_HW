from flask import current_app as app, jsonify, request, abort
from app.models import *


@app.route('/users', methods=['GET'])
def get_all_users():
    users = db.session.query(User).all()
    return jsonify([user.self_to_dict_user() for user in users])


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return {}, 200


@app.route('/users/<int:uid>', methods=['GET'])
def get_one_user(uid):
    user = db.session.query(User).get(uid)
    if user is None:
        return abort(404)
    return jsonify(user.self_to_dict_user())


@app.route('/users/<int:uid>', methods=['PUT'])
def update_user(uid):
    data = request.json
    user = db.session.query(User).filter(User.id == uid).first()
    if user is None:
        return abort(404)
    user_updated = db.session.query(User).filter(User.id == uid).update(data)
    db.session.add(user_updated)
    db.session.commit()
    db.session.close()
    return {}, 204


@app.route('/users/<int:uid>', methods=['DELETE'])
def delete_user(uid):
    result = db.session.query(User).filter(User.id == uid).delete()
    if result == 0:
        abort(404)
    db.session.commit()
    return jsonify(""), 204


@app.route('/orders', methods=['GET'])
def get_all_orders():
    orders = db.session.query(Order).all()
    return jsonify([order.self_to_dict_order() for order in orders])


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order = Order(**data)
    db.session.add(order)
    db.session.commit()
    return {}, 200


@app.route('/orders/<int:oid>', methods=['GET'])
def get_one_order(oid):
    order = db.session.query(Order).get(oid)
    if order is None:
        return abort(404)
    return jsonify(order.self_to_dict_order())


@app.route('/orders/<int:oid>', methods=['PUT'])
def update_order(oid):
    data = request.json
    order = db.session.query(Order).filter(Order.id == oid).first()
    if order is None:
        return abort(404)
    order_updated = db.session.query(Order).filter(Order.id == oid).update(data)
    db.session.add(order_updated)
    db.session.commit()
    db.session.close()
    return {}, 204


@app.route('/orders/<int:oid>/', methods=['DELETE'])
def delete_order(oid):
    result = db.session.query(Order).filter(Order.id == oid).delete()
    if result == 0:
        abort(404)
    db.session.commit()
    return jsonify(""), 204


@app.route('/offers', methods=['GET'])
def get_all_offers():
    offers = db.session.query(Offer).all()
    return jsonify([offer.self_to_dict_offer()for offer in offers])


@app.route('/offers', methods=['POST'])
def create_offer():
    data = request.json
    offer = Offer(**data)
    db.session.add(offer)
    db.session.commit()
    return {}, 200


@app.route('/offers/<int:ofid>', methods=['GET'])
def get_one_offer(ofid):
    offer = db.session.query(Offer).get(ofid)
    if offer is None:
        return abort(404)
    return jsonify(offer.self_to_dict_offer())


@app.route('/offers/<int:uid>', methods=['PUT'])
def update_offer(ofid):
    data = request.json
    offer = db.session.query(Offer).filter(Offer.id == ofid).first()
    if offer is None:
        return abort(404)
    offer_updated = db.session.query(Offer).filter(Offer.id == ofid).update(data)
    db.session.add(offer_updated)
    db.session.commit()
    db.session.close()
    return {}, 204


@app.route('/offers/<int:ofid>', methods=['DELETE'])
def delete_offer(ofid):
    result = db.session.query(Offer).filter(Offer.id == ofid).delete()
    if result == 0:
        abort(404)
    db.session.commit()
    return jsonify(""), 204
