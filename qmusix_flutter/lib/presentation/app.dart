import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import 'package:provider/provider.dart';
import 'package:qmusix/data/repository/youtube_repository_impl.dart';
import 'package:qmusix/domain/repository/youtube_repository.dart';
import 'package:qmusix/injection.dart';
import 'package:qmusix/presentation/home/bloc/video_player_bloc.dart';
import 'package:qmusix/presentation/shared/app_settings_notifier.dart';
import 'package:qmusix/router.dart';

class Application extends StatelessWidget {
  const Application({super.key});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        ChangeNotifierProvider<AppSettingsNotifier>(
          create: (_) => AppInjection.get<AppSettingsNotifier>(),
        ),
        Provider<YoutubeRepository>(create: (_) => YoutubeRepositoryImpl()),
      ],
      child: BlocProvider(
        create: (context) => VideoPlayerBloc(),
        child: Builder(
          builder: (context) {
            return MaterialApp.router(
              routerConfig: AppRouter.router,
              title: 'Music together',
              theme: ThemeData(
                colorSchemeSeed: Colors.deepPurple,
                useMaterial3: true,
                brightness: context.watch<AppSettingsNotifier>().brightness,
              ),
            );
          },
        ),
      ),
    );
  }
}
