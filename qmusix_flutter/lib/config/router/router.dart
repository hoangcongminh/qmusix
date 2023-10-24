import 'package:flutter/material.dart';
import 'package:go_router/go_router.dart';
import 'package:qmusix/homepage.dart';
import 'package:qmusix/login_page.dart';
import 'package:qmusix/register_page.dart';

class AppRouter {
  static const homePath = '/home';
  static const loginPath = '/login';
  static const registerPath = '/register';

  static get router {
    return GoRouter(
      routes: [
        GoRoute(
          path: "/",
          redirect: (context, state) => homePath,
        ),
        GoRoute(
          path: homePath,
          builder: (context, state) => const HomePage(),
        ),
        GoRoute(
          path: loginPath,
          pageBuilder: (context, state) => CustomTransitionPage(
            child: const LoginPage(),
            transitionsBuilder:
                (context, animation, secondaryAnimation, child) {
              return FadeTransition(
                opacity: animation,
                child: child,
              );
            },
          ),
        ),
        GoRoute(
          path: registerPath,
          pageBuilder: (context, state) => CustomTransitionPage(
            child: const RegisterPage(),
            transitionsBuilder:
                (context, animation, secondaryAnimation, child) {
              return FadeTransition(
                opacity: animation,
                child: child,
              );
            },
          ),
        ),
      ],
    );
  }
}
