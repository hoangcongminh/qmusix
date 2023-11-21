import 'package:get_it/get_it.dart';
import 'package:qmusix/core/const/app_const.dart';
import 'package:qmusix/data/datasource/network/client/api_client.dart';
import 'package:qmusix/data/datasource/network/services/auth_service.dart';
import 'package:qmusix/data/repository/auth_repository_impl.dart';
import 'package:qmusix/domain/repository/auth_repository.dart';
import 'package:qmusix/presentation/shared/app_settings_notifier.dart';

class AppInjection {
  static final AppInjection _singleton = AppInjection._();

  factory AppInjection() {
    return _singleton;
  }

  AppInjection._();

  static final _getIt = GetIt.I;

  static T get<T extends Object>() {
    return _getIt.get<T>();
  }

  static Future<void> setup() async {
    await _getIt.reset();

    //App
    _getIt.registerFactory<AppSettingsNotifier>(() => AppSettingsNotifier());

    //Auth
    _getIt.registerSingleton<AppClient>(
      const AppClient(baseUrl: AppConstant.baseUrl),
    );
    _getIt.registerFactory<AuthService>(
      () => AuthService(_getIt.get<AppClient>().client),
    );
    _getIt.registerFactory<AuthRepository>(
      () => AuthRepositoryImpl(_getIt.get<AuthService>()),
    );
  }
}
