import 'package:dio/dio.dart';
import 'package:pretty_dio_logger/pretty_dio_logger.dart';
import 'package:qmusix/data/datasource/network/client/interceptos/header_interceptor.dart';

class AppClient {
  final String baseUrl;
  final List<Interceptor>? interceptors;
  final BaseOptions? options;

  const AppClient({required this.baseUrl, this.interceptors, this.options});

  Dio get client {
    final dio = Dio(options);
    dio.options.baseUrl = baseUrl;
    dio.interceptors.addAll(interceptors ?? []);
    dio.interceptors.addAll([
      HeaderInterceptor(),
      PrettyDioLogger(
        requestBody: true,
        requestHeader: true,
        responseBody: true,
      )
    ]);
    return dio;
  }
}
