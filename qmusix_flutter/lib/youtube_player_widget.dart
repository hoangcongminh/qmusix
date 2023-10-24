import 'package:flutter/material.dart';
import 'package:youtube_player_iframe/youtube_player_iframe.dart';

class YoutubePlayerWidget extends StatefulWidget {
  const YoutubePlayerWidget({super.key});

  @override
  State<YoutubePlayerWidget> createState() => _YoutubePlayerWidgetState();
}

class _YoutubePlayerWidgetState extends State<YoutubePlayerWidget> {
  YoutubePlayerController? _youtubeController;

  @override
  void initState() {
    super.initState();
    _youtubeController = YoutubePlayerController.fromVideoId(
      videoId: 'L_z9YHX5ous',
      autoPlay: true,
      params: const YoutubePlayerParams(
        showControls: false,
        pointerEvents: PointerEvents.none,
      ),
    )..stream.listen(
        (event) {
          if (event.playerState == PlayerState.ended) {
            _youtubeController!.loadVideoById(
              videoId: 'mbEZ_9dhM_Y',
            );
          }
        },
      );
  }

  @override
  Widget build(BuildContext context) {
    return YoutubePlayer(
      controller: _youtubeController!,
      aspectRatio: 16 / 9,
    );
  }
}
