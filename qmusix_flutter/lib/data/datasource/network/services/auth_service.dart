import 'dart:convert';

import 'package:dio/dio.dart';
import 'package:qmusix/data/datasource/network/params/change_password_param.dart';
import 'package:qmusix/data/datasource/network/params/login_param.dart';

class AuthService {
  final Dio _dio;

  AuthService(this._dio);

  Future<void> login(LoginParam request) async {
    try {
      final response = await _dio.post(
        '/login',
        data: request.toJson(),
      );

      jsonDecode(response.data);
    } on DioException catch (_) {
      rethrow;
    } catch (e) {
      throw Exception('Unknown error');
    }
  }

  Future<void> register(LoginParam params) async {
    try {
      final response = await _dio.post(
        '/register',
        data: params.toJson(),
      );

      jsonDecode(response.data);
    } catch (e) {
      throw Exception('Unknown error');
    }
  }

  Future<void> changePassword(ChangePasswordParam params) async {
    try {
      final response = await _dio.put(
        '/register',
        data: params.toJson(),
      );

      jsonDecode(response.data);
    } catch (e) {
      throw Exception('Unknown error');
    }
  }
}
