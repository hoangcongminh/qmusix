import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:qmusix/config/router/router.dart';
import 'package:qmusix/repository.dart';
import 'package:qmusix/theme_change_notifier.dart';

class Application extends StatelessWidget {
  const Application({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider<ThemeChangeNotifier>(
          create: (_) => ThemeChangeNotifier(),
        ),
        Provider<AppRepository>(create: (_) => AppRepository()),
      ],
      child: Builder(
        builder: (context) {
          return MaterialApp.router(
            routerConfig: AppRouter.router,
            title: 'Music together',
            theme: ThemeData(
              colorSchemeSeed: Colors.deepPurple,
              useMaterial3: true,
              brightness: context.watch<ThemeChangeNotifier>().brightness,
            ),
          );
        },
      ),
    );
  }
}
