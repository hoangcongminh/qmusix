import 'package:flutter/material.dart';

class AppSettingsNotifier extends ChangeNotifier {
  var _brightness = Brightness.light;

  Brightness get brightness => _brightness;

  set brightness(Brightness value) {
    _brightness = value;
    notifyListeners();
  }
}
