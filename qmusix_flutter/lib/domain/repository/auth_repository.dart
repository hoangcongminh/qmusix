abstract class AuthRepository {
  Future<void> login({
    required String username,
    required String password,
  });
  Future<void> register({
    required String username,
    required String password,
  });

  Future<void> changePassword({
    required String username,
    required String oldPassword,
    required String newPassword,
  });

  Future<void> logout();
}
