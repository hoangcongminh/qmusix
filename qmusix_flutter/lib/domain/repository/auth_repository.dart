abstract class AuthRepository {
  Future<void> login({
    required String username,
    required String password,
  });
  Future<void> register({
    required String username,
    required String password,
  });
}
