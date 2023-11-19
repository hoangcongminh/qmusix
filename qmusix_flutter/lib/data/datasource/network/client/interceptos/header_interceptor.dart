import 'package:dio/dio.dart';

class HeaderInterceptor extends Interceptor {
  @override
  void onRequest(RequestOptions options, RequestInterceptorHandler handler) {
    options.headers.addAll({
      //   "Access-Control-Allow-Origin": "*",
      //   "Access-Control-Allow-Methods": "POST, GET, OPTIONS, PUT, DELETE, HEAD",
      // "Access-Control-Allow-Headers": "*",
    });
    super.onRequest(options, handler);
  }
}
