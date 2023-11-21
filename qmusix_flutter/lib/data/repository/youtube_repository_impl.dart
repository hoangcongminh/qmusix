import 'dart:convert';
import 'package:flutter/services.dart';
import 'package:qmusix/domain/entity/youtube.dart';
import 'package:qmusix/domain/repository/youtube_repository.dart';

class YoutubeRepositoryImpl implements YoutubeRepository {
  @override
  Future<List<Youtube>> getYoutbeSearch(String searchQuery) async {
    return Future.delayed(
      const Duration(seconds: 1),
      () async {
        final String response =
            await rootBundle.loadString('assets/example_youtube_list.json');
        final data = await json.decode(response);
        final items = data['items'] as List<dynamic>;
        return items.map((e) => Youtube.fromJson(e)).toList();
      },
    );
  }
}
