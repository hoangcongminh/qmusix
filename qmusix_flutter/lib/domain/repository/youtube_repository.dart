import 'package:qmusix/domain/entity/youtube.dart';

abstract class YoutubeRepository {
  Future<List<Youtube>> getYoutbeSearch(String searchQuery);
}
