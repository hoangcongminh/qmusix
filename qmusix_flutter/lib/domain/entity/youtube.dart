class Youtube {
  String? title;
  String? thumbnail;
  String? id;
  String? channelTitle;
  String? publishedAt;
  String? description;

  Youtube({
    this.title,
    this.thumbnail,
    this.id,
    this.channelTitle,
    this.publishedAt,
    this.description,
  });

  factory Youtube.fromJson(Map<String, dynamic> json) {
    return Youtube(
      title: json['snippet']['title'],
      thumbnail: json['snippet']['thumbnails']['high']['url'],
      id: json['id']['videoId'],
      channelTitle: json['snippet']['channelTitle'],
      publishedAt: json['snippet']['publishedAt'],
      description: json['snippet']['description'],
    );
  }
}
