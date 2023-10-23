import 'package:flutter/material.dart';
import 'package:qmusix/youtube_player_widget.dart';

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Qmusix'),
      ),
      body: LayoutBuilder(
        builder: (context, contraints) {
          if (contraints.maxWidth < 600) {
            return const VerticalView();
          } else {
            return const Padding(
              padding: EdgeInsets.symmetric(
                vertical: 100.0,
                horizontal: 200.0,
              ),
              child: Row(
                children: [
                  Expanded(
                    flex: 3,
                    child: YoutubePlayerWidget(),
                  ),
                  Expanded(
                    flex: 1,
                    child: SizedBox.shrink(),
                  ),
                  Expanded(
                    flex: 3,
                    child: NextVideoListWidget(),
                  ),
                ],
              ),
            );
          }
        },
      ),
    );
  }
}

class VerticalView extends StatelessWidget {
  const VerticalView({super.key});

  @override
  Widget build(BuildContext context) {
    return const Column(
      children: [
        YoutubePlayerWidget(),
        // NextVideoListWidget(),
      ],
    );
  }
}

class NextVideoListWidget extends StatelessWidget {
  const NextVideoListWidget({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: 10,
      itemBuilder: (context, index) {
        return const NextVideoItem();
      },
    );
  }
}

class NextVideoItem extends StatelessWidget {
  const NextVideoItem({
    super.key,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        const ListTile(
          leading: FlutterLogo(),
          title: Text('Title'),
          subtitle: Text('Artist'),
        ),
        Row(
          children: [
            TextButton(
              onPressed: () {},
              child: const Text("Upvote"),
            ),
            TextButton(
              onPressed: () {},
              child: const Text("Downvote"),
            ),
          ],
        )
      ],
    );
  }
}
