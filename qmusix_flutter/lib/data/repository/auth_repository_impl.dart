import 'package:qmusix/data/datasource/network/params/change_password_param.dart';
import 'package:qmusix/data/datasource/network/params/login_param.dart';
import 'package:qmusix/data/datasource/network/services/auth_service.dart';
import 'package:qmusix/domain/repository/auth_repository.dart';

class AuthRepositoryImpl implements AuthRepository {
  final AuthService _authService;

  AuthRepositoryImpl(this._authService);
  @override
  Future<void> login({
    required String username,
    required String password,
  }) async {
    await _authService.login(
      LoginParam(
        username: username,
        password: password,
      ),
    );
  }

  @override
  Future<void> register({
    required String username,
    required String password,
  }) async {
    await _authService.register(
      LoginParam(
        username: username,
        password: password,
      ),
    );
  }

  @override
  Future<void> changePassword({
    required String username,
    required String oldPassword,
    required String newPassword,
  }) async {
    await _authService.changePassword(
      ChangePasswordParam(
        userName: username,
        oldPassword: oldPassword,
        newPassword: newPassword,
      ),
    );
  }

  @override
  Future<void> logout() {
    // TODO: implement logout
    throw UnimplementedError();
  }
}
