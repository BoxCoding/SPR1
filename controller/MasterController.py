from flask import jsonify, request, Blueprint, abort
import datetime as dt
from bson import ObjectId,DBRef,Decimal128
import json
from model.schema.master.UserTypeMaster import UserTypeMaster, RestrictDate
from model.schema.master.StateMaster import StateMaster, StateRestrictDate
from model.schema.master.CityMaster import CityMaster, CityRestrictDate
from model.schema.master import LocalityMaster
from umongo import ValidationError

master_api = Blueprint('master_api', __name__)

no_pass_schema = RestrictDate()


def dump_user_no_pass(u):
    return no_pass_schema.dump(u)


@master_api.route('/m/usertype', methods=['POST'])
def add_usertype():
    payload = request.get_json()
    if payload is None:
        abort(400, 'Request body must be json with Content-type: application/json')
    try:
        payload['created_date'] = dt.datetime.utcnow()
        usertype = UserTypeMaster(**payload)
        usertype.commit()
    except ValidationError as ve:
        resp = jsonify(message=ve.args[0])
        resp.status_code = 400
        return resp
    return jsonify(dump_user_no_pass(usertype))


def _to_objid(data):
    try:
        return ObjectId(data)
    except Exception:
        return None


def _to_intid(data):
    try:
        return int(data)
    except Exception:
        return None


def _name_or_id_lookup(usertype):
    return {'$or': [{'name': usertype}, {'_id': _to_objid(usertype)}]}


@master_api.route('/m/usertype', methods=["GET", "DELETE"])
def get_usertype():
    usertype = request.args.get('typename')
    userType = UserTypeMaster.find_one(_name_or_id_lookup(usertype))
    if not userType:
        abort(404)
    if request.method == "DELETE":
        try:
            userType.delete()
        except ValidationError as ve:
            resp = jsonify(message=ve.args[0])
            resp.status_code = 400
            return resp
        return 'Ok'
    return jsonify(dump_user_no_pass(userType))


@master_api.route('/m/state', methods=['POST'])
def add_state():
    payload = request.get_json()
    if payload is None:
        abort(400, 'Request body must be json with Content-type: application/json')
    try:
        payload['created_date'] = dt.datetime.utcnow()
        statename = StateMaster(**payload)
        statename.commit()
    except ValidationError as ve:
        resp = jsonify(message=ve.args[0])
        resp.status_code = 400
        return resp
    return jsonify(dump_user_no_pass(statename))


@master_api.route('/m/states', methods=['POST'])
def add_states():
    payloads = request.get_json()
    print(type(payloads))
    if payloads is None:
        abort(400, 'Request body must be json with Content-type: application/json')
    state_name = []
    for payload in payloads:
        try:
            payload['created_date'] = dt.datetime.utcnow()
            statename = StateMaster(**payload)
            statename.commit()
            state_name.append(dump_user_no_pass(statename))
        except ValidationError as ve:
            resp = jsonify(message=ve.args[0])
            resp.status_code = 400
            return resp
    return jsonify(state_name)


no_pass_schemastate = StateRestrictDate()


def dump_state_master(u):
    return no_pass_schemastate.dump(u)


def _statename_or_id_lookup(statename):
    return {'$or': [{'name': statename}, {'_id': _to_objid(statename)}, {'state_id': _to_intid(statename)}]}


@master_api.route('/m/states', methods=["GET", "DELETE"])
def get_statename():
    statename = request.args.get('state')
    if statename == "all":
        state_name = []
        stateName = StateMaster.find()
        for state in stateName:
            state_name.append(dump_state_master(state))
        return jsonify(state_name)
    else:
        stateName = StateMaster.find_one(_statename_or_id_lookup(statename))
        if not stateName:
            abort(404)
        if request.method == "DELETE" and statename != "all":
            try:
                stateName.delete()
            except ValidationError as ve:
                resp = jsonify(message=ve.args[0])
                resp.status_code = 400
            return resp
        return jsonify(StateMaster.dump(stateName))


@master_api.route('/m/state', methods=['GET', 'DELETE'])
def get_state():
    result=None
    response=None
    if 'state_id' in request.args.keys():
        state_id = request.args.get('state_id')
        print(type(state_id))
        result = StateMaster.find_one({'state_id':int(state_id)})
    elif 'state_name' in request.args.keys():
        state_name = request.args.get('state_name')
        if state_name == 'all':
            state_name = []
            result = StateMaster.find()
            for state in result:
                state_name.append(StateMaster.dump(state))
            result=state_name
            return jsonify({'response': state_name}), 200
        else:
            result = StateMaster.find_one({'name': state_name})
    if not result:
        abort(404)
    response=StateMaster.dump(result)
    return jsonify({'response':response}), 200




no_pass_city_master = CityRestrictDate()


def dump_city_master(u):
    return no_pass_city_master.dump(u)


def _cityname_or_id_lookup(city):
    return {'$or': [{'name': city}, {'_id': _to_objid(city)}, {'city_id': _to_intid(city)}]}


@master_api.route('/m/city', methods=['POST'])
def add_city():
    payload = request.get_json()
    if payload is None:
        abort(400, 'Request body must be json with Content-type: application/json')
    city_id=payload['city_id']
    city_name=payload['name']
    city = CityMaster.find_one(_cityname_or_id_lookup(city_id))
    print(city)
    if city is not None:
        if city['name'] == city_name:
            return jsonify({"result":"city  already exist"}),409
        else:
            return jsonify({"result": "city  id  already in used"}),409
    state_name = payload['state']
    try:
        statename = StateMaster.find_one(_statename_or_id_lookup(state_name))
        """if statename is None:
            abort(301,"StateName not found")"""
        print(statename)
        payload['state'] = int(statename['state_id'])
        print(payload['state'])
        payload['created_date'] = dt.datetime.utcnow()
        cityName = CityMaster(**payload)
        cityName.commit()
    except ValidationError as ve:
        resp = jsonify(message=ve.args[0])
        resp.status_code = 400
        return resp
    return jsonify({'result': CityMaster.dump(cityName)})


"""def dump_city_master(u):
    return no_pass_city_master.dump(u)"""


def _localityname_or_id_lookup(loc,label):
    return {'$or': [{'name': loc}, {'_id': _to_objid(loc)}, {f'{label}_id': _to_intid(loc)}]}


@master_api.route('/m/loc', methods=['POST'])
def add_locality():
    payload = request.get_json()
    if payload is None:
        abort(400, 'Request body must be json with Content-type: application/json')
    locality_id=payload['locality_id']
    locality=payload['name']
    locality = LocalityMaster.find_one(_localityname_or_id_lookup(locality_id, 'locality'))
    print(locality)
    if locality is not None:
        if locality['name'] == locality:
            return jsonify({"result":"Locality  already exist"}),409
        else:
            return jsonify({"result": "Locality  id  already in used"}),409
    city_name = payload['city']
    try:
        city = CityMaster.find_one(_cityname_or_id_lookup(city_name))
        """if statename is None:
            abort(301,"StateName not found")"""
        print(city)
        payload['city'] = int(city['city_id'])
        print(payload['city'])
        payload['created_date'] = dt.datetime.utcnow()
        locality = LocalityMaster(**payload)
        locality.commit()
    except ValidationError as ve:
        resp = jsonify(message=ve.args[0])
        resp.status_code = 400
        return resp
    return jsonify({'result': LocalityMaster.dump(locality)}),200



"""@master_api.route('/m/city', methods=['POST'])
def add_states():
    payloads = request.get_json()
    print(type(payloads))
    if payloads is None:
        abort(400, 'Request body must be json with Content-type: application/json')
    state_name = []
    for payload in payloads:
        try:
            payload['created_date'] = dt.datetime.utcnow()
            statename = StateMaster(**payload)
            statename.commit()
            state_name.append(dump_user_no_pass(statename))
        except ValidationError as ve:
            resp = jsonify(message=ve.args[0])
            resp.status_code = 400
            return resp
    return jsonify(state_name)


no_pass_schemastate = StateRestrictDate()


def dump_city_master(u):
    return no_pass_schemastate.dump(u)


@master_api.route('/m/states', methods=["GET", "DELETE"])
def get_statename():
    statename = request.args.get('state')
    if statename == "all":
        state_name = []
        stateName = StateMaster.find()
        for state in stateName:
            state_name.append(dump_state_master(state))
        return jsonify(state_name)
    else:
        stateName = StateMaster.find_one(_name_or_id_lookup(statename))
        if not stateName:
            abort(404)
        if request.method == "DELETE" and statename != "all":
            try:
                stateName.delete()
            except ValidationError as ve:
                resp = jsonify(message=ve.args[0])
                resp.status_code = 400
            return resp
        return jsonify(StateMaster.dump(stateName))
"""
